from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load the pre-trained model and data
similarity = pickle.load(open('similarity (1).pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

# Define the recommendation function
def recommendation(song_name):
    if idx = df[df['track_name'] == song_name].index[0] :
        distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])
    
        songs = []
        for m_id in distances[1:11]:
            songs.append(df.iloc[m_id[0]].track_name)
    
        return songs
    else:
        return "Sorry, we couldn't find that song in our database."


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    song_name = request.form['song_name']
    recommended_songs = recommendation(song_name)
    return render_template('index.html', recommended_songs=recommended_songs, song_name=song_name)

if __name__ == '__main__':
    app.run(debug=True)
