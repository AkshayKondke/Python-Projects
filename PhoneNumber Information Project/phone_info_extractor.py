import phonenumbers
from phonenumbers import timezone, geocoder, carrier

try:
    number = input("Enter your number with +__: ")
    phone = phonenumbers.parse(number)


    if phonenumbers.is_valid_number(phone):
        time = timezone.time_zones_for_number(phone)
        car = carrier.name_for_number(phone, "en")
        register = geocoder.description_for_number(phone, "en")

        print("Phone Number : ", phone)
        print("Timezone(s) : ", time)
        print("Carrier : ", car)
        print("Region : ", register)

    else:
        print("The number is not valid !")

except phonenumbers.NumberParseException as e:
    print(f"Error while passing number : {e}")



