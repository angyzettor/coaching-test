import streamlit as st
import random

# Dictionnaire amélioré pour détecter plus de synonymes et variations
def coaching_response(user_input):
    user_input = user_input.lower()
    
    stress_keywords = ["stress", "anxiété", "angoisse", "relaxation", "respiration", "calme", "burn-out"]
    decision_keywords = ["décision", "choix", "hésitation", "réflexion", "incertitude", "dilemme"]
    leadership_keywords = ["leadership", "manager", "motivation", "équipe", "inspiration", "gestion des équipes", "confiance"]
    
    responses = {
        "gestion du stress": [
            "Prenez 5 minutes pour respirer profondément et vous recentrer. Exercice : Inspirez 4 secondes, retenez 4 secondes, expirez 4 secondes.",
            "Essayez la méditation en pleine conscience pendant 10 minutes. Application recommandée : Headspace.",
            "Faites une pause active : marchez 5 minutes en extérieur pour oxygéner votre cerveau."
        ],
        "prise de décision": [
            "Utilisez la matrice décisionnelle : écrivez les avantages et les inconvénients sur une feuille.",
            "Posez-vous la question : 'Quelle est la pire chose qui pourrait arriver ?' Cela aide à relativiser.",
            "Faites un test rapide : demandez-vous si cette décision aura encore de l'importance dans 1 an."
        ],
        "leadership": [
            "Un bon leader écoute activement avant de parler. Exercice : Reformulez ce que votre interlocuteur dit avant de répondre.",
            "Valorisez vos équipes en leur donnant du feedback positif spécifique : 'J'ai apprécié ton implication sur ce projet parce que…'",
            "Pratiquez la délégation : Identifiez une tâche que vous faites actuellement mais qu’un collaborateur pourrait prendre en charge."
        ]
    }
    
    if any(word in user_input for word in stress_keywords):
        return random.choice(responses["gestion du stress"])
    elif any(word in user_input for word in decision_keywords):
        return random.choice(responses["prise de décision"])
    elif any(word in user_input for word in leadership_keywords):
        return random.choice(responses["leadership"])
    else:
        return "Je ne suis pas sûr de comprendre. Essayez une question sur le stress, la prise de décision ou le leadership ! 😊"

# Interface Streamlit
st.title("🤖 Coach IA Personnel et Professionnel")
st.write("Posez une question sur la gestion du stress, la prise de décision ou le leadership, et recevez un conseil personnalisé accompagné d'un exercice pratique !")

# Saisie utilisateur
user_input = st.text_input("💬 Votre question :")

if user_input:
    response = coaching_response(user_input)
    st.write(f"💡 Réponse du Coach IA : {response}")
