Student_Scores = input("Input the list of student scores").split()
for n in range(0, len(Student_Scores)):
    Student_Scores[n] = int(Student_Scores[n])
print(Student_Scores)

Highest_Score = 0
for Score in Student_Scores:
    if Score > Highest_Score:
        Highest_Score = Score
print(f"The Highest score in the class is: {Highest_Score}")
