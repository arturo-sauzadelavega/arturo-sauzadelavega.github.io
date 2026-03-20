---
title: "Figures with LaTeX/TikZ "
date: 2026-03-12 
description: Example of TikZ templates I use to plot data for my research papers and for presentations.
hero: latex_portada.png
menu:
  sidebar:
    name: LaTeX/TikZ
    identifier: latex
    weight: 30
author:
  name: Arturo Sauza de la Vega, Ph.D.
  image: /images/author/arturo_2.jpg
math: true
---

{{< img src="arturo_cartoon_11.png"  width="400" align="center" title="Figures with TikZ" >}}

{{< vs 3 >}}


I am not looking to get involve into the huge fight of *which software is the best for plotting*. Some people enjoy using `Microsoft Excel` to generate their plots, and that is fine for me. I even use `Microsoft Excel` or `Gnuplot` plots to quickly look into my data.

Some friends and collaborators plot withi `Origin` or python, using the `matplotlib` library, and in general those figures look fine. However, I love using `LaTeX/TikZ` for plotting data to be published in research papers, but I have to recognize that is not the fastest nor a friendly way to plot information.

Okay, let's get started. 


### 2D-Plots
In general, I obtained two kind of plots, bar and XY plots. In the following sections, I am including the templates and resulting figures. Probably I am not including a wide discussion about every single line I added unless I think it is necessary.  

#### XY Graphs

> The first plot I am adding corresponds to the total QTAIM atomic charge of cations when adding water molecules into the molecular cluster.

This is the plot:

{{< img src="graficaChidaTikz.png"  width="600" align="center" title="Atomic charge vs water molecules" >}}

<details >
<summary> Check code </summary>


```
\documentclass[border=1mm]{standalone}
\usepackage{amssymb,amsmath}
\usepackage{siunitx}
\usepackage[version=3]{mhchem}

% Paquetes TikZ
\usepackage{pgfplots}
\usepgfplotslibrary{groupplots}
\pgfplotsset{compat=newest}
\usetikzlibrary{plotmarks}
\usepgflibrary{plotmarks}
\usetikzlibrary{arrows.meta}
\usepackage{tikz}
\usepackage{float}


\begin{document}
\begin{tikzpicture}
\begin{axis}[
  yticklabel style={
          /pgf/number format/.cd, fixed, fixed zerofill, precision=2
  },
  xmin=0, xmax=8.5,
  scale only axis,
  width=85mm, height=56mm,
  axis y line=left,
  axis x line=bottom,
  xlabel={Number of water molecules},
  tick style={color=black},
%  xticklabels at=edge bottom,
  ymin=0.9, ymax=1.01,
  every outer x axis line/.append style={-{Classical TikZ Rightarrow[length=1.3mm]}},
  every outer y axis line/.append style={-{Classical TikZ Rightarrow[length=1.3mm]}},
  ylabel={$q(\Omega)$, \si{\elementarycharge}},
  legend pos=north east,
]

\addplot[color=purple, mark=square*, %con el * para rellenarlo
mark options={fill=purple, color=purple, draw=black, solid}, line width=1pt]
coordinates {
(0, 1)
(1,0.965)
(2,0.937)
(3,0.918)
(4,0.908)
(5,0.907)
(6,0.910)
(7,0.905)
(8,0.904)
};

\addplot[color=orange, mark=*, %con el * para rellenarlo
 mark options={fill=orange, color=orange, draw=black, solid}, line width=1pt]
coordinates {
(0, 1)
(1,0.970)
(2,0.945)
(3,0.944)
(4,0.926)
(5,0.915)
(6,0.908)
(7,0.908)
(8,0.906)
};

\addplot[color=yellow, mark=triangle*, %con el * para rellenarlo
mark options={fill=yellow, color=yellow, draw=black, solid}, line width=1pt]
coordinates {
(0, 1)
(1,0.976)
(2,0.958)
(3,0.953)
(4,0.940)
(5,0.940)
(6,0.932)
(7,0.926)
(8,0.925)
};
\legend{$\ce{Li}^+$, $\ce{Na}^+$,$\ce{K}^+$}

\end{axis}
\end{tikzpicture}

\end{document}
```
</details>


> While working in my Ph.D., I was testing the Q-Chem capabilities related to CASSCF, v2RDM-CASSCF, and v2RDM-PDFT. I plotted some dissociation curves and compare with OpenMolcas code. This is another pretty example of 2D plots. I think this figure is helpful to check the different type of markers and lines you can use for your own plots. Additionally, in my template first few lines, I included the command `\definecolor` to use colors I define using RGB color code. 



{{< img src="scan_coordinate_more_linepoints.png"  width="600" align="center" title="QChem and OpenMolcas" >}}

<details >
<summary> Check code </summary>

