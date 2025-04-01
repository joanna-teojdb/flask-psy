from flask import Flask, render_template
import os

app = Flask(__name__)

# Dane o rasach psów
dog_breeds = [
    {
        'name': 'Labrador Retriever',
        'description': 'Labrador to jedna z najpopularniejszych ras psów na świecie. Są przyjazne, inteligentne i świetnie nadają się do rodzin.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/3/34/Labrador_on_Quantock_%282175262184%29.jpg'
    },
    {
        'name': 'Owczarek Niemiecki',
        'description': 'Owczarek niemiecki to rasa psów ceniona za inteligencję, lojalność i wszechstronność. Są często wykorzystywane w służbach mundurowych.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/d/d0/German_Shepherd_-_DSC_0346_%2810096362833633%29.jpg'
    },
    {
        'name': 'Golden Retriever',
        'description': 'Golden retrievery są znane ze swojego przyjaznego usposobienia i złocistego umaszczenia. To doskonałe psy rodzinne.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/9/93/Golden_Retriever_Carlos_%2810581914756%29.jpg'
    }
]

@app.route('/')
def index():
    return render_template('index.html', breeds=dog_breeds)

if __name__ == '__main__':
    # Pobierz port z zmiennej środowiskowej PORT (Azure) lub użyj domyślnego 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 