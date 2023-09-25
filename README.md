# HSRCompassSolver
This tool brute-forces the Naviagtion Compass puzzles located throughout the Xianzhou Loufu region in Honkai: Star Rail.<br>
**Please note that `gui.py` is a WIP, and is not functional at this time. It will be finished at a later date.**

## Usage
Sample `Compass` constructor:
```python
c = Compass(Ring(3, 4), Ring(6, 1), Ring(5, -2), [[1, 3], [2], [3]])
```
- Initial Compass Indices (First argument in `Ring()`)
  - Starting from the leftmost tick, the index is 1.
  - Indices increment by 1 going clockwise.

- Rotations and Directions (Second argument in `Ring()`)
  - Each tick advanced by one rotation is considered 1.
  - If it rotates clockwise, the direction is positive. If counterclockwise, negative.

- Rings in Compass (1st, 2nd, 3rd args in `Compass()`)
  - First argument **must be** the outermost ring.
  - Second argument **must be** the middle ring.
  - Third argument **must be** the innermost ring.

- Ring Groups (Fourth argument in `Compass()`)
  - Outermost ring is index 1, middle 2, and innermost 3.
  - The order in which the ring groups alternate can be ignored.

The sample constructor above defines a Compass with:
- Outermost ring:
  - pointing at index 3,
  - with clockwise 4-tick rotations
- Middle ring:
  - pointing at index 6,
  - with clockwise 1-tick rotations
- Innermost ring:
  - pointing at index 5,
  - with counterclockwise 2-tick rotations
- Ring rotation groups of:
  - Outermost + Innermost,
  - Middle, and
  - Innermost

## Result
The Solver will print how many times you should rotate each Ring Group.<br><br>
The order in which you rotate does not matter as rotations are additive.<br><br>
If the Solver prints `-1` in any of the "number of rotations" fields, the input was malformed.<br>
Please double-check that your `Compass` constructor is an accurate representation of the puzzle.