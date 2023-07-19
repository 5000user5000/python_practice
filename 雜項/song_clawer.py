#用來爬測試用歌曲
import yt_dlp as youtube_dl # pip安裝問題   https://stackoverflow.com/questions/75495800/error-unable-to-extract-uploader-id-youtube-discord-py
import time

#chatgpt推薦的歌曲
song_list = [
    "七里香",
    "Shape of You",
    "Bohemian Rhapsody",
    "稻香",
    "Rolling in the Deep"
]


def download_audio(url, output_path,song_name):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{output_path}\{song_name}',  # 指定下载文件的输出路径
        #'outtmpl': '%(id)s.%(ext)s',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def search_and_download(query, output_path):
    # 在YouTube上搜索相关歌曲
    search_query = query
    # 可以根据需要修改搜索查询的字符串，例如添加"cover"或"remix"等关键词
    # 更多搜索选项可以查看youtube-dl文档：https://github.com/ytdl-org/youtube-dl#embedding-youtube-dl

    # 使用youtube-dl下载音频文件
    download_audio('ytsearch1:' + search_query, output_path,search_query)

# 示例用法
#search_and_download('Despacito',"C:\\Users\\yee\\Downloads\\songData")

for i in song_list:
    search_and_download(i,"你想下載到的歌曲檔案夾路徑")
    time.sleep(5) #每下載一首歌就休息5秒
    search_and_download(i+' cover',"你想下載到的歌曲檔案夾路徑") #抓翻唱歌
    print(i)
    time.sleep(5) 
