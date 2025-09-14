from collections import deque

history = deque(maxlen=3)

def visit_page(url):
    history.append(url)
    print(f"Visiting: {url}")

def go_back():
    if history:
        current = history.pop()
        print(f"Going back: {current}")
        if history:
            print(f"Current page now: {history[-1]}")
        else:
            print("no more pages")
    else:
        print("no pages")


visit_page('/home')
visit_page('about')

go_back()