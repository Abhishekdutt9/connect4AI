import random
import math


BOT_NAME = "something sus"


class RandomAgent:
    """Agent that picks a random available move.  You should be able to beat it."""

    def get_move(self, state, depth=None):
        return random.choice(state.successors())


class HumanAgent:
    """Prompts user to supply a valid move."""

    def get_move(self, state, depth=None):
        move__state = dict(state.successors())
        prompt = "Kindly enter your move {}: ".format(sorted(move__state.keys()))
        move = None
        while move not in move__state:
            try:
                move = int(input(prompt))
            except ValueError:
                continue
        return move, move__state[move]


class MinimaxAgent:
    """Artificially intelligent agent that uses minimax to optimally select the best move."""

    def get_move(self, state, depth=None):
        """Select the best available move, based on minimax value."""
        nextp = state.next_player()
        best_util = -math.inf if nextp == 1 else math.inf
        best_move = None
        best_state = None

        for move, state in state.successors():
            util = self.minimax(state, depth)
            if ((nextp == 1) and (util > best_util)) or ((nextp == -1) and (util < best_util)):
                best_util, best_move, best_state = util, move, state
        return best_move, best_state

    def minimax(self, state, depth):
        """Determine the minimax utility value of the given state.

        Args:
            state: a connect383.GameState object representing the current board
            depth: for this agent, the depth argument should be ignored!

        Returns: the exact minimax utility value of the state
        """
        #
        # Fill this in!
        #
        nextp = state.next_player()

        if (state.is_full()):
            return state.score()

        if nextp == 1:

            v = -math.inf
            for a, s in state.successors():

                v = max(v, self.minimax(s, depth))
            return v

        elif nextp == -1:

            v = math.inf
            for a, s in state.successors():

                v = min(v, self.minimax(s, depth))
            return v


