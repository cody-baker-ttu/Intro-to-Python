#First, I will need to import the pandas module so that I can carry out dataframe operations.
import pandas as pd
#Now, I need to set my fields for column names for my dataframe
fields = ["Scaffold", "Start", "Stop", "Element", "Score", "Strand", "Class", "Family", "Divergence"]
#Now, I need to read the "aVan_rm.bed" file into a dataframe with columns, separated by tabs.
df = pd.read_csv("aVan_rm.bed", names = fields, sep = "\t")
#Now, I need a variable called classes which will allow me to see all of the TE classes in my dataframe.
classes = df.Class.unique()
print(classes)
#Now, I am sorting my dataframe into a new dataframe containing only data for SINEs.
df1 = df[df.Class == 'SINE']
#Now, I will drop the "Strand" and "Score" columns from my dataframe.
df1.drop(columns=['Strand', 'Score'])
#Now, I will calculate the length of each element in my new dataframe and add a new column called "length"
df1['Length'] = df1['Stop'] - df1['Start']
#Now, I need to calculate the mean, min, and max of my lengths of my dataframe.
df1['Length'].min()
df1['Length'].max()
df1['Length'].mean()
#Now I will create a new dataframe containing only the SINE family metulj and calculate the mean, min, and max lengths of the metulj family.
df2 = df1[df1.Family == 'metulj']
df2['Length'].min()
df2['Length'].max()
df2['Length'].mean()
#Finally, I will creae a new dataframe containing only the SINE family ZenoSINE and calculate the mean, min, and max lengths.
df3 = df1[df1.Family == 'ZenoSINE']
df3['Length'].min()
df3['Length'].max()
df3['Length'].mean()

