from nose.tools import assert_true, assert_false
from array_stack import ArrayStack


def is_matched_html(string):
    tag_stack = ArrayStack()
    open_idx = string.find("<")
    while open_idx != -1:
        close_idx = string.find(">", open_idx+1)
        if close_idx == -1:
            return False
        tag = string[open_idx + 1:close_idx]
        if tag.startswith("/"):         # It is close tag
            if tag_stack.is_empty():
                return False
            if tag_stack.pop() != tag[1:]:
                return False
        else:
            tag_stack.push(tag)

        open_idx = string.find("<", close_idx+1)

    return tag_stack.is_empty()

if __name__ == "__main__":
    html_str = "<a><b>aa</b></a>"
    assert_true(is_matched_html(html_str))
    html_str = "<a><b>aa</c></a>"
    assert_false(is_matched_html(html_str))
    print("Success ...")


