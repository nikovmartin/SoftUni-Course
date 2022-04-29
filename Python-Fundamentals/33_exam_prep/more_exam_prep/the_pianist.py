n = int(input())
piece_dict = dict()
for _ in range(n):
    data = input().split("|")
    piece = data[0]
    composer = data[1]
    key = data[2]
    piece_dict[piece] = dict()
    piece_dict[piece]["composer"] = composer
    piece_dict[piece]["key"] = key
while True:
    command = input().split("|")
    if command[0] == "Stop":
        break
    piece = command[1]
    if command[0] == "Add":
        composer = command[2]
        key = command[3]
        if piece not in piece_dict:
            piece_dict[piece] = dict()
            piece_dict[piece]["composer"] = composer
            piece_dict[piece]["key"] = key
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif command[0] == "Remove":
        if piece in piece_dict:
            del piece_dict[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command[0] == "ChangeKey":
        new_key = command[2]
        if piece in piece_dict:
            piece_dict[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
for piece in piece_dict:
    print(f"{piece} -> Composer: {piece_dict[piece]['composer']}, Key: {piece_dict[piece]['key']}")