class multipleFunctions:
    def Subfields():
        print("Subfields in AI are:")
        fields = [
            "Machine Learning",
            "Neural Networks",
            "Vision",
            "Robotics",
            "Speech Processing",
            "Natural Language Processing"
        ]
        for field in fields:
            print(field)


    def OddEven():
        num = int(input("Enter a number: "))
        print("Enter a number: ",num)
        if num % 2 == 0:
            print(f"{num} is Even number")
        else:
            print(f"{num} is Odd number")


    def Eligible():
        gender = input("Your Gender (Male/Female): ")
        print("Your Gender: ",gender)
        age = int(input("Your Age: "))
        print("Your Age: ",age)
        if gender.lower() == "male" :
            if age >= 21:
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        elif gender.lower() == "female":
            if age >= 18:
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        else:
            print("Invalid Gender Entered")


    def percentage():
        marks = []
        for i in range(1, 6):
            m = int(input(f"Subject{i} = "))
            print(f"Subject{i} = ",m)
            marks.append(m)
        total = sum(marks)
        percent = (total / (5 * 100)) * 100
        print("Total :", total)
        print("Percentage :", percent)


    def triangle():
        height = int(input("Height: "))
        print("Height: ",height)
        breadth = int(input("Breadth: "))
        print("Breadth: ",breadth)
        area = (height * breadth) / 2
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle:", area)

        height1 = int(input("Height1: "))
        print("Height1: ",height1)
        height2 = int(input("Height2: "))
        print("Height2: ",height2)
        breadth2 = int(input("Breadth: "))
        print("Breadth: ",breadth2)
        perimeter = height1 + height2 + breadth2
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:", perimeter)