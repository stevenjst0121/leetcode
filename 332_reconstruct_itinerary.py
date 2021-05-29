from typing import List
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for origin, destination in tickets:
            # [destination, whether the ticket has been used]
            graph[origin].append([destination, False])

        for _, destinations in graph.items():
            destinations.sort(key=lambda x: x[0])

        self.result = []
        self.backtrack(graph, "JFK", ["JFK"], len(tickets))
        return self.result

    def backtrack(self, graph, origin, route, ticket_count):
        # Doing backtrack + greedy, need to return True/False indicate if greedy
        # has found a solution, so we can abort the process
        if len(route) == ticket_count + 1:
            # Get copy!
            self.result = route.copy()
            return True

        for destination in graph[origin]:
            if not destination[1]:
                destination[1] = True
                route.append(destination[0])
                ret = self.backtrack(graph, destination[0], route, ticket_count)
                route.pop()
                destination[1] = False
                if ret:
                    return True
        return False

    # def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    #     """Solution 2
    #     [????] Need to fully understand
    #     """
    #     self.graph = defaultdict(list)
    #     ticket_count = 0
    #     for ticket in tickets:
    #         depart = ticket[0]
    #         arrival = ticket[1]
    #         self.graph[depart].append(arrival)

    #     for _, arrivals in self.graph.items():
    #         arrivals.sort(reverse=True)

    #     self.result = []
    #     self.dfs("JFK")
    #     return self.result[::-1]

    # def dfs(self, depart):
    #     arrivals = self.graph[depart]
    #     while arrivals:
    #         arrival = arrivals.pop()
    #         self.dfs(arrival)
    #     self.result.append(depart)

    # def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    #     """Draft 1
    #     Did not understand the problem in the first place, took long time to debug
    #     beats 37%
    #     """
    #     graph = defaultdict(list)
    #     ticket_count = 0
    #     for ticket in tickets:
    #         depart = ticket[0]
    #         arrival = ticket[1]
    #         graph[depart].append(arrival)
    #         ticket_count += 1

    #     if "JFK" not in graph:
    #         return []

    #     used = set()
    #     return self.dfs(graph, "JFK", used, ticket_count)

    # def dfs(self, graph, depart, used, count):
    #     arrivals = list(graph[depart])
    #     for arrival in sorted(arrivals):
    #         if (depart, arrival) in used:
    #             continue

    #         if count - used == 1:
    #             return [depart, arrival]

    #         used.add((depart, arrival))
    #         itinerary = self.dfs(graph, arrival, used, count)
    #         if itinerary:
    #             return [depart] + itinerary
    #         used.remove((depart, arrival))

    #     return []
