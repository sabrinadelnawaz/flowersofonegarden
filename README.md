# flowersofonegarden

**General Info**
The "Flowers of One Garden" animation project aims to visually represent themes of unity and diversity, using different types of flowers to symbolize various cultures, identities, and perspectives coexisting in a shared space. By creating an animated visual metaphor, this project attempts to address a subtle yet significant social issue: fostering a sense of inclusivity and appreciation for diversity. Through simple yet expressive design elements, it encourages viewers to reflect on the beauty of diversity, emphasizing that every "flower" (person) adds unique value to the "garden" (community).

The purpose of this project is both artistic and educational. 

I chose to undertake "Flowers of One Garden" as a way to blend my interest in digital media with a meaningful message. I wanted to explore how code could go beyond functional applications and be used to create something reflective and symbolic. Additionally, this project provided an opportunity to deepen my understanding of coding, animation, and visual storytelling, pushing me to refine my code literacy and technical skills.

Technologies Used
- Processing 4.3
- Coding Language: Python

Features
- Different coloured flowers blooming at different speeds and resetting
- Clouds moving across the sky
 
Screenshots

Setup
- If using Processing, open the .pde file within the Processing IDE, ensuring Python mode is enabled.
- Verify that your environment is set to run Processing sketches if needed (or install processing.py).
  
Usage
- To simply run the animation without making modifications: python main.py
- To customise flowers colour and size:
  flowers = [
    {'x': 50, 'y': 400, 'size': 11, 'growth': 0.1, 'color': color(255, 182, 193)},  # Light pink
    {'x': 100, 'y': 400, 'size': 11, 'growth': 0.15, 'color': color(249, 250, 68)},  # Yellow
    {'x': 150, 'y': 400, 'size': 11, 'growth': 0.2, 'color': color(232, 67, 49)},    # Red
    # Additional flowers...
]

    To change a flower’s color, adjust the color parameter using RGB values:
      # Example: Changing light pink to pastel purple
          flowers[0]['color'] = color(180, 150, 255)



bash
Copy code

Project Status
- Complete
Room for Improvement
Acknowledgements
Contact
