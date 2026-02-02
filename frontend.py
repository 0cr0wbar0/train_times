import requests
import webbrowser
import re

def menu(question: str, choices: list[str]) -> str:
    choice = None
    # ["UK", "France", "Switzerland"] -> {"1" : "UK", "2" : "France", "3" : "Switzerland"}
    choice_dict = {str(i) : c for i, c in enumerate(choices, 1)}
    while choice is None or (choice not in choice_dict.keys() and choice.lower() not in map(lambda x: x.lower(), choice_dict.values())):
        choice = input(f"{question}\n" + "\n".join(f"{k}: {v}" for k, v in choice_dict.items()) + "\n> ")
    if choice.lower() in [k.lower() for k in choice_dict.keys()]:
        return choice_dict.get(choice, "nothing").lower() 
    return choice.lower()

def single_input(question: str) -> str:
    return input(f"{question}: ").lower()

if __name__ == '__main__':
    current_url = "/"
    while True:
        try:
            response = requests.get(f"http://127.0.0.1:8000{current_url}").json()
        except Exception:
            continue
        match response.get("type"):
            case "menu":
                current_url += menu(response.get("question"), response.get("choices")) + "/"
            case "input":
                current_url += single_input(response.get("question")) + "/"
            case "via_list":
                via_list = []
                while True:
                    via_list.append(single_input("Type the name of a station you want to travel via, or type 'done' if you've finished").strip())
                    print(via_list)
                    if "done" in via_list:
                        via_list.remove("done")
                        break
                current_url += "".join(station+'~' for station in via_list).strip("~") + "/"
                print(current_url)
            case "open":
                webbrowser.open_new_tab(response.get("url"))
                break
