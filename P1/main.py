# Project 1
# Name: Youtube Manager using File IO
# Reference: Chai Aur Code
# Note: if it's get error so please add '[]' in data.txt

from manager import add_a_video,load_data, remove_a_video, list_all_videos, update_a_video


def main():
    videos = load_data()
    while True:
        print('YouTube Manager')
        print('1. Add a video')
        print('2. Remove a video')
        print('3. List all videos')
        print('4. Update a video')
        print('5. Exit')
        choice = input('Enter your choice: ')
        match choice:
            case '1': add_a_video(videos)
            case '2': remove_a_video(videos)
            case '3': list_all_videos(videos)
            case '4': update_a_video(videos)
            case '5': break
            case _: print('Invalid choice')
            

if __name__ == '__main__':
    main()
