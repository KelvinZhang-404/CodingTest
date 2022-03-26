learners_courses = {
    "Learner-0001": [
        "Course-0001",
        "Course-0002",
        "Course-0003"
    ],
    "Learner-0002": [
        "Course-0002",
        "Course-0003",
        "Course-0004"
    ],
    "Learner-0003": [
        "Course-0004",
        "Course-0005",
        "Course-0006"
    ],
    "Learner-0004": [
        "Course-0005",
        "Course-0006",
        "Course-0007"
    ]
}


def main():
    compute_single_learnt(learners_courses)


def compute_single_learnt(learners_courses):
    courses_completed = {}

    for courses in learners_courses.values():
        for course in courses:
            if course in courses_completed:
                courses_completed[course] += 1
            else:
                courses_completed[course] = 1

    single_learnt = [course for course, learnt in courses_completed.items() if learnt == 1]

    print(single_learnt)
    print(repr(__name__))


if __name__ == '__main__':
    main()
