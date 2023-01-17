import streamlit as st
import secrets
from random_word import Wordnik


wordnik_service = Wordnik()
r = Wordnik(api_key=st.secrets.WORDNIK_API) 



def generate_pw():
    letters = string.ascii_letters
    digits = string.digits  
    alphabet = letters + digits
    pwd_length = 10
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))

    return pwd

def generate_ps():
    r.get_random_words(minLength=7, maxLength=10, limit=50)
    pass
    #return passsentence
    




# # Return a single random word
# wordnik_service.get_random_word()
# # Return list of Random words
# wordnik_service.get_random_words()
# # Return Word of the day
# wordnik_service.word_of_the_day()