```
\documentclass[tikz,border=1mm]{standalone}
\usepackage{amsmath}
\usepackage{siunitx}
\usepackage[version=3]{mhchem}
% Paquetes TikZ
\usepackage{pgfplots}
\pgfplotsset{compat=1.11}
\usepgfplotslibrary{groupplots}
\pgfplotsset{compat=newest}
\usetikzlibrary{plotmarks}
\usepgflibrary{plotmarks}
\usetikzlibrary{arrows.meta}
\definecolor{sodium}{RGB}{221,221,25}
\definecolor{iceblue}{RGB}{102,255,255}
\definecolor{tan}{RGB}{210,180,140}
\definecolor{wine}{RGB}{153,0,76}
\definecolor{sulfur}{RGB}{255,160,0}

\begin{document}

\begin{tikzpicture}
\Large
  \begin{axis}[%title  = TL (7T - 9S) for CAS(8-8),
    height = 12cm,
    width  = 12cm,
    %bar width=1.2cm,
    x tick label style={/pgf/number format/1000 sep=},
    xticklabel style={rotate=0},
    yticklabel style={ /pgf/number format/.cd, fixed, fixed zerofill, precision=1 },
    %every outer x axis line/.append style={-{Classical TikZ Rightarrow[length=1.3mm]}},
    every outer y axis line/.append style={-{Classical TikZ Rightarrow[length=1.3mm]}},
    %ybar,
    ymin=-2.4, ymax=0.0,
    xmin = 1.8, xmax = 2.4,
    xlabel={distance (\AA)},
    ylabel={$\Delta E$ (eV) },
    x axis line style = { opacity = 0.5 },
    %xtick=data,
    axis x line       = bottom,
    axis y line       = left,
    tickwidth         = 2pt,
    %ybar interval     = 0.5,
   % enlarge x limits  = 0.05,
    enlarge y limits  = 0.0,
    %symbolic x coords = {CASSCF, CASPT2, tPBE, 10-tPBE, 20-tPBE, 25-tPBE, 40-tPBE, 60-tPBE, 80-tPBE },
    %nodes near coords,
    nodes near coords align={vertical},
    nodes near coords style={/pgf/number format/.cd,fixed zerofill,precision=2,fixed,fixed zerofill,precision=2},
    %every node near coord/.append style={anchor=west, rotate=90 }, %to rotate numbers over the columns
    legend style={at={(0.35,0.05)}, anchor=south west,legend columns=1},
    legend cell align={left},
  ]
%Qchem-CASSCF (2,2)
\addplot[color = brown, mark = square*, %con el * para rellenarlo
  mark options = {fill = brown, scale = 2.0, color = brown, draw = black, solid}, line
width = 1.2 pt]
      coordinates {
(0.50, 143.749)
(0.55, 99.314) 
(0.60, 66.947)
(0.65, 43.569)
(0.70, 26.861)
(0.75, 15.023)
(0.80, 6.532)
(0.85, 1.800)
(0.90, -2.853) 
(0.95, -4.968)
(1.00, -6.323)
(1.05, -6.942)
(1.10, -7.035)
(1.15, -8.723)
(1.20, -8.335)
(1.25, -7.782)
(1.30, -7.128)
(1.35, -6.422)
(1.40, -5.698)
(1.45, -4.982)
(1.50, -4.293)
(1.55, -3.645)
(1.60, -3.046)
(1.65, -2.503)
(1.70, -2.022)
(1.75, -1.604)
(1.80, -1.250)
(1.85, -0.956)
(1.90, -0.719)
(1.95, -0.532)
(2.00, -0.388)
(2.05, -0.279)
(2.10, -0.198)
(2.15, -0.139)
(2.20, -0.096)
(2.25, -0.066)
(2.30, -0.045)
(2.35, -0.031)
(2.40, -0.021)
(2.45, -0.014)
(2.50, -0.010)
(2.55, -0.007)
(2.60, -0.006)
(2.65, -0.005)
(2.70, -0.004)
(2.75, -0.004)
(2.80, 0.051) 
(2.85, 0.042)
(2.90, 0.035)
(2.95, 0.028)
(3.00, 0.023)
(3.05, 0.018)
(3.10, 0.015)
(3.15, 0.011)
(3.20, 0.009)
(3.25, 0.006)
(3.30, 0.005)
(3.35, 0.003)
(3.40, 0.002)
(3.45, 0.001)
(3.50, 0.000)
 };

%Qchem v2RDM-CASSCF (2,2)
 \addplot[color = green, mark = triangle*, %con el * para rellenarlo
 mark options = {fill = green, scale = 2.0, color = green, draw = black, solid}, line
width = 1.2 pt]
   coordinates {
(0.50, 155.314)
(0.55, 107.442)
(0.60, 73.380)
(0.65, 48.514)
(0.70, 30.648)
(0.75, 17.903)
(0.80, 8.918)
(0.85, 2.703)
(0.90, -1.788) 
(0.95, -5.300)
(1.00, -6.985)
(1.05, -7.875)
(1.10, -8.200)
(1.15, -8.130)
(1.20, -7.794)
(1.25, -7.286)
(1.30, -6.678)
(1.35, -6.020)
(1.40, -5.349)
(1.45, -4.692)
(1.50, -4.067)
(1.55, -3.487)
(1.60, -2.952)
(1.65, -2.463)
(1.70, -2.017)
(1.75, -1.629)
(1.80, -1.310)
(1.85, -1.041)
(1.90, -0.818)
(1.95, -0.636)
(2.00, -0.490)
(2.05, -0.376)
(2.10, -0.289)
(2.15, -0.220)
(2.20, -0.164)
(2.25, -0.121)
(2.30, -0.089)
(2.35, -0.065)
(2.40, -0.046)
(2.45, -0.032)
(2.50, -0.020)
(2.55, -0.011)
(2.60, -0.004)
(2.65, 0.001) 
(2.70, 0.005)
(2.80, 0.010)
(2.85, 0.012)
(2.90, 0.013)
(2.95, 0.013)
(3.00, 0.013)
(3.05, 0.012)
(3.10, 0.011)
(3.15, 0.010)
(3.20, 0.009)
(3.25, 0.007)
(3.30, 0.006)
(3.35, 0.004)
(3.40, 0.003)
(3.45, 0.001)
(3.50, 0.000)
};


%Qchem v2RDM-CAS(tPBE) (2,2)
 \addplot[color = blue, mark = *, %con el * para rellenarlo
  mark options = {fill = blue, scale = 2.0, color = blue, draw = black, solid}, line
width = 1.2 pt]
   coordinates {
(0.50, 152.067)
(0.55, 104.993)
(0.60, 70.671)
(0.65, 45.890)
(0.70, 28.049)
(0.75, 15.289)
(0.80, 6.258)
(0.85, -0.024) 
(0.90, -4.204)
(0.95, -6.694)
(1.00, -8.375)
(1.05, -9.264)
(1.10, -9.588)
(1.15, -9.516)
(1.20, -9.171)
(1.25, -8.648)
(1.30, -8.017)
(1.35, -7.329)
(1.40, -6.616)
(1.45, -5.915)
(1.50, -5.244)
(1.55, -4.607)
(1.60, -4.016)
(1.65, -3.468)
(1.70, -2.958)
(1.75, -2.573)
(1.80, -2.212)
(1.85, -1.878)
(1.90, -1.578)
(1.95, -1.328)
(2.00, -1.117)
(2.05, -0.942)
(2.10, -0.801)
(2.15, -0.683)
(2.20, -0.586)
(2.25, -0.500)
(2.30, -0.422)
(2.35, -0.353)
(2.40, -0.294)
(2.45, -0.244)
(2.50, -0.201)
(2.55, -0.164)
(2.60, -0.133)
(2.65, -0.108)
(2.70, -0.087)
(2.80, -0.055)
(2.85, -0.043)
(2.90, -0.035)
(2.95, -0.028)
(3.00, -0.022)
(3.05, -0.015)
(3.10, -0.011)
(3.15, -0.008)
(3.20, -0.005)
(3.25, -0.004)
(3.30, -0.002)
(3.35, -0.001)
(3.40, -0.001)
(3.45, -0.000)
(3.50,  0.000)
};


%OpenMolcas CASPT2 (2,2)
 \addplot[dashed, color = black,  %con el * para rellenarlo
   line width = 2.0 pt]
   coordinates {
(0.50, 142.637)
(0.55, 98.142)
(0.60, 65.794)
(0.65, 42.343)
(0.70, 25.525)
(0.75, 13.575)
(0.80, 5.189)
(0.85, -0.589) 
(0.90, -4.462)
(0.95, -6.946)
(1.00, -8.420)
(1.05, -9.167)
(1.10, -9.397)
(1.15, -9.263)
(1.20, -8.881)
(1.25, -8.340)
(1.30, -7.700)
(1.35, -7.012)
(1.40, -6.306)
(1.45, -5.610)
(1.50, -4.940)
(1.55, -4.307)
(1.60, -3.718)
(1.65, -3.181)
(1.70, -2.696)
(1.75, -2.266)
(1.80, -1.887)
(1.85, -1.562)
(1.90, -1.285)
(1.95, -1.053)
(2.00, -0.863)
(2.05, -0.707)
(2.10, -0.577)
(2.15, -0.475)
(2.20, -0.392)
(2.25, -0.330)
(2.30, -0.271)
(2.35, -0.228)
(2.40, -0.193)
(2.45, -0.161)
(2.50, -0.137)
(2.55, -0.118)
(2.60, -0.099)
(2.65, -0.086)
(2.70, -0.074)
(2.75, -0.061)
(2.80, -0.054)
(2.85, -0.044)
(2.90, -0.041)
(2.95, -0.033)
(3.00, -0.026)
(3.05, -0.024)
(3.10, -0.017)
(3.15, -0.015)
(3.20, -0.013)
(3.25, -0.008)
(3.30, -0.007)
(3.35, -0.004)
(3.40, -0.001)
(3.45,  0.001)
(3.50,  0.000)
};

%OpenMolcas CASSCF (2,2)
 \addplot[densely dotted, color = red, mark=otimes*, %con el * para rellenarlo
  mark options = {fill = red, scale = 2.0, color = red, draw = black, solid},
   line width = 1.2 pt]
   coordinates {
(0.50, 143.473)
(0.55, 98.793)
(0.60, 66.431)
(0.65, 42.960)
(0.70, 26.132)
(0.75, 14.173)
(0.80, 5.778)
(0.85, -0.011) 
(0.90, -3.895)
(0.95, -6.388)
(1.00, -7.871)
(1.05, -8.624)
(1.10, -8.855)
(1.15, -8.718)
(1.20, -8.330)
(1.25, -7.777)
(1.30, -7.124)
(1.35, -6.417)
(1.40, -5.693)
(1.45, -4.978)
(1.50, -4.289)
(1.55, -3.640)
(1.60, -3.041)
(1.65, -2.498)
(1.70, -2.017)
(1.75, -1.599)
(1.80, -1.245)
(1.85, -0.951)
(1.90, -0.714)
(1.95, -0.527)
(2.00, -0.383)
(2.05, -0.274)
(2.10, -0.193)
(2.15, -0.134)
(2.20, -0.092)
(2.25, -0.061)
(2.30, -0.040)
(2.35, -0.026)
(2.40, -0.016)
(2.45, -0.009)
(2.50, -0.005)
(2.55, -0.002)
(2.60, -0.001)
(2.65,  0.000)
(2.70,  0.001)
(2.75,  0.001)
(2.80,  0.001)
(2.85,  0.000)
(2.90,  0.000)
(2.95,  0.000)
(3.00, -0.000)
(3.05, -0.000)
(3.10, -0.000)
(3.15, -0.000)
(3.20, -0.000)
(3.25, -0.000)
(3.30, -0.000)
(3.35, -0.000)
(3.40, -0.000)
(3.45, -0.000)
(3.50,  0.000)
};

%OpenMolcas tPBE (2,2)
 \addplot[densely dashdotted, color = magenta, mark=diamond*,  %con el * para rellenarlo
  mark options = {fill = magenta, scale = 2.0, color = magenta, draw = black, solid},
   line width = 1.2 pt]
   coordinates {
(0.50, 140.475)
(0.55, 96.544)
(0.60, 64.564)
(0.65, 41.343)
(0.70, 24.703)
(0.75, 12.887)
(0.80, 4.600)
(0.85, -1.108) 
(0.90, -4.931)
(0.95, -7.380)
(1.00, -8.833)
(1.05, -9.566)
(1.10, -9.787)
(1.15, -9.650)
(1.20, -9.268)
(1.25, -8.728)
(1.30, -8.093)
(1.35, -7.408)
(1.40, -6.709)
(1.45, -6.017)
(1.50, -5.349)
(1.55, -4.715)
(1.60, -4.123)
(1.65, -3.575)
(1.70, -3.073)
(1.75, -2.619)
(1.80, -2.210)
(1.85, -1.848)
(1.90, -1.531)
(1.95, -1.259)
(2.00, -1.028)
(2.05, -0.835)
(2.10, -0.675)
(2.15, -0.544)
(2.20, -0.439)
(2.25, -0.353)
(2.30, -0.283)
(2.35, -0.228)
(2.40, -0.183)
(2.45, -0.148)
(2.50, -0.119)
(2.55, -0.096)
(2.60, -0.077)
(2.65, -0.062)
(2.70, -0.049)
(2.75, -0.040)
(2.80, -0.032)
(2.85, -0.025)
(2.90, -0.020)
(2.95, -0.016)
(3.00, -0.012)
(3.05, -0.010)
(3.10, -0.007)
(3.15, -0.006)
(3.20, -0.004)
(3.25, -0.003)
(3.30, -0.002)
(3.35, -0.001)
(3.40, -0.001)
(3.45, -0.000)
(3.50,  0.000)
};

%OpenMolcas tPBE0 (2,2)
 \addplot[densely dashdotted, color = cyan,mark=pentagon*,  %con el * para rellenarlo
  mark options = {fill = cyan, scale = 2.0, color = cyan, draw = black, solid},
   line width = 1.2 pt]
   coordinates {
(0.50, 141.225)
(0.55, 97.106)
(0.60, 65.031)
(0.65, 41.747)
(0.70, 25.060)
(0.75, 13.209)
(0.80, 4.894)
(0.85, -0.833) 
(0.90, -4.672)
(0.95, -7.132)
(1.00, -8.592)
(1.05, -9.331)
(1.10, -9.554)
(1.15, -9.417)
(1.20, -9.034)
(1.25, -8.490)
(1.30, -7.851)
(1.35, -7.161)
(1.40, -6.455)
(1.45, -5.757)
(1.50, -5.084)
(1.55, -4.447)
(1.60, -3.853)
(1.65, -3.306)
(1.70, -2.809)
(1.75, -2.364)
(1.80, -1.969)
(1.85, -1.624)
(1.90, -1.327)
(1.95, -1.076)
(2.00, -0.867)
(2.05, -0.695)
(2.10, -0.554)
(2.15, -0.442)
(2.20, -0.352)
(2.25, -0.280)
(2.30, -0.223)
(2.35, -0.177)
(2.40, -0.141)
(2.45, -0.113)
(2.50, -0.090)
(2.55, -0.072)
(2.60, -0.058)
(2.65, -0.046)
(2.70, -0.037)
(2.75, -0.030)
(2.80, -0.024)
(2.85, -0.019)
(2.90, -0.015)
(2.95, -0.012)
(3.00, -0.009)
(3.05, -0.007)
(3.10, -0.006)
(3.15, -0.004)
(3.20, -0.003)
(3.25, -0.002)
(3.30, -0.002)
(3.35, -0.001)
(3.40, -0.000)
(3.45, -0.000)
(3.50,  0.000)
};

  \legend{CASSCF(Qchem), v2RDM-CASSCF (Qchem), v2RDM-tPBE (Qchem), CASPT2 (OpenMolcas), CASSCF (Openmolcas), tPBE (Openmolcas), tPBE0 (Openmolcas)}
  \end{axis}

\end{tikzpicture}
\end{document}

```

