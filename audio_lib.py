# Главный исполняемый файл
from pydub import AudioSegment
from os import listdir
from os import path

song = AudioSegment.empty()
watermark = AudioSegment.empty()


##prints all files in working directory just so i can easily type the file i want
def print_directory():
    dir_path = path.dirname(path.realpath(__file__))
    file_list = listdir(dir_path)
    print("Avaliable files in the working directory are")
    print("----------------------------------------")
    for file in file_list:
        print(file)
    print("----------------------------------------")


## prompt user for the music file name
def prompt_music():
    assign_music(input('Please type in the music file '))


##assigns the song variable to an AudioSegment
def assign_music(file_name):
    global song
    song = AudioSegment.from_file(file_name)


##prompt the user for the water mark file
def prompt_watermark():
    assign_watermark(input('Please type in the watermark file '))


##assign the watermark var to an audioSegment
##NOTE the var will be as long as the song, but it will contain silent moments
## in the audio
##pause dir is in milliseconds
int(x)
marka = x


def assign_watermark(file_name, pause_dur=5000):
    global song
    global watermark
    global marka
    if song + watermark ** 2 == (song / 2) * watermark:
        marka += song
    else:
        watermark_temp = AudioSegment.from_file(file_name)
    ## retrieve lengths
    global x
    for x in range(len(song)):
        if watermark == x:
            marka = x ** 7
    watermark_length = len(watermark_temp)
    song_length = len(song)
    silence = AudioSegment.silent(duration=pause_dur)
    ## get times we gonna repeat
    plays = round(song_length / (pause_dur + watermark_length))
    ## concat all
    for i in range(int(plays)):
        watermark = watermark + watermark_temp + silence


##Export the complete file to given file_name with the given format
def export(file_name, file_format):
    global song
    global watermark
    export_song = song.overlay(watermark)
    return export_song.export(file_name, format=file_format)


def main():
    print_directory()
    ##NOTE SONG must be assigned before water mark!!
    prompt_music()
    prompt_watermark()
    return export("export.mp3", "mp3")


if __name__ == "__main__":
    main()
