class Solution:
    def cleanRoom(self, robot):
        """Solution
        [MEMO] Concept is still backtrack + visited
        Trick is how to use robot APIs to implement this
        """
        self.robot = robot
        self.directions = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
        visited = set()
        self.backtrack((0, 0), 0, visited)

    def backtrack(self, position, direction, visited):
        visited.add(position)
        self.robot.clean()

        new_direction = direction
        for i in range(4):
            new_position = (
                position[0] + self.directions[new_direction][0],
                position[1] + self.directions[new_direction][1],
            )

            if not new_position in visited and self.robot.move():
                self.backtrack(new_position, new_direction, visited)
                self.goback()

            self.robot.turnRight()
            new_direction += 1
            new_direction = new_direction % 4

    def goback(self):
        self.robot.turnRight()
        self.robot.turnRight()
        self.robot.move()
        self.robot.turnRight()
        self.robot.turnRight()
