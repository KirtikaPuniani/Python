Students_Height = input("Input a list of students heights ").split()
for n in range(0, len(Students_Height)):
    Students_Height[n] = int(Students_Height[n])

Total_Height = 0
for Height in Students_Height:
    Total_Height += Height
print(f"total height = {Total_Height}")

Number_of_Students = 0
for Students in Students_Height:
    Number_of_Students += 1
print(f"Number of Students = {Number_of_Students}")

Average_Height = round(Total_Height / Number_of_Students)
print(Average_Height)