class HeuristicAgent(MinimaxAgent):
    """Artificially intelligent agent that uses depth-limited minimax to select the best move."""

    def minimax(self, state, depth):
        return self.minimax_depth(state, depth)

    def minimax_depth(self, state, depth):
        """Determine the heuristically estimated minimax utility value of the given state.

        Args:
            state: a connect383.GameState object representing the current board
            depth: the maximum depth of the game tree that minimax should traverse before
                estimating the utility using the evaluation() function.  If depth is 0, no
                traversal is performed, and minimax returns the results of a call to evaluation().
                If depth is None, the entire game tree is traversed.

        Returns: the minimax utility value of the state
        """
        #
        # Fill this in!
        #
        if self.empty(state):
            print("yes")
        if(depth==None):
            depth=-1
        nextp = state.next_player()

        if (state.is_full()):
            return state.score()


        if (depth == 0):
            return (self.evaluation(state))

        newdepth=depth
        if nextp == 1:
            if (depth > 0):
                newdepth = depth - 1
            v = -math.inf
            for a, s in state.successors():
                # nextp=-1
                v = max(v, self.minimax_depth(s, newdepth))
            return v

        elif nextp == -1:
            if (depth > 0):
                newdepth = depth - 1
            v = math.inf
            for a, s in state.successors():
                v = min(v, self.minimax_depth(s, newdepth))
            return v

    def streaks(self,lst):
        """Return the lengths of all the streaks of the same element in a sequence."""
        rets = []  # list of (element, length) tuples
        prev = lst[0]
        curr_len = 1
        for curr in lst[1:]:
            if curr == prev:
                curr_len += 1
            else:
                rets.append((prev, curr_len))
                prev = curr
                curr_len = 1
        rets.append((prev, curr_len))
        return rets


    def streaksO2(self,lst):
        rets = []
        prev = lst[0]
        curr_len = 1
        if (prev == -1):
            for curr in lst[1:]:
                if (curr == -1 ):
                    curr_len += 1
                elif(curr == 0):
                    if curr==prev:
                        prev=-1
                        rets.append((prev, curr_len))

                    else:
                        prev=-1
                        curr_len+=1
                        rets.append((prev, curr_len))

                    prev = curr
                else:
                    rets.append((prev, curr_len))
                    prev = curr
                    curr_len = 1
        rets.append((prev, curr_len))
        return rets

    def streaksX2(self, lst):
        rets = []
        prev = lst[0]
        curr_len = 1
        if (prev == 1):
            for curr in lst[1:]:
                if (curr == 1):
                    curr_len += 1
                elif (curr == 0):
                    if curr == prev:
                        prev = 1
                        rets.append((prev, curr_len))

                    else:
                        prev = 1
                        curr_len += 1
                        rets.append((prev, curr_len))

                    prev = curr
                else:
                    rets.append((prev, curr_len))
                    prev = curr
                    curr_len = 1
        rets.append((prev, curr_len))
        return rets

    def evaluation(self, state):
        """Estimate the utility value of the game state based on features.

        N.B.: This method must run in O(1) time!

        Args:
            state: a connect383.GameState object representing the current board

        Returns: a heusristic estimate of the utility value of the state
        """
        p1_score = 0
        p2_score = 0

        if self.empty(state):
            print("yes")

        for run in state.get_all_rows() + state.get_all_cols() + state.get_all_diags():
            for elt,length in self.streaksX2(run):
                if (length >= 3):
                    p1_score += length

            for elt, length in self.streaksO2(run):
                if (length >= 3):
                    p2_score += length
        alpha=self.convulations(state)
        if self.half_empty(state):
            return (self.score(state)*5) +(1*(p1_score - p2_score)+(alpha*2))

        return ((p1_score - p2_score)*1) + ((state.score()*4)+alpha*1)#*6))
    def convulations(self,state):
        mid = []

        for j in range(1,len(state.get_all_cols())-2):
            mid.append(j)
        mid.append(int(len(state.get_all_cols()) / 2))

        c=0
        for i in state.get_all_rows():
            for j in mid:
                if i[j]==1:
                    c=c+1.1

                elif i[j]==-1:
                    c=c-1
        return c**2
    def score(self,state):

        p1_score = 0
        p2_score = 0
        for run in state.get_all_rows() + state.get_all_cols() + state.get_all_diags():
            for elt, length in self.streaks(run):
                if (elt == 1) and (length >= 3):
                    p1_score += length ** 2
                elif (elt == -1) and (length >= 3):
                    p2_score += length ** 2
        return p1_score - p2_score

    def half_empty(self,state):
        x=0
        z=0
        for r in range(state.num_rows):
            for c in range(state.num_cols):
                if state.board[r][c] == 0:
                    z=z+1
                else:
                    x=x+1
        if(x>z):
            return False

        return True
    def empty(self,state):
        c=0
        for r in range(state.num_rows):
            for c in range(state.num_cols):
                if state.board[r][c] == 1 or state.board[r][c] == -1:
                    c=c+1
            if(c==0):
                return True
        return False


