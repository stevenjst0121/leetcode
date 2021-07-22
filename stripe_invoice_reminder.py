import heapq
from unittest.mock import Mock, MagicMock, patch


class Invoicer:
    # https://www.1point3acres.com/bbs/thread-561847-1-1.html

    def __init__(self):
        self.heap = []

    def schedule(self, schedules):
        for ts, name, amount in schedules:
            content = f"Invoice for {name} for {amount} dollars"
            heapq.heappush(self.heap, (ts - 10, f"[Upcoming] {content}"))
            heapq.heappush(self.heap, (ts, f"[New] {content}"))
            heapq.heappush(self.heap, (ts + 20, f"[Reminder] {content}"))
            heapq.heappush(self.heap, (ts + 30, f"[Due] {content}"))

        result = []
        while self.heap:
            result.append(heapq.heappop(self.heap)[1])
        return result


def test_invoicer():
    schedules = [[0, "Alice", 200], [1, "Bob", 100]]
    invoicer = Invoicer()
    result = invoicer.schedule(schedules)
    assert len(result) == 8
    assert result[0] == "[Upcoming] Invoice for Alice for 200 dollars"
    assert result[1] == "[Upcoming] Invoice for Bob for 100 dollars"
    assert result[2] == "[New] Invoice for Alice for 200 dollars"
    assert result[3] == "[New] Invoice for Bob for 100 dollars"
    assert result[4] == "[Reminder] Invoice for Alice for 200 dollars"
    assert result[5] == "[Reminder] Invoice for Bob for 100 dollars"
    assert result[6] == "[Due] Invoice for Alice for 200 dollars"
    assert result[7] == "[Due] Invoice for Bob for 100 dollars"


@patch("stripe_invoice_reminder.Invoicer")
def test_invoice_mock(MockInvoicer):
    invoicer = MockInvoicer()
    invoicer.schedule.return_value = ["wierd stuff"]
    assert invoicer.schedule(None) == ["wierd stuff"]


def test_incoice_mock_2():
    invoicer = Invoicer()
    invoicer.schedule = MagicMock()
    invoicer.schedule.return_value = ["wierd stuff"]
    assert invoicer.schedule(None) == ["wierd stuff"]


if __name__ == "__main__":
    schedules = [
        [3, "Patty"],
        [0, "Steven"],
        [5, "Tony"],
    ]
    invoicer = Invoicer()
    result = invoicer.schedule(schedules)
