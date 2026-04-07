color=input("Enter color: ")
match color:
    case "red":
        print("Go")
    case "yellow":
        print("Wait")
    case "green":
        print("Stop")
    case _: # default case
        print("Invalid color")