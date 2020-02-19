
# There are lots of uses, qualities and parts associated with cars.
#
# 1. Create a Car Class. 
# 2. Have at least 5 variables, with at least one string, integer and boolean type in your Car class.
# 3. Create a method for the Car class in addition to the initialize method
# 4. Create and dsiplay three instances of a car.
# 5. Call your method on all three instances.

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