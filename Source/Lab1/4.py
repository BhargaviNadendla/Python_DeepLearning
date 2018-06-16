"""
Consider the following scenario. You have a list of students who are attending class "Python"

and another list of students who are attending class "Web Application".Find the list of students who are attending both the classes.

Also find the list of students who are not common in both the classes. Print the both lists.

"""
python_list = ['Bhargavi', 'Sravanthi', 'Keerthi', 'Deepthi']
webApplication_list = ['Bhargavi', 'Sravanthi', 'Preethi', 'Sruthi']
common= []
uncommon= []
python_set = set(python_list) #taking python list as a set
webApplication_set = set(webApplication_list) #taking webApplication list as a set
common.extend(list(python_set & webApplication_set)) #taking the intersection of the sets
uncommon.extend(list(python_set - webApplication_set)) #taking the difference of the sets(both sides)
uncommon.extend(list(webApplication_set - python_set))
print("Students enrolled in Python", python_set)
print("Students enrolled in Web application", webApplication_set)
print("Common students: ", common)
print("Uncommon students: ",uncommon)