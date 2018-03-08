import os
import csv

empdata=os.path.join('',"employee_data2.csv")

Emp_ID = []
Name = []
First_Name = []
Last_Name = []
DOB = []
SSN = []
State = []

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
with open(empdata, newline='') as csvfile1:
    reader = csv.reader(csvfile1, delimiter= ",")
    next(reader,None)
    for Row in reader:
        Emp_ID.append(Row[0])
        Name=Row[1].split(" ")
        First_Name.append(Name[0])
        Last_Name.append(Name[1])
        tempdob=Row[2].split("-")
        d=tempdob[2]
        tempdob[2]=tempdob[0]
        tempdob[0]=d 
        temp_join=tempdob
        temp_join='/'.join(temp_join)
        DOB.append(temp_join)
        tempssn=Row[3].split("-")
        tempssn[0]="***"
        tempssn[1]="***"
        tempssn_join="-".join(tempssn)
        SSN.append(tempssn_join)
        State.append(us_state_abbrev[Row[4]])
    pyboss=zip(Emp_ID,First_Name,Last_Name,DOB,SSN,State)

Pyboss_csv_path = os.path.join("pyboss.csv")
with open(Pyboss_csv_path,"w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Employee ID", "First Name", "Last Name", "DOB", "SSN", "State"])
    writer.writerows(pyboss)