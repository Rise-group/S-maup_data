<img src="figs/rise_logo.png" alt="Estructura Carpeta" align="center">

## S-maup: Statistical Test to Measure the Sensitivity to the Modifiable Areal Unit Problem


Juan C. Duque<sup>1,2</sup>, Henry Laniado<sup>1</sup>, Adriano Polo<sup>2,3</sup>


<sup>1</sup> Department of Mathematical Sciences, Universidad EAFIT, Medellin, Colombia

<sup>2</sup> RiSE-group, Universidad EAFIT, Medellin, Colombia

<sup>3</sup> Department of Economics, Universidad EAFIT, Medellin, Colombia


__maintainer__ = "RiSE Group"  (http://www.rise-group.org/). Universidad EAFIT

__Corresponding author__ = jduquec1@eafit.edu.co (JCD)

# Computational Experiment on MAUP effects

<img src="figs/scheme.png" alt="Estructura Carpeta" align="center">

**Folder** | **Table** | **Figure**
  ----------------- | ---------------------------- | -----------------------------------------------
  [1_SAR_realizations](1_SAR_realizations)| - |-
  [2_Spatial_aggregations](2_Spatial_aggregations)| - |-
  [3_MAUP_effects](3_MAUP_effects)|-  | Figure 3, Figure 4
  [4_t_tests_and_Levene_tests](4_t_tests_Levene_tests)| Table 2 | Figure 5
  [5_median_RCV_bar](5_median_RCV_bar)| - | Figure 7
  [6_Adjustments_of_robust_linear_regression_models](6_Adjustments_of_robust_linear_regression_models)|- | Figure 8
  [7_critical_values](7_critical_values)| Table 3  |-
  [8_power](8_power)| Table 5 |-
  [9_size](9_size)| Table 6 |-
  [10_application](10_application)| Table 7, Table 8, Table 9 |Figure 9, Figure 10, Figure 11



## Folder: <span style="color:red">1_SAR_realizations</span>

File Names:

`There is a .csv and a shapefile for each value on N (number of areas)
5  : lattice of 5x5 = 25 areas,
10 : lattice of 10x10 = 100 areas, 
15 : lattice of 15x15 = 225 areas, 
20 : lattice of 20x20 = 400 areas, 
25 : lattice of 25x25 = 625 areas, 
30 : lattice of 30x30 = 900 areas`  

Dictionary of Variables:

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

 

### [Go to folder 1_SAR_realizations](1_SAR_realizations)

## Folder: <span style="color:red">2_Spatial_aggregations</span>

File Names:

`N#_K#.csv`

Where:

`N = Number of areas, such that,
5  : lattice of 5x5 = 25 areas,
10 : lattice of 10x10 = 100 areas, 
15 : lattice of 15x15 = 225 areas, 
20 : lattice of 20x20 = 400 areas, 
25 : lattice of 25x25 = 625 areas, 
30 : lattice of 30x30 = 900 areas`  

`K = Number of regions
for N=25, k = {*3,*5,10,13,15,18,20,22,24},
for N=100, k = {*2, *4, *7, 12, 25, 40, 53, 67, 80, 90, 99},
for N =225, k = {*3, *5, 10, 15, 30, 60, 90, 120, 150, 180, 200, 220},
for N =400, k = {*4, *9, 18, 26, 50, 110, 160, 213, 267, 320, 360, 396},
for N =625, k = {*4, *6, 14, 27, 43, 80, 170, 250, 333, 417, 500, 563, 618},
for N =900, k = {*4, *9, 20, 40, 60, 120, 240, 360, 480, 600, 720, 810, 890}`

`* The effects on mean and variances is done for k ≥ 10.`

`NOTE: 
If the original file size is above 20M, then the file is splitted into pieces below 20M with the suffix "_aa", "_ab",... `


Dictionary of Variables:

**Rows** | **Example**     | **Description**
  ----------------- | -------------------------|---------------------------------------------------
  `First_row`       | `SAR1_0.9_0,SAR1_0.9_1,...,SAR50_-0.9_29`   |`SAR realization ID_rho value_aggegation ID (r=[0,..,29])`
   `Second_row`       | 0.87131977,...,-0.832686856   |`Rho estimated for that SAR realization ID`
   `Third_row`       | 0,1,2,...,29   |`r`
   `Following_k_rows`       | 0.737450726,1.16692622,...,-0.597942993   |`The attribute value for each region k is calculated as the mean value of the attribute values of the areas assigned to the region`
   
  

### [Go to folder 2_Spatial_aggregations](2_Spatial_aggregations)

## Folder: <span style="color:red">3_MAUP_effects</span>

File Names:

`RCM_RCV.csv`: Relative change in the mean (RCM) and relative change in the variance (RCV). Eq(1) and Eq(2).

`RCM_bar_RCV_bar.csv`: mean RCM and mean RCV. Eq(3) and Eq(4).


`NOTE:`

`(1) RCM_RCV.csv is splitted into pieces below 20M with the suffix "_aa", "_ab",...`

`(2) The effects on mean and variances is done for k ≥ 10.`



Dictionary of Variables:

`RCM_RCV.csv`:

**Variable name** | **Description**
  ----------------- | -------------------------------------------------------------------------
  `N`       | `sqrt(Number of areas)`
  `VarName`      | `SAR process ID`
  `k`      | `Number of regions`
  `r`      | `Aggregation ID. r = [1,...,30]`
  `RhoReference`      | `Rho_reference`
  `RhoEstimated`      | `Rho_estimated`
  `Avg_Original`      | `Mean of the original, disaggregated, variable (\mu_{o})`
  `Var_Original`      | `Variance of the original, disaggregated, variable (\sigma_{o}^{2})`
  `Avg_ag`      | `Mean of the aggregated variable (\mu_{ag})`
  `Var_ag`      | `Variance of the aggregatedvariable (\sigma_{ag}^{2})`
  `RCM`      | `Relative change in the mean (RCM). Eg(1)`
  `RCV`      | `Relative change in the variance (RCV). Eq(2)`
  `NameNew`      | `Variable name in file RCM_bar_RCV_bar.csv`
  
`RCM_bar_RCV_bar.csv`:

**Variable name** | **Description**
  ----------------- | -------------------------------------------------------------------------
  `VarName`      | `Variable name`
  `N`       | `sqrt(Number of areas)`
  `k`      | `Number of regions`
  `RhoReference`      | `Rho_reference`
  `RhoEstimated`      | `Rho_estimated`
  `RCM_bar`      | `Relative change in the mean - Average effect. Eg(3)`
  `RCV_bar`      | `Relative change in the variance - Average effect. Eq(4)`

### [Go to folder 3_MAUP_effects](3_MAUP_effects)

## Folder: <span style="color:red">4_t_tests_and_Levene_tests</span>

File Names:

`mean_and_variance_tests.csv`: Results for the two-sample t-test and the Levene test.


`NOTE:`

`(1) The tests are calculated for k ≥ 10.`


Dictionary of Variables:

**Variable name** | **Description**
  ----------------- | -------------------------------------------------------------------------
  `VarName`      | `Variable name`
  `N`       | `sqrt(Number of areas)`
  `k`      | `Number of regions`
  `pVal_two_sample_t_test`      | `pValue for two sample t-test`
  `reject_two_sample_t_test`      | `1: the two-sample t-test was rejected`
  `pVal_levene`      | `pValue for the Levene test`
  `reject_levene`      | `1: the Levene test was rejected`

### [Go to folder 4_t_tests_and_Levene_tests](4_t_tests_Levene_tests)

## Folder: <span style="color:red">5_median_RCV_bar</span>

File Names:

`median_RCV_bar.csv`: Median of each Box Plot in Fig 4 (input for Figure 7)


Dictionary of Variables:

**Variable name** | **Description**
  ----------------- | -------------------------------------------------------------------------
  `RhoReference`      | `Rho_reference`
  `N`       | `sqrt(Number of areas)`
  `k`      | `Number of regions`
  `median_RCV_bar`      | `Median of each Box Plot in Fig 4`


### [Go to folder 5_median_RCV_bar](5_median_RCV_bar)

## Folder: <span style="color:red">6_Adjustments_of_robust_linear_regression_models</span>

File Names:

`L_Fig8a.csv`: Input data to estimate Eq(7). See Figure 8a.

`Eta_Fig8b.csv`: Input data to estimate Eq(8). See Figure 8b.

`Tau_Fig8c`: Input data to estimate Eq(9). See Figure 8c.

`NOTE:`

`(1) RL_Fig8a.csv is splitted into pieces below 20M with the suffix "_aa", "_ab",...`


Dictionary of Variables:

`L_Fig8a.csv`:

**Variable name** | **Description**
  ----------------- | -------------------------------------------------------------------------
  `RhoReference`      | `Rho_reference`
  `N`       | `sqrt(Number of areas)`
  `k`      | `Number of regions`
  `k_N`      | `theta = k/N`<sup>2</sup>
  `median_RCV_bar`      | `median RCV_bar`
  `linearized_median_RCV_bar`      | `linearized median RCV_bar`
  
`Eta_Fig8b.csv`:

**Variable name** | **Description**
  ----------------- | -------------------------------------------------------------------------
  `N`       | `sqrt(Number of areas)`
  `k`      | `Number of regions`
  `Eta`      | `Eta`
  
`Tau_Fig8c.csv`:

**Variable name** | **Description**
  ----------------- | -------------------------------------------------------------------------
  `N`       | `sqrt(Number of areas)`
  `k`      | `Number of regions`
  `Tau`      | `Tau`
  

### [Go to folder 6_Adjustments_of_robust_linear_regression_models](6_Adjustments_of_robust_linear_regression_models)

## Folder: <span style="color:red">7_critical values</span>

File Names:

`Tab_Critical<N>.csv`: Critical values for Table 3.


There is one folder per each value of N. Inside those folders there are files of the type:

`MainTable_<N>_<RhoReference>.csv` that contains the S-maup for the 1,000 instances descrived in the first paragraph of section "Critical values and p-value" 

Where:

`N = Number of areas
5  : lattice of 5x5 = 25 areas,
10 : lattice of 10x10 = 100 areas, 
15 : lattice of 15x15 = 225 areas, 
20 : lattice of 20x20 = 400 areas, 
25 : lattice of 25x25 = 625 areas, 
30 : lattice of 30x30 = 900 areas` 

Dictionary of Variables:

`Tab_Critical<N>.csv`:

**Variable name** | **Description**
  ----------------- | -------------------------------------------------------------------------
  `RhoReference`      | `Rho_reference`
  `q10`     | `Significance level = 0.1`
  `q5`      | `Significance level = 0.05`
  `q1`      | `Significance level = 0.05`


`MainTable_<N>_<RhoReference>.csv`:

**Variable name** | **Description**
  ----------------- | -------------------------------------------------------------------------
  `Var`      | `Variable name`
  `N`     | `sqrt(Number of areas)`
  `RhoReference`      | `Rho_reference`
  `RhoEstimated`      | `Rho_estimated`
  `k`     | `Number of regions`
  `Theta`     | `Significance level = 0.1`
  `r`     | `Aggregation ID. r = [1,...,30]`
  `SMAUP`     | `SMAUP (Eq. 14)`
  


### [Go to folder 7_critical values](7_critical_values)

## Folder: <span style="color:red">8_power</span>

File Names:

`Tab_Power.csv`: Estimated power of S-maup (Table 5).


There is one folder per each value of N. Inside those folders there are files of the type:

`Tab_Power_<N>_<RhoReference>.csv` that contains the 1,000 instances for which the Leven test between the original variable and each one of the 30 aggregated variables is rejected. See the complete description in the first paragraph of section "Power and Size" 

Where:

`N = Number of areas
10 : lattice of 10x10 = 100 areas, 
20 : lattice of 20x20 = 400 areas, 
30 : lattice of 30x30 = 900 areas` 

Dictionary of Variables:

`Tab_Power.csv`:

**Variable name** | **Description**
  ----------------- | -------------------------------------------------------------------------
  `RhoReference`      | `Rho_reference`
  `N_100`     | `Estimated power fon N=100`
  `N_400`      | `Estimated power fon N=400`
  `N_900`      | `Estimated power fon N=900`


`Tab_Power_<N>_<RhoReference>.csv`:

**Variable name** | **Description**
  ----------------- | -------------------------------------------------------------------------
  `VarName`      | `Variable name`
  `RhoReference`      | `Rho_reference`
  `RhoEstimated`      | `Rho_estimated`
  `k`     | `Number of regions`
  `N`     | `sqrt(Number of areas)`
  `k_N`     | `theta = k/N`<sup>2</sup>
  `Smaup`     | `S-maup value`
  `reject`     | `1: Smaup rejects the null hypothesis `
  


### [Go to folder 8_power](8_power)

## Folder: <span style="color:red">9_size</span>

File Names:

`Tab_Size.csv`: Estimated size of S-maup (Table 6).


There is one folder per each value of N. Inside those folders there are files of the type:

`Tab_Size_N#_<RhoReference>.csv` that contains the 1,000 instances for which the Levene test is not rejected in all 30 cases. See the complete description in the third and fourth paragraphs of section "Power and Size" 

Where:

`N = Number of areas
10 : lattice of 10x10 = 100 areas, 
20 : lattice of 20x20 = 400 areas, 
30 : lattice of 30x30 = 900 areas` 

Dictionary of Variables:

`Tab_Size.csv`:

**Variable name** | **Description**
  ----------------- | -------------------------------------------------------------------------
  `RhoReference`      | `Rho_reference`
  `N_100`     | `Estimated size fon N=100`
  `N_400`      | `Estimated size fon N=400`
  `N_900`      | `Estimated size fon N=900`


`Tab_Size_N#_<RhoReference>.csv`:

**Variable name** | **Description**
  ----------------- | -------------------------------------------------------------------------
  `VarName`      | `Variable name`
  `N`     | `sqrt(Number of areas)`
  `RhoReference`      | `Rho_reference`
  `RhoEstimated`      | `Rho_estimated`
  `k`     | `Number of regions`
  `Theta`     | `k/N`<sup>2</sup>
  `counter`     | `counter`
  `Smaup`     | `S-maup value`
  `reject`     | `1: Smaup rejects the null hypothesis `
  

### [Go to folder 9_size](9_size)

## Folder: <span style="color:red">10_application</span>

This folder contains the data used in section "An illustrative application of the S-maup test"

The folder: `1_maps_South_Africa`, contains the shapefile of South Africa with the following attributes:

**Variable name** | **Description**
  ----------------- | -------------------------------------------------------------------------
  `LNY`      | `Logarithm of income (hourly wage)`
  `YRSCHOOL`     | `years of schooling`
  `EXP`      | `years of potential labor market experience (calculated as the age in years minus years of education plus 6)`
  `EXP2`      | `EXP`<sup>2</sup>

These maps have the information for Table 7, Table 8 and Figure 9

File `2_Table_9.csv` contains the data for Table 9, with the following attributes:

**Variable name** | **Description**
  ----------------- | -------------------------------------------------------------------------
  `N`      | `Number of areas`
  `VarName`     | `Variable name`
  `RhoEstimated`      | `Rho_estimated`
  `k`      | `Number of regions`
  `M`      | `S-maup value`
  `PseudoP`      | `p value`

The folder `3_k_136` contains the Mincer equation on 1,000 random spatial aggregations of the k = 206 municipalities into k = 136 regions. File `aggregations_k_136.csv` contains the aggregations and file  `Betas_k_136.csv` contains the Beta values for Figure 10.

The folder `4_k_52` contains the Mincer equation on 1,000 random spatial aggregations of the k = 206 municipalities into k = 52 regions. File `aggregations_k_52.csv` contains the aggregations and file  `Betas_k_52.csv` contains the Beta values for Figure 11.

### [Go to folder 10_application](10_application)
