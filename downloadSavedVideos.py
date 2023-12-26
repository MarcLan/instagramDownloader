import instaloader

# Get instance
loader = instaloader.Instaloader(download_video_thumbnails=False,save_metadata=False,compress_json=False,post_metadata_txt_pattern=None,)

# Get login session, should do python 615_import_firefox_session.py first
loader.load_session_from_file("lan__yang") 

# Get 10 saved videos
loader.download_saved_posts(max_count = 3, fast_update=True)