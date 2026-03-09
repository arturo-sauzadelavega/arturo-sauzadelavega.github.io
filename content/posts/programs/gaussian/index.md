	---
title: "Gaussian 09/16"
date: 2026-03-08
description: Gaussian Input Examples
tags: [ "Quantum Chemistry", "DFT", "MP2", "CCSD", "TD-DFT", "Transition State", "NBO"   ]
hero: gaussian.png
menu:
  sidebar:
    name: Gaussian
    identifier: gaussian
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

Gaussian is a well-known electronic structure program in the chemistry community. Probably this introduction is unnecesary because most of the people I known they already know about its existance, its story, many of the methods implemented, etc.

In my opinion, Gaussian is one of the most friendly codes out there. However, there are many tools that are very useful and we don't usually remember how to use them. This is my main motivation to write this post, to remember some of the input structures I use for special cases, or when the documentation is limited and I already figured out how to make the input run correctly.

### Standard Input File
Gaussian input files are incredibly friendly. The input files I use require in the very first few lines to include the variables `%nproc`, `%mem`, `%chk` to indicate the number of processors to be used in the calculation, the maximum memory allocated, and the name of a chekpoint file, respectively.

Checkpoint files are very useful because in this binary file is stored the geometry, basis functions and much more data useful to restart a calculation or to plot information of your interest. This information is not available only for the final optimized molecules, it is also written for all intermediate steps in a requested calculation.

The standard input file follows the structure shown below:

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

The number and types of basis functions available in Gaussian is amazing. However, sometimes you need specific basis functions that are not availabe, like all-electron relativistic basis sets. In these situations, you have to download basis functions from external sources like [Basis Set Exchange](https://www.basissetexchange.org), the [Turbomole Basis Set Library](https://basissets.turbomole.org), or the [Correlation Consistent Basis Set Repository](http://www.grant-hill.group.shef.ac.uk/ccrepo/). Then, you copy from the previous websites and paste the basis functions into the gaussian input file. This is really easy to do and I think the example in the gaussian website is clear, but the example about how to invoque a file where the basis functions were written is not avaialable in the website.

This is an input example in which I use a gaussian basis function file (`.gbs`):

```
%nproc=12
%mem=10GB
%chk=example_molecule.chk
# geom=allcheck TPSSh/gen scrf=(smd,solvent=tetrahydrofuran) int=dkh2 guess=read  emp=gd3bj scf=xqc

@./basis.gbs

 
```

This is an example of for the geometry optimization and frequencies calculation of HgCl<sub>2</sub> in combination with dispersion D3-BJ for the TPSSh functional, and using Link1 to concatenate the calculations.

```
%nproc=12
%mem=10GB
%chk=hgcl2_tpssh_crenbl-def2.chk
#  opt  tpssh/genecp emp=gd3bj scf=xqc
# iop(3/175=2238200,3/177=452900,3/178=4655000)

HgCl2

0 1
Hg 2.166542 7.340627 0.000000
Cl 4.306107 6.496803 0.000000
Cl 0.026989 8.184446 0.000000

@./basis_hgcl2.gbs

--Link1--
%chk=hgcl2_tpssh_crenbl-def2.chk
# freq geom=allcheck guess=read tpssh emp=gd3bj genecp scf=xqc
# iop(3/175=2238200,3/177=452900,3/178=4655000)

@./basis_hgcl2.gbs
  
  
  
```




### Dispersion Model for TPSSh

Sometimes you want to include dispersion correction into your calculations. The most famous functionals like PBE or B3LYP immediately loads all the empirical parameters for such functionals and you just need to include the keyword `emp=gd3bj` in case you want to run a D3-BJ dispersion calculation. However, for other functionals you have to indicate the values for the empirical parameters. To do this, you have to use the `iop` keywords. This is an example of a TPSSh-D3-BJ calculation where I need to indicate the empirical parameters:

```
%nproc=12
%mem=10GB
%chk=water.chk
# opt tpssh emp=gd3bj def2tzvp scf=xqc
# iop(3/175=2238200,3/177=452900,3/178=4655000)

water optimization

0 1
  O  0.000000  0.000000  0.000000
  H  0.758602  0.000000  0.504284
  H  0.758602  0.000000  -0.504284

--Link1--
%nproc=36
%mem=100GB
%chk=water.chk
# freq geom=allcheck guess=read tpssh emp=gd3bj def2tzvp scf=xqc
# iop(3/175=2238200,3/177=452900,3/178=4655000)
  
  
```

In this example, to perform an optimization and frequencies calculation, you have to split the calculation into two parts, one for the optimization where the dispersion is indicated, the second part corresponds to the frequencies, where once again you have to specify the dispersion model and the empirical parameters.

If you are interested in another functional, you have to find the corresponding empirical parameters. You can try looking into Prof. Grimme's papers or in his reserach group webiste where he published the complete data set to train functionals and the obtained empirical parameters.



### Natural Localized Molecular Orbitals (NLMO)

Gaussian includes an NBO version included within the many functionalities. In my research about actinide molecules, often I have to analyze NLMOs to check the bonding interaction between metal centers and ligands. We can obtain NLMOs directly with Gaussian in case you do not have other programs like ADF and NBO. 

This is an input example to obtain NLMOs with Gaussian, where I use the Iop 6/73 to obtain the NLMOs:
```
%nproc=4
%mem=16GB
%chk=water.chk

#p  pbepbe aug-cc-pvtz scf=xqc output=wfnx emp=gd3bj
# pop=nbo iop(6/73=1,6/73=2)

water

0 1
  O  0.000000  0.000000  0.000000
  H  0.758602  0.000000  0.504284
  H  0.758602  0.000000  -0.504284

water.wfx
  
  
```


