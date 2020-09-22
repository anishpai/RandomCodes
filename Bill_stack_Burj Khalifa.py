#Bills
#One morning, you go out and place a dollar bill on the
#sidewalk by the Burj Khalifa tower in Chicago. Each day thereafter,
#you go out double the number of bills.
#How long does it take for the stack of bills to exceed the height of the tower?


bill_thickness = 0.11* 0.001  #Bill thickness in meters
height_burj_khalifa = 829.8   #Height of Burj Khalifa in meters

num_bill = 1
day = 1


while num_bill * bill_thickness < height_burj_khalifa:
    print(day,num_bill, num_bill* bill_thickness)

    day= day + 1
    num_bill = num_bill*2


print(num_bill/2)
print("Amount of Money Required")
print(int(height_burj_khalifa/bill_thickness))
