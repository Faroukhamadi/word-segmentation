from typing import Callable
import util


def unigramCost(x: str):
    if x in ['two', 'word', 'words', 'three']:
        return 1
    else:
        return 1000


class WordSegmentationProblem(util.SearchProblem):
    def __init__(self, query: str, unigramCost: Callable):
        self.query = query
        self.unigramCost = unigramCost

    def startState(self):
        return self.query

    def isEnd(self, state: str):
        return len(state) == 0

    def succAndCost(self, state: str):
        res = []
        for i in range(len(state), -1, -1):
            action = state[:i]
            remainingText = state[i:]
            cost = self.unigramCost(action)
            res.append((action, remainingText, cost))
        return res


def main() -> None:
    ucs = util.UniformCostSearch(verbose=0)
    wsp = WordSegmentationProblem('twowords', unigramCost)
    ucs.solve(wsp)

    segmentedSentence = ' '.join(ucs.actions)

    print(f'{segmentedSentence=}')

main()