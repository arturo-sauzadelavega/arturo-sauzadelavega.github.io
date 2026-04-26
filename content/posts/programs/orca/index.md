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

### Hydrogen Atoms Optimization
Sometimes you have very good crystal structures, but with poorly solved hydrogen atom positions. In these situations, you can optimize with DFT or the method of your preference, only the hydrgen atoms. To do that, you have to include the `%geom` block in your input and use the keyword `OptimizeHydrogens`. The next input shows how to use such keyword.

```
! TPSS D4 def2-TZVP autoaux KDIIS SOSCF AIM
!NormalPrint printbasis largeprint NoTrah
!moread

%moinp "restart_orbitals.gbw"

%geom
 maxiter 1000
 OptimizeHydrogens true
end

%pal
nprocs 24
end

%scf
MaxIter 600
end

%MaxCore 4000

%output
Print[P_Basis]2
Print[P_MOs]1
end


* xyzfile 0 4  mol1_nd_tpss-d3.xyz


```


### Basis Set files

You can download basis functions from the [Basis Set Exchange](https://www.basissetexchange.org) website and store such functions into a file that Orca will read and used for the calculations. The following input shows how to read a basis functions file. In this input, I am performing a single-point using the X2C relativistic Hamiltonian to obtain the wave function file of a Nd complex. From the Basis Set Exchange website I downloaded the dyall-v3z and dyall-v4z basis functions.


```
! X2C TPSS D3 autoaux KDIIS SOSCF AIM
!NormalPrint printbasis largeprint NoTrah
!moread

%moinp "restart_orbitals.gbw"

%basis
 GTOName = "MyBasis.bas"
 #Dyall-v4z (Nd,B) and dyall-v3z (C,H,O,I)
end

%pal
nprocs 24
end

%scf
MaxIter 600
end

%MaxCore 4000

%output
Print[P_Basis]2
Print[P_MOs]1
end

* xyzfile 0 4  mol1_nd_tpss-d3.xyz


 
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
I am not entirely sure, but I think that since `Orca 5` the multreference methods implemented in `Orca` became really good, but probably I am wrong because I barely used `Orca 4` and I used it only for DFT and DLPNO-CCSD(T) calculations (I was not completely aware of multireference methods back then). Anyway, maybe Orca does not have all the methods and tools implemented in `OpenMolcas`, but at least I  know that their implementation of CASSCF and NEVPT2 is amazing and really fast! In comparison with OpenMolcas, you can perform calculations with more than 1 processor, and you don't have to struggle with the OpenMolcas installation to be used in parallel. But, Orca lacks of methods like RASSCF and GASSCF (as far as I know). 


#### CASSCF and NEVPT2

To perform CASSCF calculations, you need to include the `%casscf` block in the input file. Some important keywords are `nel` and `norb` to set the number of electrons and orbitals in the active space, respectively. Additionally, the `mult` keyword sets the spin multiplicity to consider. The following is an easy example of a single-state CASSCF calculation.

```
! DKH dkh-def2-tzvp autoaux  PATOM
!NormalPrint printbasis largeprint

#!moread
#
#%moinp "restart_molecule.gbw"


%pal nprocs 20 end

%scf
MaxIter 600
end

%MaxCore 5000

%output
Print[P_Basis]2
Print[P_MOs]1
end

%casscf
  nel 8
  norb 6
  mult 1
  maxiter 700
end


* xyz 0 1
  O   0.000000  0.000000   0.000000
  H   0.758602  0.000000   0.504284
  H   0.758602  0.000000  -0.504284
*

```

When you are interested on performing state-average CASSCF calculations, you need to include the `nroots` keywordi and the total number of states to be computed. In case you are interested in computing various spin multiplicities, for example, singlets and triplets, you can use the same `mult` keyword to list all spin multiplicities you are interested. Similarly, with `nroots` you can list the respective number of spin states for each spin manifold, for example, computing five singlets and five triplets for the water molecule:

```
! DKH dkh-def2-tzvp autoaux  PATOM
!NormalPrint printbasis largeprint

#!moread
#
#%moinp "restart_molecule.gbw"


%pal nprocs 20 end

%scf
MaxIter 600
end

%MaxCore 5000

%output
Print[P_Basis]2
Print[P_MOs]1
end

%casscf
  nel 8
  norb 6
  mult 1,3
  nroots 5,5
  maxiter 700
end


* xyz 0 1
  O   0.000000  0.000000   0.000000
  H   0.758602  0.000000   0.504284
  H   0.758602  0.000000  -0.504284
*


```

To perform CASCI calculations, on the top of the input you have to include the keyword `NoIter` as follows:

```
! DKH dkh-def2-tzvp autoaux  PATOM NOITER 
!NormalPrint printbasis largeprint

#!moread
#
#%moinp "restart_molecule.gbw"


%pal nprocs 20 end

%scf
MaxIter 600
end

%MaxCore 5000

%output
Print[P_Basis]2
Print[P_MOs]1
end

%casscf
  nel 8
  norb 6
  mult 1,3
  nroots 5,5
  maxiter 700
end


* xyz 0 1
  O   0.000000  0.000000   0.000000
  H   0.758602  0.000000   0.504284
  H   0.758602  0.000000  -0.504284
*


```

When computing a CASSCF wave function, sometimes you don't get the desired orbitals into the active space. Then, you have to try to rotate the correct orbital into the active space and remove the orbital you don't consider describes the chemical phenomenon you are studying. To do that, you have to use `!MOREAD` keyword to use as initial guess the last CASSCF orbitals you computed, and of course the `%moinp` block to read the orbitals. Lastly, you need the `%scf` block and the keyword `rotate` to indicate the pair of MOs to be rotated and the rotation angle in degrees. The numbers to be used are the MO indices. Remember that in `Orca`, the numbering starts with 0.

- Rotation of 90 degrees: Flipping two MOs
- Rotation of 45 degrees: A mixture of two MOs (50% each)
- Rotation of 180 degrees: Change of phase

```
! DKH dkh-def2-tzvp autoaux 
!NormalPrint printbasis largeprint
!moread

%moinp "restart_molecule.gbw"

%scf
 rotate 
  {4,8,90} #same as {4,8}
  {5,9,90}
 end
end

%pal nprocs 20 end

%scf
MaxIter 600
end

%MaxCore 5000

%output
Print[P_Basis]2
Print[P_MOs]1
end

%casscf
  nel 8
  norb 6
  mult 1,3
  nroots 5,5
  maxiter 700
end


* xyz 0 1
  O   0.000000  0.000000   0.000000
  H   0.758602  0.000000   0.504284
  H   0.758602  0.000000  -0.504284
*


```



Finally, to compute NEVPT2 or CASPT2 energies, you have to include the keyword `PTMethod SC_NEVPT2 ` for NEVPT2, and `  PTMethod SC_NEVPT2 `. For CASPT2 calculations, there are two options, the canonical CASPT2 formulation and the revised formulation based on using a different zeroth order Hamiltonian, which is called it `Orca` as CASPT2-K. To use these methods, you have to include the followink keywords:

- NEVPT2:   `PTMethod SC_NEVPT2` or `  PTMethod FIC_NEVPT2` 
- CASPT2:   `PTMethod FIC_CASPT2`
- CASPT2-K: `PTMethod FIC_CASPT2-K` 

Where `SC` stands for strongly contracted, and `FIC` stands for fully internally contracted. 

```
! DKH dkh-def2-tzvp autoaux  PATOM 
!NormalPrint printbasis largeprint

#!moread
#
#%moinp "restart_molecule.gbw"


%pal nprocs 20 end

%scf
MaxIter 600
end

%MaxCore 5000

%output
Print[P_Basis]2
Print[P_MOs]1
end

%casscf
  nel 8
  norb 6
  mult 1,3
  nroots 5,5
  maxiter 700
  PTMethod SC_NEVPT2
end


* xyz 0 1
  O   0.000000  0.000000   0.000000
  H   0.758602  0.000000   0.504284
  H   0.758602  0.000000  -0.504284
*


```


#### Magnetic Properties

The computation of zero-field splitting (ZFS) with multireference methods requires the previos type of inputs, but including a few keywords to turn on the use of relativity to compute spin-orbit coupling using the spin-orbit mean-field method (SOMF). 

This is an example to compute the ZFS parameters with CASSCF and NEVPT2 methods considering spin-orbit coupling and spin-spin coupling.

```
! DKH DKH-def2-TZVP  autoaux  KDIIS SOSCF
!NormalPrint printbasis largeprint

%pal
nprocs 24
end

%scf
MaxIter 600
end

%MaxCore 4000

%output
Print[P_Basis]2
Print[P_MOs]1
end

%casscf
 nel 2
 norb 5
 mult 3, 1
 nroots 10, 15
 rel
  dosoc true
  dossc true
 end
 PTMethod SC_NEVPT2
end


* xyz 0 3
 Cr                -0.03151260    0.27836135    0.00000000
 C                  0.60183169    1.17402169    1.55134379
 H                  1.67183167    1.17383912    1.55144126
 H                  0.24533664    2.18288802    1.55124621
 H                  0.24499943    0.66973588    2.42499508
 C                  0.60179899   -1.51298351    0.00000000
 H                  0.24514256   -2.01737590    0.87366155
 H                  0.24510974   -2.01738750   -0.87364146
 H                  1.67179899   -1.51299670   -0.00002009
 C                 -1.93151260    0.27838476    0.00000000
 H                 -2.28816652    1.28719305    0.00195626
 H                 -2.28818515   -0.22431884   -0.87462780
 H                 -2.28818570   -0.22770676    0.87267157
 C                  0.60183169    1.17402169   -1.55134379
 H                  0.24509799    2.18280366   -1.55139234
 H                  1.67183169    1.17409223   -1.55129511
 H                  0.24523807    0.66956712   -2.42499508
*
```

#### SINGLE_ANISO

In my understanding, there are two ways to use the SINGLE_ANISO module developed by Prof. Liviu Ungur and Prof. Liviu Chibotaru. The first way is including the keywords inside the `%casscf` block.

```
! DKH DKH-def2-TZVP  autoaux  KDIIS SOSCF
!NormalPrint printbasis largeprint
!MOread

%moinp "restart.gbw" 

%pal
nprocs 24
end

%scf
MaxIter 600
end

%MaxCore 2000

%output
Print[P_Basis]2
Print[P_MOs]1
end

%casscf
 nel 2
 norb 5
 mult 3, 1
 nroots 10, 15
 rel
  dosoc true
  dossc true
 end
 ANISO
  doaniso true
  MLTP 3,1,1,3
  TINT 0, 300, 50
  CRYS_element "Cr"
  CRYS_charge 4
 end
end


* xyz 0 3
 Cr                -0.03151260    0.27836135    0.00000000
 C                  0.60183169    1.17402169    1.55134379
 H                  1.67183167    1.17383912    1.55144126
 H                  0.24533664    2.18288802    1.55124621
 H                  0.24499943    0.66973588    2.42499508
 C                  0.60179899   -1.51298351    0.00000000
 H                  0.24514256   -2.01737590    0.87366155
 H                  0.24510974   -2.01738750   -0.87364146
 H                  1.67179899   -1.51299670   -0.00002009
 C                 -1.93151260    0.27838476    0.00000000
 H                 -2.28816652    1.28719305    0.00195626
 H                 -2.28818515   -0.22431884   -0.87462780
 H                 -2.28818570   -0.22770676    0.87267157
 C                  0.60183169    1.17402169   -1.55134379
 H                  0.24509799    2.18280366   -1.55139234
 H                  1.67183169    1.17409223   -1.55129511
 H                  0.24523807    0.66956712   -2.42499508
*

```
 
When your `Orca` input file request a CASSCF and NEVPT2 calculations followed by SINGLE_ANISO, then `Orca` runs the SINGLE_ANISO twice. Also, it is generated an input file for the SINGLE_ANISO module extension. This file has the same name as the calculation you submitted, but with extension `.anisoinp`.  Two more files are generated, with the CASSCF and NEVPT2 data necessary for SINGLE_ANISO, respectively. These files have extension `.CASSCF.anisofile` and `.NEVPT2.anisofile`.

This is an example of how the `.anisoinp` input file looks like:

```
&SINGLE_ANISO
DATA
 casscf_single_aniso.CASSCF.anisofile 

MLTP
4
3 1 1 3 

TINT
  0.00000000000000E+00   3.00000000000000E+02 50 

PRLV
2

CRYS
Cr 
4 

XFIE
   0.00000000000000E+00 

End Of Input

```

You can modify the file name below the `DATA` keyword to indicate if you want to use SINGLE_ANISO for the CASSCF or the NEVPT2 data, and then you can execute the `otool_single_aniso` program to use the SINGLE_ANISO module as follows:

```
$ otool_single_aniso < casscf.anisoinp > casscf_aniso.output


```

Now, just check your SINGLE_ANISO output. 




#### Ab Initio Ligand Field Theory (AILFT)

To perform the Ab Initio Ligand Fieled Theory analysis, you have to satisfy a few requirements. First, you have to work only with active spaces containing complete d or f shells, and depending on the active space, the number of roots requested must include all possible roots for all possible spin states. For example, if you want to perform the AILFT for a system like Cr(IV), with the active space of (2e, 5o), you have to include all 15 singlets and 10 triplets. If you include fewer number of states, then your calculation will failed. Also in the `%casscf` block you have to include the keyword `ActOrbs` with values `dOrbs` or `fOrbs`, depending on the metal center.

This is an example of an Uranium (IV) complex I am working on my main project for my posdoctoral apointee.

```
! DKH autoaux  KDIIS SOSCF
!NormalPrint printbasis largeprint
!moread

%moinp "guess_casscf_0.gbw"

%basis NewGTO U "SARC-DKH-TZVP" end
       newauxgto U "autoaux" end
       newGTO N "DKH-def2-TZVP" end
       newauxgto N "def2-SVP/C" end
       newGTO P "DKH-def2-TZVP" end
       newauxgto P "def2-SVP/C" end
       newGTO H "DKH-def2-TZVP" end
       newauxgto H "def2-SVP/C" end
       #newGTO C "DKH-def2-TZVP" end
       #newauxgto C "def2-SVP/C" end
end

%pal
nprocs 32
end

%scf
MaxIter 600
end

%MaxCore 4000

%output
Print[P_Basis]2
Print[P_MOs]1
end

%casscf
  nel 2
  norb 7
  mult 3,1
  nroots 21,28
  maxiter 10000
  trafostep ri
  OrbStep SuperCI
  ActConstraints 2
  ActOrbs forbs
  PTMethod SC_NEVPT2
end


* xyzfile 0 3 U_NPH3_Td2Sq_0.xyz



```

The AILFT analysis can be performed using CASSCF and NEVPT2 values.

I have only performed AILFT considering only one shell of d or f orbitals, but in `Orca 6` you can include a second shell, but I have not tried those calculations. Also, it is possible to assign different type of orbitals to `ActOrbs`, even including ligand orbitals into the AILFT calculation, but I haven't tried those calculations yet. So I expect in the near future to update this section with more `Orca` examples about these calculations.



### ZFS with DFT

Previously, I showed how to compute the Zero-Field Splitting parameters using multireference wave functions. However, in `Orca` you can compute the ZFS using linear-reponse DFT using the coupled-perturbed method.

This is an input for the computation of the ZFS parameters with DFT.

```
! DKH DKH-def2-TZVP autoaux  KDIIS SOSCF
!NormalPrint printbasis largeprint


%pal
nprocs 32
end

%scf
MaxIter 600
end

%MaxCore 4000

%output
Print[P_Basis]2
Print[P_MOs]1
end


%eprnmr
 DTensor ssandso
 DSOC cp #qro,pk, cvw
 DSS uno #direct
end

* xyz 0 3
 Cr                -0.03151260    0.27836135    0.00000000
 C                  0.60183169    1.17402169    1.55134379
 H                  1.67183167    1.17383912    1.55144126
 H                  0.24533664    2.18288802    1.55124621
 H                  0.24499943    0.66973588    2.42499508
 C                  0.60179899   -1.51298351    0.00000000
 H                  0.24514256   -2.01737590    0.87366155
 H                  0.24510974   -2.01738750   -0.87364146
 H                  1.67179899   -1.51299670   -0.00002009
 C                 -1.93151260    0.27838476    0.00000000
 H                 -2.28816652    1.28719305    0.00195626
 H                 -2.28818515   -0.22431884   -0.87462780
 H                 -2.28818570   -0.22770676    0.87267157
 C                  0.60183169    1.17402169   -1.55134379
 H                  0.24509799    2.18280366   -1.55139234
 H                  1.67183169    1.17409223   -1.55129511
 H                  0.24523807    0.66956712   -2.42499508
*

```

Where `DTensor ssandso` indicates that the computation of the D-tensor involves including spin-orbit and spin-spin coupling. `DSOC` is the method used for the computation of spin-orbit coupling, in this case, it is used the coupled-perturbed method (`cp`), and to compute the spin-spin coupling, the previous input uses unrestricted naturol orbitals (`uno`).



<div dir="rtl"> All suggestions are welcome to improve this section, just send me a message.  </div>

