def read_file(filename):
  try:
    f = open(filename, "r")
    print(f.read())
  except IOError:
    print("Error opening or reading file")
  finally:
    f.close()