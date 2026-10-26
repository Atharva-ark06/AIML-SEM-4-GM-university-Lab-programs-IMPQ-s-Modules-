# Group-aware validation

When multiple rows belong to one person, device, site, or session, random splitting may put related records in both train and test sets.

Use group-aware splitting when the deployment task requires generalization to unseen groups. Define the group unit before evaluation and verify that no group crosses partitions. Explain when a group-based split is not appropriate.