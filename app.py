import tkinter as tk

def start_stop():
    global running
    running = not running
    if running:
        btn_start_stop.config(text="Stop")
        # Start the video capture loop
        capture_loop()
    else:
        btn_start_stop.config(text="Start")

def capture_loop():
    if running:
        _, frame = webcam.read()
        frame = cv2.flip(frame, 1)
        frame, results = mediapipe_detection(frame, hands)
        draw_styled_landmarks(frame, results)
        cv2.imshow("Hand Gesture Control", frame)
        cv2.waitKey(27)
        root.after(10, capture_loop)

running = False
webcam = cv2.VideoCapture(0)

root = tk.Tk()
root.title("Hand Gesture Control")
root.geometry("300x100")

btn_start_stop = tk.Button(root, text="Start", command=start_stop)
btn_start_stop.pack(pady=10)

root.mainloop()
