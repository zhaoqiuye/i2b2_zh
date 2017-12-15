# -*- coding: utf-8 -*-
import logging

logging.basicConfig(filename='check.log', filemode='w', level=logging.DEBUG)
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s')
from fuzzywuzzy import fuzz, process
from MatchSet import queryChineseData, queryMeicData

if 1:
    """
    for inline debugging
    """
    # test_refSet=set([u"数据分析师", u"数据挖掘工程师", u"大数据开发工程师", u"机器学习工程师", u"算法工程师", u"数据库管理", u"商业分析师", u"数据科学家", u"首席数据官", u"数据产品经理", u"数据运营", u"大数据架构师"])
    # testSet = set([u"算法工程师", u"数据库管理", u"商业分析师", u"数据挖掘师"])
    test_refSet = set(queryChineseData())
    testSet = set(queryMeicData())


class RefSet(object):
    def __init__(self, dataSet=test_refSet):
        self.dataSet = dataSet
        logging.info('There are totally %d elements in the reference set' % len(self.dataSet))

    def intersect(self, otherSet):
        s = self.dataSet.intersection(otherSet)
        logging.info('There are %d elements in both sets:' % len(s))
        for a in sorted(s): print a,
        print
        return s

    def fuzzyMatch(self, otherSet):
        """
        return a dictionary: mapping every item in otherSet to its best match in the reference set.
        """
        return dict([(item, process.extractOne(item, self.dataSet, scorer=fuzz.ratio))
                     for item in otherSet])


def exp1():
    """
    Find the items in a database that have exact matches in reference set.
    """
    refSet = RefSet()
    refSet.intersect(testSet)


def exp2():
    """
    For each item not in the reference set, find its best match
    """
    refSet = RefSet()
    matchDict = refSet.fuzzyMatch(testSet.difference(refSet.dataSet))
    for key, item in matchDict.items():
        print key, ':', item[0], item[1]


if __name__ == '__main__':
    import sys

    exec '%s()' % sys.argv[1]
