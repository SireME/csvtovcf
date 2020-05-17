import csv
#wahington is a dumy csv that has contacts we wish to save
with open('washington.csv') as f:
    csv_r=csv.reader(f)
    x=""
    y=0
    for row in csv_r:
      #x is the variable that concatenates and actually gets the values for our VCARD
      #modify ist to fit your csv ---- look at csvs and how they hold data
      x="BEGIN:VCARD\n"+"VERSION:2.1\n"+"N:;{}".format(row[4])+";;;\n"+"FN:{}\n".format(row[4]) +"EMAIL;HOME:noelannane@gmail.com\n"+"END:VCARD\n"
      print(x)
      #this actually creates the vcf with name cs_f.vcf
      with open('cs_f.vcf',"a") as f2:
           f2.write(x)
      y+=1
      #this is used to reference he number of contacts
      #we want extracted you can delete it to get contacts from the whole csv
      if y==5:
        break

print('csv file successfully created with name c_f.vcf')
