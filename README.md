
<img src="figs/rise_logo.png" alt="Estructura Carpeta" width="300" height="300" align="left">

## S-maup: Statistical Test to Measure the Sensitivity to the Modifiable Areal Unit Problem


Juan C. Duque<sup>1,2</sup>, Henry Laniado<sup>1</sup>, Adriano Polo<sup>2,3</sup>


<sup>1</sup> Department of Mathematical Sciences, Universidad EAFIT, Medellin, Colombia

<sup>2</sup> RiSE-group, Universidad EAFIT, Medellin, Colombia

<sup>3</sup> Department of Economics, Universidad EAFIT, Medellin, Colombia


__maintainer__ = "RiSE Group"  (http://www.rise-group.org/). Universidad EAFIT

__Corresponding author__ = jduquec1@eafit.edu.co (JCD)

### Abstract 

This work presents a nonparametric statistical test, S-maup, to measure the sensitivity of a spatially intensive variable to the effects of the Modifiable Areal Unit Problem (MAUP). To the best of our knowledge, S-maup is the first statistic of its type and focuses on determining how much the distribution of the variable, at its highest level of spatial disaggregation, will change when it is spatially aggregated.  Through a computational experiment, we obtain the basis for the design of the statistical test under the null hypothesis of non-sensitivity to MAUP.  We performed an exhaustive simulation study for approaching the empirical distribution of the statistical test, obtaining its critical values, and computing its power and size. The results indicate that, in general, both the statistical size and power improve with increasing sample size. Finally, for illustrative purposes, an empirical application is made using the Mincer equation in South Africa, where starting from 206 municipalities, the S-maup statistic is used to find the maximum level of spatial aggregation that avoids the negative consequences of the MAUP.

```tex
@article{XX,
    author = {Duque, Juan C. AND Laniado, H. AND Polo, A.},
    journal = {PLOS ONE},
    publisher = {Public Library of Science},
    title = {S-maup: Statistical Test to Measure the Sensitivity to the Modifiable Areal Unit Problem},
    year = {2018},
    month = {mm},
    volume = {vv},
    url = {xx},
    pages = {1-25},
    abstract = {This work presents a nonparametric statistical test,  S-maup, to measure the sensitivity of a spatially intensive variable to the effects of the Modifiable Areal Unit Problem (MAUP). To the best of our knowledge,  S-maup is the first statistic of its type and focuses on determining how much the distribution of the variable, at its highest level of spatial disaggregation, will change when it is spatially aggregated. Through a computational experiment, we obtain the basis for the design of the statistical test under the null hypothesis of non-sensitivity to MAUP. We performed an exhaustive simulation study for approaching the empirical distribution of the statistical test, obtaining its critical values, and computing its power and size. The results indicate that, in general, both the statistical size and power improve with increasing sample size. Finally, for illustrative purposes, an empirical application is made using the Mincer equation in South Africa, where starting from 206 municipalities, the  S-maup statistic is used to find the maximum level of spatial aggregation that avoids the negative consequences of the MAUP.},
    number = {nn},
    doi = {xx}
}
```

# Computational Experiment on MAUP effects

<img src="figs/scheme.png" alt="Estructura Carpeta" align="center">

**Folder** | **Table** | **Figure**
  ----------------- | ---------------------------- | -----------------------------------------------
  [1_SAR_realizations](1_SAR_realizations)| - |-
  [2_Spatial_aggregations](2_Spatial_aggregations)| - |-
  [3_MAUP_effects](3_MAUP_effects)|-  | Figure 3, Figure 4
  [4_t_tests](4_t_tests)| Table 2 |-
  [5_Levene_tests](5_Levene_tests)| - | Figure 5
  [6_median_RCM](6_median_RCM)| - | Figure 7
  [7_Adjustments_of_robust_linear_regression_models](7_Adjustments_of_robust_linear_regression_models)|- | Figure 8
  [8_critical values](8_critical values)| Table 3  |-
  [9_power](9_power)| Table 5 |-
  [10_size](10_size)| Table 6 |-
  [11_application](11_application)| Table 7, Table 8, Table 9 |Figure 9, Figure 10, Figure 11



## Folder: <span style="color:red">1_SAR_realizations</span>

**Variable name** | **Description**
  ----------------- | -------------------------------------------------------------------------
  `ID`       | `Area ID`
  `SAR1_0.9`      | `First realization of a SAR process with rho = 0.9`
  `SAR2_0.9`      | `Second realization of a SAR process with rho = 0.9`
  `...`      | `...`
  `SAR50_0.9`      | `50th realization of a SAR process with rho = 0.9`
  `...`      | `...`
  `...`      | `...`
  `SAR1_-0.9`      | `First realization of a SAR process with rho = -0.9`
  `SAR2_-0.9`      | `Second realization of a SAR process with rho = -0.9`
  `...`      | `...`
  `SAR50_-0.9`      | `50th realization of a SAR process with rho = -0.9`

`NOTE: There is a .csv and a shapefile for each value on N (number of areas)
5  : lattice of 5x5 = 25 areas,
10 : lattice of 10x10 = 100 areas, 
15 : lattice of 15x15 = 225 areas, 
20 : lattice of 20x20 = 400 areas, 
25 : lattice of 25x25 = 625 areas, 
30 : lattice of 30x30 = 900 areas`   

### [Go to folder 1_SAR_realizations](1_SAR_realizations)

## Folder: <span style="color:red">2_Spatial_aggregations</span>

**SAR realization** | **Regions IDs**     | **Description**
  ----------------- | -------------------------|---------------------------------------------------
  `SAR1_0.9_22`       | `[16,13,...,10]`   |`r = 1st random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions. The list contains the ID of the regions for each area; i.e., area 0 is assigned to region ID 16, areas 1 is assigned to region ID 13,..., area 24 is assigned to region ID 10.` 
  `SAR1_0.9_22`       | `[1,5,...,3]`   |`r = 2nd random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions. The list contains the ID of the regions for each area; i.e., area 0 is assigned to region ID 1, areas 1 is assigned to region ID 5,..., area 24 is assigned to region ID 3.`
  `...`       | `...`   |`...`
  `SAR1_0.9_22`       | `[5,9,...,17]`   |`r = 29th random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions.`
  `SAR1_0.9_22`       | `[3,6,...,1]`   |`r = 30th random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions.`
  `...`       | `...`   |`...`
  `SAR50_-0.9_10`       | `[5,5,...,3]`   |`r = 1st random spatial aggregation of the 50th realization of a SAR process (SAR50), with rho = -0.9, into k = 10 regions.` 
  `...`       | `...`   |`...`
  `SAR50_-0.9_10`       | `[5,6,...,2]`   |`r = 30th random spatial aggregation of the 50th realization of a SAR process (SAR50), with rho = -0.9, into k = 10 regions.` 
  
`NOTE: There is a .csv for each value on N (number of areas)
5  : lattice of 5x5 = 25 areas,
10 : lattice of 10x10 = 100 areas, 
15 : lattice of 15x15 = 225 areas, 
20 : lattice of 20x20 = 400 areas, 
25 : lattice of 25x25 = 625 areas, 
30 : lattice of 30x30 = 900 areas` 

### [Go to folder 2_Spatial_aggregations](2_Spatial_aggregations)

## Folder: <span style="color:red">3_MAUP_effects</span>

**SAR realization** | **Regions IDs**     | **Description**
  ----------------- | -------------------------|---------------------------------------------------
  `SAR1_0.9_22`       | `[16,13,...,10]`   |`r = 1st random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions. The list contains the ID of the regions for each area; i.e., area 0 is assigned to region ID 16, areas 1 is assigned to region ID 13,..., area 24 is assigned to region ID 10.` 
  `SAR1_0.9_22`       | `[1,5,...,3]`   |`r = 2nd random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions. The list contains the ID of the regions for each area; i.e., area 0 is assigned to region ID 1, areas 1 is assigned to region ID 5,..., area 24 is assigned to region ID 3.`
  `...`       | `...`   |`...`
  `SAR1_0.9_22`       | `[5,9,...,17]`   |`r = 29th random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions.`
  `SAR1_0.9_22`       | `[3,6,...,1]`   |`r = 30th random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions.`
  `...`       | `...`   |`...`
  `SAR50_-0.9_10`       | `[5,5,...,3]`   |`r = 1st random spatial aggregation of the 50th realization of a SAR process (SAR50), with rho = -0.9, into k = 10 regions.` 
  `...`       | `...`   |`...`
  `SAR50_-0.9_10`       | `[5,6,...,2]`   |`r = 30th random spatial aggregation of the 50th realization of a SAR process (SAR50), with rho = -0.9, into k = 10 regions.` 
  
`NOTE: There is a .csv for each value on N (number of areas)
5  : lattice of 5x5 = 25 areas,
10 : lattice of 10x10 = 100 areas, 
15 : lattice of 15x15 = 225 areas, 
20 : lattice of 20x20 = 400 areas, 
25 : lattice of 25x25 = 625 areas, 
30 : lattice of 30x30 = 900 areas` 

### [Go to folder 3_MAUP_effects](3_MAUP_effects)

## Folder: <span style="color:red">4_t_tests</span>

**SAR realization** | **Regions IDs**     | **Description**
  ----------------- | -------------------------|---------------------------------------------------
  `SAR1_0.9_22`       | `[16,13,...,10]`   |`r = 1st random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions. The list contains the ID of the regions for each area; i.e., area 0 is assigned to region ID 16, areas 1 is assigned to region ID 13,..., area 24 is assigned to region ID 10.` 
  `SAR1_0.9_22`       | `[1,5,...,3]`   |`r = 2nd random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions. The list contains the ID of the regions for each area; i.e., area 0 is assigned to region ID 1, areas 1 is assigned to region ID 5,..., area 24 is assigned to region ID 3.`
  `...`       | `...`   |`...`
  `SAR1_0.9_22`       | `[5,9,...,17]`   |`r = 29th random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions.`
  `SAR1_0.9_22`       | `[3,6,...,1]`   |`r = 30th random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions.`
  `...`       | `...`   |`...`
  `SAR50_-0.9_10`       | `[5,5,...,3]`   |`r = 1st random spatial aggregation of the 50th realization of a SAR process (SAR50), with rho = -0.9, into k = 10 regions.` 
  `...`       | `...`   |`...`
  `SAR50_-0.9_10`       | `[5,6,...,2]`   |`r = 30th random spatial aggregation of the 50th realization of a SAR process (SAR50), with rho = -0.9, into k = 10 regions.` 
  
`NOTE: There is a .csv for each value on N (number of areas)
5  : lattice of 5x5 = 25 areas,
10 : lattice of 10x10 = 100 areas, 
15 : lattice of 15x15 = 225 areas, 
20 : lattice of 20x20 = 400 areas, 
25 : lattice of 25x25 = 625 areas, 
30 : lattice of 30x30 = 900 areas` 

### [Go to folder 4_t_tests](4_t_tests)

## Folder: <span style="color:red">5_Levene_tests</span>

**SAR realization** | **Regions IDs**     | **Description**
  ----------------- | -------------------------|---------------------------------------------------
  `SAR1_0.9_22`       | `[16,13,...,10]`   |`r = 1st random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions. The list contains the ID of the regions for each area; i.e., area 0 is assigned to region ID 16, areas 1 is assigned to region ID 13,..., area 24 is assigned to region ID 10.` 
  `SAR1_0.9_22`       | `[1,5,...,3]`   |`r = 2nd random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions. The list contains the ID of the regions for each area; i.e., area 0 is assigned to region ID 1, areas 1 is assigned to region ID 5,..., area 24 is assigned to region ID 3.`
  `...`       | `...`   |`...`
  `SAR1_0.9_22`       | `[5,9,...,17]`   |`r = 29th random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions.`
  `SAR1_0.9_22`       | `[3,6,...,1]`   |`r = 30th random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions.`
  `...`       | `...`   |`...`
  `SAR50_-0.9_10`       | `[5,5,...,3]`   |`r = 1st random spatial aggregation of the 50th realization of a SAR process (SAR50), with rho = -0.9, into k = 10 regions.` 
  `...`       | `...`   |`...`
  `SAR50_-0.9_10`       | `[5,6,...,2]`   |`r = 30th random spatial aggregation of the 50th realization of a SAR process (SAR50), with rho = -0.9, into k = 10 regions.` 
  
`NOTE: There is a .csv for each value on N (number of areas)
5  : lattice of 5x5 = 25 areas,
10 : lattice of 10x10 = 100 areas, 
15 : lattice of 15x15 = 225 areas, 
20 : lattice of 20x20 = 400 areas, 
25 : lattice of 25x25 = 625 areas, 
30 : lattice of 30x30 = 900 areas` 

### [Go to folder 5_Levene_tests](5_Levene_tests)

## Folder: <span style="color:red">6_median_RCM</span>

**SAR realization** | **Regions IDs**     | **Description**
  ----------------- | -------------------------|---------------------------------------------------
  `SAR1_0.9_22`       | `[16,13,...,10]`   |`r = 1st random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions. The list contains the ID of the regions for each area; i.e., area 0 is assigned to region ID 16, areas 1 is assigned to region ID 13,..., area 24 is assigned to region ID 10.` 
  `SAR1_0.9_22`       | `[1,5,...,3]`   |`r = 2nd random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions. The list contains the ID of the regions for each area; i.e., area 0 is assigned to region ID 1, areas 1 is assigned to region ID 5,..., area 24 is assigned to region ID 3.`
  `...`       | `...`   |`...`
  `SAR1_0.9_22`       | `[5,9,...,17]`   |`r = 29th random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions.`
  `SAR1_0.9_22`       | `[3,6,...,1]`   |`r = 30th random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions.`
  `...`       | `...`   |`...`
  `SAR50_-0.9_10`       | `[5,5,...,3]`   |`r = 1st random spatial aggregation of the 50th realization of a SAR process (SAR50), with rho = -0.9, into k = 10 regions.` 
  `...`       | `...`   |`...`
  `SAR50_-0.9_10`       | `[5,6,...,2]`   |`r = 30th random spatial aggregation of the 50th realization of a SAR process (SAR50), with rho = -0.9, into k = 10 regions.` 
  
`NOTE: There is a .csv for each value on N (number of areas)
5  : lattice of 5x5 = 25 areas,
10 : lattice of 10x10 = 100 areas, 
15 : lattice of 15x15 = 225 areas, 
20 : lattice of 20x20 = 400 areas, 
25 : lattice of 25x25 = 625 areas, 
30 : lattice of 30x30 = 900 areas` 

### [Go to folder 6_median_RCM](6_median_RCM)

## Folder: <span style="color:red">7_Adjustments_of_robust_linear_regression_models</span>

**SAR realization** | **Regions IDs**     | **Description**
  ----------------- | -------------------------|---------------------------------------------------
  `SAR1_0.9_22`       | `[16,13,...,10]`   |`r = 1st random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions. The list contains the ID of the regions for each area; i.e., area 0 is assigned to region ID 16, areas 1 is assigned to region ID 13,..., area 24 is assigned to region ID 10.` 
  `SAR1_0.9_22`       | `[1,5,...,3]`   |`r = 2nd random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions. The list contains the ID of the regions for each area; i.e., area 0 is assigned to region ID 1, areas 1 is assigned to region ID 5,..., area 24 is assigned to region ID 3.`
  `...`       | `...`   |`...`
  `SAR1_0.9_22`       | `[5,9,...,17]`   |`r = 29th random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions.`
  `SAR1_0.9_22`       | `[3,6,...,1]`   |`r = 30th random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions.`
  `...`       | `...`   |`...`
  `SAR50_-0.9_10`       | `[5,5,...,3]`   |`r = 1st random spatial aggregation of the 50th realization of a SAR process (SAR50), with rho = -0.9, into k = 10 regions.` 
  `...`       | `...`   |`...`
  `SAR50_-0.9_10`       | `[5,6,...,2]`   |`r = 30th random spatial aggregation of the 50th realization of a SAR process (SAR50), with rho = -0.9, into k = 10 regions.` 
  
`NOTE: There is a .csv for each value on N (number of areas)
5  : lattice of 5x5 = 25 areas,
10 : lattice of 10x10 = 100 areas, 
15 : lattice of 15x15 = 225 areas, 
20 : lattice of 20x20 = 400 areas, 
25 : lattice of 25x25 = 625 areas, 
30 : lattice of 30x30 = 900 areas` 

### [Go to folder 7_Adjustments_of_robust_linear_regression_models](7_Adjustments_of_robust_linear_regression_models)

## Folder: <span style="color:red">8_critical values</span>

**SAR realization** | **Regions IDs**     | **Description**
  ----------------- | -------------------------|---------------------------------------------------
  `SAR1_0.9_22`       | `[16,13,...,10]`   |`r = 1st random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions. The list contains the ID of the regions for each area; i.e., area 0 is assigned to region ID 16, areas 1 is assigned to region ID 13,..., area 24 is assigned to region ID 10.` 
  `SAR1_0.9_22`       | `[1,5,...,3]`   |`r = 2nd random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions. The list contains the ID of the regions for each area; i.e., area 0 is assigned to region ID 1, areas 1 is assigned to region ID 5,..., area 24 is assigned to region ID 3.`
  `...`       | `...`   |`...`
  `SAR1_0.9_22`       | `[5,9,...,17]`   |`r = 29th random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions.`
  `SAR1_0.9_22`       | `[3,6,...,1]`   |`r = 30th random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions.`
  `...`       | `...`   |`...`
  `SAR50_-0.9_10`       | `[5,5,...,3]`   |`r = 1st random spatial aggregation of the 50th realization of a SAR process (SAR50), with rho = -0.9, into k = 10 regions.` 
  `...`       | `...`   |`...`
  `SAR50_-0.9_10`       | `[5,6,...,2]`   |`r = 30th random spatial aggregation of the 50th realization of a SAR process (SAR50), with rho = -0.9, into k = 10 regions.` 
  
`NOTE: There is a .csv for each value on N (number of areas)
5  : lattice of 5x5 = 25 areas,
10 : lattice of 10x10 = 100 areas, 
15 : lattice of 15x15 = 225 areas, 
20 : lattice of 20x20 = 400 areas, 
25 : lattice of 25x25 = 625 areas, 
30 : lattice of 30x30 = 900 areas` 

### [Go to folder 8_critical values](8_critical values)

## Folder: <span style="color:red">9_power</span>

**SAR realization** | **Regions IDs**     | **Description**
  ----------------- | -------------------------|---------------------------------------------------
  `SAR1_0.9_22`       | `[16,13,...,10]`   |`r = 1st random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions. The list contains the ID of the regions for each area; i.e., area 0 is assigned to region ID 16, areas 1 is assigned to region ID 13,..., area 24 is assigned to region ID 10.` 
  `SAR1_0.9_22`       | `[1,5,...,3]`   |`r = 2nd random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions. The list contains the ID of the regions for each area; i.e., area 0 is assigned to region ID 1, areas 1 is assigned to region ID 5,..., area 24 is assigned to region ID 3.`
  `...`       | `...`   |`...`
  `SAR1_0.9_22`       | `[5,9,...,17]`   |`r = 29th random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions.`
  `SAR1_0.9_22`       | `[3,6,...,1]`   |`r = 30th random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions.`
  `...`       | `...`   |`...`
  `SAR50_-0.9_10`       | `[5,5,...,3]`   |`r = 1st random spatial aggregation of the 50th realization of a SAR process (SAR50), with rho = -0.9, into k = 10 regions.` 
  `...`       | `...`   |`...`
  `SAR50_-0.9_10`       | `[5,6,...,2]`   |`r = 30th random spatial aggregation of the 50th realization of a SAR process (SAR50), with rho = -0.9, into k = 10 regions.` 
  
`NOTE: There is a .csv for each value on N (number of areas)
5  : lattice of 5x5 = 25 areas,
10 : lattice of 10x10 = 100 areas, 
15 : lattice of 15x15 = 225 areas, 
20 : lattice of 20x20 = 400 areas, 
25 : lattice of 25x25 = 625 areas, 
30 : lattice of 30x30 = 900 areas` 

### [Go to folder 9_power](9_power)

## Folder: <span style="color:red">10_size</span>

**SAR realization** | **Regions IDs**     | **Description**
  ----------------- | -------------------------|---------------------------------------------------
  `SAR1_0.9_22`       | `[16,13,...,10]`   |`r = 1st random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions. The list contains the ID of the regions for each area; i.e., area 0 is assigned to region ID 16, areas 1 is assigned to region ID 13,..., area 24 is assigned to region ID 10.` 
  `SAR1_0.9_22`       | `[1,5,...,3]`   |`r = 2nd random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions. The list contains the ID of the regions for each area; i.e., area 0 is assigned to region ID 1, areas 1 is assigned to region ID 5,..., area 24 is assigned to region ID 3.`
  `...`       | `...`   |`...`
  `SAR1_0.9_22`       | `[5,9,...,17]`   |`r = 29th random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions.`
  `SAR1_0.9_22`       | `[3,6,...,1]`   |`r = 30th random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions.`
  `...`       | `...`   |`...`
  `SAR50_-0.9_10`       | `[5,5,...,3]`   |`r = 1st random spatial aggregation of the 50th realization of a SAR process (SAR50), with rho = -0.9, into k = 10 regions.` 
  `...`       | `...`   |`...`
  `SAR50_-0.9_10`       | `[5,6,...,2]`   |`r = 30th random spatial aggregation of the 50th realization of a SAR process (SAR50), with rho = -0.9, into k = 10 regions.` 
  
`NOTE: There is a .csv for each value on N (number of areas)
5  : lattice of 5x5 = 25 areas,
10 : lattice of 10x10 = 100 areas, 
15 : lattice of 15x15 = 225 areas, 
20 : lattice of 20x20 = 400 areas, 
25 : lattice of 25x25 = 625 areas, 
30 : lattice of 30x30 = 900 areas` 

### [Go to folder 10_size](10_size)

## Folder: <span style="color:red">11_application</span>

**SAR realization** | **Regions IDs**     | **Description**
  ----------------- | -------------------------|---------------------------------------------------
  `SAR1_0.9_22`       | `[16,13,...,10]`   |`r = 1st random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions. The list contains the ID of the regions for each area; i.e., area 0 is assigned to region ID 16, areas 1 is assigned to region ID 13,..., area 24 is assigned to region ID 10.` 
  `SAR1_0.9_22`       | `[1,5,...,3]`   |`r = 2nd random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions. The list contains the ID of the regions for each area; i.e., area 0 is assigned to region ID 1, areas 1 is assigned to region ID 5,..., area 24 is assigned to region ID 3.`
  `...`       | `...`   |`...`
  `SAR1_0.9_22`       | `[5,9,...,17]`   |`r = 29th random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions.`
  `SAR1_0.9_22`       | `[3,6,...,1]`   |`r = 30th random spatial aggregation of the first realization of a SAR process (SAR1), with rho = 0.9, into k = 22 regions.`
  `...`       | `...`   |`...`
  `SAR50_-0.9_10`       | `[5,5,...,3]`   |`r = 1st random spatial aggregation of the 50th realization of a SAR process (SAR50), with rho = -0.9, into k = 10 regions.` 
  `...`       | `...`   |`...`
  `SAR50_-0.9_10`       | `[5,6,...,2]`   |`r = 30th random spatial aggregation of the 50th realization of a SAR process (SAR50), with rho = -0.9, into k = 10 regions.` 
  
`NOTE: There is a .csv for each value on N (number of areas)
5  : lattice of 5x5 = 25 areas,
10 : lattice of 10x10 = 100 areas, 
15 : lattice of 15x15 = 225 areas, 
20 : lattice of 20x20 = 400 areas, 
25 : lattice of 25x25 = 625 areas, 
30 : lattice of 30x30 = 900 areas` 

### [Go to folder 11_application](11_application)


```python

```


## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

