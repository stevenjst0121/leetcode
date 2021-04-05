from typing import Tuple


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """First draft, O(N), beats 58%
        Solution proves that at most 4 runs, in order to have such a cycle,
        it must be back to origin before exhaust.

        We don't actually need to run all 4 cycles:
        * if the robot returns to the initial point after one cycle, that's the limit cycle trajectory.
        * if the robot doesn't face north at the end of the first cycle
        """
        x, y, direction = 0, 0, "N"
        iterations = 0
        while iterations < 4:
            for instruction in instructions:
                if instruction == "G":
                    x, y = self.go(x, y, direction)
                elif instruction == "L":
                    direction = self.turn_left(direction)
                elif instruction == "R":
                    direction = self.turn_right(direction)

            # Check if it's back to origin
            if x == 0 and y == 0:
                return True

            iterations += 1
        return False

    def go(self, x: int, y: int, direction: str) -> Tuple:
        if direction == "N":
            return (x, y + 1)
        elif direction == "E":
            return (x + 1, y)
        elif direction == "S":
            return (x, y - 1)
        elif direction == "W":
            return (x - 1, y)

    def turn_left(self, direction: str):
        if direction == "N":
            return "W"
        elif direction == "W":
            return "S"
        elif direction == "S":
            return "E"
        elif direction == "E":
            return "N"

    def turn_right(self, direction: str):
        if direction == "N":
            return "E"
        elif direction == "E":
            return "S"
        elif direction == "S":
            return "W"
        elif direction == "W":
            return "N"
