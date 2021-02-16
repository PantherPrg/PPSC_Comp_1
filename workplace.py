def treasureNecklace(necklace):
  # write your code here
  hold = necklace[0]
  largest = 0
  group = 0

  for bead in necklace:
    if bead == hold:
      group += 1
    else:
      if group > largest:
        largest = group
      group = 1
      hold = bead

  if group > largest:
    largest = group

  return str(largest) + "\n"