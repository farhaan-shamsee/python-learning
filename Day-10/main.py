# function with output

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "No data provided"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    # print(f"{formatted_f_name} {formatted_l_name}")
    return f"Result: {formatted_f_name} {formatted_l_name}"


print(format_name(input("What is your First name?: "), input("What is your Last name?: ")))

