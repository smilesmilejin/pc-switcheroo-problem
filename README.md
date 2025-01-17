# Switcheroo Problem

Problem belonging to the post-classroom Mock Interview Question Repository.

## Problem Statement

We are interested in writing a function that shuffles a linked list by swapping adjacent items.

For example, if we have a linked list with the following elements:

a → b → c → d → e → f

after shuffling, we should get the following output list:

b → a → d → c → f → e

Notice that adjacent items have swapped position:

- a swapped with b
- c swapped with d
- e swapped with f

If there are an odd number of elements, the tail should not change position.

For example, if we have a linked list with five elements:

a → b → c → d → e

After shuffling, 'e' should remain the tail.

b → a → d → c → e

Notice that the first four elements swapped position like before, but that 'e' did not move.

## Examples

### Example 1

Shuffling the following list

a → b → c → d → e → f

produces

b → a → d → c → f → e

### Example 2

Shuffling the following list

a → b → c → d → e

produces

b → a → d → c → e

### Example 3

Shuffling the following list

7 → 2

produces

2 → 7

### Example 4

Shuffling the following list

a

produces

a

## Notes for the Interviewer

### Clarifying Questions

#### Q: What should I do if there's an empty list?

A: You can assume the list will have at least one node.

#### Q: What should I do if there's only one node?

A: See the final test case for the expected behavior.

#### Q: What should I do if invalid input is passed in?

A: You can assume that the input will be valid.

#### Q: What should I do if there's a cycle in the input list?

A: You can assume there will be no cycles.

#### Q: Is it OK if I mutate the original list?

A: Yes.

### Hints

- If your candidate struggles with an initial algorithm, encourage them to walk through an example and describe how they would do it using only pen and paper.

- If your candidate struggles to determine how to handle cases where the length of the list is odd, encourage them first to solve the simpler case where the length of the list is even. The first test case has an even number of nodes.

- If your candidate's result has a cycle in it, the assertions will fail. If your candidate runs into this, encourage them to print the list nodes one by one to determine where th cycle happens in their list. This is a tricky problem where it's very easy to accidentally make a cycle!

## Optional Bonus At-Home Challenges

To be attempted after completing the interview.

- What's the complexity of the sample solution?

- If you wrote a recursive solution, try writing an iterative solution instead. If you wrote an iterative solution, try writing a recursive one. What are the tradeoffs between these two approaches? Which do you prefer?

- Expand you solution so it can handle swapping more than two numbers. It should take in an additional parameter `k`, which specifies how large of sub-groups to perform one rotation on.

  For example, with a `k` value of 3 the following list:

  a → b → c → d → e → f

  should become

  c → a → b → f → d → e

- Expand the previous solution so that it takes an additional parameter `r`, which specifies how many rotations to perform on each sub-group.
