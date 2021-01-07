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
    def find_best_strategy(self, games: List, time_left: int) -> List:
        # return list of games
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
            to_play = self.find_best_strategy(new_games, time_left - game.time)

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


def load_games() -> List:
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


def output(result: List) -> None:
    for game in result:
        print(game.name)


def main():
    games = load_games()
    solution = Solution()
    result = solution.find_best_strategy(games, MAX_TIME)
    output(result)


if __name__ == "__main__":
    main()


# Test
def test_given_dataset():
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
    result = solution.find_best_strategy(games, MAX_TIME)
    assert result == [
        Game("Motal Kombat", 10, 30),
        Game("Pump it Up", 10, 40),
        Game("Speed Racer", 10, 40),
        Game("Street Fighter II", 90, 450),
    ]
