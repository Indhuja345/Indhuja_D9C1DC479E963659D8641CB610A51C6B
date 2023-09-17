#to create objects of both the Batsman and Bowler classes and call the play() method for each object.
class Player:

  def play(self):
    print("The player is playing cricket.")


class Batsman(Player):

  def play(self):
    print("The batsman is batting.")


class Bowler(Player):

  def play(self):
    print("The bowler is bowling.")


batsman = Batsman()
bowler = Bowler()

batsman.play()
bowler.play()
