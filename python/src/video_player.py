"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist
import random

class VideoPlayer:
    """A class used to represent a Video Player."""
    
    #playing_now = ''
   
    def __init__(self):
        self._video_library = VideoLibrary()
        self._playing_now = ''
        self._playlists = {}

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        all_videos = self._video_library.get_all_videos()
        all_videos = sorted(all_videos,key = lambda v: v.title)
        print("Here's a list of all available videos:")
        for video in all_videos:
            tag_list = []
            for tag in video.tags:
                tag_list.append(tag)
            print("{} ({}) [{}]".format(video.title, video.video_id, ' '.join(tag_list)))
    
       
    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        all_videos = self._video_library.get_all_videos()
        all_ids = [v.video_id for v in all_videos]
       
        if video_id in all_ids:
            video_to_play = self._video_library.get_video(video_id)
            if video_to_play.get_flag():
                if video_to_play.flag_res == "":
                    reason  = "Not supplied"
                else:
                    reason = video_to_play.flag_res
                print("Cannot play video: Video is currently flagged (reason: {})".format(reason))
            else:
                if(self._playing_now==''):
                    video_to_play.set_pause(False)
                    print("Playing video:", video_to_play.title)
                else:
                    print("Stopping video:", self._video_library.get_video(self._playing_now).title)
                    video_to_play.set_pause(False)
                    print("Playing video:", video_to_play.title)
                self._playing_now = video_to_play.video_id
        else:
            print("Cannot play video: Video does not exist")
        

    def stop_video(self):
        """Stops the current video."""
        if self._playing_now=='':
            print("Cannot stop video: No video is currently playing")
        else:
            print("Stopping video:", self._video_library.get_video(self._playing_now).title)
            (self._video_library.get_video(self._playing_now)).set_pause(False)
            self._playing_now = ''
            


    def play_random_video(self):
        """Plays a random video from the video library."""
        all_videos = self._video_library.get_all_videos()
        if len(all_videos) != 0:
            v = random.choice(all_videos)
            self.play_video(v.video_id)
        else:
            print("No videos available")
            

    def pause_video(self):
        """Pauses the current video."""
        if self._playing_now != '':
            v = self._video_library.get_video(self._playing_now)
            if not v.get_pause():
                v.set_pause(True)
                print("Pausing video:", v.title)
            else:
                print("Video already paused:", v.title)
        else:
            print("Cannot pause video: No video is currently playing")


    def continue_video(self):
        """Resumes playing the current video."""
        if self._playing_now != '':
            v = self._video_library.get_video(self._playing_now)
            if v.get_pause():
                v.set_pause(False)
                print("Continuing video:", v.title)
            else:
                print("Cannot continue video: Video is not paused")
        else:
            print("Cannot continue video: No video is currently playing")
            

    def show_playing(self):
        """Displays video currently playing."""
        if self._playing_now != '':
            v = self._video_library.get_video(self._playing_now)
            tag_list = []
            for tag in v.tags:
                tag_list.append(tag)
            if  v.get_pause() != True:
                print("Currently playing: {} ({}) [{}]".format(v.title,
                                                               v.video_id,
                                                               ' '.join(tag_list)))
            else:
                print("Currently playing: {} ({}) [{}] - PAUSED".format(v.title,
                                                                        v.video_id,
                                                                        ' '.join(tag_list)))
        else:
            print("No video is currently playing")
            

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() in self._playlists.keys():
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            playlist = Playlist(playlist_name)
            self._playlists[playlist_name.lower()] = playlist
            print("Successfully created new playlist:", playlist_name)

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        if(playlist_name.lower() not in self._playlists.keys()):
            print("Cannot add video to {}: Playlist does not exist".format(playlist_name))
        else:
            all_videos = self._video_library.get_all_videos()
            all_ids = [v.video_id for v in all_videos]
            if video_id not in all_ids:
                print("Cannot add video to {}: Video does not exist".format(playlist_name))
            else:
                play = self._playlists.get(playlist_name.lower())
                if video_id in play.get_content():
                    print("Cannot add video to {}: Video already added".format(playlist_name))
                else:
                    play.add_content(video_id)
                    v =  self._video_library.get_video(video_id)
                    print("Added video to {}: {}".format(playlist_name, v.title))


    def show_all_playlists(self):
        """Display all playlists."""
        play_names = []
        for p in self._playlists:
            play_names.append(self._playlists[p].name)
        play_names.sort()
        if len(play_names) == 0:
            print("No playlists exist yet")
        else:
            print("Showing all playlists:")
            for elt in play_names:
                print(elt)

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() not in self._playlists.keys():
            print("Cannot show playlist {}: Playlist does not exist".format(playlist_name))
        else:
            print("Showing playlist:", playlist_name)
            p = self._playlists.get(playlist_name.lower())
            vid_ids = p.get_content()
            if len(vid_ids) == 0:
                print("No videos here yet")
            else:
                for elt in vid_ids:
                    v = self._video_library.get_video(elt)
                    tag_list = []
                    for tag in v.tags:
                        tag_list.append(tag)
                    print("{} ({}) [{}]".format(v.title, v.video_id, ' '.join(tag_list)))
        

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        if playlist_name.lower() not in self._playlists.keys():
            print("Cannot remove video from {}: Playlist does not exist".format(playlist_name))
        else:
            all_videos = self._video_library.get_all_videos()
            all_ids = [v.video_id for v in all_videos]
            if video_id not in all_ids:
                print("Cannot remove video from {}: Video does not exist".format(playlist_name))
            else:
                play = self._playlists.get(playlist_name.lower())
                if video_id not in play.get_content():
                    print("Cannot remove video from {}: Video is not in playlist".format(playlist_name))
                else:
                    play.remove_content(video_id)
                    print("Removed video from {}: {}".format(playlist_name, self._video_library.get_video(video_id).title))
                    

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower()not in self._playlists.keys():
            print("Cannot clear playlist {}: Playlist does not exist".format(playlist_name))
        else:
            play = self._playlists.get(playlist_name.lower())
            while len(play.get_content()) != 0:
                play.remove_content(play.get_content()[0])
            print("Successfully removed all videos from", playlist_name)
        

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() not in self._playlists.keys():
            print("Cannot delete playlist {}: Playlist does not exist".format(playlist_name))
        else:
            play = self._playlists.get(playlist_name.lower())
            self._playlists.pop(playlist_name.lower())
            del play
            print("Deleted playlist:", playlist_name)
        

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.
        Args:
            search_term: The query to be used in search.
        """
        lower_search = search_term.lower()
        results =[]
        for video in self._video_library.get_all_videos():
            if lower_search in video.title.lower():
                results.append(video.video_id)
        results.sort()
        if len(results) == 0:
            print("No search results for", search_term)
        else:
            print("Here are the results for {}:".format(search_term))
            for i in range(len(results)):
                v = self._video_library.get_video(results[i])
                tag_list = []
                for tag in v.tags:
                    tag_list.append(tag)
                print("{}) {} ({}) [{}]".format(i+1, v.title, v.video_id, ' '.join(tag_list)))
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.") 
            try:
                ans = int(input())
                self.play_video(results[ans-1])
            except (ValueError, IndexError) as e:
                pass
            
            
        

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        lower_search = video_tag.lower()
        results =[]
        for video in self._video_library.get_all_videos():
            tag_list = []
            for tag in video.tags:
                tag_list.append(tag)
            for tag in tag_list:
                if lower_search in tag and video.video_id not in results:
                    results.append(video.video_id)
        results.sort()
        if len(results) == 0:
            print("No search results for", video_tag)
        else:
            print("Here are the results for {}:".format(video_tag))
            for i in range(len(results)):
                v = self._video_library.get_video(results[i])
                tag_list = []
                for tag in v.tags:
                    tag_list.append(tag)
                print("{}) {} ({}) [{}]".format(i+1, v.title, v.video_id, ' '.join(tag_list)))
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.") 
            try:
                ans = int(input())
                self.play_video(results[ans-1])
            except (ValueError, IndexError) as e:
                pass
        

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        all_videos = self._video_library.get_all_videos()
        all_ids = [v.video_id for v in all_videos]
        if video_id not in all_ids:
            print("Cannot flag video: Video does not exist")
        else:
            video = self._video_library.get_video(video_id)
            if video.get_flag():
                print("Cannot flag video: Video is already flagged")
            else:
                video.set_flag(True)
                video.set_flag_res(flag_reason)
                if flag_reason == "":
                    reason  = "Not supplied"
                else:
                    reason = flag_reason
                print("Successfully flagged video: {} (reason: {})".format(video.title, reason))
        

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
