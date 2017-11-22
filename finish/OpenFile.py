def openfile():
    with open('i2b2') as file_object:
        ss=file_object.read()
        return ss.rstrip()
if __name__ == '__main__':
    print openfile()