import pygame

# Initialize Pygame
pygame.init()

# Set up the display window
window = pygame.display.set_mode((1200, 400))

# Load images
track = pygame.image.load('track6.png')
car = pygame.image.load('tesla.png')

# Scale the car image
car = pygame.transform.scale(car, (30, 60))

# Set initial car position
car_x = 155
car_y = 300

# Focal distance for the camera
focal_dis = 25

# Camera offsets for detecting road ahead
cam_x_offset = 0
cam_y_offset = 0

# Initial direction of the car
direction = 'up'

# Flag to control the main loop
drive = True

# Create a clock object to manage the frame rate
clock = pygame.time.Clock()

# Main loop
while drive:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False
    
    # Limit the loop to 60 frames per second
    clock.tick(60)
    
    # Calculate the camera's position based on the car's position and offsets
    cam_x = car_x + cam_x_offset + 15
    cam_y = car_y + cam_y_offset + 15
    
    # Detect pixel color at specific points relative to the camera position
    up_px = window.get_at((cam_x, cam_y - focal_dis))[0]
    down_px = window.get_at((cam_x, cam_y + focal_dis))[0]
    right_px = window.get_at((cam_x + focal_dis, cam_y))[0]
    
    print(up_px, right_px, down_px)  # Debugging information
    
    # Change direction (take turn) based on pixel detection
    if direction == 'up' and up_px != 255 and right_px == 255:
        # Turn right
        direction = 'right'
        cam_x_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'right' and right_px != 255 and down_px == 255:
        # Turn down
        direction = 'down'
        car_x += 30  # Adjust car's position for the turn
        cam_x_offset = 0
        cam_y_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'down' and down_px != 255 and right_px == 255:
        # Turn right
        direction = 'right'
        car_y += 30  # Adjust car's position for the turn
        cam_x_offset = 30
        cam_y_offset = 0
        car = pygame.transform.rotate(car, 90)
    elif direction == 'right' and right_px != 255 and up_px == 255:
        # Turn up
        direction = 'up'
        car_x += 30  # Adjust car's position for the turn
        cam_x_offset = 0
        car = pygame.transform.rotate(car, 90)
    
    # Drive the car in the current direction
    if direction == 'up' and up_px == 255:
        car_y -= 2
    elif direction == 'right' and right_px == 255:
        car_x += 2
    elif direction == 'down' and down_px == 255:
        car_y += 2
    
    # Draw the track and car on the window
    window.blit(track, (0, 0))
    window.blit(car, (car_x, car_y))
    
    # Draw a circle at the camera position for visualization
    pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 5, 5)
    
    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
