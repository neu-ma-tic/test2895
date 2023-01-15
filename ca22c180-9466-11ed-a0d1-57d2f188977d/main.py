import threading
import queue
import os

import youtube_handler
from player import Player
import logger
import messenger
import cache_manager

#KEYWORDS DECLARATION
PLAY = '!!play'
ADD = '!!add'
PAUSE = '!!pause'
STOP = '!!stop'
LOOP = '!!loop'
LOOP_QUEUE = '!!lq'
NEXT = '!!next'
LAST = '!!last'
QUEUE = '!!queue'
REMOVE = '!!rm'
HELP = '!!help'

HELP_MESSAGE = ('**!!play** *<yt-link/search-term>*: Play song from *yt-link* or *search-term*.\n'
                '**!!play** *<song-index>*: Play song at *song-index* on queue.\n'
                '**!!play**: Resume paused song.\n'
                '**!!add** *<yt-link/search-term>*: Add song from *yt-link* or *search-term* to queue.\n'
                '**!!pause**: Pause current song.\n'
                '**!!stop**: Stop current song and clear the queue.\n'
                '**!!loop**: Start looping current song.\n'
                '**!!lq**: Toggle looping whole queue (default off).\n'
                '**!!next**: Play next song on queue.\n'
                '**!!last**: Play previous song on queue.\n'
                '**!!queue**: Return the current queue.\n'
                '**!!rm** *<song-index>*: Remove the song at *song-index* from queue.\n'
                '**!!help**: Return this message.\n'
                )

def main():
    try:
        os.mkdir('cache')
    except:
        pass

    q = queue.Queue(1)
    t1 = threading.Thread(target=logger.initialize, args=(q,))
    t1.start()

    player_initialized = False
    songName = ''

    while True:
        if q.full() and ('!!' in (message := q.get())):

            if PLAY in message:
                if len(message) == len(PLAY):
                    if Player.unpause(): messenger.send(f'Resuming:\n**{songName}**')
                else:
                    payloadIndex = len(PLAY) + 1
                    payload = message[payloadIndex:]
                    try:
                        int(payload)
                    except:
                        songDict = youtube_handler.get_video(payload)
                        songID = songDict['id']
                        songName = songDict['title']
                        Player.single_song = songDict
                        Player.play(f'cache/{songID}.mp3')
                        messenger.send(f'Now Playing:\n**{songName}**')
                        cache_manager.clean_cache()
                        Player.on_queue = False
                        player_initialized = True
                    else:
                        songDict = Player.myQueue[int(payload) - 1]
                        songID = songDict['id']
                        songName = songDict['title']
                        Player.play(f'cache/{songID}.mp3')
                        messenger.send(f'Now Playing:\n**{songName}**')
                        Player.on_queue = True
                        player_initialized = True

            if ADD in message:
                payloadIndex = len(ADD) + 1
                payload = message[payloadIndex:]
                songDict = youtube_handler.get_video(payload)
                songName = Player.add_to_queue(songDict)
                messenger.send(f'Added to queue:\n**{songName}**')
                cache_manager.clean_cache()
                player_initialized = True

            elif PAUSE in message:
                if Player.pause(): messenger.send(f'Paused:\n**{songName}**')

            elif STOP in message:
                if Player.stop(): messenger.send('**Queue Stopped!**')
                player_initialized = False

            elif LOOP in message:
                if Player.loop(): messenger.send(f'Looping:\n**{songName}**')

            elif NEXT in message:
                songName = Player.play_next()
                messenger.send(f'Playing next song:\n**{songName}**')

            elif LAST in message:
                songName = Player.play_last()
                messenger.send(f'Playing previous song:\n**{songName}**')

            elif QUEUE in message:
                messenger.send(f'Queue:\n**{Player.get_queue()}**')

            elif REMOVE in message:
                if len(message) > len(REMOVE):
                    payloadIndex = len(REMOVE) + 1
                    payload = message[payloadIndex:]
                    songName = Player.remove_from_queue(int(payload) - 1)
                    messenger.send(f'Removed from queue:\n**{songName}**')

            elif LOOP_QUEUE in message:
                isLooping = Player.flip_qloop()
                if isLooping:
                    messenger.send('**Queue Looping!**')
                else:
                    messenger.send('**Queue NOT Looping!**')

            elif HELP in message:
                messenger.send(HELP_MESSAGE)
            
        if player_initialized: songName = Player.update()


if __name__ == "__main__":
    main()