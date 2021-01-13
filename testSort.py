import pandas as pd

people = {
    'first': ['Corey', 'Jane', 'John'], 
    'last': ['Schafer', 'Doe', 'Doe'], 
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@email.com', 'JohnDoe@email.com']
}

df = pd.DataFrame(people)
df['full_name'] = df['first'] + ' ' + df['last']

print(df)