#BMI is body mass index.
#It is just ratio of weight and (height)^2.
#enter height in meter and height in Kg.
height = float (input ("enter height in meter:"))
  weight = int (input ("enter weight in Kg:"))
  bmi = weight / (height) ** 2 
  print ("bmi is", bmi) 
  if bmi<18.5:
     print ("Underweight") 
  elif bmi >= 18.5 and bmi < 25:
      print ("Normal")
  elif bmi >= 25 and bmi < 30:
      print ("Overweight")
  else:
      print ("Obesity")
