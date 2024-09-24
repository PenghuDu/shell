#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from ase.data.pubchem import pubchem_atoms_search
from ase.io import write

#write("C20H20.xyz", images=pubchem_atoms_search(name="C20H20"))
## or use the PubChem number
write("C20H20.xyz", images=pubchem_atoms_search(cid=28123))
