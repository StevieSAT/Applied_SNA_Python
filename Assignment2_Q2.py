'''
Question 2
How many employees are represented in the network?

How many sender->recipient pairs of employees are there in the network such that sender sent at least one email to recipient? Note that even if a sender sent multiple messages to a recipient, they should only be counted once. You should not exclude cases where an employee sent emails to themselves from this [email] count.

This function should return a tuple with two integers (#employees, # sender->recipient pairs).
'''

def answer_two():
    # YOUR CODE HERE
    email = answer_one()
    employees = set(email.nodes())
    sender_recipient_pairs = set(email.edges())
    return (len(employees), len(sender_recipient_pairs))
    raise NotImplementedError()
    
    
ans_two = answer_two()
