
graphics_credits = ["""\
│    _______   │       _______    │
│---'   ____)  │ ____(____    '---│
│      (_____) │(______           │
│      (_____) │(_______          │
│      (____)  │ (_______         │
│---.__(___)   │   (__________.---│
├──────────────┴──────────────────┤
""",
                          """\
│           _______               │
│       ---'   ____)____          │
│                 ______)         │
│              __________)        │
│             (____)              │
│       ---.__(___)               │
"""]

end_screen=["┌──────────────┬──────────────────┐"]+\
            graphics_credits[0].splitlines()+\
            graphics_credits[1].splitlines()+\
           ["├─────────────────────────────────┤",
            "│So, what exactly is this screen  │",
            "│that you just unlocked? Nothing  │",
            "│really, just a generic endscreen │",
            "│and just so happens to be a      │",
            "│citation page for the rock paper │",
            "│ascii art ;)                     │",
            "├─────────────────────────────────┤",
            "│https://gist.github.com/wynand100│",
            "│4/b5c521ea8392e9c6bfe101b025c39ab│",
            "│e                                │",
            "├─────────────────────────────────┤",
            "│      PRESS ANY KEY TO EXIT      │",
            "└─────────────────────────────────┘"]

graphics_list = ["""\
    _______  
---'   ____) 
      (_____)
      (_____)
      (____) 
---.__(___)  
""",
"""\
     _______      
---'    ____)____ 
           ______)
          _______)
         _______) 
---.__________)   
""",
"""\
    _______       
---'   ____)____  
          ______) 
       __________)
      (____)      
---.__(___)       
"""]

def main_menu_text(preptext: str, resources: tuple[int, int, int]):
    return "┌────────────────────┬────────────────────┐\n"+\
           "│                    │                    │\n"*7+\
           "├────────────────────┴────────────────────┤\n"+\
          f"│{preptext}│\n"+\
           "├────────────┬───────────────┬────────────┤\n"+\
           "│    rock    │     paper     │  scissors  │\n"+\
           "├────────────┼───────────────┼────────────┤\n"+\
           "│    shop    │   End Screen  │    exit    │\n"+\
           "├────────────┼───────────────┼────────────┤\n"+\
           "│    rock    │     paper     │  scissors  │\n"+\
          f"│{str(resources[0]).center(12)}│{str(resources[1]).center(15)}│{str(resources[2]).center(12)}│\n"+\
           "└────────────┴───────────────┴────────────┘"

start_menu_text = [r"┌─────────────────────────────────────────────────────────────────────────────────────┐",
r"│ ___   ________   ___        _______           ________   ________   ________        │",
r"│ |\  \ |\   ___ \ |\  \      |\  ___ \         |\   __  \ |\   __  \ |\   ____\      │",
r"│ \ \  \\ \  \_|\ \\ \  \     \ \   __/|        \ \  \|\  \\ \  \|\  \\ \  \___|_     │",
r"│  \ \  \\ \  \ \\ \\ \  \     \ \  \_|/__       \ \   _  _\\ \   ____\\ \_____  \    │",
r"│   \ \  \\ \  \_\\ \\ \  \____ \ \  \_|\ \       \ \  \\  \|\ \  \___| \|____|\  \   │",
r"│    \ \__\\ \_______\\ \_______\\ \_______\       \ \__\\ _\ \ \__\      ____\_\  \  │",
r"│     \|__| \|_______| \|_______| \|_______|        \|__|\|__| \|__|     |\_________\ │",
r"│                                                                        \|_________| │",
r"├─────────────────────────────────────────────────────────────────────────────────────┤",
r"│                                        start                                        │",
r"│                                        close                                        │",
r"└─────────────────────────────────────────────────────────────────────────────────────┘"]

base_str = """┌────────────────────────────────────────┐
│                  quit                  │
└────────────────────────────────────────┘
┌──────────────────────────────┬─────────┐
│                              │         │
│                              │         │
│                              │         │
│                              │         │
│                              │         │
│                              │         │
│                              │         │
│                              │         │
│                              │         │
└──────────────────────────────┴─────────┘"""

def prep_items_str(items_avail):
    return "".join(
        [f"""│┌────────────────────────────┐│
││{' '*(14-(len(item.name)//2))}{item.name}{' '*(14-(len(item.name)//2)-(len(item.name)%2))}││
│└────────────────────────────┘│""" for item in items_avail]
    ) + "│                              │\n"*10

def prep_submenu_text(name):
    if len(name) == 0:
        raise Exception("You can't do that")
    if len(name) in range(10):
        return [f"│{' '*(4-len(name)//2)}{name}{' '*(5-len(name)//2-(len(name)%2))}│",
                "│         │",
                "│         │",
                "│         │",
                "│         │",
                "├─────────┤",
                "│   buy   │",
                "│ details │",
                "│  close  │"]
    elif len(name) in range(10, 19):
        return [f"│{name[0:9]}│",
                f"│{' '*(4-len(name[9:19])//2)}{name[9:19]}{' '*(5-len(name[9:19])//2-(len(name[9:19])%2))}│",
                "│         │",
                "│         │",
                "│         │",
                "├─────────┤",
                "│   buy   │",
                "│ details │",
                "│  close  │"]
    elif len(name) in range(19, 28):
        return [f"│{name[0:9]}│",
                f"│{name[9:19]}│"
                f"│{' '*(4-len(name[19:28])//2)}{name[19:28]}{' '*(5-len(name[19:28])//2-(len(name[19:28])%2))}│",
                "│         │",
                "│         │",
                "├─────────┤",
                "│   buy   │",
                "│ details │",
                "│  close  │"]
    else:
        raise Exception("You can't do that")

def prep_details_str(item):
    name = item.name
    price = item.price
    description = item.description
    description += " "*(241-len(description))
    return f"""┌────────────────────────────────────────┐
│{name.center(40)}│\n"
├─────────┬──────────────────────────────┤
│rock:    │                              │
│{price[0]}{' '*(9-len(str(price[0])))}│                              │
│paper:   │                              │
│{price[1]}{' '*(9-len(str(price[1])))}│                              │
│scissors:│                              │
│{price[2]}{' '*(9-len(str(price[2])))}│                              │
│         │                              │
│         │                              │
├─────────┴──────────────────────────────┤
│         Press any key to exit.         │
└────────────────────────────────────────┘"""