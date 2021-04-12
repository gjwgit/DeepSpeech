import utils
import os
import tarfile
from mlhub.pkg import mlask, mlcat


def main():
    # -----------------------------------------------------------------------
    # Load pre-built models and samples
    # -----------------------------------------------------------------------
    scorer = os.path.join(os.getcwd(), "deepspeech-0.9.3-models.scorer")
    model = os.path.join(os.getcwd(), "deepspeech-0.9.3-models.pbmm")
    audio = os.path.join(os.getcwd(), "audio-0.9.3.tar.gz")

    tar = tarfile.open(audio, "r:gz")
    tar.extractall()
    tar.close()

    audio_path = os.path.join(os.getcwd(), "audio")

    audio_file_list = []

    for filename in os.listdir(audio_path):
        if not filename.startswith(".") and filename.endswith("wav"):
            audio_file_list.append(os.path.join(os.getcwd(), "audio/" + filename))

    audio_file_list = sorted(audio_file_list)

    mlcat("Deepspeech","""\
Welcome to a demo of Mozilla's Deepspeech pre-built model for speech to text. 
This model is trained by machine learning techniques based on Baidu's Deep Speech research paper (
https://arxiv.org/abs/1412.5567), and implemented by Mozilla. 
In this demo, the audio will be played and then transcribed to text.
""")
    mlask(end="\n")

    # -----------------------------------------------------------------------
    # First audio
    # -----------------------------------------------------------------------

    mlcat("Experience proves this.",
          """The audio will be played and if you listen carefully you should hear:\n""")
    mlcat("",
          """Experience proves this.""")
    mlask(begin="\n")
    os.system(f'aplay {audio_file_list[0]} >/dev/null 2>&1')
    mlask()
    ds, desired_sample_rate = utils.load(model, scorer, True, "", "", "", "")
    utils.deepspeech(ds, desired_sample_rate, audio_file_list[0], "demo", True, "", "", "")

    mlask(end="\n")

    # -----------------------------------------------------------------------
    # Second audio
    # -----------------------------------------------------------------------

    mlcat("Why should one halt on the way?",
          """The audio will be played and if you listen carefully you should hear:\n""")
    mlcat("",
          """Why should one halt on the way?""")
    mlask(begin="\n")
    os.system(f'aplay {audio_file_list[1]} >/dev/null 2>&1')
    mlask()
    utils.deepspeech(ds, desired_sample_rate, audio_file_list[1], "demo", True, "", "", "")
    mlask(end="\n")

    # -----------------------------------------------------------------------
    # Third audio
    # -----------------------------------------------------------------------

    mlcat("Your power is sufficient I said.",
          """The audio will be played and if you listen carefully you should hear:\n""")
    mlcat("",
          """Your power is sufficient I said.""")
    mlask(begin="\n")
    os.system(f'aplay {audio_file_list[2]} >/dev/null 2>&1')
    mlask()
    utils.deepspeech(ds, desired_sample_rate, audio_file_list[2], "demo", True, "", "", "")


if __name__ == '__main__':
    main()
