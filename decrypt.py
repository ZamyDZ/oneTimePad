import os, sys

def main():
    decrypt(sys.argv[1],sys.argv[2])

def decrypt(filename, key):
    try:
        file = open(filename, "rb").read()
        key = open(key, "rb").read()
        decrypted = bytes(a ^ b for (a, b) in zip(file, key))
        with open ("dec_" + filename, "wb") as decrypted_out:
            decrypted_out.write(decrypted)
    except:
        e = sys.exc_info()[0]
        print("Error: " +  str(e))

# MAIN
if __name__ == '__main__':
    main()
    