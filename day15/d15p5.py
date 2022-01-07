def sort_records(mylist):
    slvi = []
    mylist.sort(key=lambda x: x[1])
    print(mylist)

    for i in range(len(mylist)-1):
        if mylist[i][1] < mylist[i+1][1] and len(slvi) == 0:
            slvi.append(mylist[i+1])

        elif mylist[i][1] < mylist[i+1][1] and len(slvi) != 0:
            break

        if mylist[i][1] == mylist[i+1][1] and len(slvi) > 0:
            slvi.append(mylist[i+1])
    slvi.sort(key=lambda x: x[0])
    
    for item in slvi:
        print(item[0])

if __name__ == '__main__':
    # n = number_of_student
    n = int(input()) 
    if 2 <= n <= 5:
        list_of_records = []
        for i in range(n):
            student_name = input()
            student_grade = float(input())
            
            students_record = [student_name, student_grade]
            list_of_records.append(students_record)
        
        sort_records(list_of_records)
        
    