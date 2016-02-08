#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
COLLECTOR:
---------
Script that wraps the complete application logic.
Here we query the WFP API and collect all available
data, storing the results in local CSV files.

'''
from collector.classes.mvam import mVAM
from collector.utilities.item import item
from collector.storage.csv import store_csv

def main():
    '''
    Program wrapper.

    '''
    m = mVAM(table='pblStatsSum')
    store_csv(data=m.query(), path='pblStatsSum.csv')

    m = mVAM(table='pblStatsSum4Maps')
    store_csv(data=m.query(), path='pblStatsSum4Maps.csv')

if __name__ == '__main__':
    main()
    print('%s Successfully collected mVAM data.' % item('success'))
