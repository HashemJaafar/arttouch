import pandas as pd
sheet_id ="1hiGgbNVlCv-Cn3h5uqRntVOCBNTKIkQAW-FZSej-HFo"
sheet_name = "سلة"

df=pd.read_excel(r"C:\Users\Liqaa Arttouch\Desktop\python_programs_by_hashem_for_photoshop\HASHEM.xlsx")

newlist=[]
for  row in df.values.tolist():
    for i in range(row[2]):
        print(i+1,row[0])
        newlist.append(row[0])

for r in newlist:
    print(r)

pd.DataFrame(newlist).to_excel('./output.xlsx', header=False, index=False)