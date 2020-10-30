# Did not event figure out 1 possible solution, think more
# Loop hole that I fall in is I tried to use map for merging,
# the problem is that this way I can only merge two lists at one point.
# However, it is likely that two accounts have no common emails, but
# the third account has common emails with both. So I need a way to
# merge all accounts given an account name.

from typing import List
from collections import defaultdict, deque


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """Solution 1
        Use a graph to connect all emails that should belong to the same account
        [MEMO] Think of using a graph for problems like:
        A long as one item satisfies some criteria, all items it relates to should all belong to this criteria.
        An undirected graph can easily find all connected items
        [MEMO] The most straight forward implementation in python using Adjancey List is just dict node -> List[node]
        [MEMO] Adjancey Matrix uses more space O(N^2), but removing a node is only O(1)

        TODO Look into Disjoint Set Union (DSU) structure
        """
        email_to_name = {}
        graph = defaultdict(set)
        for account in accounts:
            name = account[0]
            emails = account[1:]
            for email in emails:
                # assuming there must be at least one email per account
                # connect all emails belong to the same account
                # to the first email
                # Add connection to self is ok, when iterating use a seen set
                graph[account[1]].add(email)
                graph[email].add(account[1])
                email_to_name[email] = name

        result = []
        seen = set()
        for email in graph:
            if email not in seen:
                seen.add(email)
                stack = deque()
                stack.append(email)
                emails = []
                while stack:
                    node = stack.pop()
                    emails.append(node)
                    for neighbor in graph[node]:
                        if neighbor not in seen:
                            seen.add(neighbor)
                            stack.append(neighbor)
                result.append([email_to_name[email]] + sorted(emails))
        return result
