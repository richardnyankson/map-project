def get_data(file)->list:
    """ Takes a file, and returns a list of
        strings of data from the file"""
    file = open(file, "r")
    data = file.readlines()
    file.close()
    return data    # Returns the list of strings

def parse_data(data:list)-> None:
    """Takes information from the 'get_data' function and
       puts it in a format that is easier to use"""
      
    length = len(data)
    for index in range(length):
        data[index] = data[index].strip()# Removes the "\n" from the strings
    for index in range(length):
        data[index]= data[index].split(",")
    return data

def get_populations(data:list)->list:
    """Takes a list of strings from 'parse_data' and then
       returns a list of the populations"""
     
    length= len(data)
    for index in range(length):
        data[index]= data[index][-1]  # Finds the last value in the list
    return data

def leading_digits(data:list)-> None:
    """Takes a list of strings from 'get_populations' and prints the frequency"""
    freq_list = [0, 0, 0, 0, 0, 0 , 0, 0, 0, 0] # Counts the number of times the leading numbers appear
    digit_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    for number in data:
        for index in range(len(digit_list)):
            if digit_list[index] == number[0]:
                freq_list[index] += 1 / len(data) # Divide by len(data) times since its serve as range to iterate through data 

    for index in range(9):
        
        print("Frequency of {}: {}".format(digit_list[index],round(freq_list[index],3)))




def is_real(freq_list: list) -> bool:
    """Compares the frequency to Benford's law"""
    benford_freq_list = [0.301, 0.176, 0.125, 0.097, 0.079, 0.067, 0.058, 0.051, 0.046]
    for index in range(9):
        test_value = freq_list[index]
        true_value = benford_fre_list[index]
        if test_value < true_value * 0.8 or test_value > true_value * 1.2: # Checks the result is within 20% interval
            return False
    return True

# Iterates through through csV_file and prints each file
for csv_file in ["data1.csv", "data2.csv", "data3.csv"]:
    print(csv_file)
    digit_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    leading_digits(get_populations(parse_data(get_data(csv_file))))
    print('\n')


def plot_data():
    
    import turtle
    turtle.tracer(0,0)
    turtle.setworldcoordinates(-150, 15, -70, 70)

    plot = turtle.Turtle()  # Creates turtle
    plot.fillcolor('black')
# Iterates to get the first and second values in the list
    for data in parse_data(get_data("data3.csv")):
        lat = float(data[0])   
        long = float(data[1])
        radius = (float(data[2]) ** 0.5) * 0.0003  # Calculates the radius 
        x = -long
        y = lat

        plot.up()
        plot.goto(x, y)
        plot.down()
        plot.begin_fill()
        plot.circle(radius)  # Draws a circle with the radius given
        plot.end_fill()

plot_data()
