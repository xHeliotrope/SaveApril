from subprocess import Popen
from subprocess import PIPE

game_name = 'TeenageMutantNinjaTurtlesIIITheManhattanProject-Nes'
game_meta = '-1Player.Leo.Level1-000000'

class FileHandler:
    """Used for managing backup, mp4 and data logging files
    """

    def __init__(self, file_name=game_name+game_meta, file_number=0, video_path='recordings/'):
        """set the file names
        and open up the logging file for logging
        """
        self.backup = '{name}{number}{path}.bk2'.format(
                name=file_name,
                number=file_number,
                path=video_path)
        self.video = '{name}{number}{path}.mp4'.format(
                name=file_name,
                number=file_number,
                path=video_path)
        self.video_path = video_path
        self.file_number = file_number

    def create_video(self):
        """create video file from replay
        """
        create_video_command = 'python3 -m retro.scripts.playback_movie ' + self.backup
        create_video_proc = Popen(create_video_command, shell=True, stdout=PIPE) 
        create_video_proc.wait()

    def create_video_dir(self):
        """create video file from replay
        """
        create_dir_command = 'mkdir ' + self.video_path + str(self.file_number)
        create_video_proc = Popen(create_dir_command, shell=True, stdout=PIPE) 
        create_video_proc.wait()

    def rm_backup(self):
        """remove all backup files
        """
        try:
            rm_file_proc = Popen('rm ' + self.backup, shell=True, stdout=PIPE)
            rm_file_proc.wait()
        except FileNotFoundError:
            pass

    def rm_video(self):
        """remove all video files
        """
        try:
            rm_file_proc = Popen('rm ' + self.video, shell=True, stdout=PIPE)
            rm_file_proc.communicate()
        except FileNotFoundError:
            pass

    def play_video(self):
        """play the video file
        """
        try:
            play_replay = Popen('open ' + self.video, shell=True, stdout=PIPE)
            play_replay.wait()
        except:
            play_replay = Popen('xdg-open ' + self.video, shell=True, stdout=PIPE)
            play_replay.wait()
