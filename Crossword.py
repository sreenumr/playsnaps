import random

HORIZONTAL = 'H'
VERTICAL = 'V'
EMPTY = '-'

class Crossword:
    def __init__(self, width, height, words):
        self.width = width
        self.height = height
        self.words = words
        self.grid = [[EMPTY] * width for _ in range(height)]
        self.randomizer = random.Random()
        self.placed_words = []

    def _randomize_word_list(self):
        self.randomizer.shuffle(self.words)

    def _find_all_positions_for_word(self, word):
        positions = []
        length = len(word)

        # Try to find positions for horizontal placement
        for y in range(self.height):
            for x in range(self.width - length + 1):
                if all(self.grid[y][x + i] in (EMPTY, word[i]) for i in range(length)):
                    if self._check_no_adjacent(y, x, length, HORIZONTAL):
                        positions.append((x, y, HORIZONTAL))

        # Try to find positions for vertical placement
        for y in range(self.height - length + 1):
            for x in range(self.width):
                if all(self.grid[y + i][x] in (EMPTY, word[i]) for i in range(length)):
                    if self._check_no_adjacent(y, x, length, VERTICAL):
                        positions.append((x, y, VERTICAL))

        return positions

    def _check_no_adjacent(self, y, x, length, direction):
        if direction == HORIZONTAL:
            # Check left and right of the word
            if x > 0 and self.grid[y][x - 1] != EMPTY:
                return False
            if x + length < self.width and self.grid[y][x + length] != EMPTY:
                return False
            # Check above and below each character
            for i in range(length):
                if y > 0 and self.grid[y - 1][x + i] != EMPTY:
                    return False
                if y < self.height - 1 and self.grid[y + 1][x + i] != EMPTY:
                    return False
            # Ensure a row space above and below
            if y > 1:
                for i in range(length):
                    if self.grid[y - 2][x + i] != EMPTY:
                        return False
            if y < self.height - 2:
                for i in range(length):
                    if self.grid[y + 2][x + i] != EMPTY:
                        return False
            return True
        else:
            # Check above and below the word
            if y > 0 and self.grid[y - 1][x] != EMPTY:
                return False
            if y + length < self.height and self.grid[y + length][x] != EMPTY:
                return False
            # Check left and right of each character
            for i in range(length):
                if x > 0 and self.grid[y + i][x - 1] != EMPTY:
                    return False
                if x < self.width - 1 and self.grid[y + i][x + 1] != EMPTY:
                    return False
            # Ensure a column space left and right
            if x > 1:
                for i in range(length):
                    if self.grid[y + i][x - 2] != EMPTY:
                        return False
            if x < self.width - 2:
                for i in range(length):
                    if self.grid[y + i][x + 2] != EMPTY:
                        return False
            return True

    def _find_intersections(self, word):
        intersections = []
        word_len = len(word)
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] in word:
                    for i in range(word_len):
                        if self.grid[y][x] == word[i]:
                            start_col = x - i
                            start_row = y - i
                            if self._check_intersection_validity(word, x, y, HORIZONTAL, start_col):
                                intersections.append((start_col, y, HORIZONTAL))
                            if self._check_intersection_validity(word, x, y, VERTICAL, start_row):
                                intersections.append((x, start_row, VERTICAL))
        return intersections

    def _check_intersection_validity(self, word, x, y, direction, start):
        length = len(word)
        if direction == HORIZONTAL:
            if start < 0 or start + length > self.width:
                return False
            if all(self.grid[y][start + i] in (EMPTY, word[i]) for i in range(length)):
                return True
        elif direction == VERTICAL:
            if start < 0 or start + length > self.height:
                return False
            if all(self.grid[start + i][x] in (EMPTY, word[i]) for i in range(length)):
                return True
        return False

    def _place_word(self, word, position):
        x, y, direction = position

        if direction == HORIZONTAL:
            for i, char in enumerate(word):
                self.grid[y][x + i] = char
        else:
            for i, char in enumerate(word):
                self.grid[y + i][x] = char

        self.placed_words.append(word)

    def generate(self):
        self._randomize_word_list()
        for word in self.words:
            intersections = self._find_intersections(word)
            positions = self._find_all_positions_for_word(word)
            all_positions = intersections + positions
            if all_positions:
                all_positions = sorted(all_positions, key=lambda pos: self._count_intersections(word, pos), reverse=True)
                position = all_positions[0]
                self._place_word(word, position)
            else:
                print(f"Could not place the word: {word}")

    def _count_intersections(self, word, position):
        x, y, direction = position
        count = 0
        for i, char in enumerate(word):
            if direction == HORIZONTAL:
                if self.grid[y][x + i] == char:
                    count += 1
            else:
                if self.grid[y + i][x] == char:
                    count += 1
        return count

    def display(self):
        for row in self.grid:
            print(' '.join(row))

if __name__ == "__main__":
    word_list = ['apple', 'banana', 'orange', 'grape', 'pineapple', 'pomegranate']
    crossword = Crossword(15, 15, word_list)
    crossword.generate()
    crossword.display()
