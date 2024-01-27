# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, K):
    # Implement your solution here
    days = [
        {"index": 0, "day": "Mon"},
        {"index": 1, "day": "Tue"},
        {"index": 2, "day": "Wed"},
        {"index": 3, "day": "Thu"},
        {"index": 4, "day": "Fri"},
        {"index": 5, "day": "Sat"},
        {"index": 6, "day": "Sun"}
        ]
    for item in enumerate(days):
        print(item)
        # if (item.day == S):
        #     day_index = item.index
        #     break
    # print(day_index)

solution("Wed", 2)