#!/usr/bin/python

def ReadFullACSTable():
	"""Returns the full ACS table in panda format
       from ipython, run
       $ %run ReadACSTable.py
       $ acs = ReadFullACSTable()
	"""
	import numpy as np
	import pandas as pd
	#from astroquery.simbad import Simbad 
	from astroquery.vizier import Vizier
	#from astropy.table import Table

	Vizier.ROW_LIMIT = -1  #needed to bypass the 50 rows limit
	Robberto2013_table5FULL = Vizier.get_catalogs('J/ApJS/207/10/table5')
	#Robberto2013_table5FULL.pprint()
	table=Robberto2013_table5FULL[0]

	FullACS_pd = pd.DataFrame(np.array(table))
	print(FullACS_pd)
	return FullACS_pd
	
	
	
def ReadMiniACSTable():
	"""Returns the mini ACS table in panda format
       from ipython, run
       $ %run ReadACSTable.py
       $ acs = ReadMiniACSTable()
	"""
	import numpy as np
	import pandas as pd
	#from astroquery.simbad import Simbad 
	from astroquery.vizier import Vizier
	#from astropy.table import Table

	Vizier.ROW_LIMIT = -1  #needed to bypass the 50 rows limit
	Robberto2013_table5FULL = Vizier.get_catalogs('J/ApJS/207/10/table5')
	#Robberto2013_table5FULL.pprint()
	table=Robberto2013_table5FULL[0]

	FullACS_pd = pd.DataFrame(np.array(table))
	SmallACS_pd = pd.DataFrame(np.array(table),columns=['_RAJ2000','_DEJ2000','Seq','ONCacs','N','RAJ2000','DEJ2000','F435W','e_F435W','F555W','e_F555W','F658N','e_F658N','F775W','e_F775W','F850LP','e_F850LP','type']) 
	ACS850ind = SmallACS_pd.set_index(['ONCacs'])
	MiniACS_pd=ACS850ind.groupby(ACS850ind.index).mean()	
	return MiniACS_pd