class PruneAgent(HeuristicAgent):
    """Smarter computer agent that uses minimax with alpha-beta pruning to select the best move."""

    def minimax(self, state, depth):

        return self.minimax_prune(state, depth)

    def minimax_prune(self, state, depth):
        """Determine the minimax utility value the given state using alpha-beta pruning.

        The value should be equal to the one determined by ComputerAgent.minimax(), but the
        algorithm should do less work.  You can check this by inspecting the class variables
        GameState.p1_state_count and GameState.p2_state_count, which keep track of how many
        GameState objects were created over time.

        N.B.: When exploring the game tree and expanding nodes, you must consider the child nodes
        in the order that they are returned by GameState.successors().  That is, you cannot prune
        the state reached by moving to column 4 before you've explored the state reached by a move
        to to column 1.

        Args: see ComputerDepthLimitAgent.minimax() above

        Returns: the minimax utility value of the state
        """
        
        alpha = -math.inf
        beta = math.inf
        return self.minimax_prune_helper(state, depth, alpha, beta)

    def minimax_prune_helper(self, state, depth, alpha, beta):

        if (depth == None):
            depth = -1

        nextp = state.next_player()

        if (state.is_full()):
            return state.score()

        if (depth == 0):
            return self.evaluation2(state)

        newdepth = depth

        if nextp == 1:
            if (depth > 0):
                newdepth = depth - 1
            v = -math.inf
            for a, s in state.successors():
                v = max(v, self.minimax_prune_helper(s, newdepth, alpha, beta))
                alpha = max(v, alpha)
                if (beta <= alpha):
                    break

            return alpha



        elif nextp == -1:
            if (depth > 0):
                newdepth = depth - 1
            v = math.inf
            for a, s in state.successors():
                v = min(v, self.minimax_prune_helper(s, newdepth, alpha, beta))
                beta = min(v, beta)
                if (beta <= alpha):
                    break

            return beta


    def streaksO2(self,lst):
        rets = []
        prev = lst[0]
        curr_len = 1
        if (prev == -1):
            for curr in lst[1:]:
                if (curr == -1 ):
                    curr_len += 1
                elif(curr == 0):
                    if curr==prev:
                        prev=-1
                        rets.append((prev, curr_len))

                    else:
                        prev=-1
                        curr_len+=1
                        rets.append((prev, curr_len))

                    prev = curr
                else:
                    rets.append((prev, curr_len))
                    prev = curr
                    curr_len = 1
        rets.append((prev, curr_len))
        return rets

    def streaksX2(self, lst):
        rets = []
        prev = lst[0]
        curr_len = 1
        if (prev == 1):
            for curr in lst[1:]:
                if (curr == 1):
                    curr_len += 1
                elif (curr == 0):
                    if curr == prev:
                        prev = 1
                        rets.append((prev, curr_len))

                    else:
                        prev = 1
                        curr_len += 1
                        rets.append((prev, curr_len))

                    prev = curr
                else:
                    rets.append((prev, curr_len))
                    prev = curr
                    curr_len = 1
        rets.append((prev, curr_len))
        return rets

    def evaluation2(self, state):
        """Estimate the utility value of the game state based on features.

        N.B.: This method must run in O(1) time!

        Args:
            state: a connect383.GameState object representing the current board

        Returns: a heusristic estimate of the utility value of the state
        """
        p1_score = 0
        p2_score = 0

        if self.empty(state):
            print("yes")

        for run in state.get_all_rows() + state.get_all_cols() + state.get_all_diags():
            for elt,length in self.streaksX2(run):
                if (length >= 3):
                    p1_score += length

            for elt, length in self.streaksO2(run):
                if (length >= 3):
                    p2_score += length
        alpha=self.convulations(state)
        if self.half_empty(state):
            return (self.score(state)*5) +(1*(p1_score - p2_score)+(alpha*2))

        return ((p1_score - p2_score)*1) + ((state.score()*4)+alpha*1)#*6))
    def convulations(self,state):
        mid = []

        for j in range(1,len(state.get_all_cols())-2):
            mid.append(j)
        mid.append(int(len(state.get_all_cols()) / 2))

        c=0
        for i in state.get_all_rows():
            for j in mid:
                if i[j]==1:
                    c=c+1.1

                elif i[j]==-1:
                    c=c-1
        return c**2
    def score(self,state):

        p1_score = 0
        p2_score = 0
        for run in state.get_all_rows() + state.get_all_cols() + state.get_all_diags():
            for elt, length in self.streaks(run):
                if (elt == 1) and (length >= 3):
                    p1_score += length ** 2
                elif (elt == -1) and (length >= 3):
                    p2_score += length ** 2
        return p1_score - p2_score

    def half_empty(self,state):
        x=0
        z=0
        for r in range(state.num_rows):
            for c in range(state.num_cols):
                if state.board[r][c] == 0:
                    z=z+1
                else:
                    x=x+1
        if(x>z):
            return False

        return True
    def empty(self,state):
        c=0
        for r in range(state.num_rows):
            for c in range(state.num_cols):
                if state.board[r][c] == 1 or state.board[r][c] == -1:
                    c=c+1
            if(c==0):
                return True
        return False
