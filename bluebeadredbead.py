# Two red beads are placed between every two blue beads. There are N blue beads. After looking at the arrangement below work out the number of red beads.

# @ @@ @ @@ @ @@ @ @@ @ @@ @

# Implement count_red_beads(n) (in PHP count_red_beads($n); in Java, Javascript, C, C++ countRedBeads(n)) so that it returns the number of red beads.
# If there are less than 2 blue beads return 0.

def count_red_beads(nb):
    return max(0, 2 * (nb - 1))

count_red_beads(5)