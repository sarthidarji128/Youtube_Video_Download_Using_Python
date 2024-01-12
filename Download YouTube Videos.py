from pytube import YouTube
yt_video = YouTube ("https://www.youtube.com/watch?v=LRLq2t5IlKI")
v_file = yt_video.streams.filter(file_extension="mp4").get_by_resolution("720p")
v_file.download("/Users/s.d./Desktop/Perosonal/PycharmProjects")