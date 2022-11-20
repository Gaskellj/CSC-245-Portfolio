#To Call the star_travel_time function, enter the function name and perameters (Distance in light years, percentage as integer) below the function's code
#E.G. star_travel_time(4.4,50)

def star_travel_time(distance, percentage): #Recieves the perameters as the function is called
    
    SpeedOfLight = 299792458 #Sets the constant speed of light
    
    velocity = SpeedOfLight * percentage/100 #Calculates the velocity of the ship by using the speed of light and the percentage

    factor = 1 / (1 - ((velocity **2) / (SpeedOfLight **2))) ** 0.5 #Uses Einstein's equation to calculate the factor to divide by

    duration = distance * (SpeedOfLight / velocity)
    duration = duration / factor

    #Calculates the duration in two steps of the journey

    print(duration) #Outputs the duration to the screen

star_travel_time(6,50)



