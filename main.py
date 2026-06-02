from datetime import datetime


# -----------------------------
# Homework Class
# -----------------------------
class Homework:
    def __init__(self, title, description, subject, deadline, subtasks=None):
        self.title = title
        self.description = description
        self.subject = subject
        self.deadline = deadline
        self.subtasks = subtasks if subtasks else []
        self.done = False
        self.priority = "LOW"

    def mark_done(self):
        self.done = True

    def get_days_left(self):
        today = datetime.now().date()
        due_date = datetime.strptime(self.deadline, "%Y-%m-%d").date()
        return (due_date - today).days

    def is_overdue(self):
        return self.get_days_left() < 0

    def display(self):
        status = "DONE" if self.done else "PENDING"
        print("\n--------------------------")
        print(f"Title      : {self.title}")
        print(f"Description: {self.description}")
        print(f"Subject    : {self.subject}")
        print(f"Deadline   : {self.deadline}")
        print(f"Priority   : {self.priority}")
        print(f"Status     : {status}")

        if self.subtasks:
            print("Subtasks:")
            for sub in self.subtasks:
                print(f"- {sub}")


# -----------------------------
# Validation Class
# -----------------------------
class Validation:

    @staticmethod
    def validate_homework(title, subject, deadline):
        errors = []

        if not title.strip():
            errors.append("Title is required.")

        if not subject.strip():
            errors.append("Subject is required.")

        try:
            datetime.strptime(deadline, "%Y-%m-%d")
        except ValueError:
            errors.append("Deadline format must be YYYY-MM-DD.")

        return errors


# -----------------------------
# Priority Engine Class
# -----------------------------
class PriorityEngine:

    @staticmethod
    def get_priority(homework):

        if homework.done:
            return "DONE"

        days = homework.get_days_left()

        if days < 0:
            return "CRITICAL (OVERDUE)"

        elif days < 1:
            return "CRITICAL (DUE TODAY)"

        elif days <= 3:
            return "HIGH"

        elif days <= 7:
            return "MEDIUM"

        else:
            return "LOW"


# -----------------------------
# Report Generator Class
# -----------------------------
class ReportGenerator:

    @staticmethod
    def generate_report(homeworks):

        total = len(homeworks)
        completed = sum(hw.done for hw in homeworks)
        pending = total - completed
        overdue = sum(hw.is_overdue() for hw in homeworks)

        print("\n========== HOMEWORK REPORT ==========")
        print(f"Total Homework : {total}")
        print(f"Completed      : {completed}")
        print(f"Pending        : {pending}")
        print(f"Overdue        : {overdue}")

        if total > 0:
            completion_rate = (completed / total) * 100
            print(f"Completion Rate: {completion_rate:.2f}%")

        print("=====================================")


# -----------------------------
# Main Application
# -----------------------------
homework_list = []


def add_homework():

    print("\n===== ADD HOMEWORK =====")

    title = input("Enter Title: ")
    description = input("Enter Description: ")
    subject = input("Enter Subject: ")
    deadline = input("Enter Deadline (YYYY-MM-DD): ")

    subtasks = input("Enter Subtasks (comma separated): ")
    subtask_list = [s.strip() for s in subtasks.split(",")] if subtasks else []

    # Validation
    errors = Validation.validate_homework(title, subject, deadline)

    if errors:
        print("\nERRORS:")
        for error in errors:
            print("-", error)
        return

    homework = Homework(
        title,
        description,
        subject,
        deadline,
        subtask_list
    )

    # Auto Priority
    homework.priority = PriorityEngine.get_priority(homework)

    homework_list.append(homework)

    print("\nHomework added successfully!")


def view_homework():

    if not homework_list:
        print("\nNo homework found.")
        return

    print("\n===== HOMEWORK LIST =====")

    for index, hw in enumerate(homework_list):
        print(f"\nHomework #{index + 1}")
        hw.priority = PriorityEngine.get_priority(hw)
        hw.display()


def mark_homework_done():

    view_homework()

    if not homework_list:
        return

    try:
        choice = int(input("\nEnter homework number to mark as done: "))
        homework_list[choice - 1].mark_done()
        print("Homework marked as completed!")

    except:
        print("Invalid input.")


def generate_report():
    ReportGenerator.generate_report(homework_list)


# -----------------------------
# Menu System
# -----------------------------
while True:

    print("\n==============================")
    print(" HOMEWORK MANAGEMENT SYSTEM ")
    print("==============================")
    print("1. Add Homework")
    print("2. View Homework")
    print("3. Mark Homework as Done")
    print("4. Generate Report")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_homework()

    elif choice == "2":
        view_homework()

    elif choice == "3":
        mark_homework_done()

    elif choice == "4":
        generate_report()

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice.")#    