license_plates_dict = {}
commands = int(input())
for i in range(commands):
    line = input().split(" ")
    command = line[0]
    username = line[1]
    if command == "register" and username not in license_plates_dict:
        license_plate = line[2]
        print(f"{username} registered {license_plate} successfully")
        license_plates_dict[username] = license_plate
    elif command == "register" and username in license_plates_dict:
        license_plate = line[2]
        print(f"ERROR: already registered with plate number {license_plate}")
    elif command == "unregister" and username not in license_plates_dict:
        print(f"ERROR: user {username} not found")
    elif command == "unregister" and username in license_plates_dict:
        print(f"{username} unregistered successfully")
        del license_plates_dict[username]
for license in license_plates_dict:
    print(f"{license} => {license_plates_dict[license]}")