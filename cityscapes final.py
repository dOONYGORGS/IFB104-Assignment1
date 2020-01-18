
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: N10282653
#    Student name: JACOB MATTHEW KRAUT
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  CITYSCAPES
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and efficiently repeating multiple actions in
#  order to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "build_city".
#  You are required to complete this function so that when the
#  program is run it draws a city whose plan is determined by
#  randomly-generated data stored in a list which specifies what
#  style of building to erect on particular sites.  See the
#  instruction sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single Python 3 file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must not rely on any non-standard Python
# modules that need to be installed separately, because the markers
# may not have access to such modules.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

canvas_height = 700 # pixels
canvas_width = 1100 # pixels
grass_depth = 95 # vertical depth of the "grass", in pixels
half_width = canvas_width // 2 # maximum x coordinate in either direction
grid_font = ('Arial', 10, 'normal') # font for drawing the grid
grid_size = 50 # gradations for the x and y scales shown on the screen
offset = 5 # offset of the x-y coordinates from the screen's edge, in pixels
max_height = canvas_height - grass_depth # maximum positive y coordinate
max_building_height = 575 # city ordinance maximum building height
site_width = 240 # maximum width of a building site

# Define the locations of building sites approved by the
# city council (arranged from back to front)
sites = [['Site 1', [-225, 0]],
         ['Site 2', [25, 0]],
         ['Site 3', [275, 0]],
         ['Site 4', [-375, -25]],
         ['Site 5', [-125, -25]],
         ['Site 6', [125, -25]],
         ['Site 7', [375, -25]],
         ['Site 8', [-275, -50]],
         ['Site 9', [-25, -50]],
         ['Site 10', [225, -50]]]

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image.
# By default the drawing grid is displayed - call the function
# with False as the argument to prevent this.
def create_drawing_canvas(show_grid = True):

    # Set up the drawing canvas with coordinate (0, 0) in the
    # "grass" area
    setup(canvas_width, canvas_height)
    setworldcoordinates(-half_width, -grass_depth, half_width, max_height)

    # Draw as fast as possible
    tracer(False)

    # Make the sky blue
    bgcolor('sky blue')

    # Draw the "grass" as a big green rectangle (overlapping the
    # edge of the drawing canvas slightly)
    overlap = 25 # pixels
    penup()
    goto(-(half_width + overlap), -(grass_depth + overlap)) # bottom-left
    fillcolor('pale green')
    begin_fill()
    setheading(90) # face north
    forward(grass_depth + overlap * 2)
    right(90) # face east
    forward(canvas_width + overlap * 2)
    right(90) # face south
    forward(grass_depth + overlap * 2)
    end_fill()

    # Draw a nice warm sun peeking into the image at the top left
    penup()
    goto(-canvas_width // 2, canvas_height - grass_depth)
    pencolor('yellow')
    dot(350)

    # Draw a big fluffy white cloud in the sky
    goto(canvas_width // 3, canvas_height - grass_depth - 100)
    pencolor('white')
    dot(200)
    setheading(200)
    forward(100)
    dot(180)
    setheading(0)
    forward(200)
    dot(160)

    # Optionally draw x coordinates along the bottom of the
    # screen (to aid debugging and marking)
    pencolor('black')
    if show_grid:
        for x_coord in range(-half_width + grid_size, half_width, grid_size):
            goto(x_coord, -grass_depth + offset)
            write('| ' + str(x_coord), font = grid_font)

    # Optionally draw y coordinates on the left-hand edge of
    # the screen (to aid debugging and marking)
    if show_grid:
        for y_coord in range(-grid_size, max_height, grid_size):
            goto(-half_width + offset, y_coord - offset)
            write(y_coord, font = grid_font)
        goto(-half_width + offset, max_building_height - 5)
        write('Maximum allowed building height', font = grid_font)

    # Optionally mark each of the building sites approved by
    # the city council
    if show_grid:
        for site_name, location in sites:
            goto(location)
            dot(5)
            goto(location[0] - (site_width // 2), location[1])
            setheading(0)
            pendown()
            forward(site_width)
            penup()
            goto(location[0] - 40, location[1] - 17)
            write(site_name + ': ' + str(location), font = grid_font)
     
    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas.
# By default the cursor (turtle) is hidden when the program
# ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any drawing in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the build_city function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the random_plan function appearing below.  Your
# program must work correctly for any data set generated by the
# random_plan function.
#
# Each of the data sets below is a list specifying a set of
# buildings to be erected.  Each specification consists of the
# following parts:
#
# a) The site on which to erect the building, from Site 1 to 10.
# b) The style of building to be erected, from style 'A' to 'D'.
# c) The number of floors to be constructed, from 1 to 10.
# d) An extra value, either 'X' or 'O', whose purpose will be
#    revealed only in Part B of the assignment.  You should
#    ignore it while completing Part A.
#

# Each of these data sets draws just one building in each of the
# four styles
fixed_plan_1 = [[1, 'A', 6, 'O']]
fixed_plan_2 = [[2, 'B', 7, 'O']]
fixed_plan_3 = [[3, 'C', 5, 'O']]
fixed_plan_4 = [[4, 'D', 4, 'O']]
fixed_plan_5 = [[1, 'A', 9, 'X']]
fixed_plan_6 = [[2, 'B', 2, 'X']]
fixed_plan_7 = [[3, 'C', 3, 'X']]
fixed_plan_8 = [[4, 'D', 6, 'X']]

# Each of the following data sets draws just one style of
# building but at three different sizes, including the maximum
# (so that you can check your building's maximum height against
# the height limit imposed by the city council)
fixed_plan_9 = [[1, 'A', 10, 'O'], [2, 'A', 5, 'O'], [3, 'A', 1, 'O']]
fixed_plan_10 = [[1, 'B', 10, 'O'], [2, 'B', 5, 'O'], [3, 'B', 1, 'O']]
fixed_plan_11 = [[1, 'C', 10, 'O'], [2, 'C', 5, 'O'], [3, 'C', 1, 'O']]
fixed_plan_12 = [[1, 'D', 10, 'O'], [2, 'D', 5, 'O'], [3, 'D', 1, 'O']]
fixed_plan_13 = [[1, 'A', 10, 'X'], [2, 'A', 5, 'X'], [3, 'A', 1, 'X']]
fixed_plan_14 = [[1, 'B', 10, 'X'], [2, 'B', 5, 'X'], [3, 'B', 1, 'X']]
fixed_plan_15 = [[1, 'C', 10, 'X'], [2, 'C', 5, 'X'], [3, 'C', 1, 'X']]
fixed_plan_16 = [[1, 'D', 10, 'X'], [2, 'D', 5, 'X'], [3, 'D', 1, 'X']]

# Each of the following data sets draws a complete cityscape
# involving each style of building at least once. There is
# no pattern to them, they are simply specific examples of the
# kind of data returned by the random_plan function which will be
# used to assess your solution. Your program must work for any value
# that can be returned by the random_plan function, not just these
# fixed data sets.
fixed_plan_17 = \
         [[1, 'D', 2, 'O'],
          [2, 'B', 7, 'O'],
          [5, 'C', 6, 'O'],
          [6, 'A', 4, 'O']]
fixed_plan_18 = \
         [[1, 'D', 6, 'O'],
          [3, 'C', 5, 'O'],
          [4, 'B', 3, 'O'],
          [9, 'A', 9, 'O'],
          [10, 'D', 2, 'O']]
fixed_plan_19 = \
         [[5, 'C', 6, 'O'],
          [6, 'B', 9, 'O'],
          [7, 'A', 5, 'O'],
          [8, 'A', 7, 'O'],
          [9, 'D', 4, 'O']]
fixed_plan_20 = \
         [[1, 'A', 4, 'O'],
          [2, 'B', 4, 'O'],
          [3, 'A', 5, 'O'],
          [4, 'D', 7, 'O'],
          [10, 'B', 10, 'O']]
fixed_plan_21 = \
         [[1, 'B', 6, 'O'],
          [3, 'A', 4, 'O'],
          [4, 'C', 4, 'O'],
          [6, 'A', 8, 'O'],
          [8, 'C', 7, 'O'],
          [9, 'B', 5, 'O'],
          [10, 'D', 3, 'O']]
fixed_plan_22 = \
         [[1, 'A', 10, 'O'],
          [2, 'A', 9, 'O'],
          [3, 'C', 10, 'O'],
          [4, 'B', 5, 'O'],
          [5, 'B', 7, 'O'],
          [6, 'B', 9, 'O'],
          [7, 'C', 2, 'O'],
          [8, 'C', 4, 'O'],
          [9, 'A', 6, 'O'],
          [10, 'D', 7, 'O']]
fixed_plan_23 = \
         [[3, 'A', 8, 'O'],
          [4, 'C', 8, 'O'],
          [5, 'B', 4, 'O'],
          [6, 'D', 5, 'O'],
          [7, 'C', 5, 'X'],
          [8, 'A', 3, 'X'],
          [9, 'D', 2, 'X']]
fixed_plan_24 = \
         [[2, 'C', 3, 'O'],
          [3, 'B', 1, 'O'],
          [4, 'C', 3, 'X'],
          [5, 'C', 1, 'O'],
          [6, 'D', 2, 'O'],
          [7, 'B', 1, 'O'],
          [8, 'D', 2, 'O'],
          [9, 'C', 7, 'O'],
          [10, 'A', 1, 'X']]
fixed_plan_25 = \
         [[1, 'B', 7, 'X'],
          [3, 'C', 1, 'O'],
          [6, 'D', 3, 'O'],
          [7, 'A', 7, 'O'],
          [8, 'D', 3, 'X'],
          [9, 'C', 7, 'O'],
          [10, 'C', 9, 'X']]
fixed_plan_26 = \
         [[1, 'A', 6, 'O'],
          [2, 'A', 2, 'O'],
          [3, 'A', 9, 'X'],
          [4, 'D', 1, 'X'],
          [5, 'C', 7, 'O'],
          [6, 'D', 6, 'O'],
          [7, 'B', 5, 'O'],
          [8, 'A', 1, 'O'],
          [9, 'D', 10, 'X'],
          [10, 'A', 6, 'O']]
 
#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to mark your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a city
# to be built.  Your program must work for any data set returned by
# this function.  The results returned by calling this function will
# be used as the argument to your build_city function during marking.
# For convenience during code development and marking this function
# also prints the plan for the city to be built to the shell window.
#

def random_plan(print_plan = True):
    building_probability = 70 # percent
    option_probability = 20 # percent
    from random import randint, choice
    # Create a random list of building instructions
    city_plan = []
    for site in range(1, len(sites) + 1): # consider each building site
        if randint(1, 100) <= building_probability: # decide whether to build here
            style = choice(['A', 'B', 'C', 'D']) # choose building style
            num_floors = randint(1, 10) # choose number of floors
            if randint(1, 100) <= option_probability: # decide on option's value
                option = 'X'
            else:
                option = 'O'
            city_plan.append([site, style, num_floors, option])
    # Optionally print the result to the shell window
    if print_plan:
        print('\nBuildings to be constructed\n' +
              '(site, style, no. floors, option):\n\n',
              str(city_plan).replace('],', '],\n '))
    # Return the result to the student's build_city function
    return city_plan

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "build_city" function.
#

# Erect buildings as per the provided city plan


floor_height = 20

#####  Defining some basic shapes to use in my drawings #####
def diamond(size, colour):
    begin_fill()
    fillcolor(colour)
    setheading(45)
    fd(size)
    lt(90)
    fd(size)
    lt(90)
    fd(size)
    lt(90)
    fd(size)
    end_fill()
    setheading(0)

def triangle (size, colour):
    begin_fill()
    fillcolor(colour)
    fd(size/2)
    setheading(120)
    fd(size)
    setheading(240)
    fd(size)
    setheading(0)
    fd(size/2)
    end_fill()

def rectangle (length, width, colour = 'none'):
    begin_fill()
    fillcolor(colour)
    fd(length/2)
    lt(90)
    fd(width)
    lt(90)
    fd(length)
    lt(90)
    fd(width)
    lt(90)
    fd(length/2)
    end_fill()

def door (height, width, colour):
    fillcolor(colour)
    begin_fill()
    fd(width/2)
    setheading(90)
    fd(height*.75)
    circle(width/2, 180)
    fd(height*.75)
    lt(90)
    fd(width/2)
    end_fill()


#####  Definitions for my buildings  #####

    
def lighthouse_floors(floors):
    #Building the base of the lighthouse#
    fillcolor('grey')
    begin_fill()
    fd(site_width/4)
    lt(90)
    fd(floor_height)
    rt(90)
    circle(10,180)
    fd(site_width/2)
    circle(10,180)
    rt(90)
    fd(floor_height)
    lt(90)
    fd(site_width/4)
    end_fill()
    pencolor('black')
    door(25,25,'saddlebrown')
    penup()
    goto(xcor(), ycor() + floor_height + 20)
    pendown()
    #Building the remainder of the floors/tower#
    for theredandwhite in range(floors - 1): #Bottom floor is already 1 floor#
        rectangle(site_width/2,floor_height,'crimson')
        penup()
        goto(xcor(), ycor() + floor_height)
        pendown()
        rectangle((site_width/2),floor_height,'white')
        penup()
        goto(xcor(), ycor() - 10)
        pendown()
        begin_fill()
        fillcolor('lightskyblue')
        circle(10,360)
        end_fill()
        penup()
        goto(xcor(), ycor() + (floor_height + 10))
        pendown()

def lighthouse_top():
    #Construct the base of the top#
    begin_fill()
    fillcolor('crimson')
    fd(site_width/4)
    setheading(90)
    circle(-20,90)
    setheading(180)
    fd(site_width/2 + 40)
    setheading(0)
    circle(-20,90)
    setheading(0)
    fd(site_width/4)
    end_fill()
    penup()
    #Construct the lighting beacon#
    goto(xcor(), ycor() + 20)
    pendown()
    rectangle(80,80,'black')
    begin_fill()
    fd(40)
    setheading(90)
    fd(40)
    
    fillcolor('yellow')
    circle(40,180)
    fd(40)
    end_fill()
    setheading(0)
    fd(40)
    penup()
    goto(xcor(), ycor() + 30)
    pendown()
    ##Construct the railings to stop people falling off#
    rectangle(150,2,'black')
    goto(xcor()-75, ycor())
    for railingposts in range(16):
        rectangle(2,-30,'black')
        penup()
        fd(10)
        pendown()
    #Put on the roof to give it the lighthouse look#
    penup()
    goto(xcor() - 85, ycor()+ 50)
    pendown()
    rectangle(100,10,'crimson')
    fd(50)
    lt(90)
    fd(10)
    lt(90)
    fd(10)
    rt(90)
    begin_fill()
    fillcolor('crimson')
    circle(40,180)
    end_fill()
    setheading(0)

def factory_floors(floors):
    #Build the bottom floor of the factory#
    rectangle(180,130,'mediumseagreen')
    rectangle(130,110,'royalblue')
    rectangle(100,90,'lightgrey')
    for rollerdoor in range(5):
        penup()
        goto(xcor(), ycor() + 15)
        pendown()
        fd(50)
        setheading(180)
        fd(100)
        setheading(0)
        fd(50)
    penup()
    goto(xcor(), ycor() + 55)
    pendown()
    #Give the roller door it's horizontal lines for looks#
    for factorylevel in range(floors - 1):
        rectangle(site_width - 60,floor_height + 10,'mediumseagreen')
        penup()
        goto(xcor(),ycor() + 5)
        pendown()
        rectangle(20,20,'mistyrose')
        penup()
        goto(xcor() + 55,ycor())
        pendown()
        rectangle(20,20,'mistyrose')
        penup()
        goto(xcor() - 110, ycor())
        pendown()
        rectangle(20,20,'mistyrose')
        penup()
        goto(xcor() + 55, ycor() + 25)
        pendown()
        
def factory_top():
    #Build the larger of the 3 chimney's#
    for chimney in range(2):
        rectangle(40,20,'firebrick')
        penup()
        goto(xcor(), ycor() + 20)
        pendown()
        rectangle(40,20,'midnightblue')
        penup()
        goto(xcor(), ycor() + 20)
        pendown()
    begin_fill()
    fillcolor('mediumseagreen')
    fd(20)
    circle(10,180)
    fd(40)
    circle(10,180)
    fd(20)
    end_fill()
    #Add some smoke to the larger chimney#
    for smoke in range(3):
        penup()
        goto(xcor(), ycor() + 50)
        dot(60, 'grey')
    goto(xcor() - 55, ycor() - 230)
    pendown()
    #Build the second chimney#
    for chimney in range(2):
        rectangle(20,10,'firebrick')
        penup()
        goto(xcor(), ycor() + 10)
        pendown()
        rectangle(20,10,'midnightblue')
        penup()
        goto(xcor(), ycor() + 10)
        pendown()
        begin_fill()
    fillcolor('mediumseagreen')
    fd(10)
    circle(5,180)
    fd(20)
    circle(5,180)
    fd(10)
    end_fill()
    #Give the second chimney it's smoke#
    for smoke in range(3):
        penup()
        goto(xcor(), ycor() + 25)
        dot(30, 'grey')
    goto(xcor() + 110, ycor() - 115)
    pendown()
    #Build the last of the chimney's#
    for chimney in range(2):
        rectangle(20,10,'firebrick')
        penup()
        goto(xcor(), ycor() + 10)
        pendown()
        rectangle(20,10,'midnightblue')
        penup()
        goto(xcor(), ycor() + 10)
        pendown()
        begin_fill()
    fillcolor('mediumseagreen')
    fd(10)
    circle(5,180)
    fd(20)
    circle(5,180)
    fd(10)
    end_fill()
    #Give the last chimney it's smoke#
    for smoke in range(3):
        penup()
        goto(xcor(), ycor() + 25)
        dot(30, 'grey')

def hotel_floors(floors):
    #Construct the bottom floor#
    rectangle(site_width,110,'steelblue')
    length = 240
    width = 5
    #Some steps to walk into the building#
    for steps in range(3):
        rectangle(length,width,'gainsboro')
        length -= 20
        penup()
        goto(xcor(),ycor() + 5)
        pendown()
    #Add the glass front, doors, glass decoration and awning above#   
    rectangle(180,70,'skyblue')
    goto(xcor(), ycor() + 70)
    rectangle(220,20,'indianred')
    goto(xcor(), ycor() - 37.5)
    penup()
    rectangle(180,8,'indianred')
    fd(5)
    pendown()
    rectangle(2,10,'azure')
    setheading(180)
    penup()
    fd(10)
    setheading(0)
    pendown()
    rectangle(2,10,'azure')
    penup()
    fd(5)
    goto(xcor()+ 50, ycor() - 32.5)
    rectangle(5,70,'steelblue')
    goto(xcor() - 100,ycor())
    rectangle(5,70,'steelblue')
    goto(xcor() + 50,ycor() + 95)
    pendown()
    #Build each individual floor of the hotel#
    for hotelfloors in range(floors - 1):
        rectangle(site_width,floor_height*2,'steelblue')
        penup()
        goto(xcor(), ycor() + 10)
        pendown()
        rectangle(200,20,'skyblue')
        penup()
        goto(xcor(), ycor() + 10)
        rectangle(200,2,'black')
        penup()
        goto(xcor() -90, ycor()- 10)
        pendown()
        #Decorate the windows with some crossbars#
        for windows in range(13):
            rectangle(2,20,'black')
            penup()
            fd(15)
            pendown()
        penup()
        goto(xcor() - 105, ycor() + 30)
        pendown()

def hotel_top():
    #Build the poles to hold up the sign#
    rectangle(2,10,'black')
    penup()
    goto(xcor() - 80, ycor())
    pendown()
    rectangle(2,10,'black')
    penup()
    goto(xcor() + 160, ycor())
    pendown()
    rectangle(2,10,'black')
    penup()
    goto(xcor() - 80, ycor() + 10)
    pendown()
    #Build the sign#
    rectangle(200,50,'midnightblue')
    pencolor('white')
    write('H O T E L',align='center', font=('Helvetica',33,'normal'))
    pencolor('black')

def church_floors(floors):
    #Start with the front entrance and the left side barn#
    rectangle(site_width/2,100,'wheat')
    penup()
    goto(xcor() - 90, ycor())
    pendown()
    rectangle(site_width/4,60,'wheat')
    penup()
    goto(xcor() - 30, ycor() + 60)
    pendown()
    #Put the wooden roof on the left side barn#
    begin_fill()
    fillcolor('saddlebrown')
    fd(60)
    lt(90)
    fd(40)
    setheading(214)
    fd(72)
    end_fill()
    setheading(0)
    penup()
    goto(xcor() + 210, ycor() - 60)
    pendown()
    #Build the right side barn#
    rectangle(site_width/4,60,'wheat')
    penup()
    goto(xcor() - 30, ycor() + 100)
    pendown()
    #Put the wooden roof on the right side barn#
    begin_fill()
    fillcolor('saddlebrown')
    setheading(-394)
    fd(72)
    setheading(180)
    fd(60)
    rt(90)
    fd(40)
    end_fill()
    setheading(0)
    #Return to the entrance and add a large door with a golden trim#
    penup()
    goto(xcor() - 60, ycor() - 100)
    pendown()
    door(63,90,'gold')
    door(60,80,'saddlebrown')
    penup()
    goto(xcor(), ycor() + 10)
    #Put a big golden cross on the door#
    rectangle(5,60,'gold')
    goto(xcor(),ycor() + 40)
    rectangle(40,5,'gold')
    goto(xcor(), ycor() + 50)
    pendown()
    #Build the rising church tower#
    for churchfloors in range(floors - 1):
        rectangle(site_width/2,floor_height,'wheat')
        penup()
        goto(xcor(), ycor() + 7.5)
        pendown()
        rectangle(site_width/2,floor_height/4,'saddlebrown')
        penup()
        goto(xcor(), ycor() - 7.5)
        pendown()
        diamond(13,'gold')
        penup()
        goto(xcor(), ycor() + floor_height)
        pendown()

def church_top():
    #Build the triangular roof#
    rectangle(site_width/2 + 20, 7, '#4B2600')
    penup()
    goto(xcor(), ycor() + 7)
    pendown()
    triangle(100, '#552B00')
    penup()
    #Put a little golden cross on the top#
    goto(xcor(), ycor() + 87)
    rectangle(3,20,'gold')
    goto(xcor(), ycor() + 10)
    rectangle(15,3,'gold')

def crane():
    #Construct the boxes of the base#
    pensize(3)
    pencolor('black')
    rectangle(25,25,'')
    penup()
    goto(xcor(), ycor() + 25)
    pendown()
    rectangle(25,25,'')
    penup()
    goto(xcor() - 12.5, ycor() - 25)
    pendown()
    #Build in the crosshatch pattern#
    setheading(45)
    fd(35.35) #Diagonal of a square = 25 x squareroot of 2#
    setheading(135)
    fd(35.35)
    setheading(-135)
    penup()
    goto(xcor() + 25, ycor())
    pendown()
    fd(35.35)
    setheading(-45)
    fd(35.35)
    #Draw the boom of the crane#
    setheading(90)
    penup()
    goto(xcor() - 12.5, ycor() + 50)
    pendown()
    fd(10)
    penup()
    goto(xcor() + 60, ycor())
    setheading(180)
    pendown()
    fd(80)
    rt(90)
    fd(25)
    setheading(-17.35)# Angle of hypotenuse#
    fd(83.8)#Hypotenuse#
    #Add the hook to the boom#
    setheading(-90)
    fd(20)
    dot(10)
    circle(15,45)
    setheading(0)
    circle(-5,270)
    #Go back and finish the boom crosshatch#
    setheading(0)
    penup()
    goto(xcor() - 80, ycor() + 35)
    pendown()
    setheading(45)
    fd(25)
    setheading(-45)
    fd(23)
    setheading(45)
    fd(15)
    #Reset for the next drawing#
    pensize(1)
    setheading(0)
    
    
def building_A(locationx,locationy,floors,underconstruction):
    penup()
    goto(locationx,locationy)
    pendown()
    if underconstruction == 'O':
        lighthouse_floors(floors)
        lighthouse_top()
    elif underconstruction == 'X':
        lighthouse_floors(floors)
        crane()

def building_B(locationx,locationy,floors,underconstruction):
    penup()
    goto(locationx,locationy)
    pendown()
    if underconstruction == 'O':
        factory_floors(floors)
        factory_top()
    elif underconstruction == 'X':
        factory_floors(floors)
        crane()

def building_C(locationx,locationy,floors,underconstruction):
    penup()
    goto(locationx,locationy)
    pendown()
    if underconstruction == 'O':
        hotel_floors(floors)
        hotel_top()
    elif underconstruction == 'X':
        hotel_floors(floors)
        crane()

def building_D(locationx,locationy,floors,underconstruction):
    penup()
    goto(locationx,locationy)
    pendown()
    if underconstruction == 'O':
        church_floors(floors)
        church_top()
    elif underconstruction == 'X':
        church_floors(floors)
        crane()

def build_city(buildingplan):
    for building in buildingplan:
        locationx, locationy = sites[building[0]-1][1][0],sites[building[0]-1][1][1]
        floors = building[2]
        underconstruction = building[3]

        if building[1] == 'A':
            building_A(locationx,locationy,floors,underconstruction)
        elif building[1] == 'B':
            building_B(locationx,locationy,floors,underconstruction)
        elif building[1] == 'C':
            building_C(locationx,locationy,floors,underconstruction)
        elif building[1] == 'D':
            building_D(locationx,locationy,floors,underconstruction)
#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# building your city.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
# ***** Change the default argument to False if you don't want to
# ***** display the coordinates and building sites
create_drawing_canvas(True)

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with your name and/or a description of
# ***** your city
title("Krautopia")

### Call the student's function to build the city
### ***** While developing your program you can call the build_city
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_plan()" as the
### ***** argument to the build_city function.  Your program must
### ***** work for any data set that can be returned by the
### ***** random_plan function.
##build_city(fixed_plan_1) # <-- used for code development only, not marking
build_city(random_plan()) # <-- used for assessment

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#

