# 4. I => Interface Segregation Principle (ISP)
# No client should be forced to depend on interfaces they don't use.
class MediaPlayer:
    def play_audio(self, audio_file):
        raise NotImplementedError
    def play_video(self, video_file):
        raise NotImplementedError
    def stop_audio(self):
        raise NotImplementedError
    def stop_video(self):
        raise NotImplementedError
    def adjust_audio_volume(self):
        raise NotImplementedError
    def adjust_video_brightness(self):
        raise NotImplementedError
    
# In this case, any class that implements the MediaPlayer interface would be force to 
# implement all the methods, even if it doesn't need them
# For example, an audio player would have to implement the play_video, stop_video and adjust_video_brightness 
# methods, even though they are not relevant for audio play back

# To adhere to the ISP as -

class AudioPlayer:
    def play_audio(self, audio_file):
        raise NotImplementedError
    def stop_audio(self):
        raise NotImplementedError
    def adjust_audio_volume(self, volume):
        raise NotImplementedError

class VideoPlayer:
    def play_video(self, video_file):
        raise NotImplementedError
    def stop_video(self):
        raise NotImplementedError
    def adjust_video_brightness(self, brightness):
        raise NotImplementedError

# Now, We can separate implementations for Audio and Video player

class MP3Player(AudioPlayer):
    def play_audio(self, audio_file):
        # Play MP3 file
        pass
    def stop_audio(self):
        # Stop audio player
        pass
    def adjust_audio_volume(self, volume):
        # Adjust audio volume
        pass

class AVIPlayer(VideoPlayer):
    def play_video(self, video_file):
        # Play Video file
        pass
    def stop_video(self):
        # Stop video player
        pass
    def adjust_video_brightness(self, brightness):
        # Adjust video brightness logic
        pass

# if we need a class that support both audio and video playback 
# then we can implement like this

class MultimediaPlayer(AudioPlayer, VideoPlayer):
    # Implement methods for both AudioPlayer and VideoPlayer interfaces
    pass