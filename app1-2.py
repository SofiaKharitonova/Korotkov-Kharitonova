import cv2

class Detector():
  def __init__(self, W=1):
    self.weather = W
  def cloud_exist(self):
    if self.weather == 1:
      return True
    else:
      return False

class CommandSender():
  def send_message(self, message):
    print(message)

class App():
  def __init__(self):
    self.detector = Detector()
    self.command_sender = CommandSender()

  def loop1(self):
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        threshold_value = 150
        _, binary = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)
        num_white_pixels = cv2.countNonZero(binary)
        total_pixels = binary.shape[0] * binary.shape[1]
        white_pixel_percentage = num_white_pixels / total_pixels

        if white_pixel_percentage > 0.2:
            self.detector.weather = 1
        else:
            self.detector.weather = 0

        if self.detector.cloud_exist():
            self.command_sender.send_message("It's raining!")
        else:
            self.command_sender.send_message("It's not raining.")

        cv2.imshow('Binary', binary)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

run_app = App()
run_app.loop1()
