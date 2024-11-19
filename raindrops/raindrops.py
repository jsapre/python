def convert(number):
    resp_list = []
    if number % 3 == 0:
        resp_list.append("Pling")
    if number % 5 == 0:
        resp_list.append("Plang")
    if number % 7 == 0:
        resp_list.append("Plong")

    if not resp_list:
        resp_list.append(f"{number}")

    return "".join(resp_list)
