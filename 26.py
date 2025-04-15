class Score:
    def __init__(self, subject, marks):
        self.subject = subject
        self.marks = marks

class Student:
    def __init__(self, name, subjects, scores):
        self.name = name
        self.scores = [Score(subjects[i], scores[i]) for i in range(len(subjects))]

    def __str__(self):
        result = f"Student {self.name} has the following scores:\n"
        for score in self.scores:
            result += f"{score.subject}: {score.marks}\n"
        return result.strip()

    def average(self):
        total_marks = sum(score.marks for score in self.scores)
        return total_marks / len(self.scores)

def classAverage(students):
    subject_totals = {}
    subject_counts = {}

    for student in students:
        for score in student.scores:
            if score.subject not in subject_totals:
                subject_totals[score.subject] = 0
                subject_counts[score.subject] = 0
            subject_totals[score.subject] += score.marks
            subject_counts[score.subject] += 1

    averages = []
    for subject in subject_totals:
        average = subject_totals[subject] / subject_counts[subject]
        averages.append(f"{subject}:{round(average)}")

    return averages


s1 = Student('X', ['C1', 'C2', 'C3', 'C4'], [10, 20, 30, 80])
s2 = Student('Y', ['C1', 'C2'], [40, 50])
s3 = Student('Z', ['C2', 'C3'], [60, 70])

print(s1)
print(s1.average())
print(classAverage([s1, s2, s3]))