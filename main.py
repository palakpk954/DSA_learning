import cv2
from utils.gesture_detector import GestureDetector
from utils.aws_controller import AWSController

def main():
    # Initialize video capture and class modules
    cap = cv2.VideoCapture(0)
    gesture_detector = GestureDetector()
    aws = AWSController()

    print("Starting Gesture Detection System... Press 'q' to quit.")

    while True:
        success, frame = cap.read()
        if not success:
            print("Camera not accessible.")
            break

        gesture = gesture_detector.detect(frame)

        if gesture:
            print(f"Detected Gesture: {gesture}")

            # Map gesture to AWS actions
            if gesture == "ONE":
                aws.launch_instance()
            elif gesture == "FIVE":
                aws.terminate_instances()
            elif gesture == "TWO":
                aws.send_notification("Custom Action Triggered via Two Fingers")

        cv2.imshow("Hand Gesture Detection", gesture_detector.display(frame))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
