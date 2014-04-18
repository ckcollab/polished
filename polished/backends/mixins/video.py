import subprocess


class VideoMixin(object):

    def convert_to_video(self):
        subprocess.call([
            "ffmpeg",
            "-framerate", "3",
            "-pattern_type", "glob",
            "-i", "polished/*.png",
            "polished/output.mp4"
        ])
