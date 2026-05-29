#report genrator.py

import os


class ReportGenerator:

    def __init__(self, analytics_engine):
        self.analytics = analytics_engine

    def generate_summary_report(self):

        summary = self.analytics.summary()

        report = "\n===== SHIFTDESK SUMMARY REPORT =====\n"

        report += f"Total Tickets     : {summary['total_tickets']}\n"
        report += f"Closed Tickets    : {summary['closed_tickets']}\n"
        report += f"Open Tickets      : {summary['open_tickets']}\n"
        report += f"Average MTTR      : {summary['average_mttr_hours']} hrs\n"
        report += f"Average MTBF      : {summary['average_mtbf_hours']} hrs\n"

        return report

    def generate_machine_ranking_report(self):

        rankings = [
            "MC003",
            "MC002",
            "MC001"
        ]

        report = "\n===== MACHINE RANKINGS =====\n"

        rank = 1

        for machine in rankings:

            report += f"{rank}. {machine}\n"

            rank += 1

        return report

    def generate_breakdown_report(self):

        breakdowns = {
            "MC001": 10,
            "MC002": 5,
            "MC003": 2
        }

        report = "\n===== BREAKDOWN REPORT =====\n"

        for machine, count in breakdowns.items():

            report += f"{machine} : {count}\n"

        return report

    def export_report(self, filename, content):

        os.makedirs("outputs", exist_ok=True)

        filepath = os.path.join("outputs", filename)

        with open(filepath, "w") as file:
            file.write(content)

        print(f"Report exported to {filepath}")


if __name__ == "__main__":

    from analytics.analytics_engine import AnalyticsEngine

    analytics = AnalyticsEngine()

    rg = ReportGenerator(analytics)

    summary_report = rg.generate_summary_report()

    print(summary_report)

    rg.export_report(
        "summary_report.txt",
        summary_report
    )