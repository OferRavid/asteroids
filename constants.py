SCREEN_WIDTH = 1280  # Width of the game window in pixels
SCREEN_HEIGHT = 720  # Height of the game window in pixels

ASTEROID_MIN_RADIUS = 20  # Minimum radius of an asteroid
ASTEROID_KINDS = 3  # Number of asteroid types, affecting their size
ASTEROID_SPAWN_RATE = 0.8  # Time in seconds between asteroid spawns
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS  # Maximum radius of an asteroid
ASTEROIDS_MAX_SPAWN = 25  # The maximum limit for spawning new asteroids

PLAYER_RADIUS = 20  # Radius of the player's ship
PLAYER_TURN_SPEED = 300  # Rotation speed of the player's ship (degrees per second)
PLAYER_SPEED = 200  # Movement speed of the player's ship (pixels per second)

SHOT_RADIUS = 5  # Radius of a projectile shot by the player
PLAYER_SHOOT_SPEED = 500  # Speed of a projectile (pixels per second)
PLAYER_SHOOT_COOLDOWN = 0.3  # Time in seconds between player shots
