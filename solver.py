class Ring:
    def __init__(self, pos: int, tpr: int):
        assert pos <= 6 and type(pos) == int, "Position must be integers between 1 and 6"
        self.position: int = pos  # 1 - 6
        assert tpr and -6 < tpr < 6 and type(tpr) == int, "Ticks per rotation must be integers between -5 and 5 and not 0"
        self.ticks_per_rotation: int = tpr

    def rotate(self) -> int:
        self.position += self.ticks_per_rotation
        if self.position > 6 or self.position < 1:
            self.position = self.position % 6
        return self.position

    def rotations_to_solve(self) -> int:
        sim: Ring = self
        rotations: int = 0
        while sim.position != 1:
            sim.rotate()
            rotations += 1
        return rotations

    def __str__(self) -> str:
        return f"At position {self.position}, Ticks per rotation = {self.ticks_per_rotation}"


class Compass:
    def __init__(self, ring1: Ring, ring2: Ring, ring3: Ring, moveset: list[list[int]]):
        assert not any(not (1 <= element <= 3) for row in moveset for element in row), "Invalid moveset"
        self.ring1: Ring = ring1
        self.ring2: Ring = ring2
        self.ring3: Ring = ring3
        self.rawmoveset = moveset
        self.moveset: list[list[Ring]] = []
        for ringset in moveset:
            moves_together = []
            for ring in ringset:
                if ring == 1:
                    moves_together.append(ring1)
                elif ring == 2:
                    moves_together.append(ring2)
                else:
                    moves_together.append(ring3)
            self.moveset.append(moves_together)

    def rotate(self, move_number: int):
        for ring in self.moveset[move_number]:
            ring.rotate()

    def solve(self):
        solution = [-1, -1, -1]
        found = False
        for i in range(6):
            for k in range(6):
                for m in range(6):
                    if self.ring1.position == self.ring2.position == self.ring3.position == 1:
                        solution[0] = i
                        solution[1] = k
                        solution[2] = m
                        found = True
                        break
                    self.rotate(2)
                if found:
                    break
                self.rotate(1)
            if found:
                break
            self.rotate(0)
        return solution

    def print_solution(self):
        ans = self.solve()
        for i in range(3):
            print(f"Rotate ring(s) {self.rawmoveset[i]} x{ans[i]} times")

    def __str__(self):
        return f"{str(self.ring1)}\n" \
               f"{str(self.ring2)}\n" \
               f"{str(self.ring3)}"


compass = Compass(Ring(3, 4), Ring(6, 1), Ring(5, -2), [[1, 3], [2], [3]])
compass.print_solution()