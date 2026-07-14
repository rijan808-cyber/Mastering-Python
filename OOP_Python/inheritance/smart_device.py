class Camera:
    def __init__(self, camera_mp):
        self.__camera_mp = camera_mp

    def get_camera_mp(self):
        return self.__camera_mp

    def set_camera_mp(self, camera_mp):
        self.__camera_mp = camera_mp

    def take_photo(self):
        return f"Photo captured using {self.__camera_mp} MP camera."

    def __str__(self):
        return f"Camera MP   : {self.__camera_mp}"


class Phone:
    def __init__(self, phone_number):
        self.__phone_number = phone_number

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def make_call(self):
        return f"Calling {self.__phone_number}..."

    def __str__(self):
        return f"Phone Number : {self.__phone_number}"


class Smartphone(Camera, Phone):
    def __init__(self, camera_mp, phone_number, brand, storage):

        Camera.__init__(self, camera_mp)
        Phone.__init__(self, phone_number)

        self.__brand = brand
        self.__storage = storage

    def get_brand(self):
        return self.__brand

    def get_storage(self):
        return self.__storage

    def set_brand(self, brand):
        self.__brand = brand

    def set_storage(self, storage):
        self.__storage = storage

    def __str__(self):
        return (
            Camera.__str__(self)
            + "\n"
            + Phone.__str__(self)
            + f"\nBrand        : {self.__brand}"
            + f"\nStorage      : {self.__storage} GB"
        )


phone1 = Smartphone(
    108,
    "9800000000",
    "Samsung",
    256
)

print("Smartphone Details")
print(phone1)

print("\nPhone Features")
print(phone1.take_photo())
print(phone1.make_call())

phone1.set_storage(512)
phone1.set_brand("Google Pixel")

print("\nAfter Updating Details")
print(phone1)