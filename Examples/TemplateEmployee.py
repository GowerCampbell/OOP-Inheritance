class TemplateEmployee:
    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position

    def work(self):
        return f"{self.name} is working as a {self.position}."


class Manager(TemplateEmployee):
    def __init__(self, name, salary, position, team_size):
        # Directly initialize TemplateEmployee
        TemplateEmployee.__init__(self, name, salary, position)
        self.team_size = team_size


class Developer(TemplateEmployee):
    def __init__(self, name, salary, position, language):
        # Directly initialize TemplateEmployee
        TemplateEmployee.__init__(self, name, salary, position)
        self.language = language


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, position, language, team_size, responsibility):
        # Explicitly initialize Manager and Developer
        Manager.__init__(self, name, salary, position, team_size)
        Developer.__init__(self, name, salary, position, language)
        self.responsibility = responsibility


# Instances
manager = Manager("Alex", 70000, "Senior Manager", 3)
developer = Developer("Bob", 100000, "Senior Developer", "Python/Ruby")
team_lead = TeamLead("Carl", 120000, "Team Lead", "C++", 3, "Project Leader")

# Outputs
print("\nName: ", manager.name)
print("Salary: ", manager.salary)
print("Work: ", manager.work())
print("Team Size: ", manager.team_size)

print("\nName: ", developer.name)
print("Salary: ", developer.salary)
print("Work: ", developer.work())
print("Language: ", developer.language)

print("\nName: ", team_lead.name)
print("Salary: ", team_lead.salary)
print("Work: ", team_lead.work())
print("Language: ", team_lead.language)
print("Team Size: ", team_lead.team_size)
print("Responsibility: ", team_lead.responsibility)


