
import re

def analyze_sentiment(text):
    # Convert text to lowercase for uniformity
    text_lower = text.lower()
    words = text_lower.split()  # Tokenizing words from text
    
    # Define word sentiment dictionaries with weights
    positive_words = {
    'trendy': 4, 'quick-witted': 2, 'leading': 4, 'humorous': 3, 'splendid': 3,
    'trendsetting': 3, 'charitable': 2, 'chosen': 2, 'noble': 3, 'unstoppable': 4,
    'sovereign': 2, 'spectacular': 3, 'zen': 3, 'courageous': 4, 'prosperous': 2,
    'wholesome': 3, 'celestial': 4, 'cherished': 3, 'hardy': 3, 'swanky': 3,
    'adorable': 3, 'glowing': 3, 'unorthodox': 4, 'tenacious': 3, 'mind-blowing': 3,
    'hysterical': 4, 'daring': 2, 'accomplished': 3, 'radiating': 2, 'superb': 3,
    'best': 3, 'dynamic': 3, 'sharp': 2, 'resourceful': 3, 'refreshing': 2,
    'perfect': 3, 'cheer': 2, 'peerless': 3, 'victory': 3, 'blissful': 3,
    'versatile': 2, 'suave': 3, 'undaunted': 2, 'powerful': 3, 'invincible': 2,
    'wise': 2, 'state-of-the-art': 3, 'helpful': 3, 'kindhearted': 4, 'groundbreaking': 3,
    'graced': 4, 'warm': 2, 'excellent': 3, 'cool': 2, 'elated': 3, 'cultured': 4,
    'conqueror': 4, 'ethereal': 3, 'heartwarming': 4, 'outstanding': 2, 'driven': 3,
    'profound': 2, 'joy': 2, 'success': 4, 'prolific': 2, 'optimistic': 3,
    'peaceful': 3, 'electrifying': 3, 'polite': 4, 'intellectual': 3, 'reliable': 2,
    'content': 3, 'happy': 2, 'luxurious': 3, 'supreme': 4, 'legendary': 3,
    'chirpy': 4, 'steadfast': 4, 'pristine': 3, 'unbreakable': 3, 'charming': 3,
    'gifted': 2, 'sophisticated': 3, 'selfless': 4, 'perpetual': 2, 'transcendent': 4,
    'holy': 3, 'infinite': 2, 'masterful': 3, 'fighter': 3, 'divine': 3,
    'lovable': 2, 'serendipitous': 3, 'delightful': 2, 'sublime': 4, 'affluent': 4,
    'marvelous': 3, 'magnificent': 3, 'great': 2, 'honorable': 3, 'gentle': 2,
    'euphoric': 4, 'privileged': 2, 'serene': 4, 'spunky': 3, 'compassionate': 4,
    'loyal': 2, 'nice': 4, 'empowered': 2, 'joyful': 2, 'fantabulous': 2,
    'royal': 3, 'esteemed': 4, 'bold': 3, 'wonderful': 4, 'magical': 3,
    'paramount': 2, 'innovative': 3, 'jazzy': 4, 'boundless': 3, 'glorious': 4,
    'eternal': 2, 'strong': 3, 'vivacious': 4, 'refined': 4, 'mindful': 4,
    'adventurous': 2, 'awesome': 3, 'visionary': 3, 'ambitious': 4, 'enthusiastic': 2,
    'exuberant': 4, 'miraculous': 3, 'dominant': 2, 'cutting-edge': 4,
    'forward-thinking': 2, 'giving': 4, 'audacious': 2, 'favored': 4, 'skilled': 4,
    'fun': 2, 'future-oriented': 4, 'joyous': 3, 'adoring': 2, 'hopeful': 4,
    'flawless': 3, 'friendly': 3, 'tranquil': 3, 'passionate': 2, 'persistent': 2,
    'spellbinding': 3, 'unwavering': 3, 'adaptable': 4, 'survivor': 4, 'radiant': 3,
    'happiness': 3, 'grateful': 3, 'modern': 4, 'champion': 4, 'poised': 4,
    'gracious': 3, 'inspiring': 3, 'cordial': 2, 'sunny': 2, 'adept': 2,
    'hospitable': 4, 'peppy': 2, 'bubbly': 2, 'vibrant': 2, 'glamorous': 3,
    'valiant': 2, 'harmonious': 3, 'uplifting': 3, 'charismatic': 2, 'fearless': 3,
    'irreplaceable': 2, 'chic': 2, 'fortunate': 4, 'immortal': 2, 'amiable': 4,
    'rugged': 4, 'exquisite': 3, 'enchanting': 3, 'distinguished': 3, 'clever': 3,
    'unforgettable': 3, 'nonconventional': 2, 'sacred': 4, 'soothing': 2,
    'thankful': 3, 'relentless': 2, 'genius': 3, 'mesmerizing': 4, 'revolutionary': 2,
    'focused': 3, 'fated': 4, 'multifaceted': 2, 'fantastic': 2, 'resilient': 2,
    'favorite': 2, 'courteous': 3, 'heroic': 3, 'celebration': 4, 'thrilled': 3,
    'amazing': 3, 'gorgeous': 4, 'zesty': 4, 'ecstatic': 3, 'pioneering': 2,
    'philosophical': 4, 'indomitable': 4, 'lucky': 3, 'unfading': 3,
    'trailblazing': 3, 'exceptional': 2, 'satisfying': 2, 'energized': 4,
    'exciting': 3, 'delicious': 3, 'impressive': 2, 'far-sighted': 4,
    'notable': 2, 'flourishing': 3, 'fascinating': 2, 'faithful': 3,
    'trustworthy': 2, 'elegant': 2, 'groovy': 4, 'considerate': 3,
    'divinely-inspired': 3, 'nutritious': 3, 'admired': 4, 'hypnotic': 4,
    'gritty': 2, 'blessed': 4, 'resolute': 4, 'goal-oriented': 3,
    'creative': 3, 'ceaseless': 4, 'celebrated': 4, 'respectable': 3,
    'wealthy': 2, 'sociable': 3, 'revered': 2, 'brave': 3, 'motivated': 2,
    'illustrious': 4, 'phenomenal': 4, 'polished': 3, 'stylish': 3,
    'unparalleled': 4, 'well-mannered': 3, 'cheerful': 3, 'determined': 3,
    'priceless': 3, 'respected': 2, 'calm': 3, 'snazzy': 2, 'achiever': 4,
    'classy': 2, 'graceful': 2, 'breathtaking': 3, 'dashing': 4, 'hallowed': 4,
    'invaluable': 3, 'knowledgeable': 2, 'monumental': 4, 'matchless': 4,
    'talented': 2, 'avant-garde': 4, 'remarkable': 2, 'heavenly': 4,
    'welcoming': 3, 'smile': 4, 'limitless': 4, 'warrior': 4, 'imaginative': 3
}
    negative_words = {
    # General negativity
    "bad": -2, "terrible": -3, "horrible": -3, "awful": -3, "worst": -4, "disgusting": -4, "ugly": -2,
    "hate": -3, "angry": -2, "furious": -4, "miserable": -3, "sad": -2, "depressed": -4, "annoying": -2,
    "frustrating": -3, "irritating": -2, "stupid": -3, "dumb": -3, "idiotic": -3, "nonsense": -2,
    "pathetic": -3, "ridiculous": -2, "foolish": -2, "hopeless": -3, "useless": -3, "worthless": -4,
    
    # Pain and suffering
    "painful": -3, "hurtful": -3, "hateful": -4, "sickening": -4, "horrendous": -4, "nightmare": -4,
    "failure": -3, "loser": -3, "disappointing": -2, "absurd": -2, "nasty": -3, "dreadful": -3,
    "shameful": -3, "embarrassing": -2, "cringe": -2, "garbage": -3, "trash": -3,
    
    # Violence and brutality
    "brutal": -3, "vicious": -3, "hostile": -3, "toxic": -3, "poisonous": -3, "savage": -3,
    "abusive": -4, "controlling": -3, "manipulative": -3, "oppressive": -3, "exploitive": -3,
    
    # Deception and betrayal
    "betrayal": -3, "deceit": -3, "liar": -3, "dishonest": -3, "cheater": -3, "fraud": -3, "scammer": -3,
    
    # Fear and anxiety
    "terrifying": -3, "frightening": -3, "shocking": -2, "scary": -3, "ghastly": -3, "gruesome": -3,
    "creepy": -2, "disturbing": -3, "suffocating": -3, "claustrophobic": -3,
    
    # Social rejection
    "abandoned": -3, "forsaken": -3, "neglected": -3, "rejected": -3, "ostracized": -3,
    "excluded": -3, "isolated": -3, "alone": -3, "lonely": -3, "friendless": -3, "unwanted": -3,
    
    # Weakness and failure
    "broken": -3, "damaged": -3, "flawed": -2, "imperfect": -2, "weak": -2, "frail": -2,
    "helpless": -3, "powerless": -3, "incompetent": -3, "clumsy": -2, "unskilled": -2, "lazy": -2,
    
    # Arrogance and selfishness
    "arrogant": -2, "selfish": -2, "narcissistic": -3, "greedy": -3, "mean": -3, "ruthless": -3,
    "merciless": -3, "insensitive": -2, "ungrateful": -2,
    
    # Prejudice and discrimination
    "biased": -3, "prejudiced": -3, "racist": -4, "sexist": -4, "misogynistic": -4, "homophobic": -4,
    
    # Doom and despair
    "hopeless": -3, "despair": -3, "melancholy": -2, "heartbroken": -3, "devastated": -4,
    "shattered": -4, "crushed": -3, "ruined": -3, "destroyed": -4,}   
    neutral_words = {
    "book", "table", "chair", "window", "door", "pen", "paper", "bottle", 
    "glass", "room", "floor", "ceiling", "wall", "car", "bus", "train", 
    "road", "bridge", "river", "tree", "plant", "grass", "cloud", "sky", 
    "star", "moon", "sun", "ocean", "sea", "lake", "mountain", "hill", 
    "valley", "city", "village", "town", "country", "continent", "earth", 
    "world", "planet", "galaxy", "universe", "computer", "laptop", "phone", 
    "tablet", "screen", "monitor", "keyboard", "mouse", "speaker", "microphone", 
    "camera", "watch", "clock", "calendar", "day", "night", "morning", "afternoon", 
    "evening", "week", "month", "year", "decade", "century", "time", "moment", 
    "second", "minute", "hour", "human", "person", "man", "woman", "child", 
    "boy", "girl", "adult", "teenager", "baby", "family", "friend", "neighbor", 
    "colleague", "teacher", "student", "doctor", "nurse", "engineer", "scientist", 
    "artist", "musician", "writer", "actor", "director", "chef", "worker", "farmer", 
    "police", "firefighter", "soldier", "pilot", "driver", "athlete", "coach", 
    "referee", "judge", "lawyer", "politician", "leader", "follower", "citizen", 
    "traveler", "tourist", "customer", "shopkeeper", "business", "company", "store", 
    "market", "mall", "restaurant", "cafe", "hotel", "resort", "hospital", "clinic", 
    "office", "factory", "farm", "school", "college", "university", "library", 
    "museum", "theater", "stadium", "gym", "park", "playground", "zoo", "aquarium", 
    "airport", "station", "harbor", "dock", "bridge", "tunnel", "road", "street", 
    "highway", "intersection", "traffic", "signal", "sign", "bus stop", "train station", 
    "airport terminal", "runway", "platform", "track", "railway", "car", "bike", "bicycle", 
    "motorcycle", "scooter", "truck", "van", "boat", "ship", "submarine", "aeroplane", 
    "helicopter", "rocket", "spacecraft", "satellite", "planet", "asteroid", "comet", 
    "star", "galaxy", "black hole", "universe", "gravity", "physics", "chemistry", 
    "biology", "mathematics", "algebra", "geometry", "trigonometry", "calculus", 
    "statistics", "probability", "science", "experiment", "lab", "research", "discovery", 
    "innovation", "technology", "engineering", "medicine", "health", "disease", "treatment", 
    "vaccine", "cure", "surgery", "therapy", "exercise", "fitness", "nutrition", 
    "diet", "food", "meal", "breakfast", "lunch", "dinner", "snack", "fruit", "vegetable", 
    "meat", "fish", "chicken", "egg", "milk", "cheese", "bread", "butter", "jam", 
    "honey", "sugar", "salt", "pepper", "spice", "herb", "tea", "coffee", "juice", 
    "water", "soda", "soft drink", "wine", "beer", "cocktail", "beverage", "liquid", 
    "solid", "gas", "air", "fire", "earth", "metal", "wood", "plastic", "glass", 
    "ceramic", "fabric", "paper", "cardboard", "cloth", "cotton", "silk", "wool", 
    "leather", "rubber", "stone", "rock", "sand", "dust", "mud", "clay", "brick", 
    "cement", "concrete", "iron", "steel", "copper", "gold", "silver", "platinum", 
    "diamond", "gem", "crystal", "jewel", "pearl", "currency", "money", "coin", 
    "banknote", "wallet", "purse", "account", "finance", "economy", "trade", "business", 
    "market", "investment", "stock", "share", "bond", "fund", "loan", "debt", "income", 
    "expense", "profit", "loss", "salary", "wage", "earnings", "price", "cost", "budget", 
    "tax", "bill", "receipt", "payment", "purchase", "sale", "discount", "offer", "deal", 
    "contract", "agreement", "law", "policy", "rule", "regulation", "constitution", "government", 
    "state", "nation", "country", "city", "province", "district", "region", "territory", 
    "population", "community", "society", "culture", "tradition", "custom", "belief", 
    "religion", "faith", "philosophy", "ethics", "morality", "justice", "rights", 
    "freedom", "equality", "democracy", "politics", "leader", "president", "minister", 
    "governor", "mayor", "citizen", "voter", "party", "campaign", "election", "debate", 
    "speech", "media", "journalism", "news", "broadcast", "radio", "television", "newspaper", 
    "magazine", "article", "headline", "report", "story", "interview", "press", "conference", 
    "statement", "announcement", "editorial", "commentary", "opinion", "analysis", 
    "review", "summary", "survey", "poll", "data", "statistics", "trend", "pattern", 
    "forecast", "prediction", "hypothesis", "experiment", "research", "study", 
    "publication", "academic", "university", "college", "school", "education", 
    "teacher", "student", "professor", "lecture", "class", "lesson", "homework", 
    "assignment", "exam", "test", "grade", "score", "diploma", "degree", "certificate", 
    "scholarship", "internship", "career", "job", "occupation", "work", "employment", 
    "profession", "business", "entrepreneur", "startup", "industry", "company", 
    "corporation", "enterprise", "organization", "institution", "agency", "department", 
    "office", "workplace", "factory", "shop", "store", "mall", "market", "warehouse", 
    "transport", "travel", "journey", "trip", "vacation", "holiday", "tour", "destination", 
    "landmark", "attraction", "resort", "hotel", "camping", "adventure", "exploration"
}
    # Define sarcastic phrases
    sarcastic_phrases = {
    "yeah right", "oh great", "just great", "totally", "obviously", "sure", "as if", "of course", "perfect",
    "thanks a lot", "nice job", "well done", "fantastic", "brilliant", "oh wow", "good for you", 
    "congratulations", "just what I needed", "what a surprise", "lucky me", "love that", "how wonderful", 
    "must be nice", "so original", "oh joy", "such a genius", "exactly what I wanted", "wow amazing"
}
    
    # Count occurrences of positive and negative words
    positive_count = sum(1 for word in words if word in positive_words)
    negative_count = sum(1 for word in words if word in negative_words)
    neutral_count = sum(1 for word in words if word not in positive_words and word not in negative_words)

    # Simple Sentiment Classification
    if positive_count > negative_count:
        simple_sentiment = "Positive"
    elif negative_count > positive_count:
        simple_sentiment = "Negative"
    else:
        simple_sentiment = "Neutral"

    # Weighted Sentiment Score
    weighted_score = sum(positive_words.get(word, 0) for word in words) - sum(negative_words.get(word, 0) for word in words)

    # Weighted Sentiment Classification
    if weighted_score > 0:
        weighted_sentiment = "Positive"
    elif weighted_score < 0:
        weighted_sentiment = "Negative"
    else:
        weighted_sentiment = "Neutral"

    # Sarcasm Detection
    sarcastic = False

    # Rule 1: Detect common sarcastic phrases in text
    for phrase in sarcastic_phrases:
        if phrase in text_lower:
            sarcastic = True
            break

    # Rule 2: Contradictory Sentiments in Consecutive Sentences
    sentences = re.split(r'[.!?]', text)  # Split into sentences
    for i in range(len(sentences) - 1):
        sent1 = sentences[i].strip()
        sent2 = sentences[i + 1].strip()

        pos1 = sum(1 for word in sent1.split() if word in positive_words)
        neg1 = sum(1 for word in sent1.split() if word in negative_words)
        pos2 = sum(1 for word in sent2.split() if word in positive_words)
        neg2 = sum(1 for word in sent2.split() if word in negative_words)

        # Detect sarcasm if a positive sentiment is followed by a negative one or vice versa
        if (pos1 > 0 and neg2 > 0) or (neg1 > 0 and pos2 > 0):
            sarcastic = True
            break

    # Rule 3: Presence of Exaggerated Words or Emphasis
    emphasis_words = {"literally", "seriously", "totally", "absolutely", "completely"}
    if any(word in emphasis_words for word in words):
        sarcastic = True

    # If sarcasm is detected, invert sentiment
    if sarcastic:
        if weighted_sentiment == "Positive":
            weighted_sentiment = "Negative"
        elif weighted_sentiment == "Negative":
            weighted_sentiment = "Positive"

    return {
    "simple_sentiment": simple_sentiment,
    "weighted_sentiment": weighted_sentiment,
    "weighted_score": weighted_score,
    "neutral_count": neutral_count,
    "is_sarcastic": sarcastic
    }


# Example usage
text = input('enter the sentence : ')
result = analyze_sentiment(text)
print(result)
