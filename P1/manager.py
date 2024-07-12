import json

# global variabel
data = './P1/database/data.txt'

# function
def load_data():
    '''load json data from data.txt file'''
    try:
        with open(data, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    '''save data in data.txt file'''
    with open(data, 'w') as file:
        return json.dump(videos, file)

def add_a_video(videos):
    '''add all data in data.txt file'''
    name = input("Enter Video Name: ")
    time = input("Enter Video Time: ")
    videos.append({'Name':name,'Time':time})
    return save_data_helper(videos)

def remove_a_video(videos):
    '''remove selected data from data.txt file'''
    list_all_videos(videos)
    index = int(input("Enter The Video Number to Remove: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        return save_data_helper(videos)
    else:
        return print("Invalid Input")
    
def list_all_videos(videos):
    '''show all data from data.txt file'''
    print('_'*70)
    print('\n')
    for index, video in enumerate(videos, start=1):
        print(f'No: {index} \nName: {video['Name']} \nDuration: {video['Time']}\n')
    print('_'*70)
    return None

def update_a_video(videos):
    '''update selected data from data.txt file'''
    list_all_videos(videos)
    index = int(input("Enter The Video Number to Update: "))
    if 1 <= index <= len(videos):
        name = input("Enter Video Name: ")
        time = input("Enter Video Time: ")
        videos[index-1] = {'Name':name, 'Time':time}
        return save_data_helper(videos)
    else:
        return print("Invalid Input")


