from cs1graphics import *

from time import *

from array import array

from random import randint

class start_button_handler(EventHandler):

    def __init__(self, window, blocks, poles_rods_text, x, y, number_of_blocks):

        EventHandler.__init__(self)

##        global window
        self._window = window

        #graphics ob, graphic ob of rods, poles, and text
        self._blocks, self._poles_rods_text, self._x, self._y, self._number_of_blocks = blocks, poles_rods_text, x, y, number_of_blocks
        self._number_of_blocks = self._blocks[-1][-1]
##        self._y.pop(0)# Getting rid of 100
####        '''
        print("self._number_of_blocks",self._number_of_blocks)
        print("self._y = ",self._y)
        print("self._blocks = ",self._blocks)
##        print("self._x, self._y =",self._x, self._y)
                                            #216      , 480
        self._dictionary_of_points = {"A":(self._x[0],self._y[0]),
                                          #600        , 480
                                       "B":(self._x[1],self._y[0]),
                                          #983        , 480
                                       "C":(self._x[2],self._y[0])}
        print("self._dictionary_of_points = ",self._dictionary_of_points)
        self._blocks.reverse()
        self._rod_A = []
##        self._rod_A = [i for i in self._blocks[i][2]]
        for i in range(len(self._blocks)):
##            print("i= ",i)
            self._rod_A.append(self._blocks[i][2])
##            print("self._rod_A = ",self._rod_A)
##        self._rod_A = [i for i in range(len(self._blocks)+1)]
##        self._rod_A.reverse()
        self._rod_C = []
        self._rod_B = []
##        self._rods= {"A":self._rod_A,"B":self._rod_B,"C":self._rod_C}
##        print("self._rods= ",self._rods)
        '''
        print("self._x = ",self._x)
        print("self._y = ",self._y)

        print("self._rod_A = ",self._rod_A)
        print("self._blocks = ",self._blocks
        print("self._dictionary_of_points = ", self._dictionary_of_points)##'''
        self._block_y = 480 # starting point for y
        self._y_dict = {"A": (self._block_y-(2*40)), "B": self._block_y, "C":self._block_y} #dictionary of y values for 3 bricks
        self._rods= {"A":self._rod_A,"B":self._rod_B,"C":self._rod_C}
    def handle(self, event):
##        rod_A,rod_B,rod_C = final()

        if event.getDescription() == "mouse click":
            #self.testMethod(3,"A","B")
##            self.move(3,"A","B")
##            self.move2() #for testing the move2() method
            self.recursion(self._number_of_blocks+1,"A","B","C")
##            print("Hey I made it here:). arrays:", self._x, self._y)
            
    # It returns the x_y alla novak.
    def s(self, rod_letter):
        
        return self._dictionary_of_points[rod_letter][0], self._dictionary_of_points[rod_letter][1]
    
    def e(self, rod_letter):
        
        return self._dictionary_of_points[rod_letter][0], ((self._dictionary_of_points[rod_letter][1]))

    def coordiantes(self):
        """This method stores a series of x and y points in a list as a for of tuples."""
        # For instance we have 3 disks and their y by self._y since they reside on the first rod initially.
        # Since we know the points of x by the istance self._x for each rod I just iterated through each element of
        # eachy point and added to it a x point. So now we have the right coordinate for where to moeve them.
        coordinates=[]
        for i in range(len(self._x)):
            for u in range(len(self._y)):
                coordinates.append((self._x[i],self._y[u]))
 
    def move(self, d_n, s_r, e_r):

        print("disk number: "+str(d_n)+" is moved from rod", s_r," to rod ",e_r)
        
        s_x, s_y = self.s(s_r)
        
        e_x, e_y = self.e(e_r)

        e_y = self._y_dict[e_r] #reassigns the final y- value for the block
