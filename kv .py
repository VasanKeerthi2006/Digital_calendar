import calendar
reminder = {}
while True:
	print("\n1.show calendar\n2.Add Reminder\n3.View Reminder\n4.Exit")
	ch = input("choose: ")
	if ch =='1':
		y,m = int(input("year:")),int(input("Month: "))
		print(calendar.month(y,m))
	elif ch == '2':
			d = input("Date (YYYY-MM-DD): ")
			r = input("Reminder: ")
			reminder[d]= r
			print("saved.")
	elif ch == '3':
			d = input("Date (YYYY-MM-DD): ")
			print("Reminder :",reminder.get(d, "None"))
	elif ch =='4':
		break
	else:
		print("Invalid.")