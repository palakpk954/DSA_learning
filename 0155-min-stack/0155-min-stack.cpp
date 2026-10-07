class MinStack {
public:

    // Stores all elements of the stack.
    stack<int> st;

    // Stores values that can become the minimum.
    // The top always contains the current minimum.
    stack<int> minSt;

    MinStack() {
    }

    void push(int value) {
        // Push the value into the main stack.
        st.push(value);

        // If minSt is empty, this is the first element
        // and therefore the current minimum.
        if (minSt.empty()) {
            minSt.push(value);
        }
        // If the new value is smaller than or equal to
        // the current minimum, add it to minSt.
        //
        // We use >= so duplicate minimum values are also stored.
        else if (minSt.top() >= value) {
            minSt.push(value);
        }
    }

    void pop() {
        int value = st.top();
        st.pop();

        // If the removed value is the current minimum,
        // remove it from minSt as well.
        if (value == minSt.top()) {
            minSt.pop();
        }
    }

    int top() {
        return st.top();
    }

    int getMin() {
        // The top of minSt is always the minimum element.
        return minSt.top();
    }
};