##        print("s_x, s_y = ",s_x, s_y)
##        print("e_x, e_y = ",e_x, e_y)
        self._blocks[self._rods[s_r][-1]][0].moveTo(e_x,e_y)  #moves the block to the appropriate place
        #self._window.setAutoRefresh()
        print("frozen?",self._window.getAutoRefresh())
        self._window.setAutoRefresh()
        self._window.getAutoRefresh()
        print("frozen?",self._window.getAutoRefresh())
        print("one block is moved")
        self._blocks[self._rods[s_r][-1]][1].moveTo(e_x,e_y)  #moves the text box to the appropriate place
        self._window.refresh()
##        print("text is moved, type:",type(self._blocks[rods[s_r][-1]][1]))
        block_to_move = self._rods[s_r].pop()                 #stores the block and pops it from the dictionary
        self._rods[e_r].append(block_to_move)                 #appends the block to the rod where it moved
        self._window.getAutoRefresh()
##        print("rods",rods)
##        print("e_x,e_y",e_x,e_y)
##        print("self._y_dict[s_r]+=40 before: ",self._y_dict[s_r])
        self._y_dict[s_r] += 40
##        print("self._y_dict[s_r]+=40 after: ",self._y_dict[s_r])
        self._y_dict[e_r] -= 40
        sleep(1)


    def move2(self):
        self.move(0, "A", "C")
        sleep(3)
        self.move(1, "A", "B")
        
    def recursion(self, number_of_disks, starting_rod, middle_rod, ending_rod):
        
        if  number_of_disks == 0:# Base case: This check whether is the smallest disck being removed.
            sleep(.3)
            
##            self.move(number_of_disks, starting_rod, ending_rod)
##            print("sleepy sleepy .1")
            pass
        ##        print("move disk from "+str(starting_rod)+" to "+str(ending_rod))

        else: #self.move_to_tower(self, number_of_disks-1, starting_rod, ending_rod)# We know that the smaller disk is movable everywhere by the rule of the game.
##            sleep(.3)
##            self.move(number_of_disks, starting_rod, ending_rod)
            #make the window refresh here.
##            self.move(number_of_disks, starting_rod, ending_rod)
            self.recursion(number_of_disks-1, starting_rod, ending_rod, middle_rod)
            print("it's gonna move soon")
##            sleep(.3)
##            print("sleepy sleepy .3")
            self.move(number_of_disks, starting_rod, ending_rod)

##            print("number of disk: ",number_of_disks-1, " from ",starting_rod," to ",ending_rod)

            self.recursion(number_of_disks-1, middle_rod, starting_rod,ending_rod)


    def getCount(self):

        return self.testCount

class exit_button_handler(EventHandler):

    def __init__(self, window):

        EventHandler.__init__(self)

        self._window = window

    def handle(self,even):

        print("Hi I made it!")

        self._window.close()

        exit(0)

class Hanoi():

    def __init__(self):#, imput_number_of_disks, width = 1200, height = 700, gaps = 50):

        """Drawing and setting up the first points needed to create the pole, rods, and bocks."""

        self._width = 1200

        self._height = 700

        self._number_of_disks = 3#int(input("imput number of disks: "))

        self._gaps = 50

        self._count_recursions = 0

        self._number_of_rods = 3

        self._number_of_gaps = 4

        self._heights_for_rectangles = self._gaps

        self._initial_point_for_rods_and_poles = (((self._width - (self._gaps * self._number_of_gaps)) / self._number_of_rods) / 2) + self._gaps

        self._helper_variable_for_inintial_x_positions_for_rods_and_poles = self._initial_point_for_rods_and_poles - self._gaps

        # This will give us the colours of blocks and buttons randomly

        self._get_colours = (self.random_int(), self.random_int(), self.random_int())

##        print(self._get_colours)

##        print('self._cernter_point_of_x',self._center_point_of_x)

