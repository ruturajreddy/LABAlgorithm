# LAB : a leader–advocate–believer-based optimization algorithm
Reddy, R., Kulkarni, A.J., Krishnasamy, G., Shastri, A. S., Gandomi, A. H. (2023): LAB : a leader–advocate–believer-based optimization algorithm. Soft Computing (2023). https://doi.org/10.1007/s00500-023-08033-y

------
## Abstract

- a new socio-inspired metaheuristic technique for engineering and global optimization problems
- inspired by the AI-based competitive behaviour exhibited by the individuals in a group while simultaneously improving themselves and establishing a role
  - Leader, Advocate and Believer

<p align="center" width="100%">
  <img src="https://github.com/ruturajreddy/LAB-A-leader-advocate-believer-based-optimization-algorithm/blob/main/Files/Visualrepresentation.png" width=75% height=75% alt="matyas">  
</p>

- validated using the CEC 2005 (27 test problems) and CEC 2017 (29 test problems) benchmark functions
  - statistical tests used : the Wilcoxon pairwise and two-sided test as well as the Friedman Rank Test
    - results compared with other algorithms such as _FA, CI, GA, SA, PSO, Multi-CI, CMAES, ABC, SADE, CLPSO, BSA, IA, WOA, SHO, AVOA, LSHADE-Cn-EpsiN, FDB-SFS_ and _LSHADE_

- applied to solve engineering problems
  - abrasive water jet machining
  - electric discharge machining
  - micro-machining processes
    - outperformed _SA_, $f_{best}$ and $f_{better}$ by achieving 76%, 85% and 75% minimization of $R_a$ respectively for micro-milling with 0.7 mm tool diameter
    - achieved 81%, 72%, 85% minimization of Ra when compared to SA, $f_{best}$ and $f_{better}$ for 1 mm tool diameter
    - achieved 24% and 34% minimization of $B_h$ and $B_t$ as compared to SA for micro-drilling with a tool diameter 0.5 mm
    - for tool diameters 0.8 mm and 0.9 mm, 16% and 3% minimization of $B_t$, respectively, were achieved as compared to SA
  - turning of titanium alloy in a minimum quantity lubrication environment
- **results from this study highlighted that the LAB outperforms the other algorithms in terms of function evaluations and computational time**

## Flowchart
<p align="center" width="100%">
  <img src="https://github.com/ruturajreddy/LAB-A-leader-advocate-believer-based-optimization-algorithm/blob/main/Files/Flowchartpng.png" width="30%" height="30%" alt="flowchart">  
</p>

------

## CEC 2005 Functions
<p align="center" width="100%">
  <img src="https://github.com/ruturajreddy/LAB-A-leader-advocate-believer-based-optimization-algorithm/blob/main/Files/convergenceplots2005.png" alt="booth">  
</p>

#### Wilcoxon pairwise test (CEC 2005)
<p align="center" width="100%">
  <img src="https://github.com/ruturajreddy/LAB-A-leader-advocate-believer-based-optimization-algorithm/blob/main/Files/pairwise.png" alt="sixhump">  
</p>


#### Friedman Test Ranks (CEC 2005)
<p align="center" width="100%">
  <img src="https://github.com/ruturajreddy/LAB-A-leader-advocate-believer-based-optimization-algorithm/blob/main/Files/FriedmanTest.png" alt="sixhump">  
</p>

## CEC 2017 Functions
<p align="center" width="100%">
  <img src="https://github.com/ruturajreddy/LAB-A-leader-advocate-believer-based-optimization-algorithm/blob/main/Files/convergenceplots2017.png" alt="2017ConvergencePlots">  
</p>

#### Friedman Test Ranks (CEC 2017)
<p align="center" width="100%">
  <img src="https://github.com/ruturajreddy/LAB-A-leader-advocate-believer-based-optimization-algorithm/blob/main/Files/friedman2017.png" alt="sixhump">  
</p>


------
## Conclusions
- examined by solving 27 benchmark test problems from CEC 2005
  - a statistical comparison using the Wilcoxon-signed rank test
    - able to perform slightly better when compared in terms of best solution, mean solution, robustness and computational time when compared to CMAES and IA and was able to outperform PSO2011, CMAES, ABC, JDE, CLPSO, and SADE in computational time
    - LAB demonstrated low robustness but exceedingly low computational time
  - Friedman test by solving 29 benchmark functions from CEC 2017
    - was also able to solve complex problems with lower standard deviations as compared to _LSHADE-Cn-EpsiN_ and _LSHADE_
  - also validated by solving 23 real-world problems to compare exploitation, exploration, computation cost and convergence rate with other well-known and recent algorithms
    - _experimental (Kechigas, 2012), regression (Kechigas, 2012), FA, variations of CI (roulette wheel_, $f_{best}$, $f_{better}$, _alienation), GA, SA, PSO, Multi-CI_
    - run time is quite lower as compared to other algorithms for majority of the problems
    - resulted in higher standard deviation which exhibited its low robustness
 
----
## Future Work
- **enhancements can be done for better and faster computation to solve complex and higher dimension problems easily,**
  - **by introducing a method of triggering the algorithm when stuck at local minima to solve a wider range of higher-dimension complex real-life problems**
- **can be modified to solve multi-objective problems making the competitive groups to handle different objectives**
