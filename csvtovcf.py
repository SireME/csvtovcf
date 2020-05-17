import csv

with open('washington.csv') as f:
    csv_r=csv.reader(f)
    x=""
    y=0
    for row in csv_r:  
      x="BEGIN:VCARD\n"+"VERSION:2.1\n"+"N:;{}".format(row[4])+";;;\n"+"FN:{}\n".format(row[4]) +"EMAIL;HOME:noelannane@gmail.com\n"+"END:VCARD\n"
      print(x)
      with open('cs_f.vcf',"a") as f2:
           f2.write(x)  
      y+=1
      if y==5:
        break
    
print('csv file successfully created with name c_f.vcf')   