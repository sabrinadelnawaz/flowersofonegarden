# Set up screen size and initial values
def setup():
    size(800, 600)
    background(135, 206, 250)  # Sky blue
    noStroke()
    frameRate(10)
    
    global flowers, clouds
    # Initialize flowers with fixed positions in a line and different sizes
    flowers = [
        {'x': 50, 'y': 400, 'size': 11, 'growth': 0.1,'colour': color(255, 182, 193)}, # light pink
        {'x': 100, 'y': 400, 'size': 11, 'growth': 0.15, 'colour': color(249, 250, 68)}, #Yellow
        {'x': 150, 'y': 400, 'size': 11, 'growth': 0.2, 'colour': color(232, 67, 49)}, # Red
        {'x': 200, 'y': 400, 'size': 11, 'growth': 0.1, 'colour': color(49, 69, 232)}, # Dark blue 
        {'x': 250, 'y': 400, 'size': 11, 'growth': 0.15, 'colour': color(201, 49, 232)}, #purple
        {'x': 300, 'y': 400, 'size': 11, 'growth': 0.2, 'colour': color(157, 231, 255)},   # Light blue
        {'x': 350, 'y': 400, 'size': 11, 'growth': 0.1, 'colour': color(232, 141, 49)}, # orange
        {'x': 400, 'y': 400, 'size': 11, 'growth': 0.15, 'colour': color(211, 126, 163)}, #dusty rose
        {'x': 450, 'y': 400, 'size': 11, 'growth': 0.2, 'colour': color(144, 238, 144)},  # Light green
        {'x': 500, 'y': 400, 'size': 11, 'growth': 0.1, 'colour': color(126, 129, 211)}, #indigo
        {'x': 550, 'y': 400, 'size': 11, 'growth': 0.15, 'colour': color(126, 199, 211)}, # minty
        {'x': 600, 'y': 400, 'size': 11, 'growth': 0.2, 'colour': color(255, 218, 185)},   # Peach
        {'x': 650, 'y': 400, 'size': 11, 'growth': 0.1, 'colour': color(255, 62, 233)}, #hot pink
        {'x': 700, 'y': 400, 'size': 11, 'growth': 0.15, 'colour': color(237, 252, 247)}, # white
        {'x': 750, 'y': 400, 'size': 11, 'growth': 0.2, 'colour': color(238, 130, 238)}   # Violet
    ]
    # Initialize clouds with random positions and speeds
    clouds = [
        {'x': 50, 'y': 100, 'speed': 1},
        {'x': 250, 'y': 150, 'speed': 1.2},
        {'x': 550, 'y': 80, 'speed': 0.8}
    ]

# Draw each frame
def draw():
    background(135, 206, 250)  # Clear with sky blue each frame
    
    draw_ground()
    animate_flowers()
    animate_clouds()

# Draw the ground
def draw_ground():
    fill(34, 139, 34)  # Grass green
    rect(0, height * 0.75, width, height * 0.25)

# Animate flowers growing in size
def animate_flowers():
    for flower in flowers:
        flower['size'] += flower['growth']  # Increase flower size
        if flower['size'] > 20:  # Reset if too large
            flower['size'] = 10
        draw_flower(flower['x'], flower['y'], flower['size'], flower['colour'])

# Draw a flower with a stem and different colours
def draw_flower(x, y, size, petal_color):
    # Draw stem
    stroke(7, 82, 31)  # Dark green stem
    strokeWeight(3)
    line(x, y, x, height * 0.75)  # Draw line from flower centre to ground
    noStroke()

    # Draw petals
    fill(petal_color)  # Set petal colour
    for angle in range(0, 360, 45):
        petal_x = x + cos(radians(angle)) * size
        petal_y = y + sin(radians(angle)) * size
        ellipse(petal_x, petal_y, size / 2, size / 2)
    
    # Draw centre of flower
    fill(255, 215, 0)  # Yellow centre
    ellipse(x, y, size / 2, size / 2)

# Animate clouds moving across the sky
def animate_clouds():
    for cloud in clouds:
        cloud['x'] += cloud['speed']  # Move cloud
        if cloud['x'] > width + 50:  # Reset if off-screen
            cloud['x'] = -50
        draw_cloud(cloud['x'], cloud['y'])

# Draw a cloud
def draw_cloud(x, y):
    fill(255)  # White clouds
    ellipse(x, y, 60, 40)
    ellipse(x + 20, y + 10, 50, 30)
    ellipse(x - 20, y + 10, 50, 30)
