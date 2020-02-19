# Ruby Assignment
# 
# This assignment contains all of the requirements for the Ruby Assignment.
#
# Download this file.
#
# Make the changes in the file you need to complete the assignment in each section of this file.
# The assignment is worth worth up to 100 points.
#
# Save your file and attach it to an email sent to jmonberg@msu.edu 
# Use "WRA 410 Ruby Assignment" as the title of your email.
#
# When Dr. Monberg runs a copy of your ruby file, it should display all of the required elements. 
#
# Section 1 worth 20 points
# 
# Verify with Dr. Monberg that either Ruby 2.2.2 is installed on your computer or you have setup an account
# on a server like Cloud9 https://medium.com/@krissanawat/initial-setup-enviroment-430f11200b4a

puts(" ","Ruby Assignment", "-"*15, " ")

# Section 2 worth 20 points
#
# 1. Create two string variables for your first name and last name.
# 2. Display your name.
# 3. Display your name with your middle name interpolated in the middle of your name output string.
# 4. Display your name in all capitals.
# 5. Display the number of characters in your name.
# 6. Find another method of the String Class and display the results of that method for your name string.

f_name = "Ethan"
l_name = "Kolderman"
m_name = "Joseph"
cf_name = f_name.upcase()
cl_name = l_name.upcase()
name = (f_name + l_name)
array_name = name.chars()

puts("Section 2", "="*9)
print("Name: ", f_name +" "+ l_name, "\n")
print("Name with middle name interpolated: ", f_name + " #{m_name} "+ l_name, "\n")
print("Name in Capitals: ", cf_name+" "+ cl_name, "\n")
print("Number of Characters in my name: ", name.length, "\n")
print("Name when iterated over each element: ", array_name, "\n")

# Section 3 worth 20 points
#
# 1. Create an array with a list of the titles of your 5 favorite cities
# 2. Display the first element of the array.
# 3. Display all of the cities sorted in alphabetical order

puts("","Section 3","="*9)
cities = ["Rome", "Paris", "Grand Rapids", "Los Angeles", "San Francisco"]
print("First element of the array: ", cities[0], "\n")
cities = cities.sort
print("Cities in order: ", cities, "\n")

# Section 4 worth 20 points
#
# There are lots of uses, qualities and parts associated with cars.
#
# 1. Create a Car Class. 
# 2. Have at least 5 variables, with at least one string, integer and boolean type in your Car class.
# 3. Create a method for the Car class in addition to the initialize method
# 4. Create and dsiplay three instances of a car.
# 5. Call your method on all three instances.

puts("","Section 4","="*9)

class Car

    def initialize(type, maker ,model, year,fourwheel)
        @type = type
        @maker = maker
        @model = model
        @year = year
        @fourwheel = fourwheel
    end

    def display()
        puts("Type of Car: #{@type}")
        puts("Maker: #{@maker}")
        puts("Model of Car: #{@model}")
        puts("Year Made: #{@year}")
        puts("Four Wheel Drive: #{@fourwheel}")
    end
end

s_legacy = Car.new("Sedan", "Subaru" ,"Legacy", 2012, false)
c_camaro = Car.new("Sedan", "Chevy" ,"Camaro", 1969, false)
t_cruiser = Car.new("SUV", "Toyota", "FJ Cruiser", 2019, true)

s_legacy.display
puts("-"*20)
c_camaro.display
puts("-"*20)
t_cruiser.display

# Section 5 
# What is your favorite book, website, youtube series, forum, or tutorial for learning Ruby that you have
# discovered in addition to the course materials?
# Display the title and link of your favorite resource.
# Display two sentences that explain why you found that resource useful.

puts(" ", "Section 5", "="*9)
puts("My favorite youtube series for learning ruby is Ruby Programming by Jake Day Williams.",
     "The Videos he makes are concise, informative, and he gives great examples.",
     "He also spaces out the videos so only one topic is on each video which makes it really",
     "easy to watch just a few at a time.",
     "here is the link below: ",
     ("-"*46),
     "Ruby Programming: https://youtu.be/8I539U5lXWY ")

puts(" ","-"*33,"WRA 410 Ruby Assignment Completed") 