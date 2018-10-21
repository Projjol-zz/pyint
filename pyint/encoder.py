def encode(num):
    """Return varint for given number"""
    out = []
    while True:
        # get first seven bits of number
        first_seven = num & 0x7f
        num >>=2
        if num:
            # make msb 1
            out.append(first_seven | 0x80)
        else:
            out.append(first_seven)
            # reached last byte
            break
        return out