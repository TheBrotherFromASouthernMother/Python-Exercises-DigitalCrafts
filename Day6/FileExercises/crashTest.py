
#The smallish size of the content I was writing (12 bytes) took quite a while to even slow down my cpu
#I was writing about 100,000 btyes or 10mb to the crash.txt file per minute

def killComputer():
    bytesread = 0
    fh = open('crash.txt', 'a+')
    content = 'hello world'
    i = 1
    while True:
      bytesadded = fh.write(content + '\n')
      bytesread += bytesadded
      print("bytes added: {}, bytesread: {}".format(bytesadded, bytesread))
      i += 1
    
    fh.close()


if __name__ == "__main__":
    killComputer()


