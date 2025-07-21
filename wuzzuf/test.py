import wuzzuf

def titles():
    df = wuzzuf.scrap()
    titles = df['Title'].tolist()
    return titles

if __name__ == '__main__':
    print(titles())