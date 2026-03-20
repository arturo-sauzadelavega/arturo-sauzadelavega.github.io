---
title: "OpenMolcas Manual"
date: 2026-03-05
description: OpenMolcas Modules and Examples
tags: [ "Quantum Chemistry", "CASSCF", "CASPT2", "MC-PDFT", "Multireference Methods", "Spin-Orbit Coupling", "Magnetism", "Spectroscopy"  ]
hero: openmolcas.png
menu:
  sidebar:
    name: OpenMolcas
    identifier: openmolcas
    parent: programs
    weight: 30
author:
  name: Arturo Sauza de la Vega, Ph.D.
  image: /images/author/arturo_2.jpg
math: true
---

{{< img src="arturo_cartoon_08.png"  width="400" align="center" title="Coding OpenMolcas" >}}

{{< vs 3 >}}


OpenMolcas is the open-source version of Molcas, the program that was initially developed by Jan Almlöf, Björn Roos, and Per Siegbahn in the late 1980s. The complete Molcas Documentation can be found [HERE](https://www.molcas.org/documentation/manual/node1.html).

This software includes most of the methods that other programs like Gaussian or Orca have, for example, Hartree-Fock, density functional theory (DFT), coupled cluster, second-order Moller-Plesset, etc. However, OpenMolcas excels in the implementation of multiconfigurational self-consistent field (MCSCF) methods, such as complete active space self-consistent field (CASSCF), and has the capability to compute excited states, spin-orbit coupling (SOC), magnetic properties, etc., using MCSCF wave functions. This is of great importance for the study of transition metals, lanthanides, and heavy element chemistry, some of the topics of interest in the Vlaisavljevich and Miro research groups.

### Modules

OpenMolcas operates by calling various programs to perform specific tasks. Each program is called a `module` and in the OpenMolcas input, it always starts with the `&` symbol. For example, to perform a Hartree-Fock calculation, you have to include in your input the `&SCF` module.

The most common modules we use in our research groups are the following:

> - `&SEWARD`: For integrals, XYZ coordinates, basis sets, spatial symmetry point group, density fitting, etc. [Seward](https://molcas.gitlab.io/OpenMolcas/sphinx/users.guide/programs/seward.html) 
> - `&SCF`: for Hartree-Fock and DFT calculations. [Scf](https://molcas.gitlab.io/OpenMolcas/sphinx/users.guide/programs/scf.html)
> - `&GUESSORB`: To generate initial guess orbitals. [Guessorb](https://molcas.gitlab.io/OpenMolcas/sphinx/users.guide/programs/guessorb.html)
> - `&GRID_IT`: For plotting the computed molecular orbitals [GridIt](https://molcas.gitlab.io/OpenMolcas/sphinx/users.guide/programs/grid_it.html)
> - `&EXPBAS`: To increase the basis functions of a previous calculation for a new calculation [ExpBas](https://molcas.gitlab.io/OpenMolcas/sphinx/users.guide/programs/expbas.html)
> - `&RASSCF`: To perform state-specific and state-average CASSCF, RASSCF, CASCI, RASCI calculations [Rasscf](https://molcas.gitlab.io/OpenMolcas/sphinx/users.guide/programs/rasscf.html)
> - `&CASPT2`: For single-state, multistate and extended multistate CASPT2 calculations [Caspt2](https://molcas.gitlab.io/OpenMolcas/sphinx/users.guide/programs/caspt2.html)
> - `&RASSI`: For Spin-Orbit Coupling, oscillator strengths, SOC matrix elements, transition dipole moments, etc. [Rassi](https://molcas.gitlab.io/OpenMolcas/sphinx/users.guide/programs/rassi.html)
> - `&SINGLE_ANISO`: Magnetic properties (g-tensor, zero-field splitting, magnetic susceptibility), crystal field parameters, etc. [SingleAniso](https://molcas.gitlab.io/OpenMolcas/sphinx/users.guide/programs/single_aniso.html)
> - `&MCPDFT`: For MC-PDFT energies (also multistate MC-PDFT, but it is not recommended due to bad results, except for [L-PDFT](https://pubs.acs.org/doi/abs/10.1021/acs.jctc.3c00207) -on PySCF) [Mcpdft](https://molcas.gitlab.io/OpenMolcas/sphinx/users.guide/programs/mcpdft.html)

Something you have to know is that all OpenMolcas calculations necessary must start with `&GATEWAY` followed by `&SEWARD`, or only `&SEWARD` (Gateway can be used independently of Seward, but in the end, Gateway is a submodule of Seward, so people usually use only Seward) because these modules generate the one- and two-electron integrals necessary for all quantum chemical calculation, and of course, you define the basic settings for all calculations, like the molecular geometry and basis sets. This information is stored in files you don't usually observe in the submitting directory. These files are usually handled in the OpenMolcas working directory, for example, `RUNFILE` and `INPORB`. Most of the time, you don't have to worry about these files, but it is important for you to know they exist, because depending on this, you can run OpenMolcas calculations in a particular way.

Another important consideration is that every module creates files that can be used by subsequent modules, and vice versa; most modules can read output files from other modules. For example:

> - `&SEWARD` creates in the working directory the `RUNFILE`, `ONEINT`, and `ORDINT` files, containing general information about the calculation, the one-electron integrals, and the two-electron integrals, respectively. Such files are input files for the `&SCF` module, so you can perform a DFT calculation according to the Kohn-Sham equations.
> - In a second example, let us assume you perform a Hartree-Fock calculation. The `&SCF` module uses as input the files mentioned above, and once the SCF calculation converges, some of the output files of this module are the `INPORB` file, which is handled by OpenMolcas in the working directory for subsequent calculations, but you also obtain files with extensions `.ScfOrb`, `.UhfOrb`, and `.UnaOrb`, where the last two files are obtained only after an unrestricted SCF calculation. Each of these `Orb` files can be used as input for other modules. We often use these orbital files as input for the `&RASSCF` module to perform a CASSCF calculation.
> -  Similarly, the `&RASSCF` module generates files that can be used for different modules, like `&MCPDFT` to obtain the MC-PDFT energies, to `&CASPT2` module, and then obtain CASPT2 energies and wave functions, or we can directly use the `&RASSCF` output files for the `&RASSI` module.

As you can see, there is not a single way to perform a calculation with OpenMolcas. You can perform a calculation in a single input by concatenating all the desired modules, or you can split your calculation into various inputs, doing separate calculations one at a time (Check my old [Slides](https://github.com/peremiro/QuantumHawks/blob/main/doc/images/openmolcas_tutorial_2022.pdf) if you want to check better examples). 



### Submitting Jobs

{{< alert type="danger" >}}
These instructions are valid for the HPC Cluster, Argon, we have at the University of Iowa (2026) `type="danger"`.
{{< /alert >}}

Before explaining the input structure, you have to check the scripts necessary to submit OpenMolcas calculations in Argon HPC. The scripts are stored at `/Shared/lss_bvlaisavljevich/Scripts/`.

The submission scripts have names such as `openmolcas-24.sh`. Depending on the number at the end of the file name, the requested resources for your calculations change. This implies that the total memory allocated for that job is 24*8GB = 192GB. However, be sure not to request your OpenMolcas calculation to use all the requested memory, especially for memory-intensive calculations. You have to use approximately 80 to 90% of the requested memory.

We run OpenMolcas in serial, thus, the available installation in the Shared folder was compiled considering that setting. Only a few OpenMolcas modules experience slight performance improvements for a multicore/parallel installation, however, you may encounter numerical instabilities if you are not cautious while using non-serial calculations. In the Argon HPC Cluster, no parallel installation is available.

Once you are logged in to Argon HPC, to submit the calculations, use the following command:

<pre>
qsub openmolcas-24.sh
</pre>

Be sure you modified the `openmolcas-24.sh` submission script according to your calculation needs.

In case you are still interested on a launcher script for OpenMolcas calculations, this is the type of script I am using for an HPC with Sun Grid Engine.

<details >
<summary> Check code </summary>

```
#!/bin/bash
#$ -q BV
#$ -l h_rt=1200:00:00
#$ -pe smp 8
#$ -l mf=161G
#$ -N job_openmolcas
#$ -o job_openmolcas.log
#$ -e job_openmolcas.err
#$ -cwd 

#Setting working directory for OpenMolcas calculation
export JOB_HOME=/path/to/input/file/
export SCRATCH=$TMPDIR
echo ' JOB ID = ' $JOB_ID  > ${JOB_NAME}.log 
echo 'SCRATCH = ' $SCRATCH  >> ${JOB_NAME}.log
echo ' ' >> ${JOB_NAME}.log 

#Loading modules for OpenMolcas
module load python
module load py-h5py
module load py-six
module load py-matplotlib
module load intel-mkl

#Setting OpenMolcas Variables

export Project=job_openmolcas

export MOLCAS_NPROCS=1
export MOLCAS_CPUS=1
export MOLCAS_MEM=10Gb
export MOLCAS=/path/to/openmolcas/installation/
export MOLCAS_SOURCE=/path/to/openmolcas/source_code/
export MOLCAS_MOLDEN=ON

export Scratch=$TMPDIR
export WorkDir=$Scratch/$Project
export CurrDir=$PWD

#commands to run your program start here 
ulimit -c 0

#### start the calculation ####
cd $JOB_HOME

$MOLCAS/pymolcas openmolcas.input >> ${JOB_NAME}.log

```

</details>


### Input Structure

#### &GATEWAY and &SEWARD

In the **Modules** section, it was mentioned that `&GATEWAY` is a submodule of `&SEWARD`. Thus, they share many keywords. Consider the water molecule with XYZ coordinates:
```
  3
  Water 
  O   0.000000  0.000000   0.000000 
  H   0.758602  0.000000   0.504284
  H   0.758602  0.000000  -0.504284
```
When using these modules, you can call an XYZ file, or you can include the data in the input file.

- Including the XYZ coordinates in the input file:
  
```
&GATEWAY
COORD  
 3  
  Water  
  O   0.000000  0.000000   0.000000 
  H   0.758602  0.000000   0.504284
  H   0.758602  0.000000  -0.504284 
Basis = 6-31G  
End of Input

 &SEWARD 
 End of Input
```
- Calling the XYZ file:
```
&GATEWAY
COORD = water.xyz
Basis = 6-31G  
End of Input

 &SEWARD 
 End of Input
```
- Or, you can merge the `&GATEWAY` keywords into `&SEWARD`, displaying all the XYZ coordinates in the input file:

```
&SEWARD
COORD  
 3  
  Water  
  O   0.000000  0.000000   0.000000 
  H   0.758602  0.000000   0.504284
  H   0.758602  0.000000  -0.504284 
Basis = 6-31G  
End of Input

```

- Or, calling the XYZ coordinate:
```
&SEWARD
COORD = water.xyz
Basis = 6-31G  
End of Input

```

By the way, it is not necessary to include `End of Input` once you have finished writing all the keywords associated with a module, but your input looks more organized, and it is useful to avoid mistakes.

In case you want to assign different basis functions depending on the atom type, you can try this:
```
&SEWARD
COORD = water.xyz
Basis = O.6-311G, H.3-21G 
End of Input

```
Where the oxygen atom is described using the 6-31G basis set, and the hydrogen atoms use the 3-21G basis set. Assuming you want to study a molecule containing Cr, C, H, and N atoms, you can specify the basis set for each atom as shown before, but now, in this example, let us suppose you want to use the `ANO-RCC-VTZP` basis set for all the atoms, except for H atoms, which will be described with `ANO-RCC-MB` basis set. There are two ways to specify the basis sets:

> - Option 1 (the hard way):
```
&SEWARD
COORD = molecule.xyz
Basis = Cr.ANO-RCC-VTZP, C.ANO-RCC-VTZP, N.ANO-RCC-VTZP, H.ANO-RCC-MB
End of Input

```
> - Option 2 (the easy way):

```
&SEWARD
COORD = molecule.xyz
Basis = ANO-RCC-VTZP, H.ANO-RCC-MB 
End of Input

```
In option 1, you specify for each atom the basis functions to use, but the string gets long really easy, and OpenMolcas has a bug associated to this, where it cannot read a long list of atoms and basis functions, in this case, the option 2 is preferred, where you specify with the `BASIS` keyword that you are using ANO-RCC-VTZP for everything, **BUT**, for the hydrogen atoms, you are using ANO-RCC-MB.

Another interesting example about basis functions is when you want to use a different basis set for different atoms, even if they are of the same kind. In this case of situations, I recommend including the XYZ coordinates of your molecule in the input file, for example:

```
&SEWARD
Basis set
O.6-31G....
O1   0.000000  0.0000000   0.000000     /angstrom
End of Basis

Basis set
H.3-21G....
H1    0.758602 0.0000000   0.504284    /angstrom
End of Basis

Basis set
H.4-31G....
H2    0.758602 0.0000000  -0.504284    /angstrom
End of Basis

End of Input
```
Be sure to rename the elements containing the XYZ coordinates. In this case, O for O1, H for H1, and H for H2. Another option is to do the same differentiation of basis sets directly in the `XYZ` coordinates:

```
&SEWARD
COORD  
 3  
  Water  
  O.6-31G   0.000000  0.000000   0.000000     /angstrom
  H.3-21G   0.758602  0.000000   0.504284     /angstrom
  H.4-31G   0.758602  0.000000  -0.504284     /angstrom
End of Input

```

Next, I am leaving a `&SEWARD` example for one of my inputs for more advanced calculations:

```
&SEWARD
COORD =  molecule.xyz
Group = Nosym
Basis = U.ANO-RCC-VTZP, N.ANO-RCC-VTZP, C.ANO-RCC-MB, H.ANO-RCC-MB
RICD
Grid Input
 Grid = Ultrafine
End of Grid Input
ANGM
0.000000   0.000000   0.000000  Angstrom
End of Input

```
In this example, the studied `molecule` has uranium, carbon, nitrogen, and hydrogen atoms. Only U and N are described using the relativistic `ANO-RCC-VTZP` basis set, while C and H are described using the minimum basis `ANO-RCC-MB`. In OpenMolcas, when you use the `ANO-RCC` basis sets, the second-order Douglas-Kroll-Hess Hamiltonian (DKH2) to account for scalar relativistic corrections is automatically turned on. But if you are using other basis functions, be cautious and turn on the DKH Hamiltonian. Next, the `Group = Nosym` keyword implies that the molecule does not have any spatial point group symmetry (or C<sub>1</sub>). The `RICD` is to use the Cholesky Decomposition for the Resolution of the Identity, i.e., for density fitting and speed up your calculation. Then, I included the `Grid Input` and `Grid = Ultrafine` keywords because they are used for MC-PDFT calculations. MC-PDFT relies on the grid quality; that's why I use the best grid available. If you want to publish MC-PDFT results, you should use the best grid available. However, if you just want to explore what might be an MC-PDFT outcome, you can use `Grid = fine`. Finally, because I was planning to use this input for the computation of magnetic properties, with `ANGM`, it indicates the origin of angular momentum. In this case, it matches the XYZ coordinates of the Uranium center because that's the origin of the magnetic properties of that molecule.


#### &SCF
The `&SCF` module is used to run single-point calculations with the Hartree-Fock (HF) method, or using DFT. Often, we use this module to generate an initial guess wave function for further multireference calculations. Therefore, only a few examples of this module will be provided; if you want to learn all the `&SCF` features, you can check the official documentation.

With the `&SCF` module, you can perform closed-shell or open-shell HF or DFT calculations. To perform a closed-shell HF calculation, you can try:
```
&SCF
End of Input

```
That's it, as simple as that. However, the `&SCF` module takes some considerations, like the total charge is 0, and the initial guess orbitals are generated in the background. But you can specify the total charge and or use orbitals from a previous calculation with the `Lumorb` or `fileorb` keywords.

> - Using `Lumorb`, where you use the `COPY` command to manipulate an orbital file from a previous calculation, and generate the input orbitals (`INPORB`) for the new calculation (Oh!, and `$CurrDir` is a variable used to specify the path from the directory where you are submitting your calculation, check the Bash section of this webpage to check how to use environment variables, this is similar to that) :

```
>> COPY $CurrDir/previous_calculation.ScfOrb INPORB
&SCF
Lumorb
Charge = 0
End of Input

```

> - Using the `fileorb` keyword:

```
&SCF
Fileorb=$CurrDir/previous_calculation.ScfOrb
Charge = 0
End of Input

```

When dealing with open-shell molecules, like radical molecules, transition metal complexes, lanthanides, actinides, etc., you need to perform an unrestricted HF or DFT calculation. You have to include the `UHF` keyword and that's all. However, OpenMolcas might assume a different number of unpaired electrons. Therefore, I recommend you use the `ZSPIN` keyword to indicate the number of unpaired electrons (`ZSPIN = 1` for a doublet spin-state, `ZSPIN = 2` for a triplet state, `ZSPIN = 3` for a quartet, and so on...). An alternative is using the `SPIN` keyword to indicate the spin multiplicity for the calculation (`SPIN = 1` for a singlet state, `SPIN = 2` for a doublet, `SPIN = 3` for a triplet, `SPIN = 4` for a quartet, and so on...). Finally, you can select the maximum number of SCF cycles to perform with the `ITER` keyword. 

Check the following example for an unrestricted HF calculation of an anion with a total charge of -2, considering a doublet spin-state:

```
>> COPY $CurrDir/previous_calculation.ScfOrb INPORB
&SCF
Lumorb
UHF
Charge = -2
Spin = 2
Iterations = 300
End of Input

```

The previous example is equivalent to:

```
>> COPY $CurrDir/previous_calculation.ScfOrb INPORB
&SCF
Lumorb
UHF
Charge = -2
Zspin = 1
Iterations = 300
End of Input

```

Finally, to perform a DFT calculation, you just need to use the `KSDFT` functional to specify the exchange-correlation functional to use. No further changes are needed. Also, another helpful keyword is `PRORbitals`, with which you can specify which HF or Kohn-Sham orbitals to be printed. Generally, the default values work well for me, but you can use `PRORbitals = n `, where `n=0` to not print orbitals, `n=1` for orbitals with energies smaller than 2E<sub>HOMO</sub> -E<sub>LUMO</sub> (For more printing options, check the official documentation).

This is an example of a DFT calculation using the PBE functional:

```
>> COPY $CurrDir/previous_calculation.ScfOrb INPORB
&SCF
Lumorb
UHF
KSDFT = PBE
Charge = -2
Spin = 2
Iterations = 300
End of Input

```
Finally, this is an example of a Hartree-Fock calculation in a triplet state:
```
&SEWARD
COORD  
 3  
  Water  
  O   0.000000  0.000000   0.000000    
  H   0.758602  0.000000   0.504284    
  H   0.758602  0.000000  -0.504284
Basis = ANO-RCC-VTZP
Group = nosym
RICD
End of Input

&SCF
UHF
Spin = 3
Charge = 0
Iterations = 300
End of Input 

```
Some of the output files, once a calculation with this module is finished, are the `.ScfOrb` (canonical orbitals of a closed-shell HF calculation), `.UhfOrb` (canonical orbitals from an unrestricted HF calculation), and `.UnaOrb` (natural orbitals from an unrestricted HF calculation). These files can be used to restart other SCF calculations or as an initial guess for other modules, such as `&RASSCF`, for multireference calculations using the `fileorb` or `Lumorb` keywords, as shown in some examples above.


#### &GUESSORB
The `&GUESSORB` module generates guess orbitals for further calculations. The output file to be used has extension `.GssOrb`. When using this module, I always recommend to use the `PRMO = 3` keyword to print the guess orbitals in the output file. Without this keyword, no information is printed in the calculation output file. Sometimes it is also useful to request a population analysis using the guess orbitals. You can do that with the keyword `PrPopulation`.

```
&GUESSORB
PRMO = 3 
PrPopulation

```
Something you should know is that `&GUESSORB` does not take the total charge or spin multiplicity as input. It is always considered a neutral molecule.

This is an example of a calculation using the `&GUESSORB` module:

```
&SEWARD
COORD  
 3  
  Water  
  O   0.000000  0.000000   0.000000    
  H   0.758602  0.000000   0.504284    
  H   0.758602  0.000000  -0.504284
Basis = ANO-RCC-VTZP
Group = nosym
RICD
End of Input

&GUESSORB
PRMO = 3 
PrPopulation

>> COPY $CurrDir/water.GssOrb INPORB

&SCF
Lumorb
UHF
Spin = 3
Charge = 0
Iterations = 300
End of Input 

```

#### &RASSCF
The `&RASSCF` module is used to perform multireference calculations using the CASSCF and RASSCF methods. This module accepts `INPORB`, `.GssOrb`, `.ScfOrb`, `.UhfOrb`, `.UnaOrb`, and `.RasOrb` orbital files as starting orbitals for the calculations. The `.RasOrb` output file is important for the type of calculations performed in the research group. This file contains the optimized CASSCF/RASSCF orbitals. Another important file is the `.JobIph` file, which contains the CASSCF/RASSCF CI-vector (the wave function). This last file is of importance for the `&RASSI` module, keep that in mind. 

As mentioned before, you can run CASSCF and RASSCF calculations. First, we are discussing how to perform CASSCF calculations. For all CASSCF calculations, remember that your orbital space is divided into three subspaces: (i) Inactive space (with only doubly occupied orbitals), virtual space (with empty orbitals), and the active space (orbitals for which fractional occupation numbers are allowed, and the orbitals are used for a Full CI calculation). 

In the following examples, the `&RASSCF` input structures will be discussed for molecules with C<sub>1</sub> symmetry in their wave function.
For a state-specific CASSCF calculation of the water molecule in its singlet ground state, the input structure can be written as follows:

```
>>COPY $CurrDir/start_orbitals.ScfOrb  INPORB

&RASSCF
Lumorb
Symmetry = 1
Spin = 1
Inactive = 1
NACTEL = 8 
RAS2 = 6
ORBListing = ALL
ORBAppear = COMPACT
ITERations = 200 100 
End of Input

```
In this example, the `Lumorb` keyword was used to indicate `&RASSCF` must read an orbital file. `Symmetry` is used to specify the symmetry of the wave function (`Symmetry = 1` corresponds to the trivial symmetry representation, the identity). `SPIN` is used to specify the spin state to be computed, 1 for singlet, 2 for doublet, 3 for triplets, and so on. The `Inactive` keyword is used to specify the number of doubly occupied orbitals. Be aware that, depending on the number of Inactive orbitals you select, you can change the total charge of your molecule. Alternatively, only for CASSCF calculations without symmetry, you can use the keyword `CHARGE` to establish the total charge of your system, and OpenMolcas automatically determines the number of inactive orbitals. The  active space is written in the literature as (n<sub>e</sub>, n<sub>o</sub>), where n<sub>e</sub> stands for the number of electrons included in the active space, and n<sub>o</sub> as the total number of orbitals in the active space. The `&RASSCF` module uses the keywords `NACTEL` and `RAS2` to specify the number of electrons and orbitals in the active space, respectively.  I recommend using the keywords `ORBListing` and `ORBAppear` to modify the way OpenMolcas prints the molecular orbitals. For different formatting, check the `&RASSCF` module official documentation. Finally, the `ITERations` keyword is used to specify the number of CASSCF iterations (200 is the maximum) and the number of iterations for the orbital optimization (100 is the maximum).

The `&RASSCF` module could be used to compute more than a single state at a time using the state-average formalism. To perform a SA-CASSCF calculation, you have to include the keyword `CIROOT` and then indicate the number of spin-states with the same spin multiplicity to be computed.

For example, to perform a SA-CASSCF calculation for the singlet ground-state of the water molecule, and three singlet excited states (a total of 4 states):

```
>>COPY $CurrDir/start_orbitals.ScfOrb  INPORB

&RASSCF
Lumorb
Symmetry = 1
Spin = 1
Inactive = 1
NACTEL = 8 
RAS2 = 6
CIROOT = 4 4 1 
ORBListing = ALL
ORBAppear = COMPACT
ITERations = 200 100 
End of Input

```

When using `CIROOT`, the meaning of the three numbers is: (i) the number of roots (states) to compute, (ii) from the total of roots, the number of states to be included in the orbital optimization, and (iii) in the case the last number is 1, then each root has the same weight for the SA-CASSCF calculation. Alternatively, when performing a SA-CASSCF with equal weights, you can use the keyword `STAVErage` followed by only the total number of states.

The computation of RASSCF  wave functions is done following the same input structure for CASSCF, with a few differences. In the RASSCF method, we add the subspaces RAS1 and RAS3 to the methodology. RAS1 corresponds to a set of doubly occupied orbitals that allow electron excitations from the orbitals in RAS1 to the empty orbitals in RAS3. Similarly, RAS3 is a set of virtual orbitals that are allowed to hold electrons from RAS1. In the `&RASSCF` module, we specify the number of orbitals in RAS1 and RAS3, with the keywords `RAS1` and `RAS3`, respectively (and obviously, though). Additionally, the `NACTEL` keyword should be written as `NACTEL = n h p`, where `n` is the total number of electrons in RAS2, `h` is the maximum number of "holes" in RAS1 (the maximum number of electrons that can be excited from RAS1 to RAS3), and `p` is the maximum number of particles (electrons) occupying the RAS3 orbitals. By the way, for a CASSCF calculation, you can write in your input `RAS1=0`, `RAS3=0`, and `NACTEL = n 0 0` (This is equivalent to the CASSCF example shown before).

Similar to CASSCF, you can run state-specific and state-average RASSCF calculations. An example of a SA-RASSCF calculation is:

```
>>COPY $CurrDir/uranium_complex_orbitals.RasOrb  INPORB

&RASSCF
Lumorb
Symmetry = 1
Spin = 4
Charge = 0 
NACTEL = 3 2 2
RAS1 = 3 
RAS2 = 7
RAS3 = 5
CIROOT = 35 35 1 
ORBListing = ALL
ORBAppear = COMPACT
ITERations = 200 100 
End of Input

```

The methods CASSCF and RASSCF are not black-box methods. Sometimes, the CASSCF calculations converge with orbitals without chemical meaning to the phenomenon under study. For example, let us assume you are interested in calculating the  energy differences between high- and low-spin configurations of transition metal complexes. In this case, you might need to include the metal d valence orbitals into the active space, but the CASSCF calculation you performed has only ligand orbitals. Thus, you need to substitute the ligand orbitals with those required. Then, you have to manually select the orbitals you want to include in the active space and those you want to replace. To do this, you need the `ALTER` keyword.

```
>>COPY $CurrDir/start_orbitals.ScfOrb  INPORB

&RASSCF
Lumorb
Symmetry = 1
Spin = 3
Charge = 0
NACTEL = 2
RAS2 = 10
CIROOT = 10 10 1
ALTER = 3
1 35 43
1 36 45
1 38 46
ORBListing = ALL
ORBAppear = COMPACT
ITERations = 200 100 
End of Input

```
In the previous example, using `ALTER`, three pairs of orbitals have been selected for swapping. The first orbital pair has been rotated using symmetry 1, and the orbital indices for the orbitals to be swapped are 35 and 43. Then, the orbitals 36 and 45 are swapped with symmetry 1, and the final pair of orbitals has indexes 38 and 46.

 
When using the `CIONLY` keyword, you can perform CASCI and RASCI calculations where the orbital optimization is omitted. The example of a CASCI calculation is:

```
>>COPY $CurrDir/start_orbitals.ScfOrb  INPORB

&RASSCF
Lumorb
CIONLY
Symmetry = 1
Spin = 1
Inactive = 1
NACTEL = 8 
RAS2 = 6
ORBListing = ALL
ORBAppear = COMPACT
ITERations = 200 100 
End of Input

```

Finally, an input example of a SA-CASSCF calculation is shown below: 

```
&SEWARD
RICD
COORD = Cr_molecule.xyz
group = nosym
basis = Cr.ANO-RCC-VTZP, C.ANO-RCC-VDZ, H.ANO-RCC-VDZ
End of Input

>>COPY $CurrDir/previous_step.RasOrb INPORB

&RASSCF
Lumorb
Symmetry = 1
Spin = 3
NACTEL = 10 0 0
CHARGE = 0
RAS2 = 15
ALTER = 1
1 98 108
CIROOT = 20 20 1
ORBListing = ALL
ORBAppear = COMPACT
ITERations = 200 100; CIMX = 500
Sdav = 200; PRWF = 0.01
End of Input

>>COPY $WorkDir/$Project.RasOrb $CurrDir/$Project.JobIph
>>COPY $CurrDir/$Project.RasOrb INPORB

&GRID_IT
sparse
all
End of Input

```

> Sometimes I found useful using the `LEVSHFt` and `SUPSYM` keywords to obtain the active spaces you are looking for. It is a way to constrain the active space. The `LEVSHft` keyword is used to include a level shift in the molecular orbitals, while the `SUPSYM` keyword generates an artificial symmetry group, and the `&RASSCF` module tries to optimize the orbitals into that group of orbitals. To use this last keyword, you have to specify the number of artificial group of orbitals, then in the next line the total number of orbitals and their corresponding indexes.

I am also including in the next example the keyword `OUTORBitals` that I use to generate Natural orbitals for the active space in the output and luscus files.

```
&SEWARD
RICD
COORD = Cr_molecule.xyz
group = nosym
basis = Cr.ANO-RCC-VTZP, C.ANO-RCC-VDZ, H.ANO-RCC-VDZ
End of Input

>>COPY $CurrDir/previous_step.RasOrb INPORB

&RASSCF
Lumorb
Symmetry = 1
Spin = 3
NACTEL = 10 0 0
CHARGE = 0
RAS2 = 15
CIROOT = 20 20 1
Levshft = 2.0
Supsym
1
15 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120
OUTORBitals = Natural ; 15 
ORBListing = ALL
ORBAppear = COMPACT
ITERations = 200 100; CIMX = 500
Sdav = 200; PRWF = 0.01
End of Input

>>COPY $WorkDir/$Project.RasOrb $CurrDir/$Project.JobIph
>>COPY $CurrDir/$Project.RasOrb INPORB

&GRID_IT
sparse
all
End of Input


```


#### &GRID_IT

This module is used to generate a file containing molecular orbitals for visualization with the [Luscus](https://sourceforge.net/projects/luscus) program. This module takes as input the `INPORB` file to generate an output file with the extension `.lus`. Alternatively, you can use the keyword `FileOrb` to indicate your input orbitals to be plotted. You can use `&GRID_IT` to generate Luscus files for HF, DFT, GUESSORB, CASSCF, and RASSCF output orbitals.  

The luscus files contain grids for the computed orbitals. Therefore, depending on the number of orbitals and the number of points used to generate the grids, you can obtain huge Luscus files requiring hundreds of MB or even GB of disk space for storage.

You can use this module as follows:

```
>> COPY $CurrDir/molecule.RasOrb INPORB
&GRID_IT
End of Input

```

Exist keywords to control the number of orbitals to be plotted and the density of the grid. The keyword `SPARSE` is used to generate somewhat poor-quality orbitals. On the other hand, `DENSE` generates high-quality grids for your orbitals. To select the range of orbitals to be plotted, you have to include the `SELECT` keyword. For a wave function with only one symmetry, you specify the orbitals as follows:

```
>> COPY $CurrDir/molecule.RasOrb INPORB
&GRID_IT
Dense
Select = 1:30-40
End of Input

```
Or, to visualize all the orbitals, include the `ALL` keyword.
```
>> COPY $CurrDir/molecule.RasOrb INPORB
&GRID_IT
Sparse
All
End of Input

```

In case your wave function has a symmetry different than C<sub>1</sub>, for example, a C<sub>2</sub> point group with two irreducible representations, you can select the number of orbitals of each irrep to be plotted. In the next example, for the first irrep, the orbitals 15-20 included in the luscus file, and the orbitals 12-16 in the second irrep are also included in the luscus output file.

```
>> COPY $CurrDir/molecule.RasOrb INPORB
&GRID_IT
Dense
Select = 1:15-20, 2:12-16
End of Input

```

This is an OpenMolcas input example where the `&GRID_IT` module is used:

```
&SEWARD
COORD  
 3  
  Water  
  O   0.000000  0.000000   0.000000    
  H   0.758602  0.000000   0.504284    
  H   0.758602  0.000000  -0.504284
Basis = ANO-RCC-VTZP
Group = nosym
RICD
End of Input

>> COPY $CurrDir/water.ScfOrb INPORB

&RASSCF
Lumorb
Symmetry = 1
Spin = 1
Charge = 0
Nactel = 8 0 0
RAS2 = 6 
End of Input

>>COPY $CurrDir/$Project.RasOrb INPORB

&GRID_IT
Sparse
All
End of Input

```
For this example, you are plotting all the computed MOs. For a CASSCF calculation, `&GRID_IT` can plot only the orbitals in the active space by writing only the module name in the input, and of course you can add the keywords to improve the grid. You can do it like this:

```
&GRID_IT
Dense
End of Input
```
As mentioned above, this will generate the MOs only for the active space orbitals with a high-quality grid.

#### &MCPDFT
Computing MC-PDFT energies with OpenMolcas is incredibly easy. Here, we demonstrate how to calculate state-specific MC-PDFT and hybrid MC-PDFT (HMC-PDFT) energies. You have to include the `&MCPDFT` module right after the `&RASSCF` module, or you can use the `INPORB` file as shown in previous input examples. Depending on your OpenMolcas installation, you can use the keywords `KSDFT` or `FUNC` to select the translated functional for your calculation.

> - OpenMolcas v24:
  ```
  &MCPDFT
  KSDFT = t:PBE
  End of Input

  ```
  
> - OpenMolcas v25:
  ```
  &MCPDFT
  FUNC = t:PBE
  End of Input

  ```
To compute HMC-PDFT energies, you can include the `LAMBDA` keyword. For example, to compute energies with the translated functional tPBE0, it is necessary to include 25% of the CASSCF energy into the HMC-PDFT energy equation. 
  ```
  &MCPDFT
  KSDFT = t:PBE
  Lambda = 0.25
  End of Input

  ```
An input example for an MC-PDFT calculation is the following:

```
&SEWARD
COORD  
 3  
  Water  
  O   0.000000  0.000000   0.000000    
  H   0.758602  0.000000   0.504284    
  H   0.758602  0.000000  -0.504284
Basis = ANO-RCC-VTZP
Group = nosym
RICD
End of Input

>> COPY $CurrDir/water.ScfOrb INPORB

&RASSCF
Lumorb
Symmetry = 1
Spin = 1
Charge = 0
Nactel = 8 0 0
RAS2 = 6 
End of Input

>>COPY $CurrDir/$Project.RasOrb INPORB

&MCPDFT
KSDFT = t:PBE
End of Input 

&GRID_IT
Sparse
All
End of Input

```

As mentioned in the **Modules** section, the multistate MC-PDFT methods available in OpenMolcas, such as state-interaction PDFT (SI-PDFT), extended multistate PDFT (XMS-PDFT), and compressed multistate PDFT (CMS-PDFT), have limitations when describing excited-state potential energy surfaces, including conical intersections. Thus, you can use these methods at your own risk. However, on PySCF, there have been important developments in an accurate multistate MC-PDFT method, specifically the linearized PDFT (L-PDFT).

Now that the warning has been mentioned, we are describing how to perform XMS-PDFT calculations.

The computation of XMS-PDFT energies is divided into two steps:
> 1. Obtaining the correct active space and obtaining the reference states with SA-CASSCF.
> 2. Apply the XMS procedure to the CASSCF states by including the `XMSI` keyword into the `&RASSCF` module, and then computing the XMS-PDFT energies by including the `MSPDft` in the `&MCPDFT` module.

An easy example of how to run an XMS-PDFT calculation is shown as follows:

```
&SEWARD
COORD
 3
  Water
  O   0.000000  0.000000   0.000000
  H   0.758602  0.000000   0.504284
  H   0.758602  0.000000  -0.504284
Basis = ANO-RCC-VTZP
Group = nosym
RICD
End of Input

>> COPY $CurrDir/water.ScfOrb INPORB

&RASSCF
Lumorb
Symmetry = 1
Spin = 1
Charge = 0
Nactel = 8 0 0
RAS2 = 6
CIROOT = 5 5 1
End of Input

>>COPY $CurrDir/$Project.RasOrb INPORB

&RASSCF
Lumorb 
Symmetry = 1
Spin = 1      
Charge = 0
Nactel = 8 0 0
RAS2 = 6
CIROOT = 5 5 1
XMSI
End of Input


&MCPDFT
KSDFT = t:PBE
MSPDFT
WJOB
End of Input

&GRID_IT
Sparse
All
End of Input

```

> In the previous example, I included the `WJOB` keyword to write the XMS-PDFT eigen states and energies into the `.JobIph` file instead of the SA-CASSCF energies, which might be useful for subsequent calculations with the `&RASSI` module. Additionally, in case you are interested on testing CMS-PDFT calculations, you can follow exactly the same input structure, but in the second `&RASSCF` module you have to substitute `XMSI` for `CMSI` instead.


#### &CASPT2
The `&CASPT2` module is used to perform perturbation theory over a CASSCF or RASSCF reference wave function. You can perform single-state, multistate, and extended multistate CASPT2, denoted as SS-CASPT2, MS-CASPT2, and XMS-CASPT2, respectively. In the following examples, we include the `IPEA` and `IMAGINARY` shifts, two empirical parameters used to address the intruder state problem in the CASPT2 formalism. An important output file from the `&CASPT2` module is the `.JobMix` file, which contains the CASPT2 wave function and energies. This file is of importance for the `&RASSI` module.

Considering a state-specific CASSCF reference wave function, to perform the CASPT2 calculation, we use the next input structure:
```
>>COPY $CurrDir/molecule.JobIph $WorkDir

&CASPT2
MaxIter = 300
Imaginary = 0.30
IPEA = 0.25
End of Input

```

When the state-average CASSCF method was used to obtain the reference states for a CASPT2 calculation, you can perform different types of CASPT2 calculations. Let us assume the SA-CASSCF reference has 5 states, then, you can compute:
- Single-state CASPT2 (SS-CASPT2):
```
>>COPY $CurrDir/molecule_sa-casscf_5-states.JobIph   $WorkDir

&CASPT2
NoMult
Multistate
5 1 2 3 4 5
MaxIter = 300
Imaginary = 0.30
IPEA = 0.25
End of Input

```
Where the `NOMULT` keyword turns off the multistate calculation, and the `MULTISTATE` keyword is used to indicate the total number of states to be corrected with perturbation theory, and which states. In the previous example, below the `MULTISTATE` keyword, we indicated that all five states are included in the CASPT2 calculation. Instead, we could use the keyword `ALL` to do the same task. However, you can select a smaller number of states, for example, three states out of the total 5, and the state numbers are 1, 2, and 5:
```
>>COPY $CurrDir/molecule_sa-casscf_5-states.JobIph   $WorkDir

&CASPT2
NoMult
Multistate
3 1 2 5
MaxIter = 300
Imaginary = 0.30
IPEA = 0.25
End of Input

```
Selecting states, as in the last input, can be done similarly for MS-CASPT2 and XMS-CASPT2.

> - Multistate CASPT2 (MS-CASPT2):
```
>>COPY $CurrDir/molecule_sa-casscf_5-states.JobIph   $WorkDir

&CASPT2
Multistate
5 1 2 3 4 5
MaxIter = 300
Imaginary = 0.30
IPEA = 0.25
End of Input

```
> - Extended multistate CASPT2 (XMS-CASPT2):
```
>>COPY $CurrDir/molecule_sa-casscf_5-states.JobIph   $WorkDir

&CASPT2
XMultistate
5 1 2 3 4 5
MaxIter = 300
Imaginary = 0.30
IPEA = 0.25
End of Input

```

An input example using the CASPT2 module is shown below:

```
&SEWARD
COORD  
 3  
  Water  
  O   0.000000  0.000000   0.000000    
  H   0.758602  0.000000   0.504284    
  H   0.758602  0.000000  -0.504284
Basis = ANO-RCC-VTZP
Group = nosym
RICD
End of Input

>> COPY $CurrDir/water.ScfOrb INPORB

&RASSCF
Lumorb
Symmetry = 1
Spin = 1
Charge = 0
Nactel = 8 0 0
RAS2 = 6
CIROOT = 3 3 1
End of Input

&CASPT2
XMultistate
3 1 2 3 
MaxIter = 300
Imaginary = 0.30
IPEA = 0.25
End of Input

```


#### &RASSI
The `&RASSI` program is an important part of OpenMolcas because with it, you can study excited states and the coupling between them. Also, you can mix spin-orbit free states using Spin-Orbit Coupling (SOC), and compute 
transition dipole moments, oscillator strengths, etc. 
This module requires the wave function files `.JobIph` or `.JobMix` obtained from the `&RASSCF` and `&CASPT2` modules, respectively. Therefore, after each of these calculations, it is important to save and keep track of the files. Also, `&RASSI` requires you to `COPY` the `.JobIph` or `.JobMix` wave function files into `JOB00n`, where `n` depends on the number of spin-manifolds you want to include in the state-interaction calculation. Each wave function file must be obtained from separate CASSCF or CASPT2 calculations. For example, for an Fe(II) complex, you can compute quintet, triplet, and singlet state manifolds with state-average or multistate calculations. If you want to mix the three spin-state manifolds, then you should `COPY` the quintets `.JobIph` file into `JOB001`, the triplets `.JobIph` into `JOB002`, and the singlets wave function into `JOB003`.
 
A simple example is considering the interaction between spin-orbit-free states within the same spin manifold. For example, for a Ce<sup>3+</sup> complex, we use the (1e,7o) active space to compute all possible (7) doublet states. An input containing the `&RASSI` program is shown below:

```
>>> COPY $CurrDir/cerium_7-doublets.JobIph   JOB001
&RASSI 
NROF = 1 7
1 2 3 4 5 6 7
MEES
SPINorbit
EJOB
DIPRint = 10-10
End of Input

```
This input example uses the `NROF` keyword to indicate the number of `.JobIph` files to be used for the state-interaction calculations followed by the total number of roots exist in the `.JobIph` file (7 doublets), and in the next line, it is enumerated the number of all the states that will be included in the state interaction. In this case, the seven doublets are considered for the RASSI calculations. The keyword `MEES` gives `&RASSI` the instruction of computing the angular momentum matrix elements in a basis of spin-orbit-free states. The `SPINorbit` keyword is used to compute spin-orbit coupling. With `EJOB`, you read directly from the `.JobIph` file the energies of each root, and they are included in the spin-orbit-free effective Hamiltonian that will be diagonalized. The keyword `DIPRint` establishes that information regarding the dipole intensities will be printed, and the number is the threshold of the values to be printed in the output file.

Previously, an example of an Fe(II) complex was mentioned. For this complex, it was computed with the SA-CASSCF method, 5 quintets, 35 triplets, and 22 singlets. Assuming you already computed the SA-CASSCF wave functions and you have the separate `.JobIph` files, the `&RASSI` input is the following:

```
>>> COPY $CurrDir/iron-complex_5-quintets.JobIph   JOB001
>>> COPY $CurrDir/iron-complex_35-triplets.JobIph   JOB002
>>> COPY $CurrDir/iron-complex_22-singlets.JobIph   JOB003
&RASSI
NROF = 3 5 35 22
1 2 3 4 5
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
SPIN
EJOB
SOCOupling = 0.0000001

End of Input
```

In the previous examples, you can substitute `.JobIph` for `.JobMix` files to use CASPT2 wave functions instead. However, if you want to use MC-PDFT energies for the computation of magnetic and spectroscopic properties, you must use the `HDIAG` keyword to substitute the CASSCF/RASSCF energies for MC-PDFT energies in the `.JobIph` file, followed by the `EJOB` keyword. Modifying the previous cerium example including MC-PDFT energies:

```
>>> COPY $CurrDir/cerium_7-doublets.JobIph   JOB001
&RASSI 
NROF = 1 7
1 2 3 4 5 6 7
MEES
SPINorbit
HDIAG
-3199.83912632
-3199.78924142
-3199.75080295
-3199.65684400
-3199.65959939
-3199.60048863
-3199.59549124
EJOB
DIPRint = 10-10
End of Input

```
When including more spin-states manifolds, you have to include the MC-PDFT energies following the same order as the `.JobIph` files were introduced for the `NROF`  keyword.

The example of a calculation including the `&RASSI` module is as follows:
```
&SEWARD
RICD
COORD = Fe-IV_molecule.xyz
AMFI
Douglas-Kroll
group = nosym
basis = Fe.ANO-RCC-VTZP, N.ANO-RCC-VDZ, C.ANO-RCC-VDZ,  H.ANO-RCC-VDZ.
ANGM
  0.00000005767923     -0.00138625131459      0.00000007053760  Angstrom
End of Input

>>> COPY $CurrDir/quintets_casscf_sa5.JobMix JOB001
>>> COPY $CurrDir/triplets_casscf_sa35.JobMix JOB002
>>> COPY $CurrDir/singlets_casscf_sa22.JobMix JOB003

&RASSI
Properties
3
'AngMom ' 1
'AngMom ' 2
'AngMom ' 3
NROF = 3 5 35 22
1 2 3 4 5
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
SPIN
EJOB
End of Input

```



#### &SINGLE_ANISO
The `&SINGLE_ANISO` module is used right after the `&RASSI` module. Therefore, often we have both modules in the same OpenMolcas input.  This module is used to compute magnetic properties, such as Zeeman splitting, zero-field splitting, and magnetic susceptibility. It is also used for the computation of ab initio Crystal Field parameters.

The computation of g- and D-tensors is done using the `MLTP` keyword. When using it, the program reads the information in two lines. The first line is the number of multiplets (number of spin-orbit states) for which the tensors will be computed, and the second line indicates the number of spin-orbit states for each multiplet. For example, let us consider that we are interested in three multiplets. Each multiplet has 2, 4, and 4 spin-orbit states, respectively. 

```
&SINGLE_ANISO
MLTP
3
2 4 4
End of Input

```
When computing the magnetic susceptibility tensor, we can establish the temperature range (`TINT`) and the magnitude of the applied magnetic field (`XFIE`) in Tesla units:
```
&SINGLE_ANISO
XFIE = 0.1
TINT = 0.0 300 51
End of Input

```
In the previous example, the temperature range for the magnetic susceptibility spans from 0 K to 300 K, with 51 evenly distributed points.

To obtain the ab initio Crystal Field parameters, it is necessary to use the `CRYS` keyword and then specify the metal center atomic symbol. The crystal field parameters can be computed only for first-row transition metals, lanthanides, and actinides. For lanthanides and actinides, only the atomic symbol is required, for example, for a Dysprosium complex, the input structure is:

```
&SINGLE_ANISO
CRYS = Dy
End of Input

```
However, when computing the crystal field parameters for a transition metal complex, the atomic symbol and the oxidation state must be mentioned. For example, for an Fe(IV) complex:
```
&SINGLE_ANISO
CRYS = Fe ; 4
End of Input

```
An OpenMolcas input for a calculation including the `&SINGLE_ANISO` is as follows:
```
&SEWARD
RICD
COORD = Fe-IV_molecule.xyz
AMFI
Douglas-Kroll
group = nosym
basis = Fe.ANO-RCC-VTZP, N.ANO-RCC-VDZ, C.ANO-RCC-VDZ,  H.ANO-RCC-VDZ.
ANGM
  0.00000005767923     -0.00138625131459      0.00000007053760  Angstrom
End of Input

>>> COPY $CurrDir/quintets_casscf_sa5.JobIph JOB001
>>> COPY $CurrDir/triplets_casscf_sa35.JobIph JOB002
>>> COPY $CurrDir/singlets_casscf_sa22.JobIph JOB003

&RASSI
Properties
3
'AngMom ' 1
'AngMom ' 2
'AngMom ' 3
NROF = 3 5 35 22
1 2 3 4 5
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
SPIN
EJOB
SOCOupling
0.0000000001

&SINGLE_ANISO
XFIE = 0.1
TINT = 0.0 300.0 51
CRYS = Fe ; 4
MLTP
2
1 3
End Of Input

```

### Helpful Tips 

In case you are interested in checking the dominant configuration for each computed root, you can open the output file with `vi` and search for the string `energy=`. Below the printed energy, check the second column, which shows the spin and occupation of each orbital in the active space. In the last column (under the weight header), the dominant configuration for each particular state is the configuration with the largest value.

In the OpenMolcas output, the row containing important information, like the energy computed for the quantum chemistry methods, starts with `::`. Thus, from the terminal, you can `grep` the computed energies: 

- When using CASSCF/RASSCF methods, to obtain the energies, try:
```
grep "::    RASSCF"  openmolcas_casscf_calculation.output | awk '{print $(NF)}'
```

- CASPT2 method:
```
grep "::    CASPT2"  openmolcas_caspt2_calculation.output | awk '{print $(NF)}'
```
- XMS-CASPT2 method:
```
grep "::    XMS-CASPT2"  openmolcas_xms-caspt2_calculation.output | awk '{print $(NF)}'
```
- MC-PDFT method:
```
grep "::    MCPDFT"  openmolcas_mcpdft_calculation.output | awk '{print $(NF)}'
```

This might sound trivial, but when using CASSCF/RASSCF to compute many spin-state manifolds, like the previous example of an Fe(IV) complex were quintet, triplet, and singlet state manifolds were computed, you can compute the orbitals for one of the spin-state manifolds and use those converged orbitals for the computation of the other spin-states. For example:

```
&SEWARD
RICD
COORD = Fe-IV_molecule.xyz
group = nosym
basis = Fe.ANO-RCC-VTZP, N.ANO-RCC-VTZP, C.ANO-RCC-MB, H.ANO-RCC-MB
End of Input

>>COPY $CurrDir/fe-iv-starting_orbitals.ScfOrb INPORB

&RASSCF
Lumorb
Symmetry = 1
Spin = 5
NACTEL = 4 0 0
CHARGE = 0
RAS2 = 10
CIROOT = 5 5 1
ORBListing = ALL
ORBAppear = COMPACT
ITERations = 200 100; CIMX = 500
Sdav = 200; PRWF = 0.01
End of Input

>>COPY $WorkDir/$Project.RasOrb $CurrDir/${Project}_quintets.RasOrb
>>COPY $WorkDir/$Project.JobIph $CurrDir/${Project}_quintets.JobIph

>>COPY $CurrDir/${Project}_quintets.RasOrb INPORB
&RASSCF
Lumorb
Symmetry = 1
Spin = 3
NACTEL = 4 0 0
CHARGE = 0
RAS2 = 10
CIROOT = 35 35 1
End of Input

>>COPY $WorkDir/$Project.RasOrb $CurrDir/${Project}_triplets.RasOrb
>>COPY $WorkDir/$Project.JobIph $CurrDir/${Project}_triplets.JobIph

>>COPY $CurrDir/${Project}_quintets.RasOrb INPORB
&RASSCF
Lumorb
Symmetry = 1
Spin = 1
NACTEL = 4 0 0
CHARGE = 0
RAS2 = 10
CIROOT = 22 22 1
End of Input

>>COPY $WorkDir/$Project.RasOrb $CurrDir/${Project}_singlets.RasOrb
>>COPY $WorkDir/$Project.JobIph $CurrDir/${Project}_singlets.JobIph

```

> - When working with lanthanide or actinide systems, often you have to include hundreds of states into the SA-CASSCF calculation. In a few cases I deal with convergence problems, to solve this issue I use the `Sdav` keyword in the `&RASSCF` module. For example, assuming you are working with an Americium (III) complex, you can compute up to 588 triplet states. Then, you have to set the value for `Sdav` to be greater than that number of states, for example:

```
&RASSCF
Lumorb
Symmetry = 1
Spin = 3
NACTEL = 3 0 0
CHARGE = 0
RAS2 = 7
CIROOT = 588 588 1
Sdav = 700
End of Input


```


- When running a `&RASSI` calculation, you can print the spin-orbit matrix elements with `SOCoupling ` followed by the threshold. The tighter the threshold, the more complete the matrix element will be printed. However, this might affect your `&RASSI` calculation. If you are mixing hundreds of states, it is possible that your `&RASSI` calculation will never finish because it is working on printing an incredibly huge number of matrix elements, and by the end of your `&RASSI` calculation, you will see only the following header:

  ```
      ****************************************************************************************************
      *                                                                                                  *
      *                                         Spin-orbit section                                       *
      *                                                                                                  *
      ****************************************************************************************************

  ```
Therefore, it is better not to try to use the `SOCoupling` keyword unless you are computing a few dozen states.




<div dir="rtl"> All suggestions are welcome to improve this section, just send me a message.  </div>


