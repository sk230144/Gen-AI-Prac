"""
Step 1 — 100 sentences across 5 topics.
20 sentences per topic, clearly distinct subject matter, so that clustering
in later steps has a real, visible signal to detect.
"""

SENTENCES_BY_TOPIC = {
    "cooking": [
        "Add a pinch of salt to bring out the flavor of the soup.",
        "Preheat the oven to 180 degrees before baking the cake.",
        "Chop the onions finely for the curry base.",
        "Marinate the chicken overnight for the best taste.",
        "Simmer the sauce on low heat until it thickens.",
        "Whisk the eggs until they turn light and fluffy.",
        "Use fresh basil to garnish the pasta dish.",
        "Knead the dough for ten minutes until smooth.",
        "Grill the vegetables until they are slightly charred.",
        "Season the steak generously with salt and pepper.",
        "Boil the pasta until it's al dente.",
        "Fold the batter gently to keep the cake airy.",
        "Roast the nuts in a dry pan until golden.",
        "Deglaze the pan with white wine after searing the meat.",
        "Let the bread cool before slicing it.",
        "Blend the mango with yogurt for a quick smoothie.",
        "Sprinkle some cheese on top before broiling.",
        "Sauté the garlic until it becomes fragrant.",
        "Chill the dessert in the fridge for two hours.",
        "Slice the tomatoes thinly for the salad.",
    ],
    "sports": [
        "The striker scored a stunning goal in the final minute.",
        "She trained for months before the marathon.",
        "The team celebrated their championship win on the field.",
        "He broke the national record in the 100m sprint.",
        "The coach called a timeout during the final quarter.",
        "The crowd cheered as the batter hit a home run.",
        "The goalkeeper made an incredible diving save.",
        "The player was substituted due to a minor injury.",
        "The tennis match went into a tense tiebreaker.",
        "The team practiced their defense all week.",
        "The referee awarded a penalty kick in the second half.",
        "She won the gold medal in the swimming relay.",
        "The boxer trained hard for the upcoming title fight.",
        "The cyclist finished the race just seconds ahead.",
        "The basketball team executed a perfect fast break.",
        "He dribbled past three defenders before shooting.",
        "The stadium was packed for the derby match.",
        "The athlete stretched before the long jump event.",
        "The captain motivated the team before kickoff.",
        "The umpire reviewed the play on the big screen.",
    ],
    "technology": [
        "The new smartphone features a faster processor.",
        "Developers deployed the update to fix the security bug.",
        "The app uses machine learning to recommend content.",
        "Cloud storage makes it easy to access files anywhere.",
        "The startup raised funding to build its AI platform.",
        "Engineers optimized the database for faster queries.",
        "The software update improved battery life significantly.",
        "The company launched a new wearable fitness tracker.",
        "Developers use version control to manage code changes.",
        "The website experienced downtime during the server migration.",
        "The chatbot can answer customer questions instantly.",
        "The team built an API to connect the two systems.",
        "The laptop comes with a high-resolution display.",
        "Data scientists trained the model on millions of images.",
        "The app was redesigned with a simpler user interface.",
        "The router provides stable Wi-Fi throughout the house.",
        "The company patched the vulnerability within hours.",
        "The new chip improves performance while using less power.",
        "The platform supports integration with third-party tools.",
        "Engineers tested the app across multiple devices.",
    ],
    "travel": [
        "We booked a flight to explore the mountains next month.",
        "The hotel offered a stunning view of the beach.",
        "She backpacked across Europe during her summer break.",
        "The train ride through the countryside was breathtaking.",
        "They visited an ancient temple during their trip.",
        "The tour guide showed us the city's historic landmarks.",
        "We rented a car to drive along the coastal highway.",
        "The airport was crowded during the holiday season.",
        "He explored local markets to try authentic street food.",
        "The cruise stopped at three different islands.",
        "We hiked to the waterfall early in the morning.",
        "The resort included an all-inclusive dining package.",
        "They took a scenic boat ride across the lake.",
        "The passport control line moved faster than expected.",
        "We stayed in a cozy cabin near the ski slopes.",
        "The city was famous for its vibrant nightlife.",
        "She packed light for the weekend getaway.",
        "The road trip took us through five different states.",
        "We watched the sunset from the rooftop café.",
        "The travel agency planned our entire itinerary.",
    ],
    "finance": [
        "The company reported strong quarterly earnings.",
        "Investors reacted positively to the interest rate cut.",
        "She opened a savings account to build an emergency fund.",
        "The stock market rallied after the economic report.",
        "He diversified his portfolio to reduce investment risk.",
        "The bank approved the loan after reviewing the application.",
        "The startup secured a new round of venture funding.",
        "Inflation numbers came in lower than analysts expected.",
        "The mutual fund posted solid returns this year.",
        "They budgeted carefully to save for a down payment.",
        "The central bank raised interest rates to control inflation.",
        "The company's stock price dropped after the earnings miss.",
        "She consulted a financial advisor about retirement planning.",
        "The merger increased the company's market share.",
        "Credit card debt can quickly accumulate high interest.",
        "The exchange rate affected the cost of imported goods.",
        "He invested in index funds for long-term growth.",
        "The startup's valuation doubled after the latest round.",
        "The government announced a new tax relief policy.",
        "Analysts predict steady growth in the tech sector.",
    ],
}


def get_all_sentences():
    """Returns (sentences, labels) — flattened lists, same order/index."""
    sentences = []
    labels = []
    for topic, sents in SENTENCES_BY_TOPIC.items():
        sentences.extend(sents)
        labels.extend([topic] * len(sents))
    return sentences, labels


if __name__ == "__main__":
    sentences, labels = get_all_sentences()
    print(f"Total sentences: {len(sentences)}")
    print(f"Topics: {set(labels)}")
