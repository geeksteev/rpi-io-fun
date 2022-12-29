from picamera2 import Picamera2

picam2 = Picamera2()
still_config = picam2.create_still_configuration()
picam2.configure(still_config)

picam2.start()

picam2.capture_file("test.jpg")

picam2.stop()
