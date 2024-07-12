# Project 2
# Name: Youtube Manager using Sqlite3
# Reference: Chai Aur Code

# Create Database
import sqlite3

conn = sqlite3.connect('./P2/database/videos_manager.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                time TEXT NOT NULL
                )
''')

# Create Function
def list_a_videos():
    cursor.execute("SELECT * FROM videos")
    print('\n')
    print('*' * 70)
    for row in cursor.fetchall():
        print(f"ID:{row[0]}\n NAME:{row[1]}\n TIME:{row[2]}\n")
    print('*' * 70)

def add_a_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    return conn.commit()

def update_a_video(new_name, new_time, video_id):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    return conn.commit()

def delete_a_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    return conn.commit()

# Create Main Function
def main():
    while True:
        print('\n YouTube Manager APP \n')
        print('1. List Videos')
        print('2. Add Video')
        print('3. Update Video')
        print('4. Delete Video')
        print('5. Exit')
        choice = input("Enter Your Choice: ")

        match choice:
            case '1': 
                list_a_videos()
            case '2': 
                name = input('Enter Video Name: ')
                time = input('Enter Video Time: ')
                add_a_video(name, time)
            case '3': 
                video_id = int(input('Enter Id No: '))
                new_name = input('Enter New Name: ')
                new_time = input('Enter New Time: ')
                update_a_video(new_name, new_time, video_id)
            case '4':
                video_id = int(input('Enter Id No: '))
                delete_a_video(video_id)
            case '5': 
                break
            case _: 
                print('Invalid Choice')

if __name__ == '__main__':
    main()