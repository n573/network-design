
# rot = rotational
def rot13(s):
    result = ""
    # Loop over the characters
    for v in s:
        # convert to number
        c = ord(v)
        # Shift number back or forward
        if c >= ord('a') and c <= ord('z'):
            if c > ord('m'):
                c -= 13
            else:
                c += 13
        elif c >= ord('A') and c <= ord('Z'):
            if c > ord('M'):
                c -= 13
            else:
                c += 13
        # Append to result
        result += chr(c)
    return result

if __name__ == "__main__":
    msg = input()
    msg = rot13(msg)
    print(msg)
    