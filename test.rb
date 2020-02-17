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
cf_name = f_name.upcase
cl_name = l_name.upcase
name = (f_name + l_name)

puts("Section 2", "="*9)
print("Name: ", f_name +" "+ l_name, "\n")
print("Name with middle name interpolated: ", f_name + " #{m_name} "+ l_name, "\n")
print("Name in Capitals: ", cf_name+" "+ cl_name, "\n")
print("Number of Characters in my name: ", name.length, "\n")

# Section 3 worth 20 points
#
# 1. Create an array with a list of the titles of your 5 favorite movies
# 2. Display the first element of the array.
# 3. Display all of the titles sorted in alphabetical order

puts("","Section 3","="*9)
movies = ["Rocky", "Zombieland", "The Princess Bride", "The Dark Knight", "Forrest Gump"]
print("First element of the array: ",movies[0], "\n")
movies = movies.sort
print("Movies in order: ", movies, "\n")

# Section 4 worth 20 points
#
# Meals are important and there are a lot of details to keep track of for a meal.
#
# 1. Create a Meal Class. 
# 2. Have at least 5 variables, with at least one string, integer and boolean type in your Meal class.
# 3. Create a method for the class in addition to the initialize method
# 4. Create and display three instances of meals.
# 5. Call your method on all three instances.

class Meal
    def initialize(type, name, amount, calories, utensil)
        @type = type
        @name = name
        @amount = amount
        @calories = calories
        @utensil = utensil
    end

    def display()
        print("Type of cuisine: ","#{@type}", "\n")
        print("Name of Food: ","#{@name}", "\n")
        print("Amount present: ","#{@amount}", "\n")
        print("Number of calories: ","#{@calories}", "\n")
        print("Needs to use an utensil: ","#{@utensil}", "\n")
    end
end

spaghetti = Meal.new("Italian", "Spaghetti", "1/4 lbs", 650, true)
naan = Meal.new("Indian", "Naan Bread", "1/2 lbs", 200, false)
dumpling = Meal.new("Chinese", "Dumplings", "1/8 lbs", 450, true)

puts(" ", "Section 4", "="*9)
spaghetti.display
puts("-"*20)
naan.display
puts("-"*20)
dumpling.display
# Section 5 
# What is your favorite book, website, youtube series, forum, or tutorial for learning Ruby that you have
# discovered in addition to the course materials?
# Display the title and link of your favorite resource.
# Display two sentences that explain why you found that resource useful.

puts(" ", "Section 5", "="*9)

