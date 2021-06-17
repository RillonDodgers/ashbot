from app.Quote import Quote

quotes = Quote.all()
for quote in quotes:
    print(quote.quote)
