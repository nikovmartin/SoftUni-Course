parked_plates = set()
n = int(input())
for _ in range(n):
    direction, plate = input().split(", ")
    if direction == "IN":
        parked_plates.add(plate)
    else:
        parked_plates.remove(plate)
if not parked_plates:
    print("Parking Lot is Empty")
else:
    [print(x) for x in parked_plates]