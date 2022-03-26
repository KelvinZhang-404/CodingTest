import json

learner_sessions = [
    ["Course_001", "Course_002", "Course_003", "Course_004"],
    ["Course_001", "Course_003"],
    ["Course_002", "Course_001", "Course_004"],
    ["Course_001", "Course_002", "Course_003", "Course_004"],
    ["Course_001", "Course_003", "Course_002", "Course_004"]
]

x = {}

for learner in learner_sessions:
    for i in range(len(learner)):
        if i == len(learner) - 1:
            x[learner[i]] = {}
            break

        if learner[i] not in x:
            x[learner[i]] = {learner[i + 1]: 1}

        elif learner[i + 1] not in x[learner[i]]:
            x[learner[i]][learner[i + 1]] = 1

        else:
            x[learner[i]][learner[i + 1]] += 1

for course, followers in x.items():
    # find the first matching following course
    # max_follower = max(followers, key=followers.get)
    # x[course] = max_follower

    # find all matching following courses
    max_value = max(followers.values()) if followers else 0
    l = [follower for follower, value in followers.items() if value == max_value]

    x[course] = l

print(json.dumps(x))
