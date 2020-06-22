# Linear Programming in Python
#### Solving optimization problems using the [PuLP](https://github.com/coin-or/pulp) Python library.  

[Transshipment Example](https://github.com/c-jg/linear-programming/blob/master/solutions/SAS.py):

<img src="https://cguer.s3.amazonaws.com/Figure_1.png">

<img src="https://latex.codecogs.com/svg.latex?Min~25x_{14}&plus;25x_{15}&plus;25x_{16}~\cdots~&space;27.5x_{78}&plus;25x_{79}&plus;42.5x_{710}\\&space;\\&space;~~~~~~s.t.~x_{14}&plus;x_{15}&plus;x_{16}&plus;x_{17}\leq&space;350\\&space;~~~~~~~~~~~x_{24}&plus;x_{25}&plus;x_{26}&plus;x_{27}\leq&space;350\\&space;~~~~~~~~~~~x_{34}&plus;x_{35}&plus;x_{36}&plus;x_{37}\leq&space;700\\&space;~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\vdots&space;\\&space;~~~~~~~~~~~x_{49}&plus;x_{59}&plus;x_{69}&plus;x_{79}=&space;500\\&space;~~~~~~~~~~~x_{410}&plus;x_{510}&plus;x_{610}&plus;x_{710}=&space;650\\&space;~~~~~~~~~~~x_{ij}\geq&space;0&space;~~~&space;for~all~i~and~j" title="Min~25x_{14}+25x_{15}+25x_{16}~\cdots~ 27.5x_{78}+25x_{79}+42.5x_{710}\\ \\ ~~~~~~s.t.~x_{14}+x_{15}+x_{16}+x_{17}\leq 350\\ ~~~~~~~~~~~x_{24}+x_{25}+x_{26}+x_{27}\leq 350\\ ~~~~~~~~~~~x_{34}+x_{35}+x_{36}+x_{37}\leq 700\\ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\vdots \\ ~~~~~~~~~~~x_{49}+x_{59}+x_{69}+x_{79}= 500\\ ~~~~~~~~~~~x_{410}+x_{510}+x_{610}+x_{710}= 650\\ ~~~~~~~~~~~x_{ij}\geq 0 ~~~ for~all~i~and~j" />

Currently working on the following types of problems:
* Transportation
* Blending
* Transshipment
* Assignment
* Shortest Route
* Maximal Flow

Graphics built using [Networkx](https://github.com/networkx/networkx)
