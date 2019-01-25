# Two red beads are placed between every two blue beads. There are N blue beads. After looking at the arrangement below work out the number of red beads.

# @ @@ @ @@ @ @@ @ @@ @ @@ @

# Implement count_red_beads(n) (in PHP count_red_beads($n); in Java, Javascript, C, C++ countRedBeads(n)) so that it returns the number of red beads.
# If there are less than 2 blue beads return 0.

def count_red_beads(n):
    blue_beads = n
    if (blue_beads <= 2):
      return 0
    elif (blue_beads % 2 == 0):
        return blue_beads * 2
    else:
        return ((blue_beads -1) * 2)

count_red_beads(5)