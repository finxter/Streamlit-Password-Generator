import streamlit as st
import secrets
from random_word import Wordnik
import string
from random_word import ApiNinjas
import requests

#---WORDNIK API, TO BE IMPLEMENTED---#
wordnik_service = Wordnik()
r = Wordnik(api_key=st.secrets.WORDNIK_API) 


#---STREAMLIT SETTINGS---#
page_title = "PW & PW-Sentence Generator"
page_icon = ":building_construction:"
layout = "centered"

if "pw" not in st.session_state:
    st.session_state["pw"] = ''

#---PAGE CONFIG---#
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)


#---PW GENERATOR FUNCTIONS--#
def generate_pw()->None:
    """Uses the string module to get the letters and digits that make up the alphabet uses to generate the random characters. These characters are 
    appended to the pwd string which is then assigned to the session_state variable [pw]"""
    letters = string.ascii_letters
    digits = string.digits  
    alphabet = letters + digits
    pwd_length = 14
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))

    st.session_state["pw"] = pwd

#---Currently API Ninja Random Word API is used to accomplish generating the random words---#
def get_random_word()->str:
    """Uses the API Ninja API to request a word string. This string is then parsed to extract only the word and return it."""
    api_url = 'https://api.api-ninjas.com/v1/randomword'
    response = requests.get(api_url, headers={'X-Api-Key': st.secrets.API_NINJA})
    if response.status_code == requests.codes.ok:
        word_dict = response.text.split(":")
        word_dict = word_dict[1]
        word_dict  = word_dict[2:-2]
        return word_dict
    else:
        return "Error:", response.status_code, response.text

def generate_ps()->None:
    """Uses the get_random_word function to request five words. These are concatenated into a string with dashes and then 
    assigned these to the session_state variable [pw] """
    passphrase = ""
    for x in range(5):
        passphrase += f"{get_random_word()}-"
    passphrase_final = passphrase[:-1]  
    st.session_state["pw"] = passphrase_final

#---MAIN PAGE---#
"#"
st.title(f"{page_icon} {page_title}")
"#"

"---"
col1,col2 = st.columns([4,4], gap = "large")

with col1:
    st.caption("Secure password length is set at 14 chars.")
    st.button("Generate secure password", key = "pw_button", on_click = generate_pw)

with col2:
    st.caption("Secure passphrase length is set at 5 words.")
    st.button("Generate secure password sentence", key = "ps_button", on_click = generate_ps)
"#"
"#"
ocol1, ocol2, ocol3 = st.columns([1,4,1])
with ocol1:
    ''
with ocol2:
    st.caption("Generated secure PW")
    "---"
    st.subheader(st.session_state["pw"])
    "---"
    
with ocol3:
    ''
