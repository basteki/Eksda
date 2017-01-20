class adult:
    def __init__(self, age, workclass, fnlwgt, education, education_num, marital_status, occupation, relationship, race,
                 sex, capital_gain, capital_loss, hours_per_week, native_country, income):
        self.age = age
        self.workclass = workclass
        self.fnlwgt = fnlwgt
        self.education_num = education_num
        self.marital_status = marital_status
        self.occupation = occupation
        self.relationship = relationship
        self.race = race
        self.sex = sex
        self.capital_gain = capital_gain
        self.capital_loss = capital_loss
        self.hours_per_hour = hours_per_week
        self.native_country = native_country
        self.income = income

        def displayCount(self):
            print("Total adults %d" % adult.empCount)

        def getAge(self):
            return self.age


data = open('adult.csv', 'r')

adultList = []

for line in data:
    extracted_data = line.split(',', 14)

    adultList.append(adult(extracted_data[0].replace('"', ''),
                           extracted_data[1].replace('"', ''),
                           extracted_data[2].replace('"', ''),
                           extracted_data[3].replace('"', ''),
                           extracted_data[4].replace('"', ''),
                           extracted_data[5].replace('"', ''),
                           extracted_data[6].replace('"', ''),
                           extracted_data[7].replace('"', ''),
                           extracted_data[8].replace('"', ''),
                           extracted_data[9].replace('"', ''),
                           extracted_data[10].replace('"', ''),
                           extracted_data[11].replace('"', ''),
                           extracted_data[12].replace('"', ''),
                           extracted_data[13].replace('"', ''),
                           extracted_data[14].replace('"', '')
                           )
                     )

# Otrzymaliśmy listę ponad 32 tysięcy obiektów możnaby odczytywać ich parametry następująco
# for obj in adultList:
#      print(obj.workclass)

# a poważnie mówiąc aby zrozumieć najprostsze zależności w bazie możemy sporządzić małą statystykę
# względem poszczególnych parametrów, np procent ludzi o różnym wieku zarabiających powyżej  naszego progu.


ser1 = pd.read_table('adult.csv', sep=',')
# print(ser1)
ser1['age']

ageOver = []
ageUnder = []

i = 0
while (i < 99):
    ageOver.append(0)
    ageUnder.append(0)
    i += 1

over = '>50K'
under = '<=50K'
from collections import Counter

for obj in adultList:
    # Counter(obj.income) == Counter(over)
    if (str(obj.income) == str(over)):
        # ageOver[obj.age] += 1
        print("Yes")
    if (str(obj.income) == str(under)):
        # ageUnder[obj.age] += 1
        print("No")
ageOverPercentage = []


# for a in ageOver:
#     total = ageOver[a]+ageUnder[a]
#     ageOverPercentage[a] = ageOver[a]/total*100
#     print(ageOverPercentage[a])


