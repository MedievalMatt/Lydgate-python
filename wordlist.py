from xml.etree import ElementTree

# parse the XML file
tree = ElementTree.parse("C:\Users\Matt\Documents\John Lydgate Works Text Files\Python scripts and instructions\MED_wordlist.xml")

# find all `item` elements underneath the `ROOT` element
items = tree.findall("ROOT/item")

# create an empty dictionary to store the results
MED_wordlist = {}

# iterate over the `item` elements
for item in items:
  # get the value of the `id` attribute of the `item` element
  id = item.attrib["id"]

  # create an empty dictionary to store the values of the `item` element's children
  values = {}
  
  # iterate over the children of the `item` element
  for child in item:
    # check the name of the child element
    if child.tag == "headword":
      # if the child is a `headword` element, store its text value under the key "word"
      values["word"] = child.text
    elif child.tag == "speech_part":
      # if the child is a `speech_part` element, store its text value under the key "pos"
      values["pos"] = child.text
    elif child.tag == "variant":
      # if the child is a `variant` element, store its text value under the key "word"
      values["word"] = child.text

  # add the values dictionary to the MED_wordlist dictionary using the `id` value as the key
  MED_wordlist[id] = values
