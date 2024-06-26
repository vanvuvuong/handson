import pyautogui
from time import sleep


content = {
    # "1 What is Apache Kafka": 10 * 60 + 00,
    # "2 Apache Kafka Core Concepts": 17 * 60 + 49,
    # "3 Kafka Connect Core Concepts": 20 * 60 + 52,
    # "4 Kafka Streams Core Concepts": 13 * 60 + 36,
    # "5 Kafka SQL Core Concepts": 4 * 60 + 37,
    # "6 When to use What?": 6 * 60 + 29,
    # "7 Kafka Quick Start": 1 * 60 + 21,
    # "8 Installing Single Node Kafka Cluster": 9 * 60 + 18,
    # "9 Using Command-Line Producer and Consumer": 6 * 60 + 33,
    # "10 Installing a Multi-Node Kafka Cluster": 7 * 60 + 30,
    # "11 Using Consumer Groups": 8 * 60 + 4,
    # "12 Configuring your development IDE": 6 * 60 + 10,
    # "14 Understanding Kafka Storage Architecture": 3 * 60 + 10,
    # "15 Kafka Topics and Partitions": 6 * 60,
    # "16 Kafka Topic Replication": 2 * 60 + 21,
    # "17 Partition Leaders and Followers": 2 * 60 + 4,
    # "18 Kafka Log Segments": 2 * 60 + 49,
    # "19 Kafka Message Offsets": 2 * 60 + 20,
    # "20 Kafka Message Index": 4 * 60 + 49,
}
sections = {
    "Apache Kafka - Cluster Architecture": {
        "21 Understanding Kafka Cluster": 2 * 60 + 38,
        "22 Zookeeper in Kafka": 3 * 60 + 18,
        "23 Kafka Cluster Controller": 4 * 60 + 24,
        "24 Partition Allocation and Fault Tolerance": 10 * 60 + 15,
        "25 Partition Leader Vs Partition Follower": 4 * 60 + 53,
        "26 The ISR List - In Sync Replica": 4 * 60 + 34,
        "27 Committed Vs Un-Committed Records": 3 * 60 + 40,
        "28 Minimum ISR List": 2 * 60 + 55,
    },
    "Kafka Producer Internals": {
        "29 Introducing Kafka Producers": 1 * 60 + 22,
        "30 Creating your first Kafka Producer": 10 * 60 + 42,
        "31 Producer Record": 2 * 60 + 29,
        "32 Producer Serializer": 2 * 60 + 12,
        "33 Producer Partitioner": 4 * 60 + 11,
        "34 Message Timestamp": 3 * 60 + 16,
        "35 Producer Message Buffer": 2 * 60 + 40,
        "36 Producer IO Thread and Retires": 1 * 60 + 13,
        "37 Summarizing Producer Internals": 1 * 60 + 58,
    },
    "Advanced Kafka Producers": {
        "38 Horizontal Vs. Vertical Scalability": 3 * 60 + 10,
        "39 Producer Multi-Threading Scenario": 1 * 60 + 52,
        "40 Creating Multi-Threaded Kafka Producer": 11 * 60 + 46,
        "41 At Least Once Vs. At Most Once": 3 * 60 + 41,
        "42 Exactly Once - Producer Idempotence": 3 * 60 + 32,
        "43 Transactions in Kafka Producer": 12 * 60 + 50,
    },
    "Types and Serialization": {
        "44 Working with Types and Serialization": 3 * 60 + 22,
        "45 Using JSON Schema": 8 * 60 + 38,
        "46 Using AVRO Schema": 7 * 60 + 38,
    },
}

BREAK_TIME = 1
UDEMY_ZERO_SECOND = (78, 705)
UDEMY_FIRST_VIDEO = (1700, 270)
UDEMY_SECOND_VIDEO = (1700, 270 + 73)
UDEMY_NEXT_SECTION_VIDEO = (1700, 270 + 160)
"""
windows 1: udemy watching video
windows 2: udemy saving folder
windows 3: terminal
"""


def invoke_shortcut(key):
    pyautogui.hotkey("win", key)


def move_and_click(position: tuple):
    pyautogui.moveTo(position)
    pyautogui.click()


def change_video_name(video_name: str):
    pyautogui.press("f2")
    sleep(BREAK_TIME)
    pyautogui.write(video_name)
    sleep(BREAK_TIME)
    pyautogui.press("enter")


def run_record_in_one_section(video_name: str, wait_time: int):
    sleep(BREAK_TIME)
    print("Click first video")
    move_and_click(UDEMY_FIRST_VIDEO)
    sleep(15)
    print("Pause video")
    pyautogui.press("space")
    sleep(BREAK_TIME)
    print("Click on 0 second")
    move_and_click(UDEMY_ZERO_SECOND)
    move_and_click((999, 831))
    sleep(BREAK_TIME)
    print("Enter fullscreen")
    pyautogui.press("f")
    sleep(BREAK_TIME)
    print("Start recording")
    sleep(1)
    invoke_shortcut("r")
    sleep(BREAK_TIME * 3)
    pyautogui.press("space")
    sleep(wait_time + BREAK_TIME)
    pyautogui.press("esc")
    sleep(BREAK_TIME)
    invoke_shortcut("3")
    sleep(BREAK_TIME)
    pyautogui.write("kill -SIGINT $(pgrep obs)")
    sleep(BREAK_TIME)
    pyautogui.press("enter")
    sleep(BREAK_TIME)
    pyautogui.press("enter")
    sleep(BREAK_TIME)
    invoke_shortcut("2")
    sleep(BREAK_TIME)
    pyautogui.press("end")
    sleep(BREAK_TIME)
    change_video_name(video_name)
    invoke_shortcut("1")
    move_and_click(UDEMY_SECOND_VIDEO)


def run_record_multiple_sections(section_name: str, video_content: dict):
    print("Recording for section:", section_name)
    sleep(BREAK_TIME)
    for video_name, wait_time in video_content.items():
        run_record_in_one_section(video_name, wait_time)


def main():
    for section_name, video_content in sections.items():
        run_record_multiple_sections(section_name, video_content)
        move_and_click(UDEMY_NEXT_SECTION_VIDEO)


main()
