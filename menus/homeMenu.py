import curses
import menus.menuAbstract
from menus import menuAbstract
from menus.menuAbstract import MenuAbstract
from graphics import graphics_list, main_menu_text
from definitions import status, game_logic, Button, Pos, rps

class home_menu(MenuAbstract):
    def __init__(self, last_move, resources, show_end_scr):
        """last_move is a two element list of the last moves done.
        -1 = reserved value, first move/ tutorial
        0 = rock
        1 = paper
        2 = scissors"""
        buttons = [
            [
                Button("rock",      Pos(11, 5),   rps.rock),
                Button("paper",     Pos(11, 19),  rps.paper),
                Button("scissors",  Pos(11, 32),  rps.scissors)
            ],
            [
                Button("shop",       Pos(13, 5),  rps.shop),
                Button("end screen", Pos(13, 17), rps.end),
                Button("exit",       Pos(13, 34), rps.save)
            ]
        ]
        super().__init__(buttons)

        self.last_move = last_move
        self.resources = resources
        self.show_end_scr = show_end_scr
    
    def main(self):
        curses.wrapper(self.home)

    def reversed(self, var):
        return "".join(["(" if i == ")" else
                        ")" if i == "(" else
                        i for i in var[::-1]])

    def status_text(self, status):
        match status:
            case status.invalid:
                return " "*41
            case status.win:
                return f"{' '*15}Player Won!{' '*15}"
            case status.loss:
                return f"{' '*17}AI Won!{' '*17}"
            case _:
                return f"{' '*15}Nobody Won!{' '*15}"

    def home(self, w):
        curses.curs_set(0)
        w.clear()
        w.addstr(0, 0, main_menu_text(
            self.status_text(game_logic(self.last_move)),self.resources))
        
        if self.last_move[0] < 3 or self.last_move[1] < 3:
            player_graphic = graphics_list[self.last_move[0]].splitlines()
            ai_graphic = graphics_list[self.last_move[1]].splitlines()
            for i in range(6):
                w.addstr(i+1, 1, player_graphic[i])
                if self.last_move[1] == 0:
                    w.addstr(i+1, 29, self.reversed(ai_graphic[i]))
                else:
                    w.addstr(i+1, 24, self.reversed(ai_graphic[i]))
        if self.show_end_scr:
            w.addstr(19, 0, "You have not yet unlocked the end screen!")
        while True:
            try:
                # write buffer: includes graphical renditions.
                super().write_buffer(w)

                # get input and change cursor_pos correspondingly
                rcode = super().Input(w)
                if rcode != None:
                    return rcode
            except IndexError:
                while True:
                    w.clear()
                    w.addstr(0, 0, "wait, that's illegal")