import requests
import os

# Defina a chave da API do Pixabay
api_key = "47285765-89dd4e775c88a6a251412570c"

# URL base para a pesquisa
base_url = "https://pixabay.com/api/"

# Parâmetros da pesquisa
params = {
    "key": api_key,
    "q": "cat",  # Termo de pesquisa: "cat"
    "image_type": "photo",
    "per_page": 200,  # Número de imagens por página (máximo é 200)
}

# Caminho da pasta de destino
download_folder = r"C:\Users\servaux\Desktop\DATABASE\Classe2"
os.makedirs(download_folder, exist_ok=True)

# Função para fazer o download de imagens
def download_image(url, folder):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            image_name = url.split("/")[-1]
            with open(os.path.join(folder, image_name), 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"Imagem {image_name} baixada com sucesso!")
        else:
            print(f"Erro ao baixar a imagem: {url}")
    except Exception as e:
        print(f"Erro ao baixar a imagem {url}: {e}")

# Função para buscar e baixar imagens
def download_images(api_key, folder):
    all_images = []
    page = 1

    while len(all_images) < 200:  # Limite de 200 imagens
        params["page"] = page
        response = requests.get(base_url, params=params)
        data = response.json()

        if "hits" in data:
            all_images.extend(data["hits"])

        if len(all_images) >= 200:
            break
        page += 1  # Aumenta a página para buscar mais resultados

    # Baixar as 200 imagens
    for image in all_images[:200]:
        image_url = image['webformatURL']  # Você pode usar 'largeImageURL' se preferir imagens maiores
        download_image(image_url, folder)

# Chamada para fazer o download das imagens
download_images(api_key, download_folder)