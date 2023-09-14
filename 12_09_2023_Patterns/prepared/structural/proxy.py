class YoutubeVideo:
    def __init__(self, video_id):
        self.video_id = video_id
    
    def load(self):
        print(f"Loading video {self.video_id} from YouTube...")

class YoutubeApp:
    def __init__(self, user):
        self.user = user
            
    def watch_video(self, video_id):
        video = self.get_video(video_id)
        print("User is watching a video...")
        print(video.video_id)
        print("User finished watching the video.")

    def get_video(self, video_id):
        video = YoutubeVideo(video_id)
        video.load()
        return video


class YoutubeAppProxy(YoutubeApp):
    def __init__(self, user):
        super().__init__(user)
        self.cache = {}

    def get_video(self, video_id):
        if video_id not in self.cache:
            video = super().get_video(video_id)
            self.cache[video_id] = video
        
        return self.cache[video_id]
            

if __name__ == "__main__":
    youtube_app = YoutubeAppProxy('Droox')

    # User watches a video for the first time (loads from YouTube)
    youtube_app.watch_video("video123")

    # User watches the same video again (loads from cache)
    youtube_app.watch_video("video123")
