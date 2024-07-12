# Project 3
# Name: Youtube Manager using MongoDB
# Reference: Chai Aur Code


from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://user_name:password@cluster0.yjn4fmw.mongodb.net/")
db = client['youtube_manager']
videos_collection = db['videos']

def add_a_video(name, time):
    videos_collection.insert_one({'name': name, 'time': time})

def remove_a_video(video_id):
    videos_collection.delete_one({"_id":video_id})

def update_a_video(video_id, new_name, new_time):
    videos_collection.update_one(
        {'_id': video_id},
        {'$set': {'name': new_name, 'time': new_time}}
        )

def list_all_videos():
    print('\n')
    print('*'*70)
    for video in videos_collection.find():
        print(f"ID: {video['_id']} NAME: {video['name']} TIME: {video['time']}")
    print('\n')
    print('*'*70)

def main():
    while True:
        print('YouTube Manager')
        print('1. Add a video')
        print('2. Remove a video')
        print('3. Update a video')
        print('4. List all videos')
        print('5. Exit')
        choice = input('Enter your choice: ')

        match choice:
            case '1': 
                name = input('Enter Video Name: ')
                time = input('Enter Video Time: ')
                add_a_video(name, time)
            case '2': 
                video_id = ObjectId(input('Enter Video Id: '))
                remove_a_video(video_id)
            case '3': 
                video_id = ObjectId(input('Enter Video Id: '))
                new_name = input('Enter Video Name: ')
                new_time = input('Enter Video Time: ')
                update_a_video(video_id, new_name, new_time)
            case '4': list_all_videos() 
            case '5': break
            case _: print('Invalid choice')


if __name__ == '__main__':
    main()