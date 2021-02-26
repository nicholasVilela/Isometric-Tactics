class Controller:
    def __init__(
        self, 
        move_left, 
        move_right, 
        move_up, 
        move_down,
        rotate_left,
        rotate_right
        ):
        self.move_left = move_left
        self.move_right = move_right
        self.move_up = move_up
        self.move_down = move_down
        self.rotate_left = rotate_left
        self.rotate_right = rotate_right
        self.buttons = []

        self.buttons.append(self.move_left)
        self.buttons.append(self.move_right)
        self.buttons.append(self.move_up)
        self.buttons.append(self.move_down)
        self.buttons.append(self.rotate_left)
        self.buttons.append(self.rotate_right)

    def update(self, event):
        for button in self.buttons:
            button.update(event)