class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = deque()
        self.stack.append(homepage)
        self.curr_ind = 0        

    def visit(self, url: str) -> None:        
        # clean forward history       
        # how many to clean?
        size = len(self.stack)
        to_clean = size - self.curr_ind - 1
        for _ in range(to_clean):
            self.stack.pop()
        self.curr_ind = len(self.stack) - 1
        self.stack.append(url)
        self.curr_ind += 1
        

    def back(self, steps: int) -> str:
        # can we move back?
        if steps > self.curr_ind:
            self.curr_ind = 0
            return self.stack[self.curr_ind]
        self.curr_ind -= steps
        return self.stack[self.curr_ind]                
        

    def forward(self, steps: int) -> str:
        # can move forward ?
        if steps > (len(self.stack) - self.curr_ind - 1):
            self.curr_ind = len(self.stack) - 1
            return self.stack[self.curr_ind]
        self.curr_ind += steps
        return self.stack[self.curr_ind]


# TODO fix
# calls = ["BrowserHistory","visit","visit","back","visit","visit","back","forward","visit","visit","visit","visit","visit","visit","forward","forward","visit","back","visit","visit","visit","visit","forward","visit","visit","visit"]
# args = [["momn.com"],["bx.com"],["bjyfmln.com"],[3],["ijtrqk.com"],["dft.com"],[10],[10],["yc.com"],["yhl.com"],["xynxvix.com"],["izfscdv.com"],["cdenhm.com"],["ocgcjz.com"],[5],[5],["gtd.com"],[9],["hfeour.com"],["ghmh.com"],["nnm.com"],["knm.com"],[4],["cbtg.com"],["acyvwod.com"],["mydr.com"]]
# expected = [None,None,None,"momn.com",None,None,"momn.com","dft.com",None,None,None,None,None,None,"ocgcjz.com","ocgcjz.com",None,"momn.com",None,None,None,None,"knm.com",None,None,None]

# assert all([call(*arg) == exp for call,arg,exp in zip(calls, args, expected) ])