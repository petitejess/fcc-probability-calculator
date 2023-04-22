import copy
import random
# Consider using the modules imported above.


class Hat:

  def __init__(self, **balls):
    self.contents = []
    for colour, ball_count in balls.items():
      for _ in range(ball_count):
        self.contents.append(colour)

  def draw(self, draw_n):
    drawn_balls = []

    if (draw_n >= len(self.contents)):
      drawn_balls = copy.deepcopy(self.contents)
      self.contents = []
      return drawn_balls

    for _ in range(draw_n):
      random_idx = random.randint(0, len(self.contents) - 1)
      drawn_balls.append(self.contents[random_idx])
      self.contents.pop(random_idx)

    return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  match_count = 0

  for _ in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    collected_balls = hat_copy.draw(num_balls_drawn)

    drawn_ball_collection = {}
    for colour in collected_balls:
      if (colour in drawn_ball_collection.keys()):
        drawn_ball_collection[colour] += 1
      else:
        drawn_ball_collection[colour] = 1

    found_match = []
    for colour in expected_balls:
      if ((colour in drawn_ball_collection) and (drawn_ball_collection[colour] >= expected_balls[colour])):
        found_match.append(True)

      if ((len(found_match) == len(expected_balls)) and all(x == True for x in found_match)):
        match_count += 1

  return match_count / num_experiments
