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
    while True:
      if self.detector.cloud_exist():
        self.command_sender.send_message("Cloudy")
      else:
        self.command_sender.send_message("Not cloudy")

run_app = App()
run_app.loop1()
