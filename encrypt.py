import os, sys

def main():
    encrypt(sys.argv[1])

def encrypt(filename):
    to_encrypt = open(filename, "rb").read()
    size = len(to_encrypt)
    key = os.urandom(size)
    try:
        #create the key
        with open(filename + ".key", "wb") as key_out:
            key_out.write(key)
        # encrypt (XOR) of the file
        encrypted = bytes(a ^ b for (a,b) in zip(to_encrypt, key))
        #  replace the old file
        with open(filename, "wb") as encrypted_out:
            encrypted_out.write(encrypted)
    except:
        e = sys.exc_info()[0]
        print("Error: " + str(e))

# MAIN
if __name__ == '__main__':
    main()
    