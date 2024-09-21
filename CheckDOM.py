def checkDOM(strParam):
    """
    Checks the validity of HTML tags in a given string.
    Args:
        strParam (str): The input string containing HTML tags.
    Returns:
        bool or str: Returns True if all tags are valid and properly nested,
                     returns the mismatched closing tag if there is an opening tag without a corresponding closing tag,
                     returns False if there is a closing tag without a corresponding opening tag,
                     returns the mismatched opening tag if there are multiple opening tags without corresponding closing tags.
    """
    stack = []
    tags = ('b', 'i', 'em', 'div', 'p')
    mismatch = None
    last_opened = None

    idx = 0
    while idx < len(strParam):
        if strParam[idx] == '<':
            c = idx + 1
            while c < len(strParam) and strParam[c] != '>':
                c += 1
            if c == len(strParam):
                return False
            
            tag = strParam[idx + 1:c]

            if tag[0] == '/':
                tag = tag[1:]
                if tag not in tags:
                    return False
                if not stack:
                    if not mismatch:
                        mismatch = last_opened
                    else:
                        return False
                elif stack[-1] != tag:
                    if not mismatch:
                        mismatch = tag[-1]
                    else:
                        return False
                else:
                    stack.pop()

            else:
                if tag not in tags:
                    return False
                stack.append(tag)
                last_opened = tag

            idx = c
        idx += 1
    if stack:
        if len(stack) == 1:
            if mismatch == None:
                return False
            else:
                return stack[0]
        else:
            return False
    elif mismatch:
        return mismatch
    else:
        return True


print(checkDOM("<div><b><p>hello world</p></b></div>"), "True")
print(checkDOM("</div><p></p><div>"), "False")
print(checkDOM("<em></em><em></em><p></b>"), "p")
print(checkDOM("<div><p></p><b>< p></div>"), "False")
print(checkDOM( "<div><i>hello</i>world</b>"), "div")
print("")

print(checkDOM("<div><b><p>hello world</p></b></div>"))
print(checkDOM("</div><p></p><div>"))
print(checkDOM("<div><i>hello</i>world</b>"))
print(checkDOM("<div></div><p><b></b></p>"))
print(checkDOM("<div></div></div><div><p></p></div>"))        