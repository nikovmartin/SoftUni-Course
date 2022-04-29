# def extract_file(data):
#     for path in data:
#         if "." in path:
#             splitterous = path.split(".")
#             file_name = splitterous[0]
#             file_ext = splitterous[1]
#             print(f"File name: {file_name} \nFile extension: {file_ext}")
#
# path_file = input().split("\\")
# extract_file(path_file)


def extract_file(data):
    info = data[-1].split(".")
    print(f"File name: {info[0]} \nFile extension: {info[1]}")


path_file = input().split("\\")
extract_file(path_file)
