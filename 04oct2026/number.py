code = int(input("enter access code: "))

if code >= 1000 and code <= 9999:
    print("valid access code")
else:
    print("invalid access code")