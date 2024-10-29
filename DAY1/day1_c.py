# #calculating area of circle
#
# PI=3.142
# radius=float(input("enter Radius:"))
# print("Area of circle:",PI*radius*radius)

#Assignment 10--Calculate saving of a person

income=float(input("enter your monthly income:"))
expense=float(input("enter your monthly expense:"))
savings = income-expense


persave = (savings/income)*100
perspent = (expense/income)*100

print("total saving:",savings)

print("Percentage of income Spent {:.2f}".format(perspent))
print(f"Percentage of income Saved {persave:.2f}")

