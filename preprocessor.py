import pandas as pd
import re

def preprocessor(data):
    date_pattern = "\[\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{1,2}:\d{1,2}\s(?:PM|AM)\]\s"

    messages = re.split(date_pattern,data)[1:]
    dates = re.findall(date_pattern,data)
    dates = [d.replace('\u202f', ' ') for d in dates]

    df = pd.DataFrame({'user_message':messages,'message_date':dates})

    df['message_date'] = df['message_date'].str.strip().str.strip('[]')

    df['message_date'] = pd.to_datetime(
                                    df['message_date'],
                                    format='%d/%m/%y, %I:%M:%S %p'
                                    )
    
    users=[]
    messages=[]

    for msg in df['user_message']:
        entry = re.split('([\w\W]+?):\s',msg)
        if entry[1:]:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages

    df.drop(columns=['user_message'],inplace=True)

    df['month'] = df['message_date'].dt.month_name()
    df['day'] = df['message_date'].dt.day
    df['hour'] = df['message_date'].dt.hour
    df['minute'] = df['message_date'].dt.minute

    return df