##        global window
##        window = Canvas(self._width, self._height, 'skyblue', 'Towers Hanoi Game')#'skyblue'(165, 246, 245)
        self._window = Canvas(self._width, self._height, 'skyblue', 'Towers Hanoi Game')
        

    #This will give us the colours of blocks and buttons randomly

    def random_int(self):

        """This will give us the colours of blocks and buttons randomly."""

        return randint(0,255)
    
    def method_for_change_in_coordinates(self, iterations, my_condition):

        """This method will reurn the x coordinates for poles, rods, and y corrdinates for blocks as a loop keeps calling it."""

        if my_condition == "poles_and_rodes, and exit_button":

            change_in_x_coordinate = (self._initial_point_for_rods_and_poles * iterations) + (self._helper_variable_for_inintial_x_positions_for_rods_and_poles * (iterations-1))

            return change_in_x_coordinate

        else:

           change_in_y_coordinate =  480 - ((iterations - 1) * self._width / 30)

           return change_in_y_coordinate

    # Creating poles and rods, but also returning a list of memory location

    # of poles and rods plus a list of array of x-axis.

    def poles_and_rodes(self):

        """Creating poles and rods, but also returning a list of memory location

        which i have stored as tuple of the elements of poles and rods plus a list of array of x-axis."""

        # This will make the pole 20 unitea or 1/20 of the total wondow.

        poles_width = self._width / 60

        # TO DO MAKE THE CENTER POINT VARIABLE SO IT CAN BE REFERED ABSTARCTIDILY FOR EACH TOME WE NEED IT.

        poles_heights = self._heights_for_rectangles * 6

##        coordinating_x_point_for_each_rod = self._initial_point_for_rods_and_poles - self._gaps

        rods_width = (self._width - (self._gaps * self._number_of_gaps)) / self._number_of_rods

##        print("rods w = ",rods_width)

        letters_for_rods = ("A", "B", "C")

##        poles = rods = text = None

##        memory_location_of_poles =(poles, rods, text)

        list_of_memory_location_of_poles = list()

        array_of_xs = array("i",)

        for iterations in range(1, len(letters_for_rods)+1):

            get_center_point_of_x = int(self.method_for_change_in_coordinates(iterations, "poles_and_rodes, and exit_button"))

            poles = Rectangle(poles_width, poles_heights, Point(get_center_point_of_x, 355))

            rods = Rectangle(rods_width, self._heights_for_rectangles, Point(get_center_point_of_x, 530))
##            print("get_center_point_of_x = ", get_center_point_of_x)

##            print("rods x val = ", Point(self._center_point_of_x, 530))

            poles.setFillColor("sandybrown")

            rods.setFillColor("sandybrown")

            add_letter = Text(str(letters_for_rods[iterations-1]), 12, Point(get_center_point_of_x, 530))

            self._window.add(poles)

            self._window.add(rods)

            self._window.add(add_letter)

            poles, rods, text = poles, rods, add_letter

            memory_location_of_poles = (poles, rods, add_letter)

            array_of_xs.append(get_center_point_of_x)

##            print(get_center_point_of_x)

            list_of_memory_location_of_poles.append(memory_location_of_poles)

        return list_of_memory_location_of_poles, array_of_xs
##    def method_helper_for_blocks(self, iterations):

    # Creating the blocks, returning they memory locations and a list of

    # of arrays for the y-axis.

    def blocks(self):

        """It creates the blocks, returning they memory locations and a list of
        of arrays for the y-axis."""

        block_initial_width = self._width * 0.20# It gives me the width of the largest block wich is 240

        in_here_iterate_through = 0

        get_numbers = self._get_colours

        get_colors = (self.random_int(), self.random_int(), self.random_int())

        memory_location_of_blocks = []

        array_of_ys = array("i",)

        for iterations in range(1, self._number_of_disks + 1):

            change_in_y_for_point = int(self.method_for_change_in_coordinates(iterations, "blocks"))

##            w=self.method_of_center_of_x(iterations)

            disks = Rectangle((block_initial_width / iterations), 35, Point(self._initial_point_for_rods_and_poles, change_in_y_for_point))
##            print("(block_initial_width / iterations) = ",(block_initial_width / iterations))
##            print("((iterations-1)(corrdinates_for_the_center_point_of_y)=",((iterations-1)*change_in_y_for_point))

            numbers = Text(str(self._number_of_disks - iterations), 12, Point(self._initial_point_for_rods_and_poles, change_in_y_for_point))

            disks.setFillColor(get_colors)

