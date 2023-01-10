from xml.etree import ElementTree

# parse the XML file
tree = ElementTree.parse("C:\\Users\\Matt\\Documents\\John Lydgate Works Text Files\\Python scripts and instructions\\MED_wordlist.xml")

# Create a dictionary to store the key/value pairs
MED_wordlist = {}

# Iterate over the `item` elements in the tree
for item in tree.iter('item'):
  # Get the `id` attribute of the `item` element
  key = item.get('id')

  # Create a list to store the values and the words
  values = []
  words = []

  # Get the `headword` element
  headword = item.find('headword')

  # If the `headword` element is not empty, add its text to the list of values
  if headword is not None:
    words.append(headword.text)

  # Iterate over the `variant` elements
  for variant in item.iter('variant'):
    # If the `variant` element is not empty, add its text to the list of values
    if variant is not None:
      words.append(variant.text)

  # Append the words list to the values list
  values.append({'words': words})

  # Get the `speech_part` element
  speech_part = item.find('speech_part')

  # If the `speech_part` element is not empty, add its text as a dictionary with the 'pos' keyword to the list of values
  if speech_part is not None:
    values.append({'pos': speech_part.text})

  # Add the key/value pair to the dictionary
  MED_wordlist[key] = values

MED_words = []
for key in MED_wordlist:
	words = MED_wordlist[key][0]['words']
	MED_words.extend(words)





import Levenshtein

def spellchecker(word, word_list):
    closest_match = ""
    min_distance = float("inf")
    for w in word_list:
        distance = Levenshtein.distance(word, w)
        if distance < min_distance:
            min_distance = distance
            closest_match = w
    if closest_match:
        return closest_match
    else:
        return "no result"


	
