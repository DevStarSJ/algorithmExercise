def boxes_and_balls(num_red, num_blue, only_red, only_blue, both_colors):
    init_score = num_red * only_red + num_blue * only_blue
    change_count = min([num_red, num_blue])

    if min([only_red, only_blue, both_colors]) == both_colors:
        return init_score

    scores = [(num_red - x) * only_red + (num_blue - x) * only_blue + 2 * x * both_colors
               for x in range(1, change_count + 1)]\
             + [init_score]

    return max(scores)

print(boxes_and_balls(2,3,100,400,200))
print(boxes_and_balls(2,3,100,400,300))
print(boxes_and_balls(5,5,464,464,464))
print(boxes_and_balls(1,4,20,-30,-10))
print(boxes_and_balls(9,1,-1,-10,4))