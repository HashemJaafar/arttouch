import pandas as pd

input_file=r"C:\Users\Liqaa Arttouch\Desktop\python_programs_by_hashem_for_photoshop\input.xlsx"
output_file="./output.xlsx"
df=pd.read_excel(input_file)

# newlist=[]
# for  row in df.values.tolist():
#     new_var = str(row[1])+" "+str(row[3])
#     print(new_var)
#     newlist.append(new_var)

# newlist=[]
# for  row in df.values.tolist():
#     for i in range(row[1]):
#         new_var = str(row[0])
#         print(new_var)
#         newlist.append(new_var)

# add the size to string
# newlist=[]
# for  row in df.values.tolist():
#     Diameter = row[0]
#     Height = row[1]
#     Width = row[2]
#     Length = row[3]

#     my_string=""
#     if not pd.isna(Length):
#         my_string+=" الطول:"+str(Length)
#     if not pd.isna(Width):
#         my_string+=" العرض:"+str(Width)
#     if not pd.isna(Height):
#         my_string+=" الارتفاع:"+str(Height)
#     if not pd.isna(Diameter):
#         my_string+=" القطر:"+str(Diameter)
#     print(my_string)
            


# for r in newlist:
#     print(r)

# pd.DataFrame(newlist).to_excel(output_file, header=False, index=False)