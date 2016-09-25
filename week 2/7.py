# To check valid Python identifiers (alphanumerics)

# a. Use String Concatenation in your script
import re
identifier = re.compile(r"^[^\d\W]\w*\Z", re.UNICODE)

tests = ["a", "a1", "_a1", "1a", "aa$%@%", "aa bb", "aa_bb", "aa\n"]
for test in tests:
    result = re.match(identifier, test)
    print("%s\t= %s" % (test, (result is not None)))
