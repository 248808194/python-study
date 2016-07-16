def safe_float(object):
    'safe version of float()'
    try:
        retval = float(object)
    except Exception as  diag:
        retval = str(diag)
    return retval

def main():
    try:
        with open("carddata","r") as carddata:
            txnx = carddata.readlines()
    except Exception as ex:
        print(ex)
    total = 0.00
    for line in txnx:
        result = safe_float(line)
        if isinstance(result,float):
            total += result
        else:
            pass

    print(total)


main()

