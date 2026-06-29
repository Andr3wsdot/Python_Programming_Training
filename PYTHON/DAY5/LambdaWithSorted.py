students=[("Andrews",23),
          ("Aloshi",25),
          ("Harsha",19)]
sorted_stud=sorted(students,
                   key=lambda x:x[1]
)
print(sorted_stud)