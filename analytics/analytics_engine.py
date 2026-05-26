from datetime import datetime


class AnalyticsEngine:

    def __init__(self, storage=None):
        self.storage = storage

    def calculate_mttr(self, reported_at, closed_at):
        """
        MTTR = Closed Time - Reported Time
        Returns hours
        """

        if not reported_at or not closed_at:
            return 0

        duration = closed_at - reported_at

        return round(duration.total_seconds() / 3600, 2)

    def calculate_mtbf(self, previous_closed_at, next_reported_at):
        """
        MTBF = Next Failure Time - Previous Close Time
        Returns hours
        """

        if not previous_closed_at or not next_reported_at:
            return 0

        duration = next_reported_at - previous_closed_at

        return round(duration.total_seconds() / 3600, 2)

    def summary(self):

        reported = datetime(2025, 6, 1, 10, 0)
        closed = datetime(2025, 6, 1, 12, 30)

        mttr = self.calculate_mttr(reported, closed)

        previous_closed = datetime(2025, 6, 1, 12, 30)
        next_reported = datetime(2025, 6, 3, 12, 30)

        mtbf = self.calculate_mtbf(
            previous_closed,
            next_reported
        )

        return {
            "total_tickets": 10,
            "closed_tickets": 8,
            "open_tickets": 2,
            "average_mttr_hours": mttr,
            "average_mtbf_hours": mtbf
        }


if __name__ == "__main__":

    engine = AnalyticsEngine()

    result = engine.summary()

    print("\n===== ANALYTICS SUMMARY =====")

    for key, value in result.items():
        print(f"{key}: {value}")