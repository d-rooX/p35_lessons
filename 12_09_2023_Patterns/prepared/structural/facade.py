# Low-level image processing and sending subsystem
class ImageEncoder:
    def encode_image(self, image):
        print("Encoding image...")

class ImageToBytesConverter:
    def convert_to_bytes(self, encoded_image):
        print("Converting image to bytes...")

class ImageSender:
    def send_bytes(self, bytes_data, address):
        print(f"Sending bytes to address {address}...")

# Facade class
class ImageSendingFacade:
    def __init__(self):
        self.encoder = ImageEncoder()
        self.converter = ImageToBytesConverter()
        self.sender = ImageSender()

    def send_image(self, image, address):
        encoded_image = self.encoder.encode_image(image)
        bytes_data = self.converter.convert_to_bytes(encoded_image)
        self.sender.send_bytes(bytes_data, address)
        print("Image sent successfully!")

# Client code
def image_client():
    facade = ImageSendingFacade()
    image_data = "Image Data"  # Placeholder for image data
    destination_address = "123.456.789.0"  # Destination address

    facade.send_image(image_data, destination_address)


####################################################################


# Subsystem classes (complex components)
class CPU:
    def initialize(self):
        print("CPU: Initialized")

class RAM:
    def initialize(self):
        print("RAM: Initialized")

class HardDrive:
    def initialize(self):
        print("Hard Drive: Initialized")

class BIOS:
    def initialize(self):
        print("BIOS: Initialized")

# Facade class
class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.ram = RAM()
        self.hard_drive = HardDrive()
        self.bios = BIOS()

    def start(self):
        print("ComputerFacade: Starting the computer...")
        self.cpu.initialize()
        self.ram.initialize()
        self.hard_drive.initialize()
        self.bios.initialize()
        print("ComputerFacade: Computer started successfully!")

def computer_client():
    computer = ComputerFacade()
    computer.start()


if __name__ == '__main__':
    image_client()
    computer_client()
