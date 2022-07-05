while True:
    try:
        w = input()
        print(w)
    except EOFError:
        break
