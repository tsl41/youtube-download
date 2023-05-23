from flask import Flask, render_template, request
from  pytube import YouTube
import subprocess

app = Flask(__name__)
    
def get_meta_data(video_id, google_api_key):

    command = f'python info.py "{google_api_key}" "{video_id}"'
    results = subprocess.run(command, shell=True, capture_output=True, text=True)
    if results.returncode == 0:
        output = results.stdout
        title, thumbnail_url = output.split('\n')
        return title
    

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        video_url = request.form['video_url']
        try:
            #youtube object
            yt = YouTube(video_url)

            stream = yt.streams.get_highest_resolution()
             
            #actual download url of the video
            download_url = stream.url

            page_title = yt.title

            thumbnail_url = yt.thumbnail_url

            file_size = round(stream.filesize / 1048576, 2)


            return render_template('result.html', 
                                   download_url=download_url, 
                                   page_title=page_title,
                                   file_size=file_size,
                                   thumbnail_url=thumbnail_url
                                   )
        
        except Exception  as e:
            error_mssg = str(e)
            return render_template('result.html', error_mssg=error_mssg)
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)