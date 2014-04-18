import subprocess

from base import Base


class VideoMixin(Base):

    def convert_to_video(self):
        subprocess.call([
            "ffmpeg",
            "-framerate", "3",
            # Input files
            "-pattern_type", "glob",
            "-i", "polished_output/*.png",
            # Scale images to center
            "-vf",
            'scale=iw*min(1920/iw\,1080/ih):ih*min(1920/iw\,1080/ih),pad=1920:1080:(1920-iw)/2:(1080-ih)/2',
            # Yes to override
            "-y",
            # Output video
            "polished_output/output.mp4"
        ])
