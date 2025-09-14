# Union between two sets, is that it will make everything unique and add them as one

group_a = {"gym", "dumbell", "barbell", "swim"}
group_b = {"boxing", "cricket", "hiking", "swim"}

union_group = group_a.union(group_b)
print(f"union_group: {union_group}") # union_group: {'hiking', 'cricket', 'gym', 'dumbell', 'barbell', 'boxing'}


# intersection is only fetching the ones that match
intersection_match = group_a.intersection(group_b)
print(f"intersection_match: {intersection_match}") #intersection_match: {'swim'}

# differnce, gets interest that is different
difference_group = group_a.difference(group_b)
print(f"difference: {difference_group}")

# symmetric difference on each set
symmetric = group_a.symmetric_difference(group_b)
print(f"symmetric: {symmetric}") # symmetric: {'dumbell', 'gym', 'boxing', 'barbell', 'cricket', 'hiking'}

# can also use set.update()

#symmetric_diference)update, good method to check what files are missing from backup

current_files = {"report.pdf", "dog.png"}
backup_files = {"report.pdf", "photo1.png"}

sym_diff_update = current_files.symmetric_difference_update)