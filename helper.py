from urlextract import URLExtract
extractor = URLExtract()

def fetch_stats(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user']==selected_user]
    num_messages = df.shape[0]

    words = []
    links = []
    gif_count = 0

    for message in df['message']:

        links.extend(extractor.find_urls(message))
        words.extend(message.split())

        if(message.endswith('omitted\r\n')):
            #print(repr(message))
            gif_count+=1

        
    return num_messages,len(words),gif_count,len(links)

def most_busy_users(df):
    x = df['user'].value_counts().head()
    return x

