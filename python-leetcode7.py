print("Leetcode 7: Unique Email Addresses")

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
    
        # use a set to store distinct emails
        unique_emails = set()

        for email in emails:
            # split email into local and domain parts
            local = email.split('@')[0]
            domain = email.split('@')[1]

            # delete letters after '+', then remove all '.'   
            local = local.split('+')[0]
            new_local = local.replace('.', '')

            # optimized version
            # new_local = email.split('@')[0].split('+')[0].replace('.', '')  
            # unique_emails.add(new_local + '@' + email.split('@')[1])

            # add checked email to the set
            unique_emails.add(new_local + '@' + domain)

        # return the number of distinct emails
        return len(unique_emails)

# test cases
sol = Solution()
result = sol.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
print(result) # should return 2

sol2 = Solution()
result2 = sol2.numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"])
print(result2) # should return 3