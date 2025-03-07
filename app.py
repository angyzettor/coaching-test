{\rtf1\ansi\ansicpg1252\cocoartf2758
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 AppleColorEmoji;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
import random\
\
# Fonction pour g\'e9n\'e9rer une r\'e9ponse du coach IA avec recommandations pratiques\
def coaching_response(user_input):\
    responses = \{\
        "gestion du stress": [\
            "Prenez 5 minutes pour respirer profond\'e9ment et vous recentrer. Exercice : Inspirez 4 secondes, retenez 4 secondes, expirez 4 secondes.",\
            "Essayez la m\'e9ditation en pleine conscience pendant 10 minutes. Application recommand\'e9e : Headspace.",\
            "Faites une pause active : marchez 5 minutes en ext\'e9rieur pour oxyg\'e9ner votre cerveau."\
        ],\
        "prise de d\'e9cision": [\
            "Utilisez la matrice d\'e9cisionnelle : \'e9crivez les avantages et les inconv\'e9nients sur une feuille.",\
            "Posez-vous la question : 'Quelle est la pire chose qui pourrait arriver ?' Cela aide \'e0 relativiser.",\
            "Faites un test rapide : demandez-vous si cette d\'e9cision aura encore de l'importance dans 1 an."\
        ],\
        "leadership": [\
            "Un bon leader \'e9coute activement avant de parler. Exercice : Reformulez ce que votre interlocuteur dit avant de r\'e9pondre.",\
            "Valorisez vos \'e9quipes en leur donnant du feedback positif sp\'e9cifique : 'J'ai appr\'e9ci\'e9 ton implication sur ce projet parce que\'85'",\
            "Pratiquez la d\'e9l\'e9gation : Identifiez une t\'e2che que vous faites actuellement mais qu\'92un collaborateur pourrait prendre en charge."\
        ]\
    \}\
\
    for key in responses:\
        if key in user_input.lower():\
            return random.choice(responses[key])\
\
    return "Je ne suis pas s\'fbr de comprendre. Pouvez-vous reformuler votre question sur le coaching ?"\
\
# Interface Streamlit\
st.title("
\f1 \uc0\u55358 \u56598 
\f0  Coach IA Personnel et Professionnel")\
st.write("Posez une question sur la gestion du stress, la prise de d\'e9cision ou le leadership, et recevez un conseil personnalis\'e9 accompagn\'e9 d'un exercice pratique !")\
\
# Saisie utilisateur\
user_input = st.text_input("
\f1 \uc0\u55357 \u56492 
\f0  Votre question :")\
\
if user_input:\
    response = coaching_response(user_input)\
    st.write(f"
\f1 \uc0\u55357 \u56481 
\f0  R\'e9ponse du Coach IA : \{response\}")\
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\cf0 import streamlit as st\
import random\
\
# Fonction pour g\'e9n\'e9rer une r\'e9ponse du coach IA avec recommandations pratiques\
def coaching_response(user_input):\
    responses = \{\
        "gestion du stress": [\
            "Prenez 5 minutes pour respirer profond\'e9ment et vous recentrer. Exercice : Inspirez 4 secondes, retenez 4 secondes, expirez 4 secondes.",\
            "Essayez la m\'e9ditation en pleine conscience pendant 10 minutes. Application recommand\'e9e : Headspace.",\
            "Faites une pause active : marchez 5 minutes en ext\'e9rieur pour oxyg\'e9ner votre cerveau."\
        ],\
        "prise de d\'e9cision": [\
            "Utilisez la matrice d\'e9cisionnelle : \'e9crivez les avantages et les inconv\'e9nients sur une feuille.",\
            "Posez-vous la question : 'Quelle est la pire chose qui pourrait arriver ?' Cela aide \'e0 relativiser.",\
            "Faites un test rapide : demandez-vous si cette d\'e9cision aura encore de l'importance dans 1 an."\
        ],\
        "leadership": [\
            "Un bon leader \'e9coute activement avant de parler. Exercice : Reformulez ce que votre interlocuteur dit avant de r\'e9pondre.",\
            "Valorisez vos \'e9quipes en leur donnant du feedback positif sp\'e9cifique : 'J'ai appr\'e9ci\'e9 ton implication sur ce projet parce que\'85'",\
            "Pratiquez la d\'e9l\'e9gation : Identifiez une t\'e2che que vous faites actuellement mais qu\'92un collaborateur pourrait prendre en charge."\
        ]\
    \}\
    \
    for key in responses:\
        if key in user_input.lower():\
            return random.choice(responses[key])\
    \
    return "Je ne suis pas s\'fbr de comprendre. Pouvez-vous reformuler votre question sur le coaching ?"\
\
# Interface Streamlit\
st.title("
\f1 \uc0\u55358 \u56598 
\f0  Coach IA Personnel et Professionnel")\
st.write("Posez une question sur la gestion du stress, la prise de d\'e9cision ou le leadership, et recevez un conseil personnalis\'e9 accompagn\'e9 d'un exercice pratique !")\
\
# Saisie utilisateur\
user_input = st.text_input("
\f1 \uc0\u55357 \u56492 
\f0  Votre question :")\
\
if user_input:\
    response = coaching_response(user_input)\
    st.write(f"
\f1 \uc0\u55357 \u56481 
\f0  R\'e9ponse du Coach IA : \{response\}")\
}