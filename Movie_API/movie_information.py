import requests

def get_movie_information(title):
    # request with title and year
    # url = f"http://www.omdbapi.com/?i=tt3896198&apikey=c89b4ee&t={title}&y={year}"

    # request with only title 
    url = f"http://www.omdbapi.com/?i=tt3896198&apikey=c89b4ee&t={title}"

    response = requests.get(url)
    data = response.json()
    if response.status_code == 200 :
        for i in data:
            print(f"{i}:- {data[i]}")

    else:
        print(f"Error: {data['Error']}")
    
title = input("Enter the Movie Name:- ")

get_movie_information(title)
