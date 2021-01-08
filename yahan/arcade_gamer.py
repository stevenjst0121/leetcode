"""
How to run with command line input:
$ python3.8 arcade_gamer.py

How to run unit test with pytest:
$ python3.8 -m pytest arcade_gamer.py
"""

import sys
from typing import List, Set


MAX_TIME = 120


class Solution:
    def find_best_strategy(self, games: List, played: List, time_left: int) -> List:
        """
        Description:
            Given a list of games, games already played and how much time left to play, return
            a list of games to play that will result in most rewards
        """
        print(f"{played}, {time_left}")
        if not games:
            # no game to play
            return []

        result = []
        best_reward = 0  # total reward of result
        for game in games:
            # Loop through all games and try to play the game
            if game in played:
                # Played this game already
                continue
            if game[1] > time_left:
                # Since we have sorted all games by time, if the current game exceeds
                # the time limit already, there is no need to try further
                break

            # Play this game
            played.append(game)
            # Recursively call the same function and find the best strategy to play
            # the rest of games using time left
            to_play = self.find_best_strategy(games, played, time_left - game[1])

            # Calculate reward
            reward = game[2]
            for play in to_play:
                reward += play[2]

            # Set result to current strategy if the current reward is better
            if reward > best_reward:
                best_reward = reward
                result = []
                result.append(game)
                result.extend(to_play)
                print(f"Setting result = {result}")

            # Remove game from played
            played.remove(game)

        return result


def load_games() -> List:
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
    games = load_games()
    solution = Solution()
    result = solution.find_best_strategy(games, [], MAX_TIME)
    output(result)


if __name__ == "__main__":
    main()


# Test
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
    result = solution.find_best_strategy(games, [], MAX_TIME)
    print(result)
    assert result == [
        ("Motal Kombat", 10, 30),
        ("Pump it Up", 10, 40),
        ("Speed Racer", 10, 40),
        ("Street Fighter II", 90, 450),
    ]
