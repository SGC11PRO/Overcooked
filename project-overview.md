# Game flow
1. Appear order on the service board (time + ingredients) over time
2. Chefs actions: 
    - Move
    - Carry ingredients (pick up + drop)
    - Chop & Cook
    - Mount plates
    - Deliver plates on correct station

3. When delivering the order, it dissapears and add score

# Elements
- Chef1, Chef2
- Worktops: Chefs cannot walk on this block
- Stations
    - Ingredients spawners (Drawers)
    - Cutting board
    - Pan
    - Blender
    - Delivery counter
    - Bin
    - Stack of dishes

- Foundations
    - Hand-over surface -> can hold items
    - Floor
    - Solid wall -> cannot hold items. Only to separate top/bottom zones

- Objects
    - Dishes
    - Ingredients

# Timeline
1. **Objects and graphical interface**
    - Create a class for each main game element
    - Behaviour logic inside each class (not main program)
    - Save kitchen layout as table read by the kitchen at start
    - Define constants (positions, times, points, penalties, game duration...)
    - Score counter, failure counter and service timer
    - Basic data structures for recipes, waiting orders and state of each station