</details>


> When I finished my undergraduate studies at UNAM, I had to plot some plots with discontinuities in the y-axis. You can look at those plots in my [undergraduate thesis](https://tesiunam.dgb.unam.mx/F/RTU7NTG8QB45RPYK71C42RQLLXXLIXYL57LQED9F7KKMAM7KQR-03664) or looking into this paper about [the hydrolisis of epoxides](https://doi.org/10.1039/D1OB01026C). To do that, I used the following code:

{{< img src="graficasCatalisis.png"  width="600" align="center" title="QTAIM charges and epoxides reactions " >}}

<details >
<summary> Check code </summary>

```
\documentclass[tikz,border=1mm]{standalone}

\usepackage{tikz}
\usepackage{pgfplots}
\usepackage{amssymb,amsmath}
\usepackage[utf8]{inputenc}
\usetikzlibrary{plotmarks}
\usepgflibrary{plotmarks}
\usetikzlibrary{arrows.meta}
\pgfplotsset{compat=1.12}
\usetikzlibrary{pgfplots.groupplots}

\begin{document}
\begin{tikzpicture}

\pgfplotsset{
  broken axis style/.style={
    axis lines*     = left,
    axis line style = {-{Classical TikZ Rightarrow[length=1.3mm,width=3.0pt]}},
    yticklabel style={
        /pgf/number format/fixed,
        /pgf/number format/fixed zerofill,
        /pgf/number format/precision=2,
    },
    scaled y ticks  = false,   % <-- AQUÍ también, para ambos bloques
    enlargelimits   = false,
    width           = 12cm,
    xmin = 0, xmax = 4.2,
    xtick distance  = 1,
    legend cell align = left,
  }
}

% =========================================================
% EJE INFERIOR
% =========================================================
\begin{axis}[
  broken axis style,
  height = 3.5cm,
  at     = {(0,0)},
  ymin   = -0.14,
  ymax   = -0.09,
  %ytick  = {-0.10},
  xlabel         = {Number of water molecules},
  xtick distance = 1,
  axis line style = {-},
  every outer y axis line/.append style = {-},
  clip = false,
]


%Horizontal blue line 
\addplot+[ blue, solid, line width = 2.0pt, mark=none, const plot, empty line=jump, ]
coordinates { 
(0,-0.10)
(4,-0.10) 
};

\node at (2, -0.11) {\textbf{Basic Catalysis} };


  % Marcas del crunch (borde superior del eje inferior)
  \draw[white, line width=3pt]
      ([xshift=-4pt]current axis.north west) --
      ([xshift= 4pt]current axis.north west);
  \draw[black, line width=1pt]
      ([xshift=-6pt, yshift=-4pt]current axis.north west) --
      ([xshift= 6pt, yshift= 4pt]current axis.north west);
  \draw[black, line width=1pt]
      ([xshift=-3pt, yshift=-4pt]current axis.north west) --
      ([xshift= 3pt, yshift= 4pt]current axis.north west);

\end{axis}

% =========================================================
% EJE SUPERIOR
% =========================================================
\begin{axis}[
  broken axis style,
  height = 8cm,
  at     = {(0,2.4cm)}, %Para la separación entre bloques de los dos ejes discontinuos
  ymin   = -0.055,
  ymax   =  0.03,
  ytick distance = 0.01,
  %ytick  = {-0.06,-0.05,-0.04,-0.03,-0.02,-0.01,0.00,0.01,0.02},
  ylabel = {$\Delta$q($\Omega$) (a.u.)},
  % -----------------------------------------------
  scaled y ticks = false,        % <-- deshabilita el ×10⁻²
  yticklabel={
      \pgfmathprintnumber[
          fixed,
          fixed zerofill,
          precision=2
      ]{\tick}
  },
  % -----------------------------------------------
  xlabel      = {},
  xtick       = \empty,
  xticklabels = \empty,
  axis x line = none,
  legend pos  = north east,
  clip = false,
]

  % --- Serie 1: O_E (azul) ---
\addplot[ color = blue, mark = square*, mark options = {fill=red, color=blue, draw=black, solid}, ]
coordinates {
(0,0)
(1,-0.0324)
(2,-0.0419)
(3,-0.0464)
(4,-0.0451)
};

% --- Serie 2: O_1 (rojo) ---
\addplot[ color = red, mark = ball, mark options = {ball color = red}, mark size = 2.8pt, ]
coordinates {
(0,0)
(1,0.0043)
(2,0.0050)
(3,0.0053)
(4,0.0051)
};

% --- Línea horizontal roja ---
\addplot+[ red, solid, line width = 2.0pt, mark=none, const plot, empty line=jump, ]
coordinates { 
(0,0.01494)
(4,0.01494) 
};

% --- Línea en y=0 (negra punteada) ---
\addplot+[ black, dotted, mark=none, line width=1.5pt, const plot, empty line=jump, ]
coordinates { 
(0,0)
(4,0) 
};

\node at (2, 0.02) {\textbf{Acid Catalysis} };



  % Marcas del crunch (borde inferior del eje superior)
  \draw[white, line width=3pt]
      ([xshift=-4pt]current axis.south west) --
      ([xshift= 4pt]current axis.south west);
  \draw[black, line width=1pt]
      ([xshift=-6pt, yshift=-4pt]current axis.south west) --
      ([xshift= 6pt, yshift= 4pt]current axis.south west);
  \draw[black, line width=1pt]
      ([xshift=-3pt, yshift=-4pt]current axis.south west) --
      ([xshift= 3pt, yshift= 4pt]current axis.south west);

  \legend{
      $\textrm{O}_{\textrm{N}}$,
      $\textrm{O}_{\textrm{E}}$
  }

\end{axis}

\end{tikzpicture}
\end{document}

```

</details>

> This plot might be silly,  but sometimes you want to modify the marks with letters or $\LaTeX$ math symbols. To do that, you can follow this next example, where I changed the marks for numbers. In the following example, I use the numbers 1 and 2 for marks, also the symbols $\S$ and $\nabla$

{{< img src="plot_letters-in-datapoints.png"  width="600" align="center" title="Letter/numbers in marks" >}}

<details >
<summary> Check code </summary>

```
\documentclass[tikz,border=1mm]{standalone}
\usepackage{amsmath}
\usepackage{siunitx}
\usepackage[version=3]{mhchem}

% Paquetes TikZ
\usepackage{pgfplots}
\pgfplotsset{compat=1.11}
\usepgfplotslibrary{groupplots}
\pgfplotsset{compat=newest}
\usetikzlibrary{plotmarks}
\usepgflibrary{plotmarks}
\usetikzlibrary{arrows.meta}

\begin{document}
\begin{tikzpicture}
\LARGE
  \begin{axis}[
 height = 12cm,
 width  = 14cm,
 %bar width=0.7cm,
 scaled y ticks=false, %to display 0.0000 values and avoid the appearence fo 10⁻² 
 x tick label style={/pgf/number format/1000 sep=},
 xticklabel style={rotate=0}, %rotate labels in x axis 
 yticklabel style={ /pgf/number format/.cd, fixed, fixed zerofill, precision=2, /tikz/.cd },
 every outer y axis line/.append style={-{Classical TikZ Rightarrow[length=1.3mm]}},
 ylabel={ $E_{\textrm{DMRG-CI}}$  (Ha) },
 xlabel={Bond dimension (m) },
 x axis line style = { opacity = 0.5 },
 ymax = -3188.02,
 ymin = -3188.102,
 xmin = 0,
 xtick={100,200,500,700,1000},
 axis x line       = bottom,
 axis y line       = left,
 tickwidth         = 2pt,
 enlarge y limits  = 0.02,
 legend style={at={(0.5,0.85)}, anchor=north,legend columns=-1, legend cell align={left} },
  ] 

%Root 1
\addplot[dashed, color = blue, mark = text, text mark ={ 1 }, mark size=3pt, line width = 1pt,  mark options = {draw=black}] coordinates {
(100	,-3188.09465)
(200	,-3188.09291)
(500	,-3188.09073)
(700	,-3188.09674)
(1000	,-3188.09064)
};

%Root 2
\addplot[dashed, color = red, line width = 1.0pt, mark = text, text mark = { 2 },  mark options = {draw=black,scale=1.1}] coordinates {
(100	,-3188.100296)
(200	,-3188.099202)
(500	,-3188.101142)
(700	,-3188.100900)
(1000	,-3188.101154)
};

%Root 3
\addplot[dashed, color = teal, line width = 1.5pt, mark = text, text mark = { $\S$ },  mark options = {draw=black,scale=1.1}] coordinates {
(100	,-3188.08497)
(200	,-3188.07189)
(500	,-3188.05244)
(700	,-3188.07898)
(1000	,-3188.07557)
};

% Root 4
\addplot[dashed, color = brown, line width = 1.0pt, mark = text, text mark = { $\nabla$ },  mark options = {draw=black,scale=1.2}] coordinates {
(100	,-3188.08551)
(200	,-3188.08633)
(500	,-3188.08518)
(700	,-3188.08748)
(1000	,-3188.08495)
};

  \legend{T$_1$, T$_2$, T$_3$, T$_4$ }
  \end{axis}

\end{tikzpicture}
\end{document}
```

</details>


> During my internship at Los Alamos National Laboratory, I learned from my mentors María, Ping, and Ernesto, that when analyzing trends, not only plotting average data is important, we can extract or show important information when including error bars. This is really useful to demonstrate the calculations were done correctly. The next example shows the error bars to indicate the deviation of plotted bond distances.

{{< img src="plot_xy_error-lines.png"  width="600" align="center" title="Error bars for each point" >}}

<details >
<summary> Check code </summary>


```
\documentclass[tikz,border=1mm]{standalone}
\usepackage{amsmath}
\usepackage{siunitx}
\usepackage[version=3]{mhchem}

% Paquetes TikZ
\usepackage{pgfplots}
\usetikzlibrary{patterns}
\pgfplotsset{compat=1.11}
\usepgfplotslibrary{groupplots}
\pgfplotsset{compat=newest}
\usetikzlibrary{plotmarks}
\usepgflibrary{plotmarks}
\usetikzlibrary{arrows.meta}

\begin{document}
\begin{tikzpicture}
\huge
  \begin{axis}[ 
    height = 15cm,
    width  = 20cm,
    x dir=reverse, 
    x tick label style={/pgf/number format/.cd, fixed, fixed zerofill, precision=2},
    yticklabel style={ /pgf/number format/.cd, fixed, fixed zerofill, precision=2 },
    every outer x axis line/.append style={-{Classical TikZ Rightarrow[length=1.3mm]}},
    every outer y axis line/.append style={-{Classical TikZ Rightarrow[length=1.3mm]}},
    ymax = 2.75,
    ymin = 2.18, 
    xmin = 0.96, 
    xmax = 1.18,
    ylabel= { Ln--X Bond distance   (\AA)},
    xlabel = {Shannon Radius 8 C.N. (\AA)},  
    x axis line style = { opacity = 0.5 },
    axis x line       = bottom,
    axis y line       = left,
    tickwidth         = 2pt,
    enlarge y limits  = 0.0,
    nodes near coords align={vertical},
    nodes near coords style={/pgf/number format/.cd,fixed zerofill,precision=2,fixed,fixed zerofill,precision=2},
    legend style={at={(0.01,0.20)}, anchor=north west,legend columns=2},
    legend cell align={left}
  ]
%Bond Distances Ln-N (DFT)
\addplot [color = blue, mark size=5pt, mark= ball, draw = black, only marks,error bars/.cd,y dir=both,y explicit ] coordinates { 
(1.160,	2.700) += (0, 0.0)  -=  (0, 0.0)  
(1.143,	2.669) += (0, 0.0)  -=  (0, 0.0)
(1.126,	2.651) += (0, 0.0)  -=  (0, 0.0)
(1.109,	2.633) += (0, 0.047)  -=  (0, 0.075)
(1.093, 2.598) += (0, 0.058)  -=  (0, 0.065)
(1.079,	2.604) += (0, 0.0)  -=  (0, 0.0)
(1.066,	2.595) += (0, 0.0)  -=  (0, 0.0)
(1.053,	2.576) += (0, 0.0)  -=  (0, 0.0)
(1.040,	2.562) += (0, 0.047)  -=  (0, 0.074)
(1.027,	2.548) += (0, 0.059)  -=  (0, 0.070)
(1.015,	2.534) += (0, 0.053)  -=  (0, 0.064)
%(1.004,    )
(0.994,	2.512) += (0, 0.063)  -=  (0, 0.076)
(0.985,	2.504) += (0, 0.067)  -=  (0, 0.082)
(0.977,	2.495) += (0, 0.064)  -=  (0, 0.081)
};
%Bond Distances Ln-O (DFT)
\addplot [color = red, mark size=4pt, mark = square*, draw = black, only marks, error bars/.cd,y dir=both,y explicit ] coordinates {
(1.160, 2.468) += (0, 0.0) -= (0, 0.0)   
(1.143, 2.446) += (0, 0.0) -= (0, 0.0)
(1.126, 2.426) += (0, 0.0) -= (0, 0.0)
(1.109, 2.410) += (0, 0.009) -= (0, 0.009)
(1.093, 2.404) += (0, 0.019) -= (0, 0.019)
(1.079, 2.383) += (0, 0.0) -= (0, 0.0)
(1.066, 2.382) += (0, 0.0) -= (0, 0.0)
(1.053, 2.367) += (0, 0.0) -= (0, 0.0)
(1.040, 2.351) += (0, 0.015) -= (0, 0.016)
(1.027, 2.340) += (0, 0.023) -= (0, 0.023)
(1.015, 2.328) += (0, 0.015) -= (0, 0.015)
%(1.004, )
(0.994, 2.321) += (0, 0.028) -= (0, 0.028)
(0.985, 2.306) += (0, 0.018) -= (0, 0.018)
(0.977, 2.301) += (0, 0.023) -= (0, 0.023)
};


%Bond Distances Ln-N (Expt)
\addplot [color = blue, dashed, mark size=5pt, mark= o,mark options={solid}, draw = blue, line width = 1.2 pt] coordinates {
(1.066, 2.550)
(1.053, 2.530)
(1.040, 2.520)
(1.027, 2.510)
(1.015, 2.490)
(1.004, 2.480)
(0.985, 2.460) 
};

%Bond Distances Ln-O (Expt)
\addplot [color = red, dashed, mark size=5pt, mark= square ,mark options={solid}, draw = red, line width = 1.2 pt] coordinates {
(1.066, 2.350) 
(1.053, 2.340)
(1.040, 2.330)
(1.027, 2.310)
(1.015, 2.310)
(1.004, 2.290)
(0.985, 2.270)
};

%Adding cations labels
%La
\addplot[black,line width=0.7mm,line legend,sharp plot] coordinates{ (1.160, 2.700)} node[above,font=\sffamily]{La} ;
%Ce
\addplot[black,line width=0.7mm,line legend,sharp plot] coordinates{ (1.143, 2.665)} node[below,font=\sffamily]{Ce} ;
%Pr
\addplot[black,line width=0.7mm,line legend,sharp plot] coordinates{ (1.126, 2.651)} node[above,font=\sffamily]{Pr} ;
%Nd
\addplot[black,line width=0.7mm,line legend,sharp plot] coordinates{ (1.114, 2.58)} node[above,font=\sffamily]{Nd} ;
%Pm
\addplot[black,line width=0.7mm,line legend,sharp plot] coordinates{ (1.093, 2.49)} node[above,font=\sffamily]{Pm} ;
%Sm
\addplot[black,line width=0.7mm,line legend,sharp plot] coordinates{ (1.079, 2.610)} node[above,font=\sffamily]{Sm} ;
%Eu
\addplot[black,line width=0.7mm,line legend,sharp plot] coordinates{ (1.066, 2.540)} node[below,font=\sffamily]{Eu} ;
%Gd
\addplot[black,line width=0.7mm,line legend,sharp plot] coordinates{ (1.053, 2.520)} node[below,font=\sffamily]{Gd} ;
%Tb
\addplot[black,line width=0.7mm,line legend,sharp plot] coordinates{ (1.040, 2.565)} node[above,font=\sffamily]{Tb} ;
%Dy
\addplot[black,line width=0.7mm,line legend,sharp plot] coordinates{ (1.027, 2.550)} node[above,font=\sffamily]{Dy} ;
%Ho
\addplot[black,line width=0.7mm,line legend,sharp plot] coordinates{ (1.015, 2.480)} node[below,font=\sffamily]{Ho} ;
%Er
\addplot[black,line width=0.7mm,line legend,sharp plot] coordinates{ (1.004, 2.480)} node[above,font=\sffamily]{Er} ;
%Tm
\addplot[black,line width=0.7mm,line legend,sharp plot] coordinates{ (0.994, 2.464)} node[below,font=\sffamily]{Tm} ;
%Yb
\addplot[black,line width=0.7mm,line legend,sharp plot] coordinates{ (0.985, 2.520)} node[above,font=\sffamily]{Yb} ;
%Lu
\addplot[black,line width=0.7mm,line legend,sharp plot] coordinates{ (0.969, 2.490)} node[below,font=\sffamily]{Lu} ;


%Adding trend lines for each bond distance plot.
 %Ln-N distance trend line
\draw [color = black, line width = 1.5pt] (1.17, 2.699231) -- (0.96, 2.475728) ;
 %Ln-O distance trend line 
\draw [color = black, line width = 1.5pt] (1.17, 2.469044) -- (0.96, 2.283572) ;

%Adding R^2
%Ln-N (DFT) R^2
\addplot[black,line width=0.7mm,line legend,sharp plot] coordinates{ (0.99, 2.65)} node[above,font=\sffamily]{\color{blue}R$^2$=0.9895  } ;
%Ln-O (DFT) R^2
\addplot[black,line width=0.7mm,line legend,sharp plot] coordinates{ (0.99, 2.21)} node[above,font=\sffamily]{\color{red}R$^2$=0.9922  } ;

\legend{Ln--N (DFT), Ln--O (DFT), Ln--N (Expt), Ln--O (Expt)}
\end{axis}

\end{tikzpicture}
\end{document}
```

</details>

> Since I started using multireference methods to study transition metal, lanthanide, and actinide complexes, I am using relative energy plots to visually assess the ground state and the excited state manifolds of such complexes. I found particularly very useful these kind of plots to decide the number of spin-states when I cannot include all spin states and I need to truncate the expensive calculations. In the following example I plotted 5 quintets, 44 triplets, and 50 singlets states of an Fe(IV) complex I studied [here](https://doi.org/10.1039/D4SC04880F) with many multireference methods, but in this plot I am showing relative NEVPT2 energies.

{{< img src="spin-states_energy-ladder.png"  width="300" align="center" title="Relative energies plot" >}}

<details >
<summary> Check code </summary>

```
\documentclass[tikz,border=1mm]{standalone}
\usepackage{amsmath}
\usepackage{siunitx}
\usepackage[version=3]{mhchem}

% Paquetes TikZ
\usepackage{pgfplots}
\pgfplotsset{compat=1.11}
\usepgfplotslibrary{groupplots}
\pgfplotsset{compat=newest}
\usetikzlibrary{plotmarks}
\usepgflibrary{plotmarks}
\usetikzlibrary{arrows.meta}

\begin{document}
\begin{tikzpicture}
  \begin{axis}[
    height = 15cm,
    width  = 7cm,
    x tick label style={/pgf/number format/1000 sep=},
    xticklabel style={rotate=0}, %rotate labels in x axis 
    yticklabel style={ /pgf/number format/.cd, fixed, fixed zerofill, precision=1 },
    every outer y axis line/.append style={-{Classical TikZ Rightarrow[length=1.3mm]}},
    ylabel={$E$   (eV)},
    x axis line style = { opacity = 0.5 },
    ymax = 20.0,
    xtick={Quintet,Triplet,Singlet},
    axis x line       = bottom,
    axis y line       = left,
    tickwidth         = 2pt,
    enlarge x limits  = 0.15,
    enlarge y limits  = 0.02,
    symbolic x coords = {Quintet,Triplet,Singlet},
    legend style={at={(0.5,0.93)}, anchor=north,legend columns=3, legend cell align={left}},
  ] 
%SA(5 quintets)-NEVPT2
\addplot[color = blue, only marks, mark= -, mark size=12pt, line width=1.0pt ] coordinates {
(Quintet, 5.811)
(Quintet, 7.126)
(Quintet, 7.707)
(Quintet, 11.263)
(Quintet, 11.634)
};

%SA(45 triplets)-NEVPT2
\addplot[color = blue, only marks, mark = -, mark size=12pt, line width=1.0pt] coordinates {
(Triplet, 3.847) 
(Triplet, 4.418)
(Triplet, 7.440)
(Triplet, 7.641)
(Triplet, 7.724)
(Triplet, 4.680)
(Triplet, 4.874)
(Triplet, 8.143)
(Triplet, 8.391)
(Triplet, 8.388)
(Triplet, 10.494)
(Triplet, 10.567)
(Triplet, 6.527)
(Triplet, 9.768)
(Triplet, 9.854)
(Triplet, 9.347)
(Triplet, 9.884) 
(Triplet, 10.068)
(Triplet, 10.067)
(Triplet, 7.147)
(Triplet, 9.604)
(Triplet, 11.939) 
(Triplet, 11.055)
(Triplet, 10.431)
(Triplet, 12.847)
(Triplet, 10.545)
(Triplet, 11.329)
(Triplet, 12.637)
(Triplet, 13.062)
(Triplet, 13.211)
(Triplet, 13.153)
(Triplet, 13.316)
(Triplet, 13.379)
(Triplet, 13.306)
(Triplet, 12.972)
(Triplet, 13.409)
(Triplet, 13.841)
(Triplet, 14.835)
(Triplet, 12.357)
(Triplet, 14.876)
(Triplet, 14.883)
(Triplet, 15.201)
(Triplet, 16.358)
(Triplet, 18.236)
(Triplet, 16.478)
};

%SA(50 singlets)-NEVPT2
\addplot[color = blue, only marks, mark = -, mark size=12pt, line width=1.0pt] coordinates {
(Singlet, 5.191) 
(Singlet, 4.663)
(Singlet, 0.000)
(Singlet, 8.458)
(Singlet, 8.070)
(Singlet, 8.774)
(Singlet, 6.438)
(Singlet, 5.971)
(Singlet, 9.145)
(Singlet, 9.289)
(Singlet, 9.717)
(Singlet, 11.066)
(Singlet, 9.960)
(Singlet, 11.352)
(Singlet, 5.872)
(Singlet, 10.369) 
(Singlet, 10.581)
(Singlet, 11.513)
(Singlet, 10.981)
(Singlet, 11.729)
(Singlet, 12.318)
(Singlet, 12.777)
(Singlet, 11.156)
(Singlet, 11.547)
(Singlet, 10.627)
(Singlet, 13.398)
(Singlet, 11.752)
(Singlet, 12.042)
(Singlet, 13.551)
(Singlet, 12.168)
(Singlet, 13.069)
(Singlet, 13.426)
(Singlet, 13.764)
(Singlet, 13.934)
(Singlet, 13.676)
(Singlet, 13.816)
(Singlet, 14.561)
(Singlet, 14.427)
(Singlet, 15.567)
(Singlet, 15.748)
(Singlet, 14.550)
(Singlet, 15.907)
(Singlet, 15.884)
(Singlet, 13.979)
(Singlet, 18.326)
(Singlet, 17.268)
(Singlet, 17.390)
(Singlet, 16.798)
(Singlet, 18.899)
(Singlet, 18.210)
};

\legend{NEVPT2}
\end{axis}

\end{tikzpicture}
\end{document}
```

</details>


> I am very proud of this plot, where I am including the frontier molecular orbitals of a series of [Uranium (III) bisdicarbollide complexes]() I studied with collaboratoris in Prof. Omar Farha's group. Unfortunately, this plot was not included in the final manuscript and supporting information, but it was an amazing \TikZ / $\LaTeX$ coding experience. 

{{< img src="diagram_homo-lumo_sarc-dkh_b3lyp.png"  width="600" align="center" title="Uranium III FMOs" >}}

<details >
<summary> Check code </summary>

```
\documentclass[tikz,border=1mm]{standalone}
\usepackage{amsmath}
\usepackage{siunitx}
\usepackage[version=3]{mhchem}

% Paquetes TikZ
\usepackage{tikz-dimline}
\usepackage{pgfplots}
\pgfplotsset{compat=newest}
\usepgfplotslibrary{groupplots}
\usetikzlibrary{plotmarks}
\usepgflibrary{plotmarks}
\usetikzlibrary{arrows.meta}

\begin{document}
\begin{tikzpicture}
  \begin{axis}[
    height = 12cm,
    width  = 10cm,
    x tick label style = {/pgf/number format/1000 sep=},
    xticklabel style   = {rotate=0},
    yticklabel style={
        /pgf/number format/fixed,
        /pgf/number format/fixed zerofill,
        /pgf/number format/precision=1,
    },
    scaled y ticks = false,
    every outer y axis line/.append style={
        -{Classical TikZ Rightarrow[length=1.3mm]}
    },
    ylabel        = {$\Delta E$ (eV)},
    x axis line style = {opacity=0.5},
    ymax =  4.5,
    ymin = -2.2,
    axis x line   = bottom,
    axis y line   = left,
    tickwidth     = 2pt,
    enlarge x limits = 0.15,
    enlarge y limits = 0.02,
    % FIX 1: el paréntesis en "2U-(CF3)2" confunde al parser de coordenadas
    % de TikZ. Se reemplaza por un nombre sin paréntesis y se usa xticklabels
    % para mostrar el texto con formato correcto.
    symbolic x coords = {2U-H, 2U-Ph, 2U-Cl, 2U-CF3, 2U-CF32},
    xtick         = {2U-H, 2U-Ph, 2U-Cl, 2U-CF3, 2U-CF32},
    xticklabels   = {2U-H, 2U-Ph, 2U-Cl,
                     2U-CF$_3$, 2U-(CF$_3$)$_2$},
    legend style  = {
        at          = {(0.5,1.10)},
        anchor      = north,
        legend columns = 2,
        legend cell align = left,
    },
  ]

% --- 2U-H (rojo) ---
\addplot[color=red, only marks, mark=-, mark size=12pt, line width=1.0pt]
    coordinates {
    (2U-H,  3.7035)
    (2U-H,  3.6137)
    (2U-H,  3.4803)
    (2U-H,  3.3388)
    (2U-H,  0.0000)
    (2U-H, -0.0898)
    (2U-H, -0.1279)
    (2U-H, -1.8912)
    };

% --- 2U-Ph (azul) ---
\addplot[color=blue, only marks, mark=-, mark size=12pt, line width=1.0pt]
    coordinates {
    (2U-Ph,  3.6980)
    (2U-Ph,  3.6790)
    (2U-Ph,  3.6354)
    (2U-Ph,  3.2871)
    (2U-Ph,  0.0000)
    (2U-Ph, -0.0844)
    (2U-Ph, -0.1225)
    (2U-Ph, -1.7769)
    };

% --- 2U-Cl (verde) ---
\addplot[color=green, only marks, mark=-, mark size=12pt, line width=1.0pt]
    coordinates {
    (2U-Cl,  3.4776)
    (2U-Cl,  3.4259)
    (2U-Cl,  3.3579)
    (2U-Cl,  3.2490)
    (2U-Cl,  0.0000)
    (2U-Cl, -0.0925)
    (2U-Cl, -0.1252)
    (2U-Cl, -1.7851)
    };

% --- 2U-CF3 (naranja) ---
\addplot[color=orange, only marks, mark=-, mark size=12pt, line width=1.0pt]
    coordinates {
    (2U-CF3,  3.4722)
    (2U-CF3,  3.3443)
    (2U-CF3,  3.0096)
    (2U-CF3,  2.9307)
    (2U-CF3,  0.0000)
    (2U-CF3, -0.0163)
    (2U-CF3, -0.1061)
    (2U-CF3, -1.8340)
    };

% --- 2U-(CF3)2 (negro) — nombre interno: 2U-CF32 ---
\addplot[color=black, only marks, mark=-, mark size=12pt, line width=1.0pt]
    coordinates {
    (2U-CF32,  2.9007)
    (2U-CF32,  2.8545)
    (2U-CF32,  2.5470)
    (2U-CF32,  2.5334)
    (2U-CF32,  0.0000)
    (2U-CF32, -0.0925)
    (2U-CF32, -0.1197)
    (2U-CF32, -1.9075)
    };

% --- alpha-HOMO labels ---
\node[above, font=\bfseries\sffamily\footnotesize]
    at (axis cs:2U-H,     0.00) {$\alpha$-HOMO};
\node[above, font=\bfseries\sffamily\footnotesize]
    at (axis cs:2U-Ph,    0.00) {$\alpha$-HOMO};
\node[above, font=\bfseries\sffamily\footnotesize]
    at (axis cs:2U-Cl,    0.00) {$\alpha$-HOMO};
\node[above, font=\bfseries\sffamily\footnotesize]
    at (axis cs:2U-CF3,   0.00) {$\alpha$-HOMO};
\node[above, font=\bfseries\sffamily\footnotesize]
    at (axis cs:2U-CF32,  0.00) {$\alpha$-HOMO};

% --- alpha-HOMO-3 labels ---
\node[above, font=\bfseries\sffamily\footnotesize]
    at (axis cs:2U-H,     -1.8912) {$\alpha$-HOMO-3};
\node[above, font=\bfseries\sffamily\footnotesize]
    at (axis cs:2U-Ph,    -1.7769) {$\alpha$-HOMO-3};
\node[above, font=\bfseries\sffamily\footnotesize]
    at (axis cs:2U-Cl,    -1.7851) {$\alpha$-HOMO-3};
\node[above, font=\bfseries\sffamily\footnotesize]
    at (axis cs:2U-CF3,   -1.8340) {$\alpha$-HOMO-3};
\node[above, font=\bfseries\sffamily\footnotesize]
    at (axis cs:2U-CF32,  -1.9075) {$\alpha$-HOMO-3};

% --- alpha-LUMO labels ---
\node[below, font=\bfseries\sffamily\footnotesize]
    at (axis cs:2U-H,     3.3388) {$\alpha$-LUMO};
\node[below, font=\bfseries\sffamily\footnotesize]
    at (axis cs:2U-Ph,    3.2871) {$\alpha$-LUMO};
\node[below, font=\bfseries\sffamily\footnotesize]
    at (axis cs:2U-Cl,    3.2490) {$\alpha$-LUMO};
\node[below, font=\bfseries\sffamily\footnotesize]
    at (axis cs:2U-CF3,   2.9307) {$\alpha$-LUMO};
\node[below, font=\bfseries\sffamily\footnotesize]
    at (axis cs:2U-CF32,  2.5334) {$\alpha$-LUMO};

% --- alpha-LUMO+3 labels ---
\node[above, font=\bfseries\sffamily\footnotesize]
    at (axis cs:2U-H,     3.7035) {$\alpha$-LUMO+3};
\node[above, font=\bfseries\sffamily\footnotesize]
    at (axis cs:2U-Ph,    3.6980) {$\alpha$-LUMO+3};
\node[above, font=\bfseries\sffamily\footnotesize]
    at (axis cs:2U-Cl,    3.4776) {$\alpha$-LUMO+3};
\node[above, font=\bfseries\sffamily\footnotesize]
    at (axis cs:2U-CF3,   3.4722) {$\alpha$-LUMO+3};
\node[above, font=\bfseries\sffamily\footnotesize]
    at (axis cs:2U-CF32,  2.9007) {$\alpha$-LUMO+3};

% =========================================================
% FIX 2: \dimline necesita coordenadas TikZ simples.
% Se definen con \coordinate (dentro del entorno axis, que
% permite axis cs:) y luego se pasan a \dimline.
% =========================================================
% Flechas de acotación dibujadas manualmente con TikZ puro.
% Se usan coordenadas axis cs: directamente dentro del axis.
% El estilo "gapArrow" define una flecha de doble punta sin extensiones.
\tikzset{
  gapArrow/.style={
    -{Bar[width=4pt]}, % punta: barra vertical
    shorten >=0pt,
    shorten <=0pt,
    line width=0.6pt,
  },
  gapLabel/.style={
    font=\footnotesize,
    fill=white,
    inner sep=1pt,
  },
}

% Macro auxiliar: \drawgap{xcoord}{ybot}{ytop}{label}
\newcommand{\drawgap}[4]{%
  \draw[{Bar[width=4pt]}-{Bar[width=4pt]}, line width=0.6pt]
      (axis cs:#1,#2) -- (axis cs:#1,#3)
      node[midway, right, font=\footnotesize, fill=white, inner sep=1pt, rotate=90] {#4};
}

\drawgap{2U-H}{0.25}{3.10}{3.34 eV}
\drawgap{2U-Ph}{0.25}{3.00}{3.29 eV}
\drawgap{2U-Cl}{0.25}{2.95}{3.25 eV}
\drawgap{2U-CF3}{0.25}{2.65}{2.93 eV}
\drawgap{2U-CF32}{0.25}{2.30}{2.53 eV}

  \end{axis}

\end{tikzpicture}
\end{document}

```

</details>

> So far, I think you already noticed that the data I want to plot is included using the format `(x,y)`. This is fine when the number of data points is small. However, when plotting hundreds or thousands of points, the `.tex` file turns tedious and incredibly large. In these situations, it is better to plot the data written into a `.txt` or `.dat` file (I usually use these extensions). To do that, check the next example where I plot the absorption and emission spectra of an Americium (III) complex with their respective oscillator strengths. 

{{< img src="americium_spectra.png"  width="600" align="center" title="Absorption/Emission Spectra of Am(H2O)9" >}}

<details >
<summary> Check code </summary>

```
\documentclass[tikz,border=1mm]{standalone}
\usepackage{amsmath}
\usepackage{siunitx}
\usepackage[version=3]{mhchem}

% Paquetes TikZ
\usepackage{pgfplots}
\pgfplotsset{compat=newest}
\usepgfplotslibrary{groupplots}
\usetikzlibrary{plotmarks}
\usepgflibrary{plotmarks}
\usetikzlibrary{arrows.meta}

\begin{document}
\begin{tikzpicture}
\LARGE

% =========================================================
% EJE PRINCIPAL (izquierdo): Espectros de absorción/emisión
% =========================================================
  \begin{axis}[
    name   = main axis,       % <-- nombre para referenciar después
    height = 12cm,
    width  = 18cm,
    x tick label style = {/pgf/number format/1000 sep=},
    xticklabel style   = {rotate=0},
    % Formato eje y izquierdo
    yticklabel style={
        /pgf/number format/fixed,
        /pgf/number format/fixed zerofill,
        /pgf/number format/precision=1,
    },
    %scaled y ticks = false,
    every outer y axis line/.append style={
        -{Classical TikZ Rightarrow[length=1.3mm]}
    },
    % Etiquetas
    ylabel = {Intensity (a.u.)},
    xlabel = {Wavelength (nm)},
    % Rango de ejes
    x axis line style = {opacity=0.5},
    ymin =  0.0,
    xmin =  200,
    xmax = 1600,
    xtick distance = 200,
    % Estilo de ejes
    axis x line = bottom,
    axis y line = left,
    tickwidth   = 2pt,
    % Márgenes
    enlarge x limits = 0.01,
    enlarge y limits = {0.04, upper},
    % Leyenda
    legend style = {
        at            = {(0.78, 0.99)},
        anchor        = north,
        legend columns = 1,
        legend cell align = left,
    },
  ]

  % --- Absorción ---
  \addplot[
      smooth, color = red,
      line width = 1.5pt,
  ] file {rassi_am9w_caspt2_sa_7-31_SO_absorption_spectrum_nm.dat};
  \addlegendentry{Abs (7Sept+31Quint)}

  % --- Emisión ---
  \addplot[
      smooth, color = blue, solid,
      line width = 1.5pt,
  ] file {rassi_am9w_caspt2_sa_7-31_SO_emission_spectrum_nm.dat};
  \addlegendentry{Em (7Sept+31Quint)}

  % --- Experimento (comentado) ---
  %\addplot[black, solid, line width=2.0pt]
  %    file{am9w_expt_nm.dat};
  %\addlegendentry{Experiment}

  \end{axis}

% =========================================================
% EJE SECUNDARIO (derecho): Fuerza del oscilador (f)
% =========================================================
% Estructura del archivo .dat esperada:
%   columna 1: longitud de onda (nm)
%   columna 2: fuerza del oscilador (f)
%
% Ejemplo de contenido del archivo:
%   350.0   0.0023
%   420.5   0.0150
%   580.2   0.0004
%   750.0   0.0310
%   ...
% =========================================================
  \begin{axis}[
    % ---------------------------------------------------
    % Comparte exactamente el mismo espacio que el eje principal
    % ---------------------------------------------------
    at     = {(main axis.south west)},   % misma posición
    anchor = south west,
    height = 12cm,
    width  = 18cm,
    % ---------------------------------------------------
    % Mismo rango x que el eje principal
    % ---------------------------------------------------
    xmin = 200,
    xmax = 1600,
    xtick distance = 200,
    % ---------------------------------------------------
    % Eje x: completamente oculto (ya lo muestra el eje principal)
    % ---------------------------------------------------
    axis x line   = none,
    xtick         = \empty,
    xticklabels   = \empty,
    xlabel        = {},
    % ---------------------------------------------------
    % Eje y DERECHO: fuerza del oscilador
    % ---------------------------------------------------
    axis y line*  = right,               % <-- eje y a la derecha
    ylabel        = {Oscillator strength $f$},
    %ylabel style  = {
    %    at        = {(ticklabel* cs:1.02)},
    %    anchor    = south,
    %    rotate    = -90,
    %},
    % Formato del eje y derecho (3 decimales para f)
    yticklabel style = {
        /pgf/number format/fixed,
        /pgf/number format/fixed zerofill,
        /pgf/number format/precision=1,
    },
    %scaled y ticks = false,
    every outer y axis line/.append style={
        -{Classical TikZ Rightarrow[length=1.3mm]}
    },
    ymin = 0.0,
    ymax = 20E-5,
    % ---------------------------------------------------
    % Estilo de las barras
    % ---------------------------------------------------
    ycomb,                               % <-- barras verticales delgadas
    enlarge x limits = 0.01,
    enlarge y limits = {0.04, upper},
    tickwidth = 2pt,
    % ---------------------------------------------------
    % Leyenda del eje secundario (se añade a la del principal)
    % ---------------------------------------------------
    legend style = {
        at             = {(0.78, 0.99)},
        anchor         = north,
        legend columns = 1,
        legend cell align = left,
    },
    clip = false,
  ]

  % --- Barras de fuerza del oscilador (Absorción) ---
  \addplot[
      ycomb,                             % barras verticales
      color     = red!60!white,
      line width = 1.2pt,                % grosor de cada barra
  ] file {abs_oscillators.dat};
  %\addlegendentry{$f$ Abs}

  % --- Barras de fuerza del oscilador (Emisión) ---
  % (Descomentar si se tienen datos de emisión)
  \addplot[
      ycomb,
      color     = blue!60!white,
      line width = 1.2pt,
  ] file {ems_oscillators.dat};
  %\addlegendentry{$f$ Em}
  \end{axis}

\end{tikzpicture}
\end{document}

```
</details>




