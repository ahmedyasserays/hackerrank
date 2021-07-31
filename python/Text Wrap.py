import textwrap
def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    return "\n".join(wrapper.wrap(string))
