marks = []

sub1 = int(input("Enter English Marks: "))
sub2 = int(input("Enter Hindi Marks: "))
sub3 = int(input("Enter Marathi Marks: "))
sub4 = int(input("Enter Maths Marks: "))
sub5 = int(input("Enter Science Marks: "))

marks = [sub1, sub2, sub3, sub4, sub5]
print("Marks Added!")

marks.sort()
print("Highest Marks is: ",marks[-1])

print("Lowest Marks is: ",marks[0])

average = (sum(marks) * 100) / 500
print("Average is: ",average,"%")

pass_count = 0
fail_count = 0

for sub in marks:
    if sub >= 40:
        pass_count += 1
    else:
        fail_count += 1 
        
print("Total Pass Count: ",pass_count)
print("Total Fail Count: ",fail_count)

if fail_count <= 1:
        print("You are failed!")
elif average >= 90:
    print("You are passed with grade A")
elif average >= 80:
    print("You are passed with grade B")
elif average >= 60:
    print("You are passed with grade C")
elif average >= 40:
    print("You are passed with grade D")
elif average < 40:
    print("You are failed!")