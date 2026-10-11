import java.util.*;

class BSTIterator {

    private Stack<TreeNode> stack;

    public BSTIterator(TreeNode root) {
        stack = new Stack<>();
        pushLeft(root);
    }

    public int next() {

        TreeNode node = stack.pop();

        // Process the right subtree
        if (node.right != null) {
            pushLeft(node.right);
        }

        return node.val;
    }

    public boolean hasNext() {
        return !stack.isEmpty();
    }

    private void pushLeft(TreeNode node) {

        while (node != null) {
            stack.push(node);
            node = node.left;
        }
    }
}