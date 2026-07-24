#Version1
# # services/capability_service.py

# WEATHER = "weather"
# MARKET = "market"
# DISEASE = "disease"
# PEST = "pest"
# SCHEME = "scheme"
# FARM = "farm"
# GENERAL = "general"


# keywords = {

#     WEATHER: [
#         "rain",
#         "weather",
#         "temperature",
#         "humidity",
#         "wind",
#         "irrigation",
#         "irrigate",
#         "water"
#     ],

#     MARKET: [
#         "price",
#         "market",
#         "sell",
#         "buy",
#         "mandi",
#         "harvest"
#     ],

#     DISEASE: [
#         "disease",
#         "yellow",
#         "spot",
#         "fungus",
#         "blight",
#         "rot"
#     ],

#     PEST: [
#         "pest",
#         "insect",
#         "worm",
#         "bug",
#         "pesticide",
#         "spray"
#     ],

#     SCHEME: [
#         "scheme",
#         "subsidy",
#         "government",
#         "loan",
#         "insurance"
#     ],

#     FARM: [
#         "crop",
#         "soil",
#         "fertilizer",
#         "seed",
#         "farm"
#     ]
# }


# def detect_capabilities(question: str):

#     # Convert to lowercase
#     question = question.lower()

#     capabilities = []

#     # Loop through every capability
#     for capability, words in keywords.items():

#         # Loop through every keyword
#         for word in words:

#             # Check if keyword exists in question
#             if word in question:

#                 capabilities.append(capability)

#                 # No need to check remaining words
#                 break

#     # Nothing matched
#     if not capabilities:
#         capabilities.append(GENERAL)

#     return capabilities



#Version2

import re


WEATHER = "weather"
MARKET = "market"
DISEASE = "disease"
PEST = "pest"
SCHEME = "scheme"
FARM = "farm"
GENERAL = "general"


capability_keywords = {

    WEATHER: [
        "rain",
        "weather",
        "temperature",
        "humidity",
        "wind",
        "irrigation",
        "irrigate",
        "water"
    ],

    MARKET: [
        "price",
        "market",
        "sell",
        "buy",
        "mandi",
        "harvest"
    ],

    DISEASE: [
        "disease",
        "yellow",
        "spot",
        "fungus",
        "blight",
        "rot"
    ],

    PEST: [
        "pest",
        "insect",
        "worm",
        "bug",
        "pesticide",
        "spray"
    ],

    SCHEME: [
        "scheme",
        "subsidy",
        "government",
        "loan",
        "insurance"
    ],

    FARM: [
        "crop",
        "soil",
        "fertilizer",
        "seed",
        "farm"
    ]
}

def detect_capabilities(question: str):

    question = question.lower()

    # Remove punctuation
    question = re.sub(r"[^\w\s]", "", question)

    # Split into words
    question_words = question.split()

    capabilities = []

    for capability, keywords in capability_keywords.items():

        for keyword in keywords:

            if keyword in question_words:

                capabilities.append(capability)
                break

    if not capabilities:
        capabilities.append(GENERAL)

    return capabilities