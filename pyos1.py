class Task:
    taskid = 0

    def __init__(self, target):
        Task.taskid += 1
        self.taskid = Task.taskid
        self.target = target
        self.sendval = None

    def run(self):
        return self.target.send(self.sendval)