##            numbers.setFillColor()

            self._window.add(disks)

            self._window.add(numbers)

            get_colors = (self.random_int(), self.random_int(), self.random_int())

            array_of_ys.append(change_in_y_for_point)

            memory_location_of_blocks.append((disks, numbers, iterations - 1))

        return memory_location_of_blocks, array_of_ys

    # Creating the start button and exit button.

    def Buttons(self):

        # Start button

        start_button = Button("Start!", Point(self._initial_point_for_rods_and_poles, 580))

        start_button.setFontSize(18)

        start_button.setFillColor(self._get_colours)

        self._window.add(start_button)

##        start_button.addHandler(start_button_handler(self._window))


        # Exit button

        exit_button = Button("EXIT",Point(self.method_for_change_in_coordinates(3, "poles_and_rodes, and exit_button"), 580))

        exit_button.setFontSize(18)

        exit_button.setFillColor(self._get_colours)

        self._window.add(exit_button)

        self.random_int()

##        self.method_for_change_in_coordinates(3, "poles_and_rodes, and exit_button")

##        self.method_for_change_in_coordinates(3,"")

        memory_location_of_poles_rods_and_text, array_xs, = self.poles_and_rodes()

        list_of_blocks, array_ys = self.blocks()

##        print("array_xs, array_ys = ",array_xs, array_ys)

        ex_bt, st_bt = self.Buttons()

        st_bt.addHandler(start_button_handler(self._window, list_of_blocks, memory_location_of_poles_rods_and_text, array_xs, array_ys, self._number_of_disks))

##        list_of_blocks.addHandler(start_button_handler(self._window))

        ex_bt.addHandler(exit_button_handler(self._window))

##        print("list_of_blocks  =",list_of_blocks )

def main():

    self.random_int()

##        self.method_for_change_in_coordinates(3, "poles_and_rodes, and exit_button")

##        self.method_for_change_in_coordinates(3,"")

    memory_location_of_poles_rods_and_text, array_xs, = self.poles_and_rodes()

    list_of_blocks, array_ys = self.blocks()

##        print("array_xs, array_ys = ",array_xs, array_ys)

    ex_bt, st_bt = self.Buttons()

    st_bt.addHandler(start_button_handler(self._window, list_of_blocks, memory_location_of_poles_rods_and_text, array_xs, array_ys, self._number_of_disks))

##        list_of_blocks.addHandler(start_button_handler(self._window))

    ex_bt.addHandler(exit_button_handler(self._window))

##        print("list_of_blocks  =",list_of_blocks )
if __name__ == "__main__":

##
    a = Hanoi()#(5,1200,700,50)
    
##    hanoi.main()
##

    a.poles_and_rodes()

##

    a.blocks()
##
    a.Buttons()
    b=start_button_handler()

    b=start_button_handler('<cs1graphics.Canvas object at 0x000001B017E56550>',
                           [('<cs1graphics.Rectangle object at 0x000001B017EEF908>', '<cs1graphics.Text object at 0x000001B017EEFA58>', 0),
                            ('<cs1graphics.Rectangle object at 0x000001B017EEFBE0>', '<cs1graphics.Text object at 0x000001B017EEFD30>', 1),
                            ('<cs1graphics.Rectangle object at 0x000001B017EEFEB8>', '<cs1graphics.Text object at 0x000001B017EF7048>', 2)],
                           [('<cs1graphics.Rectangle object at 0x000001B017ECC7B8>', '<cs1graphics.Rectangle object at 0x000001B017EE4CC0>', '<cs1graphics.Text object at 0x000001B017EE4DD8>'),
                            ('<cs1graphics.Rectangle object at 0x000001B017EEF0B8>', '<cs1graphics.Rectangle object at 0x000001B017EEF128>', '<cs1graphics.Text object at 0x000001B017EEF240>'),
                            ('<cs1graphics.Rectangle object at 0x000001B017EEF4E0>', '<cs1graphics.Rectangle object at 0x000001B017EEF550>', '<cs1graphics.Text object at 0x000001B017EEF668>')],
                           array('i', [216, 600, 983]),array('i', [100, 480, 440, 400]))
    b.final()
    
