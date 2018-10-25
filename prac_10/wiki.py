import wikipedia

term = input("Please enter a search term: ")
while term != "":
    try:
        page = wikipedia.page(term)
        print(page.title)
        print(page.summary)
        print(page.url)
    except wikipedia.exceptions.DisambiguationError as error:
        print(error.options)
    except wikipedia.exceptions.PageError:
        print("{} page does not exist on WikiPedia")
    term = input("Please enter a search term: ")
