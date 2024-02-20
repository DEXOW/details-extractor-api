from src.extractor import DetailsExtractor

data = [
    "[VSC23-SAMP-1113-STEV] I want to book a flight for Steven, heading to Miami in 2 days.",
    "[VSC23-SAMP-1210-MARY] Can you arrange a flight to Bangkok for Mary on the 10th of December?",
    "[VSC23-SAMP-1113-JOHN] I’d like to make a reservation for John on a flight to Kansas next Monday.",
    "[VSC23-FG5Q-DUB7-JULY] Could you secure a flight to Dubai for Rachel on the 7th of July?",
    "[VSC23-FG5Q-GW12-LIS2] Please reserve a seat for Lisa on a flight to Glasgow in 12 days.",
    "[VSC23-FG5Q-5JAR-BOOK] Book a flight to Dublin departing on the 5th of January for Robert, if you could, please.",
    "[VSC23-FG5Q-MSAT-KUAL] Let's arrange a flight to Kuala Lumpur for Michael next Saturday, please.",
    "[VSC23-FG5Q-EMBA-20TH] I need a flight booking for Emily to Baghdad on the 20th."
]

for details in data:
    extractor = DetailsExtractor(details)
    print(extractor.extract())