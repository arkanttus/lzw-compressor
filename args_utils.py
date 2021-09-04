import sys
import os


def validate_encode():
    if len(sys.argv) >= 3:
        file_to_compress = sys.argv[2] if sys.argv[2] else ''
        path_save_bin_file = sys.argv[3] if sys.argv[3] else ''

        if not os.path.isfile(file_to_compress):
            # Check if file exists
            print("The txt file does not exists")
            exit(1)

        if file_to_compress.split("/")[-1].split(".")[1] != "txt":
            # Check if file to compress is a .txt
            print("The file must be a .txt")
            exit(1)

        if not os.path.exists('/'.join(path_save_bin_file.split("/")[0:-1])):
            # Check if path to save file exists
            print("The path to save bin file does not exists")
            exit(1)

        if path_save_bin_file.split("/")[-1].split(".")[1] != "bin":
            # Check if file to save is a .bin
            print("The file to save must be a .bin")
            exit(1)

        return (file_to_compress, path_save_bin_file)
    else:
        print(f"Arguments required to encode operation:\n"
                f"1. Path to file that will be compressed\n"
                f"2. Path to where bin file will be saved")
        exit(1)


def validate_decode():
    if len(sys.argv) >= 3:
        path_to_bin_file = sys.argv[2] if sys.argv[2] else ''
        path_to_save_txt_file = sys.argv[3] if sys.argv[3] else ''

        if not os.path.isfile(path_to_bin_file):
            # Check if file exists
            print("The bin file does not exists")
            exit(1)

        if path_to_bin_file.split("/")[-1].split(".")[1] != "bin":
            # Check if file to save is a .bin
            print("The file to save must be a .bin")
            exit(1)

        if not os.path.exists('/'.join(path_to_save_txt_file.split("/")[0:-1])):
            # Check if path to save txt file exists
            print("The path to save txt file does not exists")
            exit(1)

        if path_to_save_txt_file.split("/")[-1].split(".")[1] != "txt":
            # Check if file to save is a .bin
            print("The file to save must be a .txt")
            exit(1)

        return (path_to_bin_file, path_to_save_txt_file)
    else:
        print(f"Arguments required to decode operation:\n"
                f"1. Path to bin file\n"
                f"2. Path to where txt file will be saved")
        exit(1)


def get_args():
    if sys.stdin and sys.stdin.isatty():
        # running in terminal

        if len(sys.argv) > 1:
            operation = sys.argv[1]
            if operation not in ['encode', 'decode']:
                # Check if operation is valid
                print("The operation must be 'encode' or 'decode'")
                exit(1)
        else:
            print(f"Arguments required:\n"
                f"1. The operation ('encode' or 'decode')\n"
                f"2. Path to file txt (in encode operation) or bin (in decode operation)\n"
                f"3. Path to save decoded file (in encode operation) or txt file (in decode operation)")
            exit(1)

        if operation == 'encode':
            file_to_compress, path_save_bin_file = validate_encode()
            return (operation, file_to_compress, path_save_bin_file)

        elif operation == 'decode':
            path_to_bin_file, path_to_save_txt_file = validate_decode()
            return (operation, path_to_bin_file, path_to_save_txt_file)
