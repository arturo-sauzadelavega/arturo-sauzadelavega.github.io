	---
title: "Orca 6.1.1"
date: 2026-03-08
description: Onput examples of Orca 6.1.1
tags: [ "Quantum Chemistry", "DFT", "MP2", "CCSD", "TD-DFT", "Transition State", "NBO", "Multireference methods", "AILFT"   ]
hero: orca_6.png
menu:
  sidebar:
    name: Orca
    identifier: orca
    parent: programs
    weight: 30
author:
  name: Arturo Sauza de la Vega, Ph.D.
  image: /images/author/arturo_2.jpg
math: true
---

{{< img src="arturo_cartoon_08.png"  width="400" align="center" title="Coding OpenMolcas" >}}

{{< vs 3 >}}


### Introduction



### Standard Input File

```
%nproc=12
%mem=10GB
%chk=file.chk
# keywords

Title for your calculation

charge multiplicity
XYZ coordinates


```

For a DFT geometry optimization and frequency calculation of the water molecule, this is an easy example:

```
%nproc=4
%mem=16GB
%chk=water.chk

#p opt freq tpsstpss aug-cc-pvtz scf=xqc pop=(full,nbo) output=wfn

water

0 1
  O  0.000000  0.000000  0.000000
  H  0.758602  0.000000  0.504284
  H  0.758602  0.000000  -0.504284

water.wfn


```



### Basis Set files


```
%nproc=12
%mem=10GB
%chk=example_molecule.chk
# geom=allcheck TPSSh/gen scrf=(smd,solvent=tetrahydrofuran) int=dkh2 guess=read  emp=gd3bj scf=xqc

@./basis.gbs

 
```

### Time-Dependent DFT (TD-DFT)


### Multireference Methods

#### CASSCF and NEVPT2

#### Magnetic Properties

#### ZFS with DFT 

#### Ab Initio Ligand Field Theory (AILFT)

