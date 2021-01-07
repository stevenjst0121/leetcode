"""
How to run with command line input:
$ python3.8 arcade_gamer.py

How to run unit test with pytest:
$ python3.8 -m pytest arcade_gamer.py
"""

import sys
from typing import List, Set


MAX_TIME = 120


class Game:
    def __init__(self, name: str, time: int, reward: int) -> None:
        self.name = name
        self.time = time
        self.reward = reward

    def __eq__(self, other: "Game") -> bool:
        return self.name == other.name and self.time == other.time and self.reward == other.reward

    def __lt__(self, other: "Game") -> bool:
        return self.time < other.time

    def __repr__(self) -> str:
        return f"Game: name={self.name}, time={self.time}, reward={self.reward}"


class Solution:
    def find_best_strategy_class(self, games: List, time_left: int) -> List:
        if not games:
            return []

        result = []
        best_reward = 0
        for game in games:
            if game.time > time_left:
                break

            # play this game
            new_games = games.copy()
            new_games.remove(game)
            to_play = self.find_best_strategy_class(new_games, time_left - game.time)

            # calculate reward
            reward = game.reward
            for played in to_play:
                reward += played.reward
            if reward > best_reward:
                best_reward = reward
                result = []
                result.append(game)
                result.extend(to_play)

        return result

    def find_best_strategy_no_class(self, games: List, time_left: int) -> List:
        """
        Description:
            Given a list of games and how much time left to play, return
            a list of games to play that will result in most rewards
        """
        if not games:
            # no game to play
            return []

        result = []
        best_reward = 0  # total reward of result
        for game in games:
            # Loop through all games and try to play the game
            if game[1] > time_left:
                # Since we have sorted all games by time, if the current game exceeds
                # the time limit already, there is no need to try further
                break

            # Play this game
            new_games = games.copy()
            new_games.remove(game)
            # Recursively call the same function and find the best strategy to play
            # the rest of games using time left
            to_play = self.find_best_strategy_no_class(new_games, time_left - game[1])

            # Calculate reward
            reward = game[2]
            for played in to_play:
                reward += played[2]

            # Set result to current strategy if the current reward is better
            if reward > best_reward:
                best_reward = reward
                result = []
                result.append(game)
                result.extend(to_play)

        return result


def load_games_class() -> List:
    # Load data in time-sorted order
    num_lines = sys.stdin.readline()
    num_lines = int(num_lines)

    games = []
    for _ in range(num_lines):
        line = sys.stdin.readline()
        data = line.split(",")
        assert len(data) == 3

        game = Game(data[0], int(data[1]), int(data[2]))
        games.append(game)
    games.sort()
    return games


def load_games_no_class() -> List:
    # Load data in time-sorted order
    num_lines = sys.stdin.readline()
    num_lines = int(num_lines)

    # Read games line-by-line and add all games to a list
    games = []
    for _ in range(num_lines):
        line = sys.stdin.readline()
        data = line.split(",")
        assert len(data) == 3

        # Each game is a tuple in such format of (name, time, reward)
        game = (data[0], int(data[1]), int(data[2]))
        games.append(game)

    # Sort all games by time
    games.sort(key=lambda x: x[1])
    return games


def output(result: List) -> None:
    for game in result:
        print(game.name)


def main():
    games = load_games_no_class()
    solution = Solution()
    result = solution.find_best_strategy_no_class(games, MAX_TIME)
    output(result)


if __name__ == "__main__":
    main()


# Test
def test_given_dataset_class():
    # GIVEN
    games = []
    games.append(Game("Pac-man", 80, 400))
    games.append(Game("Motal Kombat", 10, 30))
    games.append(Game("Super Tetris", 25, 100))
    games.append(Game("Pump it Up", 10, 40))
    games.append(Game("Street Fighter II", 90, 450))
    games.append(Game("Speed Racer", 10, 40))
    games.sort()

    # WHEN
    solution = Solution()

    # THEN
    result = solution.find_best_strategy_class(games, MAX_TIME)
    assert result == [
        Game("Motal Kombat", 10, 30),
        Game("Pump it Up", 10, 40),
        Game("Speed Racer", 10, 40),
        Game("Street Fighter II", 90, 450),
    ]


def test_given_dataset_no_class():
    # GIVEN
    games = []
    games.append(("Pac-man", 80, 400))
    games.append(("Motal Kombat", 10, 30))
    games.append(("Super Tetris", 25, 100))
    games.append(("Pump it Up", 10, 40))
    games.append(("Street Fighter II", 90, 450))
    games.append(("Speed Racer", 10, 40))
    games.sort(key=lambda x: x[1])  # sort by time

    # WHEN
    solution = Solution()

    # THEN
    result = solution.find_best_strategy_no_class(games, MAX_TIME)
    assert result == [
        ("Motal Kombat", 10, 30),
        ("Pump it Up", 10, 40),
        ("Speed Racer", 10, 40),
        ("Street Fighter II", 90, 450),
    ]
