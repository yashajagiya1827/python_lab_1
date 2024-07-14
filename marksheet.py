sub1=int(input("enter sub1 marks:-"))
sub2=int(input("enter sub2 marks:-"))
sub3=int(input("enter sub3 marks:-"))
sub4=int(input("enter sub4 marks:-"))
sub5=int(input("enter sub5 marks:-"))
avg = sub1+sub2+sub3+sub4+sub5
avg/=2

if(avg >= 70):
    print("grade a")
elif(avg >= 60 and avg < 70):
    print("grade b")
elif(avg >= 50 and avg < 60):
    print("grade c")
elif(avg >= 40 and avg < 50):
    print("grade d")
elif(avg >= 33):
    print("grade e")
else:
    print("grade F ,Sorry! Bad luck Try Next Time...")