import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Movable Dot"
DOT_RADIUS = 10
DOT_SPEED = 5

class DotWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, update_rate=1/60)
        arcade.set_background_color(arcade.color.DARK_MIDNIGHT_BLUE)
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.dx = 0
        self.dy = 0

    def on_draw(self):
        self.clear()
        arcade.draw_circle_filled(self.x, self.y, DOT_RADIUS, arcade.color.AMBER)

    def on_update(self, delta_time: float):
        self.x += self.dx
        self.y += self.dy

        # Keep inside screen bounds
        self.x = max(DOT_RADIUS, min(SCREEN_WIDTH - DOT_RADIUS, self.x))
        self.y = max(DOT_RADIUS, min(SCREEN_HEIGHT - DOT_RADIUS, self.y))

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol in (arcade.key.W, arcade.key.UP):
            self.dy = DOT_SPEED
        elif symbol in (arcade.key.S, arcade.key.DOWN):
            self.dy = -DOT_SPEED
        elif symbol in (arcade.key.A, arcade.key.LEFT):
            self.dx = -DOT_SPEED
        elif symbol in (arcade.key.D, arcade.key.RIGHT):
            self.dx = DOT_SPEED
        elif symbol == arcade.key.ESCAPE:
            arcade.exit()

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol in (arcade.key.W, arcade.key.UP, arcade.key.S, arcade.key.DOWN):
            self.dy = 0
        if symbol in (arcade.key.A, arcade.key.LEFT, arcade.key.D, arcade.key.RIGHT):
            self.dx = 0


def main():
    window = DotWindow()
    arcade.run()

if __name__ == "__main__":
    main()
