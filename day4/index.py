def calculator(operation):
    match operation:
        case "hello":
            return "hello people"
        case "hi":
            return "hi people"
        case "welcome":
            return "welcome people"


responce = calculator("hi")

print(responce)