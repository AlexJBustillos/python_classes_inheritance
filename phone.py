class Phone:
    """ This is a phone class that can be used for inheritance purposes """
    def __init__(self, phone_number, color):
        self.phone_number = phone_number
        self.color = color

    def __str__(self):
        return f"This phone belongs to {self.phone_number}"

    def call(self, other_number):
        print(f"Calling number: {other_number}")

    def text(self, other_number, message):
        print(f"Sending text to {other_number}")
        print(message)

    def open_app(self, app_name):
        print(f"Opening {app_name}")

class Android(Phone):
    def __init__(self, phone_number, color):
        super().__init__(phone_number, color)
        self.passcode = None
        self.battery = 50
    def __str__(self):
        return f"Android phone that belongs to number {self.phone_number}"

    def set_passcode(self, passcode):
        self.passcode = passcode

    def unlock_phone(self, passcode):
        if passcode == self.passcode:
            print('Phone unlocked')

    def view_battery_life(self):
        print(f"Battery Life: {self.battery}")

    def charge_phone(self, charging_amount):
        self.battery += charging_amount

        if self.battery > 100:
            self.battery = 100
    
    def view_phone_number(self):
        print(f"Phone number: {self.phone_number}")

frank_phone = Android('800-888-8888', 'black')

frank_phone.view_battery_life()
frank_phone.charge_phone(200)
frank_phone.view_battery_life()
frank_phone.view_phone_number()

frank_phone.call('1-877-kars-4-kids')
frank_phone.open_app('Zoom')

class Iphone(Phone):
    def __init__(self, phone_number, color):
        super().__init__(phone_number, color)
        self.face_id = None
        self.icloud = 5
    def __str__(self):
        return f"Iphone belongs to Yami and her number is: {self.phone_number}"
    
    def set_face_id(self, face_id):
        self.face_id = face_id

    def unlock_icloud(self, face_id):
        if face_id == self.face_id:
            print("You can view your files now")

    def view_icloud_gb(self):
        print(f"Icloud storage: {self.icloud}")
    
    def add_storage(self, cloud_storage):
        self.icloud += cloud_storage

        if self.icloud < 5:
            self.icloud = 1

    def view_number(self):
        print(f"Number: {self.phone_number}")
    
sonia_phone = Iphone('800-888-5555', 'red')

sonia_phone.view_icloud_gb()
sonia_phone.add_storage(200)
sonia_phone.view_icloud_gb()
sonia_phone.view_number()

sonia_phone.call('unavailable')
sonia_phone.open_app('crunchyroll')