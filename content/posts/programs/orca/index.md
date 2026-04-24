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
I still remember my first approach to using Orca. I was an undergraduate student at UNAM, and more specifically, I was working at the Institute of Chemistry at UNAM under the supervision of Prof. Tomás Rocha Rinza, and José Manuel Guevara Vela was visiting us from Spain, I think he was in his last year of grad school at the University of Oviedo, working with Prof. Ángel Martín Pendás. Back then, I was working only with Gaussian 16 and GAMESS, but Manuel showed me how to use Orca 3.5 to compute DLPNO-CCSD(T) energies that I used for the computation of energy barriers and rate constants of my project consisting on exploring the [hydrolisis reaction of epoxides using water clusters as bifunctional catalysts](https://doi.org/10.1039/D1OB01026C).

Fortunately, the Orca manual was very well written. Actually, it is outstanding. I think that of all chemistry software that I have tried, the Orca manual is the best. Probably this post in my webpage is unnecessary because the manual is very complete, full of many examples for all the implemented functionalities. Still, I am writing this post as a remainder for most of the calculations I had performed, and when I am looking for an especifit sort of calculation, instead of looking into the manual, I can quickly check this post and then just copy and paste the input structure for the new calculation to be performed.


### Standard Input File

The input structure is really simple and in general it is friendly. The first few lines should start with the exclamation sign `!` and after that, you can write a wide variety of keywords, like the method you are using for your computation, the basis set, the density fitting approach you are using, whether you want to perform a single point, geometry optimization, frequency calculation, transition state optimization, etc.

The simplest DFT input is the following:

```
! Opt Freq def2-TZVP RI autoaux PBE AIM  D4
! printbasis largeprint KDIIS SOSCF NoTrah

%pal nprocs 4 end

%scf
MaxIter 600
end

%MaxCore 1000

%output
Print[P_Basis]2
Print[P_MOs]1
end

* xyz 0 1
  O   0.000000  0.000000   0.000000
  H   0.758602  0.000000   0.504284
  H   0.758602  0.000000  -0.504284
*
```
In case someone without experience with Orca is reading this post, let me explain the input. The calculation will do geometry optimization and once that part of the calculation converges, a vibrational analysis will be performed. This is indicated by the keywords `Opt` and `Freq`. To do this calculation, we are using the PBE exchange-correlation functional with def2-TZVP basis functions and D4 dispersion model. Additionally, the density fitting calculation is performed because it was written the `RI` keyword. For density fitting, the auxiliary basis functions were build automatically by Orca because the `autoaux` keyword was included.

The `AIM` keyword is included to generate wave function files with extension `.wfn` and `.wfx` that can be used with programs such as `AIMAll`, `MultiWfn`, `NCIPLOT`, or `Promolden`to perform quantum chemical topology analysis. Additionally, in this input I included the `KDIIS` and `SOSCF` keywords to speed up the SCF calculations. These two keywords are not necessary, they could be removed without afdamaging the calculation. Also, it is important to use `NoTRAH`. This keyword is used to solve the SCF, but in my experience it takes too many itereations to converge. Still, I use it when the normal SCF algorithms don't work. In those situations I give a try to the TRAH algorithm by removing that keyword.

Additional instructions for the calculation can be included using `blocks`. These blocks start with the percentage symbol, followed by the block name, for example, `%scf` controls features related to the SCF calculation. In the previous input, the `%pal` block is included to specify the number of processors to be used in the calculation (be aware that this number must match with the total number of processors requested for the calculation with the submission script), the `%maxcore` indicates the number of megabytes to be used for each requested core, and `%output` indicates the extra information that you want to print in the output file. In this case, the MOs and the basis set used.


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
This is an input I used to compute excitations from a Lanthanum (III) complex with SMD solvation model. For this calculation, I used the Douglas-Kroll-Hess Hamiltonian to second-order to include scalar relativistic corrections. In this calculation, I requested the calculation of 10 excited states as observed in the `%tddft` block.

```
!DKH2 DKH-def2-TZVP autoaux LARGEPRINT CAM-B3LYP NoTRAH Mulliken Loewdin Mayer AIM

%basis NewGTO La "SARC-DKH-TZVP" end
       newauxgto La "autoaux" end
       newGTO C "DKH-def2-TZVP" end
       newauxgto C "def2-SVP/C" end
       newGTO H "DKH-def2-SVP" end
       newauxgto H "def2-SVP/C" end
       newGTO B "DKH-def2-SVP" end
       newauxgto B "def2-SVP/C" end
       newGTO O "DKH-def2-SVP" end
       newauxgto O "def2-SVP/C" end
       newGTO I "SARC-DKH-TZVP" end
       newauxgto I "autoaux" end
end

%cpcm smd true
      SMDsolvent "acetonitrile"
end
%tddft
 nroots 10
end

%pal
nprocs 24
end

%MaxCore 4000

* xyzfile 0 1 mol1_la_opt.xyz

```


### Multireference Methods

#### CASSCF and NEVPT2

#### Magnetic Properties

#### ZFS with DFT 

#### Ab Initio Ligand Field Theory (AILFT)




<div dir="rtl"> All suggestions are welcome to improve this section, just send me a message.  </div>

