from typing import List, Set, Dict, Tuple, Optional, Text
from operator import itemgetter

# import spacy package.

import spacy 

# Please fill in the following varibales. 
Name="Rachel_Hansen"
Email="rachelhansen@email.arizona.edu"
Collaborator="Shashi Armstrong"

# load  the small english core web model from spacy.

nlp = spacy.load("en_core_web_sm")

def tokenize_text(text: Text) -> List[Text]:
    """This functions tokenize a text by iterating 
            over its tokens by using spacy English tokenizer.
        =============
        Params:
            text
        Return:
            A list of tokenized items. ["token1, "token2"...etc]
    """
    doc = nlp(text)
    return([token.text for token in doc])
   
def recognize_name_entity(text: Text) -> List[Text]:
    """This function recognizes name entities in a text by using Spacy
        English tokenizer.
        #NOTE: Please read about converting span (span1, span2..etc)
                into list of strings ["span1", "span2"...etc].
        =============
        Params:
            text 
        Return:
            A list of tokenized name entities. ex: ['entity1', 'entity2'...etc] 
    """

    doc = nlp(text)
    return ([ent.text for ent in doc.ents])
   

def get_entity_labels(text: Text) -> List[Tuple[Text, Text]]:
    """This function obtains the labels of entities.
        #NOTE: Please read about the types of label methods in spacy. You should 
                return a string label rahter than an integer label. 
        =============
        Params:
            text 
        :Return:
            A list of tuples  of entities and its labels. 
            ex: [("entity1", "label1"), ("entity2", "label2")...etc]
    """

    doc = nlp(text)
    return ([(ent.text, ent.label_) for ent in doc.ents])

    
def get_lemmas(text: Text) -> List[Tuple[Text, Text]]:
    """This function finds  lemmas in a text by using Spacy 
        English tokenizer. It must return a token and its lemma.
        #NOTE: Please o read about the types of lemma methods in spacy. Your should  
                return a string lemma rahter than an integer lemma. 
        =============
        :Params:
            text 
        :Return:
            A list of of tuples of tokens and their stem. 
            ex: [('tokens', 'token'), ...etc] 
    """

    doc = nlp(text)
    return ([(token.text, token.lemma_) for token in doc])

def get_POS_tags(text: Text) ->  List[Tuple[Text, ...]]:
    """This function obtains  with its the associated POS and tags of each token 
        in a text by using Spacy tags.  It must return the verb itself, 
        part of of speech (POS), and the associated tag. 
        #NOTE: Read Spacy POS and assciated tags. 
    =============
        Params:
            text
        Return:
            A list of tuples of strings. ex: [('get', 'VERB', 'VB'),...etc] 
    """

    doc = nlp(text)
    return ([(token.text, token.pos_, token.tag_) for token in doc])
  

def pos_frequency(text: Text) ->  List[Tuple[Text, int]]:
    """This function returns frequency counts of part of speech (POS) 
        in a text. It must return the POS and its frequency. 
        #NOTE: Refer to couting in Spacy, count the frequencies of the given attributes, make a list of the dictionary of the POS
               and counts, then sort the list. Also, make sure to sort your output by the key.
        =============
        Params:
            text 
        Return:
            A sorted list  of tuples of strings and integers sorted by the key. ex: [('ADV', 2),...etc]
    """

    list = get_POS_tags(text)
    d = {}
    for i in list:
        if i[1] not in d.keys():
            d[i[1]] = 1
        else:
            d[i[1]] += 1
    list2 = []
    for k in d:
        list2.append((k, d[k]))
    return sorted(list2, key=lambda pos: pos[0])
    
def parse_dependency(text: Text) -> List[Tuple[Text, ...]]:
    """This function parse a single sentence.
    =============
        Params:
            text 
        Return:
            A list of tuples of strings. Ex: [('is', 'ROOT'), ...etc]
    """
    doc = nlp(text)
    return ([(token.text, token.dep_) for token in doc])

def count_dependency(text: Text) -> List[Tuple[Text, int]]:
    """This function extracts the dependencies of sentences  and thier frequenciesin a text. 
        It must return a parsed dependency and its frequency.
        #NOTE: Refer to couting in Spacy, count the frequencies of the given attributes, make a  list of the dictionary of the DEP
               and counts, then sort the list. Also, make sure to sort your output by the key. 
        ============
        Params:
            text 
        Return:
            A sorted list of tuples of strings and integers sorted by the key. Ex: [('ROOT', 1),...etc]
    """
    
    deps = parse_dependency(text)
    dict = {}
    for dep in deps:
        if dep[1] not in dict.keys():
            dict[dep[1]] = 1
        else:
            dict[dep[1]] += 1
    list3 = []
    for k in dict:
        list3.append((k, dict[k]))
    return sorted(list3, key=lambda tuple: tuple[0])
