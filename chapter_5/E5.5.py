print ("kilogram          pound      |     pound          kilogram")

for i in range(1,200,2): 
    kg_pre_pound = i * 2.2 
for j in range(20,516,5) :
    pound_per_kg = j * 0.454 
        
    print ("  ",i,"          ",round(kg_pre_pound,1),"     |       ",j,"           ",round(pound_per_kg,2))