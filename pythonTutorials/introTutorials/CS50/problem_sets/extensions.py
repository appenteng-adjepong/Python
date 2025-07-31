def main():
    file = input("File name: ").lower()
    my_function(file)


def my_function(file):
    if "." in file:
        file_list = file.split(".")
        match file_list[1]:
            case "gif":
                print("image/gif")
            case "jpeg" | "jpg":
                print("image/jpeg")
            case "png":
                print("image/png")
            case "pdf":
                print("document/pdf")
            case "txt":
                print("document/txt")
            case "zip":
                print("document/zip")
            case _:
                print("application/octet-stream")
    else:
        print("application/octet-stream")
    pass


if __name__ == "__main__":
    main()