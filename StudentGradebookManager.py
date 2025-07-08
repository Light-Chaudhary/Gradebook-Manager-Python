# Python Student Gradebook Manager 

try : 
    name = input("Enter your name: ")
    science_mark = int(input ("Enter science_mark: "))
    math_mark = int(input ("Enter math_mark: "))
    cs_mark = int(input ("Enter cs_mark: "))

    dic = { "name" : name,
        "Science_mark" : science_mark, 
        "Math_mark" : math_mark,
        "Computer_Science_mark" : cs_mark}
    print("\nGradeBook Entry: ")
    print(dic)

    def average (sci, math, cs) :
        return (sci + math + cs) / 3

    avg = (average(science_mark, math_mark, cs_mark))
    print(f"Average Mark: {avg:.2f}")

    with open("grades.txt", "a") as f :
        f.write(f"Name: {name}\n")
        f.write(f"Science mark: {science_mark}\n")
        f.write(f"Math mark: {math_mark}\n")
        f.write(f"Computer Science mark: {cs_mark}\n")
        f.write(f"Average: {avg:.2f}\n")
        f.write("-" * 40 + "\n")


except ValueError : 
    print ("Please! Enter valid data ")
except Exception as e:
    print("Something Unholy Occured!")

