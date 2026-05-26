class AnalyticsEngine:

    def __init__(self, storage):
        self.storage = storage
    def get_closed_tickets(self):
        pass
    def calculate_mttr(self, machine_id):
        pass
    def calculate_mttr(self, machine_id):
        pass
    def calculate_mtbf(self, machine_id):
        pass
    def breakdown_count_by_machine(self):
        pass
    def machine_rankings(self):
        pass
    def summary(self):
        pass
if __name__ == "__main__":
    engine = AnalyticsEngine(storage)
    print(engine.summary())