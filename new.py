score = 0
ans = ['kathmandu','141181','cow', 'mount everest', 'TIA' ]
ques = ['Capital City?', 'Area of Nepal?', 'National Animal?', 'Highest Mountain?','International Airport?']
for j in range(len(ques)):
    a = input(f"what is the {ques[j]}? ")
    if(a.lower() == ans[j].lower()):
        score += 1
    print(score)