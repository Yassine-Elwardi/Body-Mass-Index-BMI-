class BMI:
    def __init__(self, name, age, weight, height):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__height = height

    def getBMI(self):
        bmi = self.__weight / (self.__height * self.__height)
        return round(bmi, 2)
    
    def getStatus(self):
        bmi = self.getBMI()
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def getWeight(self):
        return self.__weight
    def getHeight(self):
        return self.__height
    
    

def main():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    bmi1 = BMI(name, age, weight, height)
    print(f"The BMI of {bmi1.getName()} is {bmi1.getBMI()} and he is {bmi1.getStatus()}")

main()



  




