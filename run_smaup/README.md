<img src="../data/figs/rise_logo.png" alt="Estructura Carpeta" align="center">

## Run the S-maup Test in different programming languages


Juan C. Duque<sup>1,2</sup>, Henry Laniado<sup>1</sup>, Adriano Polo<sup>2,3</sup>

<sup>1</sup> Department of Mathematical Sciences, Universidad EAFIT, Medellin, Colombia

<sup>2</sup> RiSE-group, Universidad EAFIT, Medellin, Colombia

<sup>3</sup> Department of Economics, Universidad EAFIT, Medellin, Colombia


__maintainer__ = "RiSE Group"  (http://www.rise-group.org/). Universidad EAFIT

__Corresponding author__ = jduquec1@eafit.edu.co (JCD)


### Description

Download the S-maup test in different languages! (Matlab, R and Python)

#### INPUTS:
	N = Number of areas
	k = Number of regions
	rhoEst = level of spatial autocorrelation
#### OUTPUT:
	It returns the S-maup statistical, print the decision to reject or not to reject the null hypothesis
	and print the level of significance for the decision.


### Matlab Users

	>> N = 25
	>> k = 10
	>> rhoEst = 0.8
	>> Smaup = testSmaup(N, k, rhoEst)   %%%Atlernative: Smaup = testSmaup(N, k, rhoEst)
	==========================
	Estadistico M =0.12191
	Pseudo p_value > 0.10 
	H0 is not rejected
	==========================

### R Users
   			   
	> N <- 865
	> k <- 90
	> rhoEst <- 0.801
	> Smaup <- testSmaup(N, k, rhoEst)   ### Alternative: Smaup <- testSmaup(865, 90, 0.801)
	================================
	Statistic M = 0.366546071907841 
	Pseudo p_value < 0.05 **
	H0 is rejected
	================================

### Python Users
   			   
	In [1]: N = 865
	   ...:	k = 90 
	   ...:	rhoEst = 0.801
	   ...: Smaup = testSmaup(N, k, rhoEst) ### Alternative: Smaup <- testSmaup(865, 90, 0.801)
	====================================
	Statistic M =  0.3665460719078407
	Pseudo p-value < 0.05 **
	H0 is rejected
	====================================

