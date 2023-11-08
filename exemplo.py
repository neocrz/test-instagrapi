import os
from dotenv import load_dotenv
# Carregar SESSION ID
load_dotenv() 
from insta import cl, getinfo_media, data_to_csv

if __name__ == "__main__":
    user_busca = "instagram"
    qtd_posts = 15
    user_id = cl.user_id_from_username(user_busca)
    medias = cl.user_medias(user_id, 1)
    data = getinfo_media(user_busca, qtd_posts)
    data_to_csv(data)