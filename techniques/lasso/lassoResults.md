
<!--Figure out most important categories in aggregate.-->




|                     |LarsCV5|LarsCV10|LassoCV5|LassoCV20|LassoCV4|LassoCV5grid100|LassoCV5grid500|
|--:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Number of variables | 72    | 72     | 1002   | 1086   | 972    | 1020   |  |
| $\log_{10} \lambda$ | -4.44 | -4.58  | -5.02  | -5.08  | -4.96  | -5.02  |  |
| Time to run         | 53.32 | 110.03 | 177.75 | 617.16 | 146.17 | 177.48 |  |
| MSE                 | 0.38  | 0.38   | 0.29   | 0.29   | 0.29   | 0.29   |  |
| $R^2$               | 0.45  | 0.45   | 0.57   | 0.57   | 0.57   | 0.57   |  |




## LarsCV5 

### Code: 

    model = skl.LassoLarsCV(normalize = True, cv = 5)
    model.fit(X,Y)
    predictions = model.predict(X)
    alpha = model.alpha_,

### Results:

    Time to run: 53.32005000114441 to run
    \lambda:  (3.603796827667866e-05,) log10: [-4.4432397] ln: [-10.2309375]
    Coefficients: 
    [ 0.00166889  0.         -0.18421037 ...  0.          0.
    0.        ]
    Mean squared error: 0.38
    Coefficient of determination: 0.45
    age : 0.002 age
    educ_cat_1.0 : -0.184 
    educ_cat_2.0 : -0.060 
    educ_cat_4.0 : 0.187 
    educ_cat_5.0 : 0.378 
    male_0.0 : -0.266 
    hhtenure_1 : 0.000 owned or being bought
    hhtenure_2 : -0.055 rented for cash
    metarea_5606 : 0.006 new york-northern new jersey-long island, ny-nj-pa
    metarea_8840 : 0.032 washington, dc/md/va
    metarea_9998 : -0.043 niu, household not in a metropolitan area
    unitsstr_1 : -0.002 mobile home or trailer
    marst_1 : 0.004 married, spouse present
    marst_6 : -0.052 never married/single
    citizen_5 : -0.066 not a citizen
    occ_0 : -0.262 Missing data?
    occ_10 : 0.047 chief executives and legislators/public administration
    occ_20 : 0.030 general and operations managers
    occ_1020 : 0.006 software developers, applications and systems software
    occ_3060 : 0.111 physicians and surgeons
    occ_3255 : 0.059 
    occ_4600 : -0.052 childcare workers
    ind_0 : 0.087 
    ind_7380 : 0.028 
    educ_124 : 0.015 professional school degree
    occly_10 : 0.302 chief executives and legislators/public administration
    occly_20 : 0.093 general and operations managers
    occly_50 : 0.108 
    occly_110 : 0.084 computer and information systems managers
    occly_120 : 0.037 financial managers
    occly_430 : 0.127 managers, nec (including postmasters)
    occly_1020 : 0.092 software developers, applications and systems software
    occly_2100 : 0.106 lawyers, and judges, magistrates, and other judicial workers
    occly_2540 : -0.164 teacher assistants
    occly_3050 : 0.016 pharmacists
    occly_3060 : 0.070 physicians and surgeons
    occly_3255 : 0.027 
    occly_3600 : -0.038 nursing, psychiatric, and home health aides
    occly_4020 : -0.052 
    occly_4110 : -0.009 waiters and waitresses
    occly_4220 : -0.110 janitors and building cleaners
    occly_4230 : -0.129 maids and housekeeping cleaners
    occly_4610 : -0.114 personal care aides
    occly_4720 : -0.221 cashiers
    occly_4760 : -0.052 retail salespersons
    occly_5620 : -0.085 stock clerks and order fillers
    occly_9620 : -0.046 laborers and freight, stock, and material movers, hand
    indly_490 : 0.161 
    indly_4970 : -0.004 
    indly_5380 : -0.061 
    indly_7380 : 0.109 
    indly_7580 : -0.119 
    indly_7860 : -0.062 
    indly_8470 : -0.032 
    indly_8680 : -0.163 
    indly_9160 : -0.005 
    classwly_13 : -0.780 self-employed, not incorporated
    classwly_14 : 0.155 self-employed, incorporated
    classwly_25 : 0.083 federal government employee
    pension_at_w_ly_3 : 0.403 included in pension plan at work
    firmsize_ly_1 : -0.118 under 10
    firmsize_ly_9 : 0.013 1000+
    actnlfly_0 : 0.399 niu
    actnlfly_20 : -0.277 taking care of home/family
    actnlfly_30 : -0.257 going to school
    spmmort_1 : 0.089 owners with a mortgage
    spmmort_3 : -0.009 renters
    health_1 : 0.028 excellent
    health_3 : -0.017 good
    health_4 : -0.059 fair
    paidhour_1 : 0.102 no
    paidhour_2 : -0.014 yes


### grid:


    model.alphas_
    array([0.00145097, 0.00091279, 0.00078381, 0.00076329, 0.00066709,
        0.00058632, 0.00056714, 0.0005586 , 0.00041656, 0.0003813 ,
        0.00035643, 0.00034924, 0.000345  , 0.00033496, 0.00031425,
        0.00030957, 0.00029335, 0.00029041, 0.00027613, 0.00026769,
        0.0002629 , 0.00025293, 0.00025093, 0.0002473 , 0.00023157,
        0.00022688, 0.0002202 , 0.00022007, 0.00021279, 0.00021016,
        0.00020668, 0.00020487, 0.00020047, 0.00019916, 0.00019909,
        0.00019695, 0.00018677, 0.00018533, 0.00018219, 0.00017915,
        0.00017863, 0.00017561, 0.00017409, 0.00017221, 0.0001718 ,
        0.00017072, 0.00017047, 0.00016915, 0.00016724, 0.00016476,
        0.00016369, 0.00016101, 0.00016038, 0.00015949, 0.00015905,
        0.00015731, 0.00015586, 0.00015421, 0.00015357, 0.00015255,
        0.00014551, 0.00014518, 0.00014359, 0.00014156, 0.00014101,
        0.00012934, 0.00012827, 0.00012774, 0.00012657, 0.00012609,
        0.00012599, 0.00012499, 0.00013964])













## LarsCV10

### Code:

    model = skl.LassoLarsCV(normalize = True, cv = 10)
    model.fit(X,Y)
    predictions = model.predict(X)

### Results:

    #%% Show results...
    Time to run: 110.0322937965393 to run
    \lambda:  (2.606836917831437e-05,) log10: [-4.58388614] ln: [-10.55478789]
    Coefficients: 
    [ 0.00166889  0.         -0.18421037 ...  0.          0.
    0.        ]
    Mean squared error: 0.38
    Coefficient of determination: 0.45
    age : 0.002 age
    educ_cat_1.0 : -0.184 
    educ_cat_2.0 : -0.060 
    educ_cat_4.0 : 0.187 
    educ_cat_5.0 : 0.378 
    male_0.0 : -0.266 
    hhtenure_1 : 0.000 owned or being bought
    hhtenure_2 : -0.055 rented for cash
    metarea_5606 : 0.006 new york-northern new jersey-long island, ny-nj-pa
    metarea_8840 : 0.032 washington, dc/md/va
    metarea_9998 : -0.043 niu, household not in a metropolitan area
    unitsstr_1 : -0.002 mobile home or trailer
    marst_1 : 0.004 married, spouse present
    marst_6 : -0.052 never married/single
    citizen_5 : -0.066 not a citizen
    occ_0 : -0.262 Missing data?
    occ_10 : 0.047 chief executives and legislators/public administration
    occ_20 : 0.030 general and operations managers
    occ_1020 : 0.006 software developers, applications and systems software
    occ_3060 : 0.111 physicians and surgeons
    occ_3255 : 0.059 
    occ_4600 : -0.052 childcare workers
    ind_0 : 0.087 
    ind_7380 : 0.028 
    educ_124 : 0.015 professional school degree
    occly_10 : 0.302 chief executives and legislators/public administration
    occly_20 : 0.093 general and operations managers
    occly_50 : 0.108 
    occly_110 : 0.084 computer and information systems managers
    occly_120 : 0.037 financial managers
    occly_430 : 0.127 managers, nec (including postmasters)
    occly_1020 : 0.092 software developers, applications and systems software
    occly_2100 : 0.106 lawyers, and judges, magistrates, and other judicial workers
    occly_2540 : -0.164 teacher assistants
    occly_3050 : 0.016 pharmacists
    occly_3060 : 0.070 physicians and surgeons
    occly_3255 : 0.027 
    occly_3600 : -0.038 nursing, psychiatric, and home health aides
    occly_4020 : -0.052 
    occly_4110 : -0.009 waiters and waitresses
    occly_4220 : -0.110 janitors and building cleaners
    occly_4230 : -0.129 maids and housekeeping cleaners
    occly_4610 : -0.114 personal care aides
    occly_4720 : -0.221 cashiers
    occly_4760 : -0.052 retail salespersons
    occly_5620 : -0.085 stock clerks and order fillers
    occly_9620 : -0.046 laborers and freight, stock, and material movers, hand
    indly_490 : 0.161 
    indly_4970 : -0.004 
    indly_5380 : -0.061 
    indly_7380 : 0.109 
    indly_7580 : -0.119 
    indly_7860 : -0.062 
    indly_8470 : -0.032 
    indly_8680 : -0.163 
    indly_9160 : -0.005 
    classwly_13 : -0.780 self-employed, not incorporated
    classwly_14 : 0.155 self-employed, incorporated
    classwly_25 : 0.083 federal government employee
    pension_at_w_ly_3 : 0.403 included in pension plan at work
    firmsize_ly_1 : -0.118 under 10
    firmsize_ly_9 : 0.013 1000+
    actnlfly_0 : 0.399 niu
    actnlfly_20 : -0.277 taking care of home/family
    actnlfly_30 : -0.257 going to school
    spmmort_1 : 0.089 owners with a mortgage
    spmmort_3 : -0.009 renters
    health_1 : 0.028 excellent
    health_3 : -0.017 good
    health_4 : -0.059 fair
    paidhour_1 : 0.102 no
    paidhour_2 : -0.014 yes

### Grid

    model.alphas_
    array([0.00145097, 0.00091279, 0.00078381, 0.00076329, 0.00066709,
        0.00058632, 0.00056714, 0.0005586 , 0.00041656, 0.0003813 ,
        0.00035643, 0.00034924, 0.000345  , 0.00033496, 0.00031425,
        0.00030957, 0.00029335, 0.00029041, 0.00027613, 0.00026769,
        0.0002629 , 0.00025293, 0.00025093, 0.0002473 , 0.00023157,
        0.00022688, 0.0002202 , 0.00022007, 0.00021279, 0.00021016,
        0.00020668, 0.00020487, 0.00020047, 0.00019916, 0.00019909,
        0.00019695, 0.00018677, 0.00018533, 0.00018219, 0.00017915,
        0.00017863, 0.00017561, 0.00017409, 0.00017221, 0.0001718 ,
        0.00017072, 0.00017047, 0.00016915, 0.00016724, 0.00016476,
        0.00016369, 0.00016101, 0.00016038, 0.00015949, 0.00015905,
        0.00015731, 0.00015586, 0.00015421, 0.00015357, 0.00015255,
        0.00014551, 0.00014518, 0.00014359, 0.00014156, 0.00014101,
        0.00012934, 0.00012827, 0.00012774, 0.00012657, 0.00012609,
        0.00012599, 0.00012499, 0.00013964])
















## LassoCV4

### Code

    model = skl.LassoCV(normalize = True, cv = 4)
    model.fit(X,Y)
    predictions = model.predict(X)

### Results

    Time to run: 146.17036056518555 to run
    \lambda:  (1.0976026558339681e-05,) log10: [-4.95955485] ln: [-11.41979707]
    Coefficients: 
    [ 0.00399206 -0.         -0.13001351 ... -0.00634325  0.
    -0.        ]
    Mean squared error: 0.29
    Coefficient of determination: 0.57
    age ( age ) : 0.004
    educ_cat_1.0 (  ) : -0.130
    educ_cat_2.0 (  ) : -0.035
    educ_cat_4.0 (  ) : 0.066
    educ_cat_5.0 (  ) : 0.292
    race_cat_1.0 (  ) : 0.041
    race_cat_2.0 (  ) : -0.013
    male_0.0 (  ) : -0.275
    hhtenure_1 ( owned or being bought ) : 0.051
    hhtenure_3 ( occupied without payment of cash rent ) : -0.021
    region_11 ( new england division ) : 0.029
    region_21 ( east north central division ) : -0.007
    region_32 ( east south central division ) : -0.039
    region_42 ( pacific division ) : 0.034
    metarea_120 ( albany, ga ) : -0.098
    metarea_280 ( altoona, pa msa ) : -0.023
    metarea_320 ( amarillo, tx ) : -0.003
    metarea_440 ( ann arbor, mi ) : 0.075
    metarea_462 ( oshkosh-neenah, wi ) : -0.167
    metarea_480 ( asheville, nc ) : -0.077
    metarea_521 ( atlanta-sandy springs-marietta, ga ) : 0.007
    metarea_641 ( austin-round rock, tx ) : 0.045
    metarea_680 ( bakersfield, ca ) : -0.124
    metarea_721 ( baltimore-towson, md ) : 0.065
    metarea_730 ( bangor, me ) : -0.035
    metarea_741 ( barnstable town, ma ) : -0.038
    metarea_760 ( baton rouge, la ) : 0.018
    metarea_841 ( beaumont-port arthur, tx ) : 0.062
    metarea_880 ( billings, mt ) : -0.024
    metarea_920 ( biloxi-gulfport, ms ) : -0.008
    metarea_960 ( binghamton, ny ) : -0.001
    metarea_1081 ( boise city-nampa, id ) : -0.071
    metarea_1124 ( boston-cambridge-quincy, ma-nh ) : 0.019
    metarea_1280 ( buffalo-niagara falls, ny ) : -0.038
    metarea_1360 ( cedar rapids, ia ) : -0.034
    metarea_1440 ( charleston-north charleston, sc ) : -0.016
    metarea_1480 ( charleston, wv ) : -0.074
    metarea_1605 ( chicago-naperville-joliet, il-in-wi ) : 0.052
    metarea_1700 ( coeur d'alene, id ) : -0.071
    metarea_1720 ( colorado springs, co ) : -0.003
    metarea_1800 ( columbus, ga/al ) : -0.116
    metarea_1922 ( dallas-fort worth-arlington, tx ) : 0.021
    metarea_1930 ( danbury, ct ) : 0.111
    metarea_2001 ( springfield, oh ) : -0.003
    metarea_2002 ( dayton, oh ) : -0.135
    metarea_2030 ( decatur, al ) : -0.012
    metarea_2083 ( denver-aurora, co ) : 0.030
    metarea_2241 ( duluth, mn/wi ) : -0.117
    metarea_2300 ( el centro, ca ) : -0.112
    metarea_2310 ( el paso, tx ) : -0.074
    metarea_2360 ( erie, pa ) : -0.119
    metarea_2400 ( eugene-springfield, or ) : -0.019
    metarea_2581 ( fayetteville-springdale-rogers, ar-mo ) : 0.033
    metarea_2640 ( flint, mi ) : -0.109
    metarea_2670 ( fort collins-loveland, co ) : -0.039
    metarea_2840 ( fresno, ca ) : -0.074
    metarea_2900 ( gainesville, fl ) : -0.058
    metarea_3060 ( greeley, co ) : -0.024
    metarea_3162 ( greenville, sc ) : -0.016
    metarea_3181 ( hagerstown-martinsburg, md-wv ) : 0.014
    metarea_3362 ( houston-baytown-sugar land, tx ) : 0.077
    metarea_3440 ( huntsville,al ) : -0.041
    metarea_3480 ( indianapolis, in ) : 0.021
    metarea_3520 ( jackson, mi ) : -0.048
    metarea_3560 ( jackson, ms ) : -0.015
    metarea_3590 ( jacksonville,fl ) : 0.002
    metarea_3600 ( jacksonville, nc ) : -0.013
    metarea_3621 ( janvesville, wi ) : -0.004
    metarea_3661 ( johnson city, tn ) : -0.046
    metarea_3760 ( kansas city, mo/ks ) : 0.047
    metarea_3830 ( kingston, ny ) : 0.010
    metarea_4000 ( lancaster, pa ) : 0.067
    metarea_4040 ( lansing-east lansing, mi ) : -0.019
    metarea_4100 ( las cruces, nm ) : -0.036
    metarea_4130 ( las vegas-paradise, nv ) : 0.015
    metarea_4150 ( lawrence, ks ) : 0.018
    metarea_4200 ( lawton, ok ) : -0.020
    metarea_4280 ( lexington-fayette, ky ) : -0.040
    metarea_4483 ( los angeles-long beach-santa ana, ca ) : 0.013
    metarea_4600 ( lubbock, tx ) : -0.066
    metarea_4640 ( lynchburg, va ) : -0.016
    metarea_4681 ( macon, ga ) : -0.048
    metarea_4720 ( madison, wi ) : 0.001
    metarea_4940 ( merced, ca ) : -0.030
    metarea_5001 ( miami-fort lauderdale-miami beach, fl ) : 0.037
    metarea_5081 ( milwaukee-waukesha-west allis, wi ) : -0.001
    metarea_5121 ( minneapolis-st. paul-bloomington, mn/wi ) : 0.038
    metarea_5220 ( monroe, mi ) : 0.093
    metarea_5321 ( muskegon-norton shores, mi ) : -0.055
    metarea_5331 ( myrtle beach-conway-north myrtle beach, sc ) : -0.066
    metarea_5481 ( new haven, ct ) : 0.008
    metarea_5606 ( new york-northern new jersey-long island, ny-nj-pa ) : 0.192
    metarea_5790 ( ocala, fl ) : -0.074
    metarea_5801 ( midland, tx ) : 0.092
    metarea_5840 ( ocean city, nj ) : -0.303
    metarea_5910 ( olympia, wa ) : -0.082
    metarea_5960 ( orlando, fl ) : -0.052
    metarea_6081 ( pensacola-ferry pass-brent, fl ) : -0.084
    metarea_6161 ( philadelphia-camden-wilmington, pa/nj/de ) : 0.052
    metarea_6201 ( phoenix-mesa-scottsdale, az ) : 0.009
    metarea_6280 ( pittsburg, pa ) : -0.010
    metarea_6401 ( portland-south portland, me ) : 0.035
    metarea_6520 ( provo-orem, ut ) : -0.016
    metarea_6680 ( reading, pa ) : -0.081
    metarea_6980 ( st. cloud, mn ) : -0.044
    metarea_7130 ( salisbury, md ) : -0.067
    metarea_7321 ( san diego-carlsbad-san marcos, ca ) : 0.034
    metarea_7364 ( napa, ca ) : 0.032
    metarea_7365 ( san francisco-oakland-fremont, ca ) : 0.118
    metarea_7401 ( san jose-sunnyvale-santa clara, ca ) : 0.148
    metarea_7461 ( san luis obispo-paso robles, ca ) : 0.063
    metarea_7471 ( santa barbara-santa maria-goleta, ca ) : 0.053
    metarea_7481 ( santa cruz-watsonville, ca ) : 0.043
    metarea_7511 ( sarasota-bradenton-venice, fl ) : 0.001
    metarea_7520 ( savannah, ga ) : 0.030
    metarea_7601 ( seattle-tacoma-bellevue, wa ) : 0.013
    metarea_7760 ( sioux falls, sd ) : -0.020
    metarea_7920 ( springfield, mo ) : -0.020
    metarea_8160 ( syracuse, ny ) : -0.007
    metarea_8240 ( tallahassee, fl ) : -0.003
    metarea_8440 ( topeka, ks ) : 0.020
    metarea_8600 ( tuscaloosa, al ) : -0.041
    metarea_8731 ( oxnard-thousand oaks-ventura, ca ) : 0.060
    metarea_8740 ( vero beach, fl ) : -0.073
    metarea_8750 ( victoria, tx ) : -0.005
    metarea_8760 ( vineland-milville-bridgetown, nj ) : 0.058
    metarea_8781 ( visalia-porterville, ca ) : -0.015
    metarea_8840 ( washington, dc/md/va ) : 0.155
    metarea_8920 ( waterloo-cedar falls, ia ) : -0.033
    metarea_8940 ( wausau, wi ) : -0.032
    metarea_9040 ( wichita, ks ) : -0.040
    metarea_9321 ( youngstown-warren-boardman, oh ) : -0.086
    metarea_9997 ( other metropolitan areas, unidentified ) : -0.043
    metarea_9998 ( niu, household not in a metropolitan area ) : -0.066
    metarea_9999 ( missing data ) : -0.019
    unitsstr_1 ( mobile home or trailer ) : -0.030
    unitsstr_7 ( 5-9 family building ) : -0.006
    unitsstr_11 ( one unit, unspecified type ) : 0.025
    nfams_1 ( 1 family or n/a ) : 0.006
    nfams_6 ( 6 ) : -0.067
    nfams_8 ( 8 ) : 0.120
    ncouples_2 ( 2 ) : -0.057
    nmothers_2 ( 2 ) : -0.022
    nmothers_3 ( 3 ) : -0.087
    nfathers_2 ( 2 ) : -0.021
    nfathers_3 ( 3 ) : -0.047
    marst_1 ( married, spouse present ) : 0.103
    marst_3 ( separated ) : -0.023
    marst_5 ( widowed ) : -0.040
    marst_6 ( never married/single ) : -0.074
    famsize_6 ( 6 family members present ) : -0.008
    famsize_7 ( 7 family members present ) : -0.012
    famsize_8 ( 8 family members present ) : -0.028
    famsize_14 ( 14 family members present ) : -0.062
    famsize_15 ( 15 family members present ) : -0.259
    ftype_2 ( nonfamily householder ) : 0.044
    ftype_3 ( related subfamily ) : -0.060
    ftype_4 ( unrelated subfamily ) : -0.018
    famkind_1 ( husband/wife family ) : -0.036
    famkind_3 ( female reference person ) : 0.127
    yrimmig_1985 ( 1984-1985 ) : 0.006
    yrimmig_2001 ( 2000-2001 (2001 cps: 1998-2001) ) : -0.012
    yrimmig_2003 ( 2002-2003 (2003 cps: 2000-2003) ) : -0.014
    yrimmig_2005 ( 2004-2005 (2005 cps: 2002-2005) ) : -0.040
    yrimmig_2007 ( 2004-2007 ) : -0.021
    yrimmig_2009 ( 2006-2009 ) : -0.023
    yrimmig_2012 ( 2010-2012 (2014 cps: 2010-2011) ) : -0.066
    citizen_1 ( born in u.s ) : 0.000
    citizen_3 ( born abroad of american parents ) : 0.011
    citizen_5 ( not a citizen ) : -0.059
    hispan_0 ( not hispanic ) : 0.011
    hispan_410 ( central/south american ) : -0.010
    occ_0 ( Missing data? ) : -0.275
    occ_10 ( chief executives and legislators/public administration ) : 0.077
    occ_20 ( general and operations managers ) : 0.081
    occ_136 (  ) : 0.079
    occ_150 ( purchasing managers ) : 0.037
    occ_220 ( constructions managers ) : 0.091
    occ_325 (  ) : 0.132
    occ_340 (  ) : -0.004
    occ_350 ( medical and health services managers ) : 0.121
    occ_420 ( social and community service managers ) : 0.021
    occ_500 ( agents and business managers of artists, performers, and athletes ) : 0.335
    occ_565 (  ) : 0.101
    occ_600 ( cost estimators ) : 0.252
    occ_630 (  ) : 0.003
    occ_640 (  ) : 0.024
    occ_650 (  ) : 0.048
    occ_725 (  ) : 0.066
    occ_735 (  ) : 0.180
    occ_810 ( appraisers and assessors of real estate ) : 0.062
    occ_830 ( credit analysts ) : 0.056
    occ_850 ( personal financial advisors ) : 0.094
    occ_860 ( insurance underwriters ) : 0.018
    occ_940 ( tax preparers ) : -0.147
    occ_950 ( financial specialists, nec ) : 0.031
    occ_1005 (  ) : 0.043
    occ_1010 ( computer programmers ) : 0.006
    occ_1020 ( software developers, applications and systems software ) : 0.065
    occ_1060 ( database administrators ) : 0.206
    occ_1105 (  ) : 0.101
    occ_1240 ( mathematical science occupations, nec ) : 0.004
    occ_1320 ( aerospace engineers ) : 0.102
    occ_1330 (  ) : 0.064
    occ_1350 ( chemical engineers ) : 0.177
    occ_1430 ( industrial engineers, including health and safety ) : 0.070
    occ_1460 ( mechanical engineers ) : 0.166
    occ_1520 ( petroleum, mining and geological engineers, including mining safety engineers ) : 0.301
    occ_1530 ( engineers, nec ) : 0.018
    occ_1540 ( drafters ) : 0.015
    occ_1660 (  ) : 0.177
    occ_1700 ( astronomers and physicists ) : 0.076
    occ_1720 ( chemists and materials scientists ) : 0.083
    occ_1800 ( economists and market researchers ) : 0.240
    occ_1820 ( psychologists ) : 0.049
    occ_1860 (  ) : -0.011
    occ_1910 ( biological technicians ) : -0.093
    occ_1930 ( geological and petroleum technicians, and nuclear technicians ) : -0.159
    occ_1965 (  ) : -0.006
    occ_2000 ( counselors ) : -0.005
    occ_2060 ( religious workers, nec ) : -0.410
    occ_2100 ( lawyers, and judges, magistrates, and other judicial workers ) : 0.067
    occ_2160 (  ) : -0.009
    occ_2200 ( postsecondary teachers ) : 0.039
    occ_2300 ( preschool and kindergarten teachers ) : -0.018
    occ_2430 ( librarians ) : -0.021
    occ_2440 ( library technicians ) : -0.298
    occ_2540 ( teacher assistants ) : -0.044
    occ_2710 (  ) : 0.097
    occ_2750 ( musicians, singers, and related workers ) : -0.249
    occ_2825 ( public relations specialists ) : 0.089
    occ_2830 (  ) : 0.011
    occ_2960 (  ) : -0.661
    occ_3010 ( dentists ) : 0.206
    occ_3060 ( physicians and surgeons ) : 0.191
    occ_3110 ( physician assistants ) : 0.093
    occ_3160 ( physical therapists ) : 0.042
    occ_3200 ( radiation therapists ) : 0.096
    occ_3230 ( speech language pathologists ) : 0.100
    occ_3235 (  ) : -0.911
    occ_3255 (  ) : 0.152
    occ_3257 (  ) : 0.100
    occ_3420 (  ) : -0.087
    occ_3600 ( nursing, psychiatric, and home health aides ) : -0.009
    occ_3620 ( physical therapist assistants and aides ) : 0.029
    occ_3645 (  ) : -0.032
    occ_3740 ( firefighters ) : 0.057
    occ_3800 ( sheriffs, bailiffs, correctional officers, and jailers ) : -0.024
    occ_3850 (  ) : 0.057
    occ_3860 (  ) : 0.183
    occ_3900 ( animal control ) : -0.054
    occ_3940 ( crossing guards ) : -0.029
    occ_4000 ( chefs and cooks ) : -0.032
    occ_4020 (  ) : -0.073
    occ_4040 ( bartenders ) : -0.207
    occ_4050 ( combined food preparation and serving workers, including fast food ) : -0.175
    occ_4060 ( counter attendant, cafeteria, food concession, and coffee shop ) : -0.253
    occ_4120 ( food servers, nonrestaurant ) : -0.085
    occ_4140 ( dishwashers ) : -0.211
    occ_4220 ( janitors and building cleaners ) : -0.033
    occ_4230 ( maids and housekeeping cleaners ) : -0.060
    occ_4250 ( grounds maintenance workers ) : -0.037
    occ_4350 ( nonfarm animal caretakers ) : -0.121
    occ_4430 ( entertainment attendants and related workers, nec ) : -0.185
    occ_4460 ( funeral service workers and embalmers ) : -0.184
    occ_4530 ( baggage porters, bellhops, and concierges ) : -0.030
    occ_4540 ( tour and travel guides ) : 0.065
    occ_4600 ( childcare workers ) : -0.243
    occ_4610 ( personal care aides ) : -0.053
    occ_4640 ( residential advisors ) : -0.057
    occ_4700 ( first-line supervisors of sales workers ) : 0.008
    occ_4720 ( cashiers ) : -0.032
    occ_4760 ( retail salespersons ) : -0.012
    occ_4840 ( sales representatives, services, all other ) : 0.005
    occ_4850 ( sales representatives, wholesale and manufacturing ) : 0.112
    occ_4900 ( models, demonstrators, and product promoters ) : -0.139
    occ_4920 ( real estate brokers and sales agents ) : 0.167
    occ_4950 ( door-to-door sales workers, news and street vendors, and related workers ) : -0.204
    occ_5000 ( first-line supervisors of office and administrative support workers ) : 0.027
    occ_5010 ( switchboard operators, including answering service ) : -0.129
    occ_5110 ( billing and posting clerks ) : -0.083
    occ_5120 ( bookkeeping, accounting, and auditing clerks ) : -0.080
    occ_5160 ( bank tellers ) : -0.043
    occ_5220 ( court, municipal, and license clerks ) : -0.092
    occ_5310 ( interviewers, except eligibility and loan ) : -0.043
    occ_5360 ( human resources assistants, except payroll and timekeeping ) : -0.017
    occ_5400 ( receptionists and information clerks ) : -0.056
    occ_5530 ( meter readers, utilities ) : -0.043
    occ_5540 ( postal service clerks ) : -0.015
    occ_5610 ( shipping, receiving, and traffic clerks ) : -0.170
    occ_5820 ( word processors and typists ) : -0.174
    occ_5840 ( insurance claims and policy processing clerks ) : -0.047
    occ_5920 ( statistical assistants ) : -0.012
    occ_5940 ( office and administrative support workers, nec ) : -0.051
    occ_6220 ( brickmasons, blockmasons, and stonemasons ) : -0.028
    occ_6260 ( construction laborers ) : -0.070
    occ_6320 ( construction equipment operators except paving, surfacing, and tamping equipment operators ) : 0.066
    occ_6330 ( drywall installers, ceiling tile installers, and tapers ) : -0.110
    occ_6500 ( reinforcing iron and rebar workers ) : -0.158
    occ_6730 ( highway maintenance workers ) : -0.054
    occ_6750 (  ) : -0.280
    occ_6800 ( derrick, rotary drill, and service unit operators, and roustabouts, oil, gas, and mining ) : 0.013
    occ_6840 ( mining machine operators ) : 0.010
    occ_6910 (  ) : -0.087
    occ_6920 (  ) : -0.077
    occ_7000 ( first-line supervisors of mechanics, installers, and repairers ) : 0.076
    occ_7130 ( security and fire alarm systems installers ) : 0.080
    occ_7140 ( aircraft mechanics and service technicians ) : 0.002
    occ_7260 ( vehicle and mobile equipment mechanics, installers, and repairers, nec ) : -0.152
    occ_7360 ( millwrights ) : 0.034
    occ_7410 ( electrical power-line installers and repairers ) : 0.074
    occ_7440 (  ) : -0.160
    occ_7510 ( coin, vending, and amusement machine servicers and repairers ) : -0.120
    occ_7560 ( riggers ) : 0.000
    occ_7700 ( first-line supervisors of production and operating workers ) : 0.065
    occ_7710 ( aircraft structure, surfaces, rigging, and systems assemblers ) : -0.009
    occ_7720 ( electrical, electronics, and electromechanical assemblers ) : -0.000
    occ_7750 ( assemblers and fabricators, nec ) : -0.046
    occ_7800 ( bakers ) : -0.134
    occ_7855 ( food processing, nec ) : -0.023
    occ_8000 ( grinding, lapping, polishing, and buffing machine tool setters, operators, and tenders, metal and plastic ) : -0.128
    occ_8100 ( molders and molding machine setters, operators, and tenders, metal and plastic ) : -0.059
    occ_8250 ( prepress technicians and workers ) : 0.022
    occ_8255 (  ) : -0.132
    occ_8300 ( laundry and dry-cleaning workers ) : -0.021
    occ_8330 ( shoe and leather workers and repairers ) : -0.219
    occ_8350 ( tailors, dressmakers, and sewers ) : -0.119
    occ_8440 (  ) : 0.863
    occ_8550 ( woodworkers including model makers and patternmakers, nec ) : -0.120
    occ_8620 ( water wastewater treatment plant and system operators ) : 0.007
    occ_8630 ( plant and system operators, nec ) : 0.132
    occ_8650 ( crushing, grinding, polishing, mixing, and blending workers ) : -0.074
    occ_8740 ( inspectors, testers, sorters, samplers, and weighers ) : -0.032
    occ_8760 ( medical, dental, and ophthalmic laboratory technicians ) : -0.093
    occ_8800 ( packaging and filling machine operators and tenders ) : -0.034
    occ_8810 ( painting workers and dyers ) : -0.056
    occ_8830 ( photographic process workers and processing machine operators ) : -0.042
    occ_8950 ( helpers--production workers ) : -0.074
    occ_8965 ( other production workers including semiconductor processors and cooling and freezing equipment operators ) : -0.095
    occ_9110 (  ) : -0.374
    occ_9120 (  ) : -0.236
    occ_9150 ( motor vehicle operators, all other ) : -0.157
    occ_9200 ( locomotive engineers and operators ) : 0.110
    occ_9240 ( railroad conductors and yardmasters ) : 0.098
    occ_9330 (  ) : 0.150
    occ_9350 ( parking lot attendants ) : -0.097
    occ_9600 ( industrial truck and tractor operators ) : -0.115
    occ_9620 ( laborers and freight, stock, and material movers, hand ) : -0.080
    occ_9640 ( packers and packagers, hand ) : -0.313
    occ_9720 ( refuse and recyclable material collectors ) : -0.054
    occ_9730 (  ) : 0.000
    occ_9840 (  ) : -0.238
    ind_0 (  ) : -0.026
    ind_280 (  ) : 0.065
    ind_370 (  ) : 0.032
    ind_380 (  ) : 0.104
    ind_390 (  ) : 0.014
    ind_470 (  ) : 0.113
    ind_570 (  ) : 0.040
    ind_580 (  ) : 0.129
    ind_680 (  ) : 0.014
    ind_690 (  ) : 0.131
    ind_1190 (  ) : -0.030
    ind_1480 (  ) : -0.117
    ind_1670 (  ) : -0.033
    ind_1680 (  ) : -0.083
    ind_1790 (  ) : 0.072
    ind_1870 (  ) : 0.021
    ind_1880 (  ) : -0.007
    ind_2290 (  ) : 0.009
    ind_2390 (  ) : 0.051
    ind_2470 (  ) : -0.035
    ind_2670 (  ) : 0.081
    ind_2680 (  ) : 0.019
    ind_2790 (  ) : -0.040
    ind_3090 (  ) : 0.005
    ind_3170 (  ) : 0.110
    ind_3360 (  ) : 0.036
    ind_3380 (  ) : 0.009
    ind_3390 (  ) : 0.032
    ind_3570 (  ) : 0.040
    ind_3580 (  ) : 0.008
    ind_3670 (  ) : 0.007
    ind_3970 (  ) : 0.001
    ind_4090 (  ) : 0.021
    ind_4170 (  ) : 0.094
    ind_4380 (  ) : 0.064
    ind_4470 (  ) : 0.004
    ind_4670 (  ) : 0.043
    ind_4870 (  ) : -0.033
    ind_4880 (  ) : -0.066
    ind_4990 (  ) : -0.107
    ind_5070 (  ) : -0.027
    ind_5190 (  ) : -0.052
    ind_5380 (  ) : -0.016
    ind_5590 (  ) : 0.050
    ind_5690 (  ) : -0.043
    ind_6080 (  ) : 0.151
    ind_6270 (  ) : 0.117
    ind_6480 (  ) : 0.018
    ind_6490 (  ) : 0.103
    ind_6570 (  ) : 0.040
    ind_6670 (  ) : 0.001
    ind_6680 (  ) : 0.003
    ind_6970 (  ) : 0.069
    ind_6990 (  ) : 0.033
    ind_7080 (  ) : -0.025
    ind_7190 (  ) : 0.108
    ind_7380 (  ) : 0.035
    ind_7470 (  ) : 0.022
    ind_7570 (  ) : 0.027
    ind_7680 (  ) : -0.008
    ind_7770 (  ) : -0.047
    ind_7860 (  ) : -0.010
    ind_7890 (  ) : -0.075
    ind_7980 (  ) : 0.004
    ind_8170 (  ) : -0.042
    ind_8190 (  ) : 0.027
    ind_8370 (  ) : -0.037
    ind_8380 (  ) : -0.014
    ind_8470 (  ) : -0.036
    ind_8570 (  ) : -0.019
    ind_8580 (  ) : -0.232
    ind_8590 (  ) : -0.051
    ind_8660 (  ) : -0.024
    ind_8670 (  ) : -0.047
    ind_8870 (  ) : 0.049
    ind_8880 (  ) : -0.041
    ind_8980 (  ) : -0.028
    ind_9090 (  ) : -0.085
    ind_9290 (  ) : -0.039
    ind_9370 (  ) : -0.004
    ind_9890 (  ) : -0.004
    educ_10 ( grades 1, 2, 3, or 4 ) : -0.049
    educ_20 ( grades 5 or 6 ) : -0.025
    educ_30 ( grades 7 or 8 ) : -0.005
    educ_71 ( 12th grade, no diploma ) : 0.007
    educ_73 ( high school diploma or equivalent ) : -0.000
    educ_81 ( some college but no degree ) : -0.005
    educ_91 ( associate's degree, occupational/vocational program ) : 0.006
    educ_111 ( bachelor's degree ) : 0.079
    educ_124 ( professional school degree ) : 0.018
    educ_125 ( doctorate degree ) : 0.107
    occly_10 ( chief executives and legislators/public administration ) : 0.523
    occly_20 ( general and operations managers ) : 0.288
    occly_40 (  ) : 0.277
    occly_50 (  ) : 0.365
    occly_60 (  ) : 0.204
    occly_100 ( administrative services managers ) : 0.056
    occly_110 ( computer and information systems managers ) : 0.401
    occly_120 ( financial managers ) : 0.271
    occly_136 (  ) : 0.161
    occly_137 (  ) : 0.074
    occly_140 ( industrial production managers ) : 0.268
    occly_150 ( purchasing managers ) : 0.138
    occly_160 ( transportation, storage, and distribution managers ) : 0.052
    occly_205 ( farmers, ranchers, and other agricultural managers ) : -0.032
    occly_220 ( constructions managers ) : 0.258
    occly_230 ( education administrators ) : 0.220
    occly_300 ( architectural and engineering managers ) : 0.382
    occly_310 ( food service and lodging managers ) : 0.027
    occly_350 ( medical and health services managers ) : 0.153
    occly_360 ( natural science managers ) : 0.057
    occly_410 ( property, real estate, and community association managers ) : 0.128
    occly_420 ( social and community service managers ) : 0.050
    occly_430 ( managers, nec (including postmasters) ) : 0.245
    occly_520 ( wholesale and retail buyers, except farm products ) : 0.027
    occly_630 (  ) : 0.147
    occly_710 ( management analysts ) : 0.171
    occly_726 (  ) : 0.035
    occly_740 (  ) : 0.034
    occly_800 ( accountants and auditors ) : 0.147
    occly_820 ( budget analysts ) : 0.085
    occly_840 ( financial analysts ) : 0.223
    occly_850 ( personal financial advisors ) : 0.088
    occly_910 ( credit counselors and loan officers ) : 0.045
    occly_940 ( tax preparers ) : -0.159
    occly_1006 (  ) : 0.267
    occly_1010 ( computer programmers ) : 0.184
    occly_1020 ( software developers, applications and systems software ) : 0.265
    occly_1030 (  ) : 0.058
    occly_1106 (  ) : 0.373
    occly_1107 (  ) : 0.087
    occly_1200 ( actuaries ) : 0.596
    occly_1220 ( operations research analysts ) : 0.094
    occly_1300 ( architects, except naval ) : 0.101
    occly_1320 ( aerospace engineers ) : 0.222
    occly_1330 (  ) : 0.000
    occly_1360 ( civil engineers ) : 0.224
    occly_1400 ( computer hardware engineers ) : 0.187
    occly_1410 ( electrical and electronics engineers ) : 0.248
    occly_1420 ( environmental engineers ) : 0.169
    occly_1430 ( industrial engineers, including health and safety ) : 0.028
    occly_1440 ( marine engineers and naval architects ) : 0.297
    occly_1500 (  ) : 0.265
    occly_1530 ( engineers, nec ) : 0.258
    occly_1660 (  ) : 0.039
    occly_1700 ( astronomers and physicists ) : 0.038
    occly_1710 ( atmospheric and space scientists ) : -0.088
    occly_1800 ( economists and market researchers ) : 0.058
    occly_1860 (  ) : -0.119
    occly_1930 ( geological and petroleum technicians, and nuclear technicians ) : -0.000
    occly_1965 (  ) : -0.076
    occly_2000 ( counselors ) : -0.000
    occly_2016 (  ) : -0.011
    occly_2025 (  ) : -0.011
    occly_2060 ( religious workers, nec ) : -0.060
    occly_2100 ( lawyers, and judges, magistrates, and other judicial workers ) : 0.277
    occly_2300 ( preschool and kindergarten teachers ) : -0.018
    occly_2320 ( secondary school teachers ) : 0.058
    occly_2330 ( special education teachers ) : 0.033
    occly_2340 ( other teachers and instructors ) : -0.195
    occly_2430 ( librarians ) : -0.019
    occly_2540 ( teacher assistants ) : -0.408
    occly_2550 ( education, training, and library workers, nec ) : -0.006
    occly_2700 ( actors, producers, and directors ) : 0.045
    occly_2720 ( athletes, coaches, umpires, and related workers ) : -0.183
    occly_2740 ( dancers and choreographers ) : -0.356
    occly_2760 ( entertainers and performers, sports and related workers, all other ) : 0.159
    occly_2800 ( announcers ) : 0.214
    occly_2825 ( public relations specialists ) : 0.126
    occly_2840 ( technical writers ) : 0.066
    occly_2850 ( writers and authors ) : 0.177
    occly_2910 ( photographers ) : -0.118
    occly_2960 (  ) : -0.128
    occly_3000 ( chiropractors ) : -0.147
    occly_3010 ( dentists ) : 0.313
    occly_3030 ( dieticians and nutritionists ) : -0.028
    occly_3040 ( optometrists ) : 0.121
    occly_3050 ( pharmacists ) : 0.538
    occly_3060 ( physicians and surgeons ) : 0.371
    occly_3110 ( physician assistants ) : 0.099
    occly_3120 ( podiatrists ) : 0.750
    occly_3150 ( occupational therapists ) : 0.146
    occly_3160 ( physical therapists ) : 0.071
    occly_3200 ( radiation therapists ) : 0.084
    occly_3220 ( respiratory therapists ) : 0.101
    occly_3230 ( speech language pathologists ) : 0.019
    occly_3235 (  ) : -0.055
    occly_3250 ( veterinarians ) : 0.323
    occly_3255 (  ) : 0.081
    occly_3256 (  ) : 0.608
    occly_3257 (  ) : 0.045
    occly_3258 (  ) : 0.311
    occly_3310 ( dental hygienists ) : 0.185
    occly_3320 ( diagnostic related technologists and technicians ) : 0.159
    occly_3420 (  ) : -0.001
    occly_3500 ( licensed practical and licensed vocational nurses ) : 0.035
    occly_3510 ( medical records and health information technicians ) : -0.194
    occly_3600 ( nursing, psychiatric, and home health aides ) : -0.255
    occly_3610 ( occupational therapy assistants and aides ) : 0.174
    occly_3630 ( massage therapists ) : -0.145
    occly_3645 (  ) : -0.193
    occly_3647 (  ) : -0.145
    occly_3649 (  ) : -0.164
    occly_3655 (  ) : -0.271
    occly_3710 ( first-line supervisors of police and detectives ) : 0.165
    occly_3720 ( first-line supervisors of fire fighting and prevention workers ) : 0.209
    occly_3820 ( police officers and detectives ) : 0.149
    occly_3840 (  ) : -0.232
    occly_3850 (  ) : 0.060
    occly_3860 (  ) : 0.122
    occly_3900 ( animal control ) : 0.553
    occly_3930 ( security guards and gaming surveillance officers ) : -0.239
    occly_3940 ( crossing guards ) : -0.988
    occly_3955 (  ) : -0.479
    occly_4010 ( first-line supervisors of food preparation and serving workers ) : -0.081
    occly_4020 (  ) : -0.263
    occly_4030 ( food preparation workers ) : -0.398
    occly_4050 ( combined food preparation and serving workers, including fast food ) : -0.318
    occly_4060 ( counter attendant, cafeteria, food concession, and coffee shop ) : -0.252
    occly_4110 ( waiters and waitresses ) : -0.334
    occly_4120 ( food servers, nonrestaurant ) : -0.380
    occly_4130 ( food preparation and serving related workers, nec ) : -0.330
    occly_4140 ( dishwashers ) : -0.434
    occly_4150 ( host and hostesses, restaurant, lounge, and coffee shop ) : -0.541
    occly_4200 ( first-line supervisors of housekeeping and janitorial workers ) : -0.039
    occly_4220 ( janitors and building cleaners ) : -0.271
    occly_4230 ( maids and housekeeping cleaners ) : -0.337
    occly_4250 ( grounds maintenance workers ) : -0.208
    occly_4300 ( first-line supervisors of gaming workers ) : 0.113
    occly_4350 ( nonfarm animal caretakers ) : -0.052
    occly_4430 ( entertainment attendants and related workers, nec ) : -0.187
    occly_4520 ( personal appearance workers, nec ) : -0.247
    occly_4530 ( baggage porters, bellhops, and concierges ) : -0.312
    occly_4540 ( tour and travel guides ) : -1.049
    occly_4600 ( childcare workers ) : -0.093
    occly_4610 ( personal care aides ) : -0.338
    occly_4620 ( recreation and fitness workers ) : -0.362
    occly_4650 ( personal care and service workers, all other ) : -0.251
    occly_4700 ( first-line supervisors of sales workers ) : 0.076
    occly_4710 (  ) : 0.175
    occly_4720 ( cashiers ) : -0.386
    occly_4760 ( retail salespersons ) : -0.228
    occly_4800 ( advertising sales agents ) : 0.040
    occly_4810 ( insurance sales agents ) : 0.006
    occly_4820 ( securities, commodities, and financial services sales agents ) : 0.072
    occly_4840 ( sales representatives, services, all other ) : 0.016
    occly_4850 ( sales representatives, wholesale and manufacturing ) : 0.066
    occly_4900 ( models, demonstrators, and product promoters ) : -0.273
    occly_4920 ( real estate brokers and sales agents ) : 0.016
    occly_4930 ( sales engineers ) : 0.181
    occly_4940 ( telemarketers ) : -0.416
    occly_4950 ( door-to-door sales workers, news and street vendors, and related workers ) : -0.213
    occly_5000 ( first-line supervisors of office and administrative support workers ) : 0.039
    occly_5010 ( switchboard operators, including answering service ) : -0.195
    occly_5100 ( bill and account collectors ) : -0.081
    occly_5160 ( bank tellers ) : -0.259
    occly_5240 ( customer service representatives ) : -0.139
    occly_5260 ( file clerks ) : -0.166
    occly_5300 ( hotel, motel, and resort desk clerks ) : -0.180
    occly_5310 ( interviewers, except eligibility and loan ) : -0.181
    occly_5320 ( library assistants, clerical ) : -0.585
    occly_5340 ( new account clerks ) : -0.097
    occly_5350 ( correspondent clerks and order clerks ) : -0.081
    occly_5400 ( receptionists and information clerks ) : -0.180
    occly_5410 ( reservation and transportation ticket agents and travel clerks ) : -0.071
    occly_5420 ( information and record clerks, all other ) : -0.164
    occly_5510 ( couriers and messengers ) : -0.067
    occly_5560 ( postal service mail sorters, processors, and processing machine operators ) : -0.217
    occly_5610 ( shipping, receiving, and traffic clerks ) : -0.021
    occly_5620 ( stock clerks and order fillers ) : -0.341
    occly_5630 ( weighers, measurers, checkers, and samplers, recordkeeping ) : -0.081
    occly_5700 ( secretaries and administrative assistants ) : -0.061
    occly_5810 ( data entry keyers ) : -0.186
    occly_5840 ( insurance claims and policy processing clerks ) : -0.064
    occly_5850 ( mail clerks and mail machine operators, except postal service ) : -0.456
    occly_5860 ( office clerks, general ) : -0.206
    occly_6005 ( first-line supervisors of farming, fishing, and forestry workers ) : 0.008
    occly_6040 ( graders and sorters, agricultural products ) : -0.272
    occly_6050 ( agricultural workers, nec ) : -0.150
    occly_6100 ( fishing and hunting workers ) : 0.182
    occly_6200 ( first-line supervisors of construction trades and extraction workers ) : 0.215
    occly_6210 ( boilermakers ) : -0.124
    occly_6230 ( carpenters ) : -0.079
    occly_6240 ( carpet, floor, and tile installers and finishers ) : -0.042
    occly_6250 ( cement masons, concrete finishers, and terrazzo workers ) : -0.025
    occly_6260 ( construction laborers ) : -0.078
    occly_6300 ( paving, surfacing, and tamping equipment operators ) : 0.072
    occly_6320 ( construction equipment operators except paving, surfacing, and tamping equipment operators ) : 0.002
    occly_6355 ( electricians ) : 0.078
    occly_6420 ( painters, construction and maintenance ) : -0.268
    occly_6440 ( pipelayers, plumbers, pipefitters, and steamfitters ) : 0.039
    occly_6460 ( plasterers and stucco masons ) : -0.194
    occly_6515 ( roofers ) : -0.079
    occly_6600 ( helpers, construction trades ) : -0.238
    occly_6700 ( elevator installers and repairers ) : 0.114
    occly_6710 ( fence erectors ) : -0.389
    occly_6800 ( derrick, rotary drill, and service unit operators, and roustabouts, oil, gas, and mining ) : 0.313
    occly_6820 ( earth drillers, except oil and gas ) : 0.225
    occly_6940 ( extraction workers, nec ) : 0.064
    occly_7010 ( computer, automated teller, and office machine repairers ) : -0.040
    occly_7100 ( electrical and electronics repairers, transportation equipment, and industrial and utility ) : 0.045
    occly_7130 ( security and fire alarm systems installers ) : 0.031
    occly_7140 ( aircraft mechanics and service technicians ) : 0.049
    occly_7160 ( automotive glass installers and repairers ) : -0.132
    occly_7200 ( automotive service technicians and mechanics ) : -0.013
    occly_7220 ( heavy vehicle and mobile equipment service technicians and mechanics ) : 0.065
    occly_7360 ( millwrights ) : 0.102
    occly_7420 ( telecommunications line installers and repairers ) : 0.057
    occly_7510 ( coin, vending, and amusement machine servicers and repairers ) : -0.021
    occly_7560 ( riggers ) : 0.005
    occly_7610 ( helpers--installation, maintenance, and repair workers ) : -0.411
    occly_7700 ( first-line supervisors of production and operating workers ) : 0.038
    occly_7710 ( aircraft structure, surfaces, rigging, and systems assemblers ) : -0.137
    occly_7720 ( electrical, electronics, and electromechanical assemblers ) : -0.122
    occly_7730 ( engine and other machine assemblers ) : -0.072
    occly_7750 ( assemblers and fabricators, nec ) : -0.156
    occly_7800 ( bakers ) : -0.211
    occly_7810 ( butchers and other meat, poultry, and fish processing workers ) : -0.119
    occly_7830 ( food and tobacco roasting, baking, and drying machine operators and tenders ) : -0.098
    occly_7840 ( food batchmakers ) : -0.289
    occly_7855 ( food processing, nec ) : -0.035
    occly_7950 ( cutting, punching, and press machine setters, operators, and tenders, metal and plastic ) : -0.156
    occly_8000 ( grinding, lapping, polishing, and buffing machine tool setters, operators, and tenders, metal and plastic ) : -0.063
    occly_8220 ( metal workers and plastic workers, nec ) : -0.078
    occly_8300 ( laundry and dry-cleaning workers ) : -0.162
    occly_8310 ( pressers, textile, garment, and related materials ) : -0.387
    occly_8320 ( sewing machine operators ) : -0.284
    occly_8340 ( shoe machine operators and tenders ) : -0.011
    occly_8400 ( textile bleaching and dyeing, and cutting machine setters, operators, and tenders ) : -0.071
    occly_8410 ( textile knitting and weaving machine setters, operators, and tenders ) : -0.293
    occly_8440 (  ) : 0.093
    occly_8460 ( textile, apparel, and furnishings workers, nec ) : -0.068
    occly_8510 ( furniture finishers ) : -0.203
    occly_8600 ( power plant operators, distributors, and dispatchers ) : 0.295
    occly_8630 ( plant and system operators, nec ) : 0.100
    occly_8710 ( cutting workers ) : -0.173
    occly_8740 ( inspectors, testers, sorters, samplers, and weighers ) : -0.016
    occly_8800 ( packaging and filling machine operators and tenders ) : -0.130
    occly_8830 ( photographic process workers and processing machine operators ) : -0.004
    occly_8850 ( adhesive bonding machine operators and tenders ) : -0.029
    occly_8910 ( etchers, engravers, and lithographers ) : -0.428
    occly_8920 ( molders, shapers, and casters, except metal and plastic ) : 0.027
    occly_8965 ( other production workers including semiconductor processors and cooling and freezing equipment operators ) : -0.086
    occly_9030 ( aircraft pilots and flight engineers ) : 0.576
    occly_9040 ( air traffic controllers and airfield operations specialists ) : 0.374
    occly_9110 (  ) : -0.006
    occly_9130 ( driver/sales workers and truck drivers ) : -0.034
    occly_9140 ( taxi drivers and chauffeurs ) : -0.300
    occly_9200 ( locomotive engineers and operators ) : 0.031
    occly_9310 ( ship and boat captains and operators ) : 0.310
    occly_9330 (  ) : 0.000
    occly_9350 ( parking lot attendants ) : -0.306
    occly_9360 ( automotive and watercraft service attendants ) : -0.265
    occly_9415 (  ) : -0.292
    occly_9510 ( crane and tower operators ) : 0.043
    occly_9600 ( industrial truck and tractor operators ) : -0.032
    occly_9610 ( cleaners of vehicles and equipment ) : -0.356
    occly_9620 ( laborers and freight, stock, and material movers, hand ) : -0.236
    occly_9630 ( machine feeders and offbearers ) : -0.089
    occly_9640 ( packers and packagers, hand ) : -0.090
    occly_9730 (  ) : 0.142
    occly_9750 ( material moving workers, nec ) : -0.157
    occly_9840 (  ) : 0.192
    indly_170 (  ) : -0.034
    indly_280 ( other primary metal industries ) : 0.078
    indly_290 ( screw machine products ) : -0.013
    indly_370 ( cycles and miscellaneous transportation equipment ) : 0.203
    indly_380 ( photographic equipment and supplies ) : 0.248
    indly_390 ( toys, amusement, and sporting goods ) : 0.319
    indly_480 (  ) : 0.014
    indly_490 (  ) : 0.419
    indly_570 (  ) : 0.179
    indly_590 ( mobile home dealers ) : 0.254
    indly_670 ( vending machine operators ) : 0.058
    indly_1170 (  ) : 0.092
    indly_1190 (  ) : -0.008
    indly_1270 (  ) : -0.024
    indly_1290 (  ) : -0.024
    indly_1480 (  ) : -0.074
    indly_1670 (  ) : -0.575
    indly_1680 (  ) : -0.109
    indly_1690 (  ) : 0.261
    indly_1870 (  ) : 0.150
    indly_1890 (  ) : 0.052
    indly_2070 (  ) : 0.293
    indly_2090 (  ) : 0.207
    indly_2190 (  ) : 0.253
    indly_2280 (  ) : 0.109
    indly_2290 (  ) : 0.088
    indly_2490 (  ) : 0.041
    indly_2590 (  ) : -0.089
    indly_2780 (  ) : -0.282
    indly_2790 (  ) : 0.057
    indly_2880 (  ) : 0.037
    indly_2970 (  ) : 0.024
    indly_3080 (  ) : 0.008
    indly_3190 (  ) : 0.043
    indly_3360 (  ) : 0.069
    indly_3380 (  ) : 0.122
    indly_3390 (  ) : 0.095
    indly_3490 (  ) : 0.047
    indly_3570 (  ) : 0.043
    indly_3580 (  ) : 0.052
    indly_3590 (  ) : 0.069
    indly_3680 (  ) : 0.022
    indly_3870 (  ) : -0.117
    indly_3890 (  ) : -0.010
    indly_3970 (  ) : 0.084
    indly_3980 (  ) : -0.042
    indly_4080 (  ) : 0.008
    indly_4180 (  ) : 0.059
    indly_4270 (  ) : 0.057
    indly_4380 (  ) : 0.131
    indly_4390 (  ) : 0.003
    indly_4480 (  ) : 0.006
    indly_4490 (  ) : 0.137
    indly_4585 (  ) : 0.057
    indly_4590 (  ) : -0.211
    indly_4670 (  ) : 0.124
    indly_4690 (  ) : -0.063
    indly_4770 (  ) : 0.012
    indly_4780 (  ) : -0.006
    indly_4790 (  ) : 0.107
    indly_4880 (  ) : -0.141
    indly_4970 (  ) : -0.146
    indly_4980 (  ) : -0.111
    indly_5070 (  ) : -0.007
    indly_5090 (  ) : -0.038
    indly_5170 (  ) : -0.154
    indly_5180 (  ) : -0.219
    indly_5270 (  ) : -0.270
    indly_5280 (  ) : -0.082
    indly_5290 (  ) : -0.103
    indly_5370 (  ) : -0.402
    indly_5380 (  ) : -0.229
    indly_5390 (  ) : -0.144
    indly_5470 (  ) : -0.236
    indly_5490 (  ) : -0.334
    indly_5570 (  ) : -0.235
    indly_5580 (  ) : -0.057
    indly_5670 (  ) : -0.201
    indly_5690 (  ) : -0.080
    indly_6070 (  ) : 0.002
    indly_6090 (  ) : 0.125
    indly_6170 (  ) : 0.107
    indly_6180 (  ) : -0.046
    indly_6190 (  ) : -0.195
    indly_6280 (  ) : 0.116
    indly_6290 (  ) : 0.021
    indly_6380 (  ) : -0.038
    indly_6470 (  ) : -0.156
    indly_6672 (  ) : 0.273
    indly_6680 (  ) : 0.134
    indly_6690 (  ) : 0.048
    indly_6695 (  ) : 0.049
    indly_6770 (  ) : -0.081
    indly_6970 (  ) : 0.079
    indly_6990 (  ) : 0.062
    indly_7070 (  ) : 0.018
    indly_7170 (  ) : -0.154
    indly_7190 (  ) : 0.055
    indly_7270 (  ) : 0.137
    indly_7290 (  ) : 0.121
    indly_7370 (  ) : 0.021
    indly_7380 (  ) : 0.132
    indly_7390 (  ) : 0.115
    indly_7460 (  ) : 0.075
    indly_7470 (  ) : 0.117
    indly_7490 (  ) : -0.021
    indly_7570 (  ) : 0.013
    indly_7580 (  ) : -0.401
    indly_7590 (  ) : -0.055
    indly_7680 (  ) : -0.084
    indly_7690 (  ) : -0.087
    indly_7860 (  ) : -0.103
    indly_7870 (  ) : -0.112
    indly_7880 (  ) : -0.047
    indly_7970 (  ) : 0.051
    indly_7980 (  ) : 0.014
    indly_8170 (  ) : -0.105
    indly_8180 (  ) : 0.027
    indly_8270 (  ) : -0.021
    indly_8370 (  ) : -0.107
    indly_8380 (  ) : -0.054
    indly_8390 (  ) : -0.352
    indly_8470 (  ) : -0.200
    indly_8560 (  ) : -0.086
    indly_8570 (  ) : -0.094
    indly_8660 (  ) : -0.070
    indly_8670 (  ) : -0.147
    indly_8680 (  ) : -0.129
    indly_8690 (  ) : -0.067
    indly_8770 (  ) : -0.009
    indly_8780 (  ) : -0.120
    indly_8870 (  ) : 0.049
    indly_8880 (  ) : -0.020
    indly_8890 (  ) : -1.242
    indly_8980 (  ) : -0.054
    indly_9070 (  ) : -0.028
    indly_9160 (  ) : -0.244
    indly_9170 (  ) : -0.062
    indly_9290 (  ) : -0.009
    indly_9370 (  ) : -0.013
    indly_9470 (  ) : 0.062
    indly_9480 (  ) : -0.022
    indly_9590 (  ) : 0.034
    indly_9890 (  ) : 0.000
    classwly_13 ( self-employed, not incorporated ) : -1.105
    classwly_14 ( self-employed, incorporated ) : 0.221
    classwly_25 ( federal government employee ) : 0.128
    classwly_27 ( state government employee ) : -0.093
    classwly_28 ( local government employee ) : -0.019
    pension_at_w_ly_2 ( pension plan at work, but not included ) : -0.031
    pension_at_w_ly_3 ( included in pension plan at work ) : 0.314
    firmsize_ly_1 ( under 10 ) : -0.211
    firmsize_ly_4 ( 10 to 49 ) : -0.072
    firmsize_ly_6 ( 50 to 99 ) : -0.010
    firmsize_ly_8 ( 500 to 999 ) : 0.020
    firmsize_ly_9 ( 1000+ ) : 0.036
    actnlfly_0 ( niu ) : 0.389
    actnlfly_10 ( ill or disabled ) : -0.005
    actnlfly_20 ( taking care of home/family ) : -0.338
    actnlfly_30 ( going to school ) : -0.480
    actnlfly_40 ( retired ) : -0.220
    actnlfly_50 ( other ) : 0.127
    spmmort_1 ( owners with a mortgage ) : 0.069
    statefip_2 ( alaska ) : 0.117
    statefip_5 ( arkansas ) : -0.009
    statefip_6 ( california ) : 0.047
    statefip_9 ( connecticut ) : 0.074
    statefip_11 ( district of columbia ) : 0.030
    statefip_15 ( hawaii ) : 0.056
    statefip_16 ( idaho ) : -0.044
    statefip_20 ( kansas ) : -0.051
    statefip_21 ( kentucky ) : -0.002
    statefip_23 ( maine ) : -0.067
    statefip_25 ( massachusetts ) : 0.039
    statefip_29 ( missouri ) : -0.053
    statefip_30 ( montana ) : -0.017
    statefip_31 ( nebraska ) : 0.000
    statefip_32 ( nevada ) : 0.036
    statefip_33 ( new hampshire ) : 0.023
    statefip_35 ( new mexico ) : -0.030
    statefip_37 ( north carolina ) : -0.004
    statefip_40 ( oklahoma ) : -0.014
    statefip_41 ( oregon ) : -0.016
    statefip_42 ( pennsylvania ) : -0.002
    statefip_44 ( rhode island ) : 0.021
    statefip_45 ( south carolina ) : -0.029
    statefip_46 ( south dakota ) : -0.034
    statefip_47 ( tennessee ) : -0.013
    statefip_54 ( west virginia ) : -0.042
    statefip_56 ( wyoming ) : 0.060
    state_ly_6 ( california ) : -0.017
    state_ly_10 ( delaware ) : -0.074
    state_ly_12 ( florida ) : 0.006
    state_ly_16 ( idaho ) : -0.023
    state_ly_23 ( maine ) : -0.053
    state_ly_24 ( maryland ) : 0.013
    state_ly_25 ( massachusetts ) : 0.119
    state_ly_34 ( new jersey ) : -0.022
    state_ly_37 ( north carolina ) : 0.020
    state_ly_40 ( oklahoma ) : -0.032
    state_ly_49 ( utah ) : -0.042
    state_ly_51 ( virginia ) : 0.042
    state_ly_91 ( abroad ) : -0.085
    whymove_1 ( change in marital status ) : -0.024
    whymove_2 ( to establish own household ) : -0.065
    whymove_5 ( to look for work or lost job ) : -0.248
    whymove_10 ( wanted new or better housing ) : 0.010
    whymove_11 ( wanted better neighborhood ) : 0.042
    whymove_12 ( for cheaper housing ) : -0.032
    whymove_14 ( attend/leave college ) : -0.251
    whymove_18 ( natural disaster ) : 0.125
    whymove_19 ( foreclosure or eviction ) : 0.017
    mig_stat_ly_4 ( moved within state, different county ) : 0.003
    mig_stat_ly_6 ( abroad ) : -0.006
    health_1 ( excellent ) : 0.027
    health_3 ( good ) : -0.054
    health_4 ( fair ) : -0.128
    health_5 ( poor ) : -0.172
    vet1_2 ( august 1990 to august 2001 ) : 0.002
    vet1_4 ( vietnam era (august 1964 to april 1975) ) : -0.064
    csvisleg_1 ( no ) : 0.010
    csvisleg_2 ( yes ) : 0.000
    csvisleg_98 ( blank ) : -0.014
    paidhour_1 ( no ) : 0.108
    paidhour_2 ( yes ) : -0.033
    union_1 ( no union coverage ) : -0.010
    union_2 ( member of labor union ) : 0.071
    bpl_1.0 ( usa, canada & dependent ) : 0.005
    bpl_8.0 ( developed asia ) : 0.018
    fbpl_5.0 ( central and caribean ) : -0.011
    fbpl_7.0 ( europe ) : 0.004
    fbpl_9.0 ( east asia ) : -0.006
    grid: [1.45096612e-03 1.35317586e-03 1.26197633e-03 1.17692335e-03
    1.09760266e-03 1.02362791e-03 9.54638815e-04 8.90299354e-04
    8.30296157e-04 7.74336975e-04 7.22149255e-04 6.73478812e-04
    6.28088594e-04 5.85757525e-04 5.46279428e-04 5.09462023e-04
    4.75125988e-04 4.43104086e-04 4.13240354e-04 3.85389337e-04
    3.59415386e-04 3.35191992e-04 3.12601173e-04 2.91532900e-04
    2.71884559e-04 2.53560449e-04 2.36471324e-04 2.20533948e-04
    2.05670698e-04 1.91809181e-04 1.78881884e-04 1.66825844e-04
    1.55582341e-04 1.45096612e-04 1.35317586e-04 1.26197633e-04
    1.17692335e-04 1.09760266e-04 1.02362791e-04 9.54638815e-05
    8.90299354e-05 8.30296157e-05 7.74336975e-05 7.22149255e-05
    6.73478812e-05 6.28088594e-05 5.85757525e-05 5.46279428e-05
    5.09462023e-05 4.75125988e-05 4.43104086e-05 4.13240354e-05
    3.85389337e-05 3.59415386e-05 3.35191992e-05 3.12601173e-05
    2.91532900e-05 2.71884559e-05 2.53560449e-05 2.36471324e-05
    2.20533948e-05 2.05670698e-05 1.91809181e-05 1.78881884e-05
    1.66825844e-05 1.55582341e-05 1.45096612e-05 1.35317586e-05
    1.26197633e-05 1.17692335e-05 1.09760266e-05 1.02362791e-05
    9.54638815e-06 8.90299354e-06 8.30296157e-06 7.74336975e-06
    7.22149255e-06 6.73478812e-06 6.28088594e-06 5.85757525e-06
    5.46279428e-06 5.09462023e-06 4.75125988e-06 4.43104086e-06
    4.13240354e-06 3.85389337e-06 3.59415386e-06 3.35191992e-06
    3.12601173e-06 2.91532900e-06 2.71884559e-06 2.53560449e-06
    2.36471324e-06 2.20533948e-06 2.05670698e-06 1.91809181e-06
    1.78881884e-06 1.66825844e-06 1.55582341e-06 1.45096612e-06]































## LassoCV5

### Code

    model = skl.LassoCV(cv=5, normalize=True)
    model.fit(X,Y)
    predictions = model.predict(X)

### Results

    Time to run: 177.74616646766663 to run
    \lambda:  (9.546388151822239e-06,) log10: [-5.02016091] ln: [-11.55934768]
    Coefficients: 
    [ 0.00400128 -0.         -0.12686468 ... -0.00622842  0.
    -0.        ]
    Mean squared error: 0.29
    Coefficient of determination: 0.57
    age ( age ) : 0.004
    educ_cat_1.0 (  ) : -0.127
    educ_cat_2.0 (  ) : -0.033
    educ_cat_4.0 (  ) : 0.066
    educ_cat_5.0 (  ) : 0.287
    race_cat_1.0 (  ) : 0.042
    race_cat_2.0 (  ) : -0.013
    male_0.0 (  ) : -0.274
    male_1.0 (  ) : 0.000
    hhtenure_1 ( owned or being bought ) : 0.051
    hhtenure_3 ( occupied without payment of cash rent ) : -0.024
    region_11 ( new england division ) : 0.027
    region_21 ( east north central division ) : -0.009
    region_32 ( east south central division ) : -0.036
    region_42 ( pacific division ) : 0.027
    metarea_120 ( albany, ga ) : -0.112
    metarea_200 ( albuquerque, nm ) : -0.004
    metarea_280 ( altoona, pa msa ) : -0.038
    metarea_320 ( amarillo, tx ) : -0.016
    metarea_440 ( ann arbor, mi ) : 0.090
    metarea_462 ( oshkosh-neenah, wi ) : -0.177
    metarea_480 ( asheville, nc ) : -0.089
    metarea_521 ( atlanta-sandy springs-marietta, ga ) : 0.009
    metarea_641 ( austin-round rock, tx ) : 0.050
    metarea_680 ( bakersfield, ca ) : -0.129
    metarea_721 ( baltimore-towson, md ) : 0.068
    metarea_730 ( bangor, me ) : -0.038
    metarea_741 ( barnstable town, ma ) : -0.057
    metarea_760 ( baton rouge, la ) : 0.026
    metarea_841 ( beaumont-port arthur, tx ) : 0.073
    metarea_860 ( bellingham, wa ) : 0.020
    metarea_880 ( billings, mt ) : -0.033
    metarea_920 ( biloxi-gulfport, ms ) : -0.025
    metarea_960 ( binghamton, ny ) : -0.017
    metarea_1081 ( boise city-nampa, id ) : -0.075
    metarea_1124 ( boston-cambridge-quincy, ma-nh ) : 0.017
    metarea_1280 ( buffalo-niagara falls, ny ) : -0.043
    metarea_1360 ( cedar rapids, ia ) : -0.041
    metarea_1440 ( charleston-north charleston, sc ) : -0.024
    metarea_1480 ( charleston, wv ) : -0.081
    metarea_1605 ( chicago-naperville-joliet, il-in-wi ) : 0.057
    metarea_1700 ( coeur d'alene, id ) : -0.081
    metarea_1720 ( colorado springs, co ) : -0.011
    metarea_1800 ( columbus, ga/al ) : -0.133
    metarea_1922 ( dallas-fort worth-arlington, tx ) : 0.023
    metarea_1930 ( danbury, ct ) : 0.122
    metarea_2001 ( springfield, oh ) : -0.029
    metarea_2002 ( dayton, oh ) : -0.140
    metarea_2030 ( decatur, al ) : -0.030
    metarea_2082 ( boulder, co ) : 0.005
    metarea_2083 ( denver-aurora, co ) : 0.033
    metarea_2241 ( duluth, mn/wi ) : -0.129
    metarea_2300 ( el centro, ca ) : -0.130
    metarea_2310 ( el paso, tx ) : -0.080
    metarea_2360 ( erie, pa ) : -0.136
    metarea_2400 ( eugene-springfield, or ) : -0.026
    metarea_2581 ( fayetteville-springdale-rogers, ar-mo ) : 0.047
    metarea_2640 ( flint, mi ) : -0.127
    metarea_2670 ( fort collins-loveland, co ) : -0.048
    metarea_2760 ( fort wayne, in ) : -0.010
    metarea_2840 ( fresno, ca ) : -0.079
    metarea_2900 ( gainesville, fl ) : -0.075
    metarea_3060 ( greeley, co ) : -0.034
    metarea_3162 ( greenville, sc ) : -0.026
    metarea_3181 ( hagerstown-martinsburg, md-wv ) : 0.024
    metarea_3362 ( houston-baytown-sugar land, tx ) : 0.079
    metarea_3440 ( huntsville,al ) : -0.055
    metarea_3480 ( indianapolis, in ) : 0.028
    metarea_3520 ( jackson, mi ) : -0.061
    metarea_3560 ( jackson, ms ) : -0.027
    metarea_3590 ( jacksonville,fl ) : 0.007
    metarea_3600 ( jacksonville, nc ) : -0.025
    metarea_3621 ( janvesville, wi ) : -0.015
    metarea_3661 ( johnson city, tn ) : -0.058
    metarea_3720 ( kalamazoo-portage, mi ) : -0.008
    metarea_3760 ( kansas city, mo/ks ) : 0.059
    metarea_3830 ( kingston, ny ) : 0.026
    metarea_4000 ( lancaster, pa ) : 0.079
    metarea_4040 ( lansing-east lansing, mi ) : -0.027
    metarea_4080 ( laredo, tx ) : -0.007
    metarea_4100 ( las cruces, nm ) : -0.048
    metarea_4130 ( las vegas-paradise, nv ) : 0.019
    metarea_4150 ( lawrence, ks ) : 0.043
    metarea_4200 ( lawton, ok ) : -0.031
    metarea_4280 ( lexington-fayette, ky ) : -0.046
    metarea_4483 ( los angeles-long beach-santa ana, ca ) : 0.017
    metarea_4600 ( lubbock, tx ) : -0.083
    metarea_4640 ( lynchburg, va ) : -0.026
    metarea_4681 ( macon, ga ) : -0.067
    metarea_4720 ( madison, wi ) : 0.011
    metarea_4940 ( merced, ca ) : -0.043
    metarea_5001 ( miami-fort lauderdale-miami beach, fl ) : 0.040
    metarea_5081 ( milwaukee-waukesha-west allis, wi ) : -0.004
    metarea_5121 ( minneapolis-st. paul-bloomington, mn/wi ) : 0.041
    metarea_5160 ( mobile, al ) : 0.001
    metarea_5170 ( modesto, ca ) : -0.000
    metarea_5200 ( monroe, la ) : -0.010
    metarea_5220 ( monroe, mi ) : 0.106
    metarea_5321 ( muskegon-norton shores, mi ) : -0.066
    metarea_5331 ( myrtle beach-conway-north myrtle beach, sc ) : -0.078
    metarea_5481 ( new haven, ct ) : 0.013
    metarea_5606 ( new york-northern new jersey-long island, ny-nj-pa ) : 0.196
    metarea_5790 ( ocala, fl ) : -0.091
    metarea_5801 ( midland, tx ) : 0.108
    metarea_5840 ( ocean city, nj ) : -0.331
    metarea_5910 ( olympia, wa ) : -0.087
    metarea_5960 ( orlando, fl ) : -0.057
    metarea_6081 ( pensacola-ferry pass-brent, fl ) : -0.096
    metarea_6161 ( philadelphia-camden-wilmington, pa/nj/de ) : 0.056
    metarea_6201 ( phoenix-mesa-scottsdale, az ) : 0.013
    metarea_6280 ( pittsburg, pa ) : -0.012
    metarea_6401 ( portland-south portland, me ) : 0.045
    metarea_6520 ( provo-orem, ut ) : -0.022
    metarea_6680 ( reading, pa ) : -0.090
    metarea_6980 ( st. cloud, mn ) : -0.053
    metarea_7080 ( salem, or ) : -0.008
    metarea_7130 ( salisbury, md ) : -0.083
    metarea_7321 ( san diego-carlsbad-san marcos, ca ) : 0.039
    metarea_7364 ( napa, ca ) : 0.052
    metarea_7365 ( san francisco-oakland-fremont, ca ) : 0.123
    metarea_7401 ( san jose-sunnyvale-santa clara, ca ) : 0.154
    metarea_7461 ( san luis obispo-paso robles, ca ) : 0.081
    metarea_7471 ( santa barbara-santa maria-goleta, ca ) : 0.068
    metarea_7481 ( santa cruz-watsonville, ca ) : 0.059
    metarea_7511 ( sarasota-bradenton-venice, fl ) : 0.011
    metarea_7520 ( savannah, ga ) : 0.036
    metarea_7560 ( scranton-wilkes-barre, pa ) : -0.001
    metarea_7601 ( seattle-tacoma-bellevue, wa ) : 0.023
    metarea_7681 ( shreveport-bossier city, la ) : 0.007
    metarea_7760 ( sioux falls, sd ) : -0.024
    metarea_7920 ( springfield, mo ) : -0.027
    metarea_8160 ( syracuse, ny ) : -0.016
    metarea_8240 ( tallahassee, fl ) : -0.018
    metarea_8440 ( topeka, ks ) : 0.042
    metarea_8600 ( tuscaloosa, al ) : -0.058
    metarea_8700 ( valdosta, ga ) : -0.010
    metarea_8731 ( oxnard-thousand oaks-ventura, ca ) : 0.068
    metarea_8740 ( vero beach, fl ) : -0.093
    metarea_8750 ( victoria, tx ) : -0.016
    metarea_8760 ( vineland-milville-bridgetown, nj ) : 0.074
    metarea_8781 ( visalia-porterville, ca ) : -0.027
    metarea_8840 ( washington, dc/md/va ) : 0.156
    metarea_8920 ( waterloo-cedar falls, ia ) : -0.045
    metarea_8940 ( wausau, wi ) : -0.045
    metarea_9040 ( wichita, ks ) : -0.035
    metarea_9321 ( youngstown-warren-boardman, oh ) : -0.097
    metarea_9997 ( other metropolitan areas, unidentified ) : -0.047
    metarea_9998 ( niu, household not in a metropolitan area ) : -0.066
    metarea_9999 ( missing data ) : -0.020
    unitsstr_1 ( mobile home or trailer ) : -0.028
    unitsstr_7 ( 5-9 family building ) : -0.007
    unitsstr_11 ( one unit, unspecified type ) : 0.026
    nfams_1 ( 1 family or n/a ) : 0.007
    nfams_4 ( 4 ) : -0.004
    nfams_6 ( 6 ) : -0.082
    nfams_8 ( 8 ) : 0.152
    ncouples_2 ( 2 ) : -0.058
    nmothers_2 ( 2 ) : -0.022
    nmothers_3 ( 3 ) : -0.089
    nfathers_1 ( 1 ) : 0.001
    nfathers_2 ( 2 ) : -0.021
    nfathers_3 ( 3 ) : -0.051
    marst_1 ( married, spouse present ) : 0.119
    marst_3 ( separated ) : -0.025
    marst_5 ( widowed ) : -0.043
    marst_6 ( never married/single ) : -0.073
    famsize_3 ( 3 family members present ) : 0.000
    famsize_6 ( 6 family members present ) : -0.009
    famsize_7 ( 7 family members present ) : -0.014
    famsize_8 ( 8 family members present ) : -0.031
    famsize_14 ( 14 family members present ) : -0.084
    famsize_15 ( 15 family members present ) : -0.293
    ftype_2 ( nonfamily householder ) : 0.044
    ftype_3 ( related subfamily ) : -0.061
    ftype_4 ( unrelated subfamily ) : -0.024
    famkind_1 ( husband/wife family ) : -0.053
    famkind_3 ( female reference person ) : 0.128
    yrimmig_0 ( niu ) : 0.002
    yrimmig_1985 ( 1984-1985 ) : 0.009
    yrimmig_2001 ( 2000-2001 (2001 cps: 1998-2001) ) : -0.015
    yrimmig_2003 ( 2002-2003 (2003 cps: 2000-2003) ) : -0.018
    yrimmig_2005 ( 2004-2005 (2005 cps: 2002-2005) ) : -0.043
    yrimmig_2007 ( 2004-2007 ) : -0.025
    yrimmig_2009 ( 2006-2009 ) : -0.027
    yrimmig_2012 ( 2010-2012 (2014 cps: 2010-2011) ) : -0.070
    citizen_1 ( born in u.s ) : 0.000
    citizen_3 ( born abroad of american parents ) : 0.015
    citizen_5 ( not a citizen ) : -0.056
    hispan_0 ( not hispanic ) : 0.010
    hispan_410 ( central/south american ) : -0.012
    occ_0 ( Missing data? ) : -0.276
    occ_10 ( chief executives and legislators/public administration ) : 0.077
    occ_20 ( general and operations managers ) : 0.082
    occ_40 (  ) : 0.001
    occ_135 (  ) : 0.002
    occ_136 (  ) : 0.084
    occ_150 ( purchasing managers ) : 0.038
    occ_220 ( constructions managers ) : 0.092
    occ_325 (  ) : 0.173
    occ_340 (  ) : -0.013
    occ_350 ( medical and health services managers ) : 0.122
    occ_420 ( social and community service managers ) : 0.025
    occ_500 ( agents and business managers of artists, performers, and athletes ) : 0.357
    occ_565 (  ) : 0.107
    occ_600 ( cost estimators ) : 0.262
    occ_630 (  ) : 0.005
    occ_640 (  ) : 0.033
    occ_650 (  ) : 0.059
    occ_725 (  ) : 0.079
    occ_735 (  ) : 0.186
    occ_810 ( appraisers and assessors of real estate ) : 0.080
    occ_830 ( credit analysts ) : 0.076
    occ_850 ( personal financial advisors ) : 0.096
    occ_860 ( insurance underwriters ) : 0.027
    occ_940 ( tax preparers ) : -0.154
    occ_950 ( financial specialists, nec ) : 0.044
    occ_1005 (  ) : 0.067
    occ_1007 (  ) : 0.006
    occ_1010 ( computer programmers ) : 0.007
    occ_1020 ( software developers, applications and systems software ) : 0.066
    occ_1060 ( database administrators ) : 0.217
    occ_1105 (  ) : 0.109
    occ_1240 ( mathematical science occupations, nec ) : 0.055
    occ_1320 ( aerospace engineers ) : 0.105
    occ_1330 (  ) : 0.118
    occ_1350 ( chemical engineers ) : 0.189
    occ_1430 ( industrial engineers, including health and safety ) : 0.078
    occ_1460 ( mechanical engineers ) : 0.170
    occ_1510 (  ) : 0.004
    occ_1520 ( petroleum, mining and geological engineers, including mining safety engineers ) : 0.321
    occ_1530 ( engineers, nec ) : 0.018
    occ_1540 ( drafters ) : 0.021
    occ_1560 ( surveying and mapping technicians ) : -0.006
    occ_1660 (  ) : 0.247
    occ_1700 ( astronomers and physicists ) : 0.112
    occ_1720 ( chemists and materials scientists ) : 0.092
    occ_1800 ( economists and market researchers ) : 0.260
    occ_1820 ( psychologists ) : 0.060
    occ_1860 (  ) : -0.013
    occ_1910 ( biological technicians ) : -0.119
    occ_1930 ( geological and petroleum technicians, and nuclear technicians ) : -0.192
    occ_1965 (  ) : -0.017
    occ_2000 ( counselors ) : -0.006
    occ_2060 ( religious workers, nec ) : -0.418
    occ_2100 ( lawyers, and judges, magistrates, and other judicial workers ) : 0.068
    occ_2160 (  ) : -0.021
    occ_2200 ( postsecondary teachers ) : 0.049
    occ_2300 ( preschool and kindergarten teachers ) : -0.020
    occ_2430 ( librarians ) : -0.027
    occ_2440 ( library technicians ) : -0.320
    occ_2540 ( teacher assistants ) : -0.049
    occ_2710 (  ) : 0.107
    occ_2720 ( athletes, coaches, umpires, and related workers ) : 0.063
    occ_2750 ( musicians, singers, and related workers ) : -0.260
    occ_2760 ( entertainers and performers, sports and related workers, all other ) : 0.061
    occ_2825 ( public relations specialists ) : 0.095
    occ_2830 (  ) : 0.022
    occ_2960 (  ) : -0.738
    occ_3000 ( chiropractors ) : -0.010
    occ_3010 ( dentists ) : 0.213
    occ_3060 ( physicians and surgeons ) : 0.193
    occ_3110 ( physician assistants ) : 0.096
    occ_3160 ( physical therapists ) : 0.045
    occ_3200 ( radiation therapists ) : 0.120
    occ_3210 ( recreational therapists ) : -0.005
    occ_3230 ( speech language pathologists ) : 0.107
    occ_3235 (  ) : -0.990
    occ_3255 (  ) : 0.151
    occ_3257 (  ) : 0.149
    occ_3420 (  ) : -0.091
    occ_3600 ( nursing, psychiatric, and home health aides ) : -0.012
    occ_3620 ( physical therapist assistants and aides ) : 0.045
    occ_3645 (  ) : -0.036
    occ_3646 (  ) : -0.004
    occ_3700 ( first-line supervisors of correctional officers ) : 0.012
    occ_3740 ( firefighters ) : 0.063
    occ_3800 ( sheriffs, bailiffs, correctional officers, and jailers ) : -0.032
    occ_3850 (  ) : 0.061
    occ_3860 (  ) : 0.238
    occ_3900 ( animal control ) : -0.172
    occ_3940 ( crossing guards ) : -0.032
    occ_4000 ( chefs and cooks ) : -0.042
    occ_4020 (  ) : -0.077
    occ_4040 ( bartenders ) : -0.216
    occ_4050 ( combined food preparation and serving workers, including fast food ) : -0.179
    occ_4060 ( counter attendant, cafeteria, food concession, and coffee shop ) : -0.263
    occ_4120 ( food servers, nonrestaurant ) : -0.088
    occ_4140 ( dishwashers ) : -0.214
    occ_4220 ( janitors and building cleaners ) : -0.034
    occ_4230 ( maids and housekeeping cleaners ) : -0.062
    occ_4250 ( grounds maintenance workers ) : -0.037
    occ_4350 ( nonfarm animal caretakers ) : -0.124
    occ_4430 ( entertainment attendants and related workers, nec ) : -0.189
    occ_4460 ( funeral service workers and embalmers ) : -0.221
    occ_4530 ( baggage porters, bellhops, and concierges ) : -0.037
    occ_4540 ( tour and travel guides ) : 0.186
    occ_4600 ( childcare workers ) : -0.245
    occ_4610 ( personal care aides ) : -0.055
    occ_4640 ( residential advisors ) : -0.070
    occ_4700 ( first-line supervisors of sales workers ) : 0.011
    occ_4720 ( cashiers ) : -0.035
    occ_4760 ( retail salespersons ) : -0.012
    occ_4800 ( advertising sales agents ) : 0.003
    occ_4840 ( sales representatives, services, all other ) : 0.006
    occ_4850 ( sales representatives, wholesale and manufacturing ) : 0.111
    occ_4900 ( models, demonstrators, and product promoters ) : -0.152
    occ_4920 ( real estate brokers and sales agents ) : 0.169
    occ_4950 ( door-to-door sales workers, news and street vendors, and related workers ) : -0.211
    occ_5000 ( first-line supervisors of office and administrative support workers ) : 0.026
    occ_5010 ( switchboard operators, including answering service ) : -0.137
    occ_5110 ( billing and posting clerks ) : -0.088
    occ_5120 ( bookkeeping, accounting, and auditing clerks ) : -0.086
    occ_5160 ( bank tellers ) : -0.048
    occ_5220 ( court, municipal, and license clerks ) : -0.107
    occ_5310 ( interviewers, except eligibility and loan ) : -0.048
    occ_5360 ( human resources assistants, except payroll and timekeeping ) : -0.033
    occ_5400 ( receptionists and information clerks ) : -0.059
    occ_5530 ( meter readers, utilities ) : -0.074
    occ_5540 ( postal service clerks ) : -0.029
    occ_5610 ( shipping, receiving, and traffic clerks ) : -0.175
    occ_5820 ( word processors and typists ) : -0.187
    occ_5840 ( insurance claims and policy processing clerks ) : -0.052
    occ_5920 ( statistical assistants ) : -0.042
    occ_5940 ( office and administrative support workers, nec ) : -0.057
    occ_6220 ( brickmasons, blockmasons, and stonemasons ) : -0.041
    occ_6260 ( construction laborers ) : -0.074
    occ_6320 ( construction equipment operators except paving, surfacing, and tamping equipment operators ) : 0.066
    occ_6330 ( drywall installers, ceiling tile installers, and tapers ) : -0.127
    occ_6500 ( reinforcing iron and rebar workers ) : -0.198
    occ_6730 ( highway maintenance workers ) : -0.069
    occ_6750 (  ) : -0.330
    occ_6800 ( derrick, rotary drill, and service unit operators, and roustabouts, oil, gas, and mining ) : 0.020
    occ_6840 ( mining machine operators ) : 0.013
    occ_6910 (  ) : -0.136
    occ_6920 (  ) : -0.166
    occ_7000 ( first-line supervisors of mechanics, installers, and repairers ) : 0.080
    occ_7130 ( security and fire alarm systems installers ) : 0.093
    occ_7140 ( aircraft mechanics and service technicians ) : 0.001
    occ_7150 ( automotive body and related repairers ) : 0.007
    occ_7260 ( vehicle and mobile equipment mechanics, installers, and repairers, nec ) : -0.168
    occ_7360 ( millwrights ) : 0.041
    occ_7410 ( electrical power-line installers and repairers ) : 0.081
    occ_7440 (  ) : -0.268
    occ_7510 ( coin, vending, and amusement machine servicers and repairers ) : -0.145
    occ_7550 ( manufactured building and mobile home installers ) : 0.000
    occ_7560 ( riggers ) : 0.000
    occ_7630 ( other installation, maintenance, and repair workers including wind turbine service technicians, and commercial divers, and signal and track switch repairers ) : -0.009
    occ_7700 ( first-line supervisors of production and operating workers ) : 0.063
    occ_7710 ( aircraft structure, surfaces, rigging, and systems assemblers ) : -0.023
    occ_7720 ( electrical, electronics, and electromechanical assemblers ) : -0.004
    occ_7750 ( assemblers and fabricators, nec ) : -0.051
    occ_7800 ( bakers ) : -0.136
    occ_7855 ( food processing, nec ) : -0.034
    occ_8000 ( grinding, lapping, polishing, and buffing machine tool setters, operators, and tenders, metal and plastic ) : -0.137
    occ_8100 ( molders and molding machine setters, operators, and tenders, metal and plastic ) : -0.081
    occ_8120 (  ) : -0.037
    occ_8250 ( prepress technicians and workers ) : 0.041
    occ_8255 (  ) : -0.143
    occ_8300 ( laundry and dry-cleaning workers ) : -0.025
    occ_8330 ( shoe and leather workers and repairers ) : -0.243
    occ_8350 ( tailors, dressmakers, and sewers ) : -0.131
    occ_8440 (  ) : 0.944
    occ_8550 ( woodworkers including model makers and patternmakers, nec ) : -0.152
    occ_8610 ( stationary engineers and boiler operators ) : 0.001
    occ_8620 ( water wastewater treatment plant and system operators ) : 0.009
    occ_8630 ( plant and system operators, nec ) : 0.139
    occ_8650 ( crushing, grinding, polishing, mixing, and blending workers ) : -0.094
    occ_8710 ( cutting workers ) : -0.006
    occ_8740 ( inspectors, testers, sorters, samplers, and weighers ) : -0.034
    occ_8760 ( medical, dental, and ophthalmic laboratory technicians ) : -0.109
    occ_8800 ( packaging and filling machine operators and tenders ) : -0.036
    occ_8810 ( painting workers and dyers ) : -0.070
    occ_8830 ( photographic process workers and processing machine operators ) : -0.049
    occ_8840 (  ) : -0.019
    occ_8930 ( paper goods machine setters, operators, and tenders ) : 0.008
    occ_8950 ( helpers--production workers ) : -0.101
    occ_8965 ( other production workers including semiconductor processors and cooling and freezing equipment operators ) : -0.099
    occ_9110 (  ) : -0.389
    occ_9120 (  ) : -0.241
    occ_9150 ( motor vehicle operators, all other ) : -0.179
    occ_9200 ( locomotive engineers and operators ) : 0.124
    occ_9240 ( railroad conductors and yardmasters ) : 0.117
    occ_9330 (  ) : 0.187
    occ_9350 ( parking lot attendants ) : -0.105
    occ_9600 ( industrial truck and tractor operators ) : -0.119
    occ_9620 ( laborers and freight, stock, and material movers, hand ) : -0.082
    occ_9640 ( packers and packagers, hand ) : -0.317
    occ_9720 ( refuse and recyclable material collectors ) : -0.069
    occ_9730 (  ) : 0.001
    occ_9840 (  ) : -0.280
    ind_0 (  ) : -0.028
    ind_280 (  ) : 0.084
    ind_370 (  ) : 0.045
    ind_380 (  ) : 0.106
    ind_390 (  ) : 0.023
    ind_470 (  ) : 0.120
    ind_570 (  ) : 0.042
    ind_580 (  ) : 0.142
    ind_680 (  ) : 0.029
    ind_690 (  ) : 0.159
    ind_1190 (  ) : -0.034
    ind_1480 (  ) : -0.126
    ind_1670 (  ) : -0.044
    ind_1680 (  ) : -0.087
    ind_1790 (  ) : 0.110
    ind_1870 (  ) : 0.027
    ind_1880 (  ) : -0.016
    ind_2290 (  ) : 0.011
    ind_2390 (  ) : 0.064
    ind_2470 (  ) : -0.081
    ind_2480 (  ) : -0.005
    ind_2670 (  ) : 0.090
    ind_2680 (  ) : 0.038
    ind_2790 (  ) : -0.097
    ind_3090 (  ) : 0.017
    ind_3170 (  ) : 0.121
    ind_3360 (  ) : 0.040
    ind_3380 (  ) : 0.011
    ind_3390 (  ) : 0.034
    ind_3570 (  ) : 0.044
    ind_3580 (  ) : 0.010
    ind_3670 (  ) : 0.033
    ind_3690 (  ) : -0.012
    ind_3970 (  ) : 0.007
    ind_4090 (  ) : 0.032
    ind_4170 (  ) : 0.099
    ind_4190 (  ) : 0.004
    ind_4380 (  ) : 0.068
    ind_4470 (  ) : 0.010
    ind_4670 (  ) : 0.043
    ind_4770 (  ) : -0.020
    ind_4870 (  ) : -0.039
    ind_4880 (  ) : -0.073
    ind_4990 (  ) : -0.123
    ind_5070 (  ) : -0.032
    ind_5170 (  ) : -0.002
    ind_5190 (  ) : -0.065
    ind_5380 (  ) : -0.018
    ind_5590 (  ) : 0.060
    ind_5690 (  ) : -0.046
    ind_6080 (  ) : 0.148
    ind_6270 (  ) : 0.131
    ind_6480 (  ) : 0.023
    ind_6490 (  ) : 0.116
    ind_6570 (  ) : 0.047
    ind_6670 (  ) : 0.002
    ind_6680 (  ) : 0.005
    ind_6970 (  ) : 0.071
    ind_6990 (  ) : 0.033
    ind_7080 (  ) : -0.033
    ind_7190 (  ) : 0.112
    ind_7380 (  ) : 0.034
    ind_7470 (  ) : 0.025
    ind_7570 (  ) : 0.034
    ind_7680 (  ) : -0.014
    ind_7770 (  ) : -0.053
    ind_7860 (  ) : -0.011
    ind_7890 (  ) : -0.084
    ind_7980 (  ) : 0.007
    ind_8170 (  ) : -0.045
    ind_8190 (  ) : 0.028
    ind_8370 (  ) : -0.039
    ind_8380 (  ) : -0.021
    ind_8470 (  ) : -0.038
    ind_8570 (  ) : -0.023
    ind_8580 (  ) : -0.250
    ind_8590 (  ) : -0.055
    ind_8660 (  ) : -0.026
    ind_8670 (  ) : -0.056
    ind_8870 (  ) : 0.053
    ind_8880 (  ) : -0.050
    ind_8980 (  ) : -0.031
    ind_9090 (  ) : -0.092
    ind_9290 (  ) : -0.041
    ind_9370 (  ) : -0.007
    ind_9890 (  ) : -0.005
    educ_10 ( grades 1, 2, 3, or 4 ) : -0.053
    educ_20 ( grades 5 or 6 ) : -0.026
    educ_30 ( grades 7 or 8 ) : -0.007
    educ_71 ( 12th grade, no diploma ) : 0.011
    educ_73 ( high school diploma or equivalent ) : -0.000
    educ_81 ( some college but no degree ) : -0.005
    educ_91 ( associate's degree, occupational/vocational program ) : 0.007
    educ_111 ( bachelor's degree ) : 0.076
    educ_124 ( professional school degree ) : 0.016
    educ_125 ( doctorate degree ) : 0.106
    occly_10 ( chief executives and legislators/public administration ) : 0.525
    occly_20 ( general and operations managers ) : 0.289
    occly_40 (  ) : 0.289
    occly_50 (  ) : 0.368
    occly_60 (  ) : 0.222
    occly_100 ( administrative services managers ) : 0.065
    occly_110 ( computer and information systems managers ) : 0.405
    occly_120 ( financial managers ) : 0.273
    occly_136 (  ) : 0.164
    occly_137 (  ) : 0.094
    occly_140 ( industrial production managers ) : 0.273
    occly_150 ( purchasing managers ) : 0.141
    occly_160 ( transportation, storage, and distribution managers ) : 0.057
    occly_205 ( farmers, ranchers, and other agricultural managers ) : -0.039
    occly_220 ( constructions managers ) : 0.258
    occly_230 ( education administrators ) : 0.229
    occly_300 ( architectural and engineering managers ) : 0.390
    occly_310 ( food service and lodging managers ) : 0.027
    occly_350 ( medical and health services managers ) : 0.156
    occly_360 ( natural science managers ) : 0.088
    occly_410 ( property, real estate, and community association managers ) : 0.131
    occly_420 ( social and community service managers ) : 0.058
    occly_430 ( managers, nec (including postmasters) ) : 0.245
    occly_500 ( agents and business managers of artists, performers, and athletes ) : 0.001
    occly_520 ( wholesale and retail buyers, except farm products ) : 0.047
    occly_630 (  ) : 0.149
    occly_710 ( management analysts ) : 0.175
    occly_726 (  ) : 0.052
    occly_740 (  ) : 0.039
    occly_800 ( accountants and auditors ) : 0.148
    occly_820 ( budget analysts ) : 0.098
    occly_840 ( financial analysts ) : 0.240
    occly_850 ( personal financial advisors ) : 0.092
    occly_910 ( credit counselors and loan officers ) : 0.049
    occly_940 ( tax preparers ) : -0.168
    occly_1006 (  ) : 0.272
    occly_1010 ( computer programmers ) : 0.186
    occly_1020 ( software developers, applications and systems software ) : 0.266
    occly_1030 (  ) : 0.064
    occly_1050 ( computer support specialists ) : 0.001
    occly_1106 (  ) : 0.380
    occly_1107 (  ) : 0.092
    occly_1200 ( actuaries ) : 0.613
    occly_1220 ( operations research analysts ) : 0.103
    occly_1300 ( architects, except naval ) : 0.111
    occly_1320 ( aerospace engineers ) : 0.224
    occly_1360 ( civil engineers ) : 0.230
    occly_1400 ( computer hardware engineers ) : 0.198
    occly_1410 ( electrical and electronics engineers ) : 0.251
    occly_1420 ( environmental engineers ) : 0.186
    occly_1430 ( industrial engineers, including health and safety ) : 0.026
    occly_1440 ( marine engineers and naval architects ) : 0.322
    occly_1500 (  ) : 0.299
    occly_1510 (  ) : 0.012
    occly_1530 ( engineers, nec ) : 0.263
    occly_1550 ( engineering technicians, except drafters ) : 0.001
    occly_1560 ( surveying and mapping technicians ) : -0.011
    occly_1640 ( conservation scientists and foresters ) : 0.012
    occly_1660 (  ) : 0.036
    occly_1700 ( astronomers and physicists ) : 0.034
    occly_1710 ( atmospheric and space scientists ) : -0.110
    occly_1800 ( economists and market researchers ) : 0.059
    occly_1860 (  ) : -0.128
    occly_1930 ( geological and petroleum technicians, and nuclear technicians ) : -0.001
    occly_1965 (  ) : -0.077
    occly_2000 ( counselors ) : -0.002
    occly_2016 (  ) : -0.019
    occly_2025 (  ) : -0.023
    occly_2060 ( religious workers, nec ) : -0.080
    occly_2100 ( lawyers, and judges, magistrates, and other judicial workers ) : 0.281
    occly_2300 ( preschool and kindergarten teachers ) : -0.018
    occly_2320 ( secondary school teachers ) : 0.064
    occly_2330 ( special education teachers ) : 0.041
    occly_2340 ( other teachers and instructors ) : -0.198
    occly_2430 ( librarians ) : -0.019
    occly_2540 ( teacher assistants ) : -0.410
    occly_2550 ( education, training, and library workers, nec ) : -0.013
    occly_2630 ( designers ) : -0.005
    occly_2700 ( actors, producers, and directors ) : 0.077
    occly_2720 ( athletes, coaches, umpires, and related workers ) : -0.238
    occly_2740 ( dancers and choreographers ) : -0.410
    occly_2760 ( entertainers and performers, sports and related workers, all other ) : 0.161
    occly_2800 ( announcers ) : 0.234
    occly_2825 ( public relations specialists ) : 0.130
    occly_2840 ( technical writers ) : 0.077
    occly_2850 ( writers and authors ) : 0.189
    occly_2910 ( photographers ) : -0.127
    occly_2960 (  ) : -0.138
    occly_3000 ( chiropractors ) : -0.163
    occly_3010 ( dentists ) : 0.323
    occly_3030 ( dieticians and nutritionists ) : -0.041
    occly_3040 ( optometrists ) : 0.157
    occly_3050 ( pharmacists ) : 0.552
    occly_3060 ( physicians and surgeons ) : 0.377
    occly_3110 ( physician assistants ) : 0.107
    occly_3120 ( podiatrists ) : 0.807
    occly_3150 ( occupational therapists ) : 0.157
    occly_3160 ( physical therapists ) : 0.079
    occly_3200 ( radiation therapists ) : 0.081
    occly_3220 ( respiratory therapists ) : 0.111
    occly_3230 ( speech language pathologists ) : 0.026
    occly_3235 (  ) : -0.053
    occly_3250 ( veterinarians ) : 0.339
    occly_3255 (  ) : 0.083
    occly_3256 (  ) : 0.646
    occly_3257 (  ) : 0.042
    occly_3258 (  ) : 0.322
    occly_3310 ( dental hygienists ) : 0.193
    occly_3320 ( diagnostic related technologists and technicians ) : 0.163
    occly_3420 (  ) : -0.004
    occly_3500 ( licensed practical and licensed vocational nurses ) : 0.039
    occly_3510 ( medical records and health information technicians ) : -0.209
    occly_3600 ( nursing, psychiatric, and home health aides ) : -0.257
    occly_3610 ( occupational therapy assistants and aides ) : 0.200
    occly_3630 ( massage therapists ) : -0.160
    occly_3645 (  ) : -0.201
    occly_3647 (  ) : -0.159
    occly_3649 (  ) : -0.181
    occly_3655 (  ) : -0.285
    occly_3710 ( first-line supervisors of police and detectives ) : 0.172
    occly_3720 ( first-line supervisors of fire fighting and prevention workers ) : 0.223
    occly_3750 ( fire inspectors ) : 0.003
    occly_3820 ( police officers and detectives ) : 0.157
    occly_3840 (  ) : -0.280
    occly_3850 (  ) : 0.060
    occly_3860 (  ) : 0.118
    occly_3900 ( animal control ) : 0.754
    occly_3930 ( security guards and gaming surveillance officers ) : -0.242
    occly_3940 ( crossing guards ) : -1.007
    occly_3955 (  ) : -0.494
    occly_4010 ( first-line supervisors of food preparation and serving workers ) : -0.089
    occly_4020 (  ) : -0.266
    occly_4030 ( food preparation workers ) : -0.407
    occly_4050 ( combined food preparation and serving workers, including fast food ) : -0.325
    occly_4060 ( counter attendant, cafeteria, food concession, and coffee shop ) : -0.266
    occly_4110 ( waiters and waitresses ) : -0.342
    occly_4120 ( food servers, nonrestaurant ) : -0.391
    occly_4130 ( food preparation and serving related workers, nec ) : -0.343
    occly_4140 ( dishwashers ) : -0.443
    occly_4150 ( host and hostesses, restaurant, lounge, and coffee shop ) : -0.560
    occly_4200 ( first-line supervisors of housekeeping and janitorial workers ) : -0.048
    occly_4220 ( janitors and building cleaners ) : -0.274
    occly_4230 ( maids and housekeeping cleaners ) : -0.342
    occly_4250 ( grounds maintenance workers ) : -0.213
    occly_4300 ( first-line supervisors of gaming workers ) : 0.125
    occly_4350 ( nonfarm animal caretakers ) : -0.061
    occly_4430 ( entertainment attendants and related workers, nec ) : -0.197
    occly_4465 (  ) : 0.001
    occly_4500 ( barbers ) : -0.003
    occly_4520 ( personal appearance workers, nec ) : -0.258
    occly_4530 ( baggage porters, bellhops, and concierges ) : -0.324
    occly_4540 ( tour and travel guides ) : -1.144
    occly_4600 ( childcare workers ) : -0.095
    occly_4610 ( personal care aides ) : -0.340
    occly_4620 ( recreation and fitness workers ) : -0.368
    occly_4650 ( personal care and service workers, all other ) : -0.271
    occly_4700 ( first-line supervisors of sales workers ) : 0.078
    occly_4710 (  ) : 0.175
    occly_4720 ( cashiers ) : -0.387
    occly_4760 ( retail salespersons ) : -0.230
    occly_4800 ( advertising sales agents ) : 0.044
    occly_4810 ( insurance sales agents ) : 0.010
    occly_4820 ( securities, commodities, and financial services sales agents ) : 0.079
    occly_4840 ( sales representatives, services, all other ) : 0.019
    occly_4850 ( sales representatives, wholesale and manufacturing ) : 0.064
    occly_4900 ( models, demonstrators, and product promoters ) : -0.280
    occly_4920 ( real estate brokers and sales agents ) : 0.018
    occly_4930 ( sales engineers ) : 0.199
    occly_4940 ( telemarketers ) : -0.431
    occly_4950 ( door-to-door sales workers, news and street vendors, and related workers ) : -0.216
    occly_5000 ( first-line supervisors of office and administrative support workers ) : 0.041
    occly_5010 ( switchboard operators, including answering service ) : -0.212
    occly_5100 ( bill and account collectors ) : -0.091
    occly_5110 ( billing and posting clerks ) : -0.004
    occly_5160 ( bank tellers ) : -0.265
    occly_5240 ( customer service representatives ) : -0.144
    occly_5260 ( file clerks ) : -0.174
    occly_5300 ( hotel, motel, and resort desk clerks ) : -0.198
    occly_5310 ( interviewers, except eligibility and loan ) : -0.188
    occly_5320 ( library assistants, clerical ) : -0.598
    occly_5340 ( new account clerks ) : -0.135
    occly_5350 ( correspondent clerks and order clerks ) : -0.099
    occly_5400 ( receptionists and information clerks ) : -0.184
    occly_5410 ( reservation and transportation ticket agents and travel clerks ) : -0.087
    occly_5420 ( information and record clerks, all other ) : -0.179
    occly_5510 ( couriers and messengers ) : -0.078
    occly_5560 ( postal service mail sorters, processors, and processing machine operators ) : -0.237
    occly_5610 ( shipping, receiving, and traffic clerks ) : -0.026
    occly_5620 ( stock clerks and order fillers ) : -0.345
    occly_5630 ( weighers, measurers, checkers, and samplers, recordkeeping ) : -0.100
    occly_5700 ( secretaries and administrative assistants ) : -0.066
    occly_5810 ( data entry keyers ) : -0.195
    occly_5840 ( insurance claims and policy processing clerks ) : -0.068
    occly_5850 ( mail clerks and mail machine operators, except postal service ) : -0.469
    occly_5860 ( office clerks, general ) : -0.211
    occly_6005 ( first-line supervisors of farming, fishing, and forestry workers ) : 0.024
    occly_6040 ( graders and sorters, agricultural products ) : -0.290
    occly_6050 ( agricultural workers, nec ) : -0.156
    occly_6100 ( fishing and hunting workers ) : 0.194
    occly_6200 ( first-line supervisors of construction trades and extraction workers ) : 0.216
    occly_6210 ( boilermakers ) : -0.148
    occly_6230 ( carpenters ) : -0.087
    occly_6240 ( carpet, floor, and tile installers and finishers ) : -0.056
    occly_6250 ( cement masons, concrete finishers, and terrazzo workers ) : -0.042
    occly_6260 ( construction laborers ) : -0.082
    occly_6300 ( paving, surfacing, and tamping equipment operators ) : 0.094
    occly_6320 ( construction equipment operators except paving, surfacing, and tamping equipment operators ) : 0.003
    occly_6355 ( electricians ) : 0.078
    occly_6420 ( painters, construction and maintenance ) : -0.278
    occly_6440 ( pipelayers, plumbers, pipefitters, and steamfitters ) : 0.040
    occly_6460 ( plasterers and stucco masons ) : -0.218
    occly_6515 ( roofers ) : -0.093
    occly_6520 ( sheet metal workers, metal-working ) : -0.013
    occly_6600 ( helpers, construction trades ) : -0.258
    occly_6700 ( elevator installers and repairers ) : 0.135
    occly_6710 ( fence erectors ) : -0.411
    occly_6800 ( derrick, rotary drill, and service unit operators, and roustabouts, oil, gas, and mining ) : 0.318
    occly_6820 ( earth drillers, except oil and gas ) : 0.237
    occly_6920 (  ) : 0.063
    occly_6940 ( extraction workers, nec ) : 0.073
    occly_7010 ( computer, automated teller, and office machine repairers ) : -0.050
    occly_7040 ( electric motor, power tool, and related repairers ) : 0.003
    occly_7100 ( electrical and electronics repairers, transportation equipment, and industrial and utility ) : 0.065
    occly_7130 ( security and fire alarm systems installers ) : 0.041
    occly_7140 ( aircraft mechanics and service technicians ) : 0.054
    occly_7160 ( automotive glass installers and repairers ) : -0.159
    occly_7200 ( automotive service technicians and mechanics ) : -0.020
    occly_7220 ( heavy vehicle and mobile equipment service technicians and mechanics ) : 0.067
    occly_7340 ( maintenance and repair workers, general ) : -0.006
    occly_7360 ( millwrights ) : 0.106
    occly_7420 ( telecommunications line installers and repairers ) : 0.061
    occly_7510 ( coin, vending, and amusement machine servicers and repairers ) : -0.034
    occly_7550 ( manufactured building and mobile home installers ) : 0.024
    occly_7560 ( riggers ) : 0.059
    occly_7600 (  ) : 0.047
    occly_7610 ( helpers--installation, maintenance, and repair workers ) : -0.443
    occly_7700 ( first-line supervisors of production and operating workers ) : 0.038
    occly_7710 ( aircraft structure, surfaces, rigging, and systems assemblers ) : -0.170
    occly_7720 ( electrical, electronics, and electromechanical assemblers ) : -0.138
    occly_7730 ( engine and other machine assemblers ) : -0.105
    occly_7750 ( assemblers and fabricators, nec ) : -0.162
    occly_7800 ( bakers ) : -0.218
    occly_7810 ( butchers and other meat, poultry, and fish processing workers ) : -0.127
    occly_7830 ( food and tobacco roasting, baking, and drying machine operators and tenders ) : -0.119
    occly_7840 ( food batchmakers ) : -0.302
    occly_7855 ( food processing, nec ) : -0.040
    occly_7950 ( cutting, punching, and press machine setters, operators, and tenders, metal and plastic ) : -0.176
    occly_8000 ( grinding, lapping, polishing, and buffing machine tool setters, operators, and tenders, metal and plastic ) : -0.075
    occly_8220 ( metal workers and plastic workers, nec ) : -0.091
    occly_8300 ( laundry and dry-cleaning workers ) : -0.170
    occly_8310 ( pressers, textile, garment, and related materials ) : -0.400
    occly_8320 ( sewing machine operators ) : -0.294
    occly_8340 ( shoe machine operators and tenders ) : -0.042
    occly_8400 ( textile bleaching and dyeing, and cutting machine setters, operators, and tenders ) : -0.109
    occly_8410 ( textile knitting and weaving machine setters, operators, and tenders ) : -0.328
    occly_8440 (  ) : 0.095
    occly_8460 ( textile, apparel, and furnishings workers, nec ) : -0.101
    occly_8500 ( cabinetmakers and bench carpenters ) : -0.012
    occly_8510 ( furniture finishers ) : -0.236
    occly_8600 ( power plant operators, distributors, and dispatchers ) : 0.309
    occly_8630 ( plant and system operators, nec ) : 0.104
    occly_8710 ( cutting workers ) : -0.185
    occly_8740 ( inspectors, testers, sorters, samplers, and weighers ) : -0.023
    occly_8800 ( packaging and filling machine operators and tenders ) : -0.143
    occly_8830 ( photographic process workers and processing machine operators ) : -0.016
    occly_8850 ( adhesive bonding machine operators and tenders ) : -0.064
    occly_8910 ( etchers, engravers, and lithographers ) : -0.479
    occly_8920 ( molders, shapers, and casters, except metal and plastic ) : 0.058
    occly_8965 ( other production workers including semiconductor processors and cooling and freezing equipment operators ) : -0.090
    occly_9030 ( aircraft pilots and flight engineers ) : 0.582
    occly_9040 ( air traffic controllers and airfield operations specialists ) : 0.384
    occly_9110 (  ) : -0.025
    occly_9130 ( driver/sales workers and truck drivers ) : -0.042
    occly_9140 ( taxi drivers and chauffeurs ) : -0.309
    occly_9200 ( locomotive engineers and operators ) : 0.038
    occly_9310 ( ship and boat captains and operators ) : 0.326
    occly_9330 (  ) : 0.000
    occly_9350 ( parking lot attendants ) : -0.316
    occly_9360 ( automotive and watercraft service attendants ) : -0.284
    occly_9415 (  ) : -0.325
    occly_9510 ( crane and tower operators ) : 0.051
    occly_9600 ( industrial truck and tractor operators ) : -0.037
    occly_9610 ( cleaners of vehicles and equipment ) : -0.366
    occly_9620 ( laborers and freight, stock, and material movers, hand ) : -0.241
    occly_9630 ( machine feeders and offbearers ) : -0.121
    occly_9640 ( packers and packagers, hand ) : -0.098
    occly_9650 ( pumping station operators ) : 0.004
    occly_9730 (  ) : 0.191
    occly_9750 ( material moving workers, nec ) : -0.179
    occly_9840 (  ) : 0.200
    indly_170 (  ) : -0.035
    indly_280 ( other primary metal industries ) : 0.075
    indly_290 ( screw machine products ) : -0.019
    indly_370 ( cycles and miscellaneous transportation equipment ) : 0.196
    indly_380 ( photographic equipment and supplies ) : 0.252
    indly_390 ( toys, amusement, and sporting goods ) : 0.324
    indly_480 (  ) : 0.034
    indly_490 (  ) : 0.419
    indly_570 (  ) : 0.180
    indly_590 ( mobile home dealers ) : 0.268
    indly_670 ( vending machine operators ) : 0.067
    indly_1070 (  ) : 0.004
    indly_1090 (  ) : 0.015
    indly_1170 (  ) : 0.105
    indly_1190 (  ) : -0.011
    indly_1270 (  ) : -0.028
    indly_1290 (  ) : -0.037
    indly_1480 (  ) : -0.076
    indly_1670 (  ) : -0.593
    indly_1680 (  ) : -0.114
    indly_1690 (  ) : 0.338
    indly_1870 (  ) : 0.155
    indly_1890 (  ) : 0.070
    indly_2070 (  ) : 0.298
    indly_2090 (  ) : 0.229
    indly_2190 (  ) : 0.258
    indly_2280 (  ) : 0.119
    indly_2290 (  ) : 0.092
    indly_2470 (  ) : 0.019
    indly_2490 (  ) : 0.054
    indly_2590 (  ) : -0.102
    indly_2780 (  ) : -0.301
    indly_2790 (  ) : 0.111
    indly_2880 (  ) : 0.045
    indly_2970 (  ) : 0.047
    indly_3080 (  ) : 0.020
    indly_3190 (  ) : 0.048
    indly_3360 (  ) : 0.071
    indly_3380 (  ) : 0.129
    indly_3390 (  ) : 0.097
    indly_3490 (  ) : 0.056
    indly_3570 (  ) : 0.047
    indly_3580 (  ) : 0.059
    indly_3590 (  ) : 0.073
    indly_3680 (  ) : 0.033
    indly_3870 (  ) : -0.121
    indly_3890 (  ) : -0.012
    indly_3970 (  ) : 0.092
    indly_3980 (  ) : -0.047
    indly_4080 (  ) : 0.025
    indly_4170 (  ) : 0.002
    indly_4180 (  ) : 0.078
    indly_4270 (  ) : 0.063
    indly_4380 (  ) : 0.137
    indly_4390 (  ) : 0.014
    indly_4470 (  ) : 0.001
    indly_4480 (  ) : 0.022
    indly_4490 (  ) : 0.147
    indly_4560 (  ) : 0.009
    indly_4585 (  ) : 0.072
    indly_4590 (  ) : -0.237
    indly_4670 (  ) : 0.128
    indly_4690 (  ) : -0.070
    indly_4770 (  ) : 0.030
    indly_4780 (  ) : -0.026
    indly_4790 (  ) : 0.112
    indly_4880 (  ) : -0.146
    indly_4970 (  ) : -0.150
    indly_4980 (  ) : -0.122
    indly_5070 (  ) : -0.012
    indly_5090 (  ) : -0.045
    indly_5170 (  ) : -0.161
    indly_5180 (  ) : -0.234
    indly_5270 (  ) : -0.278
    indly_5280 (  ) : -0.110
    indly_5290 (  ) : -0.122
    indly_5370 (  ) : -0.415
    indly_5380 (  ) : -0.231
    indly_5390 (  ) : -0.151
    indly_5470 (  ) : -0.254
    indly_5490 (  ) : -0.346
    indly_5570 (  ) : -0.252
    indly_5580 (  ) : -0.066
    indly_5591 (  ) : 0.008
    indly_5670 (  ) : -0.216
    indly_5690 (  ) : -0.086
    indly_6070 (  ) : 0.006
    indly_6090 (  ) : 0.134
    indly_6170 (  ) : 0.113
    indly_6180 (  ) : -0.052
    indly_6190 (  ) : -0.204
    indly_6280 (  ) : 0.139
    indly_6290 (  ) : 0.025
    indly_6380 (  ) : -0.038
    indly_6470 (  ) : -0.164
    indly_6672 (  ) : 0.285
    indly_6680 (  ) : 0.134
    indly_6690 (  ) : 0.050
    indly_6695 (  ) : 0.059
    indly_6770 (  ) : -0.081
    indly_6970 (  ) : 0.077
    indly_6990 (  ) : 0.062
    indly_7070 (  ) : 0.017
    indly_7170 (  ) : -0.188
    indly_7190 (  ) : 0.063
    indly_7270 (  ) : 0.139
    indly_7290 (  ) : 0.121
    indly_7370 (  ) : 0.028
    indly_7380 (  ) : 0.131
    indly_7390 (  ) : 0.116
    indly_7460 (  ) : 0.078
    indly_7470 (  ) : 0.116
    indly_7490 (  ) : -0.028
    indly_7570 (  ) : 0.012
    indly_7580 (  ) : -0.405
    indly_7590 (  ) : -0.059
    indly_7680 (  ) : -0.086
    indly_7690 (  ) : -0.090
    indly_7860 (  ) : -0.104
    indly_7870 (  ) : -0.118
    indly_7880 (  ) : -0.067
    indly_7970 (  ) : 0.055
    indly_7980 (  ) : 0.011
    indly_8170 (  ) : -0.109
    indly_8180 (  ) : 0.028
    indly_8270 (  ) : -0.025
    indly_8370 (  ) : -0.109
    indly_8380 (  ) : -0.060
    indly_8390 (  ) : -0.362
    indly_8470 (  ) : -0.203
    indly_8560 (  ) : -0.098
    indly_8570 (  ) : -0.097
    indly_8660 (  ) : -0.069
    indly_8670 (  ) : -0.154
    indly_8680 (  ) : -0.129
    indly_8690 (  ) : -0.074
    indly_8770 (  ) : -0.012
    indly_8780 (  ) : -0.130
    indly_8870 (  ) : 0.052
    indly_8880 (  ) : -0.026
    indly_8890 (  ) : -1.294
    indly_8980 (  ) : -0.060
    indly_9070 (  ) : -0.032
    indly_9160 (  ) : -0.246
    indly_9170 (  ) : -0.070
    indly_9290 (  ) : -0.013
    indly_9370 (  ) : -0.014
    indly_9380 (  ) : -0.007
    indly_9470 (  ) : 0.062
    indly_9480 (  ) : -0.027
    indly_9590 (  ) : 0.036
    indly_9890 (  ) : 0.000
    classwly_13 ( self-employed, not incorporated ) : -1.108
    classwly_14 ( self-employed, incorporated ) : 0.220
    classwly_25 ( federal government employee ) : 0.128
    classwly_27 ( state government employee ) : -0.093
    classwly_28 ( local government employee ) : -0.020
    pension_at_w_ly_2 ( pension plan at work, but not included ) : -0.032
    pension_at_w_ly_3 ( included in pension plan at work ) : 0.312
    firmsize_ly_1 ( under 10 ) : -0.212
    firmsize_ly_4 ( 10 to 49 ) : -0.073
    firmsize_ly_6 ( 50 to 99 ) : -0.011
    firmsize_ly_8 ( 500 to 999 ) : 0.020
    firmsize_ly_9 ( 1000+ ) : 0.035
    actnlfly_0 ( niu ) : 0.388
    actnlfly_10 ( ill or disabled ) : -0.008
    actnlfly_20 ( taking care of home/family ) : -0.340
    actnlfly_30 ( going to school ) : -0.482
    actnlfly_40 ( retired ) : -0.224
    actnlfly_50 ( other ) : 0.128
    spmmort_1 ( owners with a mortgage ) : 0.068
    statefip_2 ( alaska ) : 0.128
    statefip_5 ( arkansas ) : -0.015
    statefip_6 ( california ) : 0.052
    statefip_9 ( connecticut ) : 0.077
    statefip_11 ( district of columbia ) : 0.032
    statefip_15 ( hawaii ) : 0.068
    statefip_16 ( idaho ) : -0.044
    statefip_20 ( kansas ) : -0.063
    statefip_21 ( kentucky ) : -0.008
    statefip_23 ( maine ) : -0.070
    statefip_25 ( massachusetts ) : 0.045
    statefip_29 ( missouri ) : -0.059
    statefip_30 ( montana ) : -0.018
    statefip_31 ( nebraska ) : 0.003
    statefip_32 ( nevada ) : 0.038
    statefip_33 ( new hampshire ) : 0.027
    statefip_35 ( new mexico ) : -0.031
    statefip_37 ( north carolina ) : -0.007
    statefip_39 ( ohio ) : -0.000
    statefip_40 ( oklahoma ) : -0.017
    statefip_41 ( oregon ) : -0.011
    statefip_42 ( pennsylvania ) : -0.005
    statefip_44 ( rhode island ) : 0.026
    statefip_45 ( south carolina ) : -0.029
    statefip_46 ( south dakota ) : -0.035
    statefip_47 ( tennessee ) : -0.019
    statefip_54 ( west virginia ) : -0.045
    statefip_56 ( wyoming ) : 0.062
    state_ly_6 ( california ) : -0.022
    state_ly_10 ( delaware ) : -0.090
    state_ly_12 ( florida ) : 0.010
    state_ly_16 ( idaho ) : -0.029
    state_ly_23 ( maine ) : -0.061
    state_ly_24 ( maryland ) : 0.018
    state_ly_25 ( massachusetts ) : 0.127
    state_ly_34 ( new jersey ) : -0.030
    state_ly_37 ( north carolina ) : 0.030
    state_ly_40 ( oklahoma ) : -0.038
    state_ly_49 ( utah ) : -0.052
    state_ly_51 ( virginia ) : 0.047
    state_ly_91 ( abroad ) : -0.091
    whymove_1 ( change in marital status ) : -0.029
    whymove_2 ( to establish own household ) : -0.068
    whymove_3 ( other family reason ) : 0.004
    whymove_4 ( new job or job transfer ) : -0.000
    whymove_5 ( to look for work or lost job ) : -0.254
    whymove_10 ( wanted new or better housing ) : 0.013
    whymove_11 ( wanted better neighborhood ) : 0.048
    whymove_12 ( for cheaper housing ) : -0.034
    whymove_14 ( attend/leave college ) : -0.287
    whymove_18 ( natural disaster ) : 0.146
    whymove_19 ( foreclosure or eviction ) : 0.026
    mig_stat_ly_4 ( moved within state, different county ) : 0.006
    mig_stat_ly_6 ( abroad ) : -0.007
    health_1 ( excellent ) : 0.027
    health_3 ( good ) : -0.054
    health_4 ( fair ) : -0.129
    health_5 ( poor ) : -0.174
    vet1_2 ( august 1990 to august 2001 ) : 0.004
    vet1_3 ( may 1975 to july 1990 ) : 0.001
    vet1_4 ( vietnam era (august 1964 to april 1975) ) : -0.067
    csvisleg_1 ( no ) : 0.013
    csvisleg_2 ( yes ) : 0.002
    csvisleg_98 ( blank ) : -0.015
    paidhour_1 ( no ) : 0.109
    paidhour_2 ( yes ) : -0.031
    union_1 ( no union coverage ) : -0.011
    union_2 ( member of labor union ) : 0.073
    bpl_1.0 ( usa, canada & dependent ) : 0.004
    bpl_8.0 ( developed asia ) : 0.021
    fbpl_5.0 ( central and caribean ) : -0.013
    fbpl_7.0 ( europe ) : 0.005
    fbpl_9.0 ( east asia ) : -0.006

### Grid:

    grid: [1.45096612e-03 1.35317586e-03 1.26197633e-03 1.17692335e-03
    1.09760266e-03 1.02362791e-03 9.54638815e-04 8.90299354e-04
    8.30296157e-04 7.74336975e-04 7.22149255e-04 6.73478812e-04
    6.28088594e-04 5.85757525e-04 5.46279428e-04 5.09462023e-04
    4.75125988e-04 4.43104086e-04 4.13240354e-04 3.85389337e-04
    3.59415386e-04 3.35191992e-04 3.12601173e-04 2.91532900e-04
    2.71884559e-04 2.53560449e-04 2.36471324e-04 2.20533948e-04
    2.05670698e-04 1.91809181e-04 1.78881884e-04 1.66825844e-04
    1.55582341e-04 1.45096612e-04 1.35317586e-04 1.26197633e-04
    1.17692335e-04 1.09760266e-04 1.02362791e-04 9.54638815e-05
    8.90299354e-05 8.30296157e-05 7.74336975e-05 7.22149255e-05
    6.73478812e-05 6.28088594e-05 5.85757525e-05 5.46279428e-05
    5.09462023e-05 4.75125988e-05 4.43104086e-05 4.13240354e-05
    3.85389337e-05 3.59415386e-05 3.35191992e-05 3.12601173e-05
    2.91532900e-05 2.71884559e-05 2.53560449e-05 2.36471324e-05
    2.20533948e-05 2.05670698e-05 1.91809181e-05 1.78881884e-05
    1.66825844e-05 1.55582341e-05 1.45096612e-05 1.35317586e-05
    1.26197633e-05 1.17692335e-05 1.09760266e-05 1.02362791e-05
    9.54638815e-06 8.90299354e-06 8.30296157e-06 7.74336975e-06
    7.22149255e-06 6.73478812e-06 6.28088594e-06 5.85757525e-06
    5.46279428e-06 5.09462023e-06 4.75125988e-06 4.43104086e-06
    4.13240354e-06 3.85389337e-06 3.59415386e-06 3.35191992e-06
    3.12601173e-06 2.91532900e-06 2.71884559e-06 2.53560449e-06
    2.36471324e-06 2.20533948e-06 2.05670698e-06 1.91809181e-06
    1.78881884e-06 1.66825844e-06 1.55582341e-06 1.45096612e-06]





















































































## LassoCV10

### Code: 

    model = skl.LassoCV(normalize = True, cv = 10)
    model.fit(X,Y)
    predictions = model.predict(X)

### Results

    Time to run: 617.1552991867065 to run
    \lambda:  (8.302961573649618e-06,) log10: [-5.08076697] ln: [-11.69889829]
    Coefficients: 
    [ 0.00401511 -0.         -0.1233951  ... -0.00635141  0.
    -0.        ]
    Mean squared error: 0.29
    Coefficient of determination: 0.57
    age ( age ) : 0.004
    educ_cat_1.0 (  ) : -0.123
    educ_cat_2.0 (  ) : -0.032
    educ_cat_4.0 (  ) : 0.067
    educ_cat_5.0 (  ) : 0.283
    race_cat_1.0 (  ) : 0.043
    race_cat_2.0 (  ) : -0.012
    male_0.0 (  ) : -0.273
    hhtenure_1 ( owned or being bought ) : 0.051
    hhtenure_3 ( occupied without payment of cash rent ) : -0.027
    region_11 ( new england division ) : 0.026
    region_21 ( east north central division ) : -0.011
    region_32 ( east south central division ) : -0.034
    region_42 ( pacific division ) : 0.021
    metarea_120 ( albany, ga ) : -0.124
    metarea_200 ( albuquerque, nm ) : -0.008
    metarea_280 ( altoona, pa msa ) : -0.051
    metarea_320 ( amarillo, tx ) : -0.026
    metarea_440 ( ann arbor, mi ) : 0.103
    metarea_462 ( oshkosh-neenah, wi ) : -0.187
    metarea_480 ( asheville, nc ) : -0.098
    metarea_521 ( atlanta-sandy springs-marietta, ga ) : 0.012
    metarea_641 ( austin-round rock, tx ) : 0.054
    metarea_680 ( bakersfield, ca ) : -0.134
    metarea_721 ( baltimore-towson, md ) : 0.071
    metarea_730 ( bangor, me ) : -0.041
    metarea_741 ( barnstable town, ma ) : -0.073
    metarea_760 ( baton rouge, la ) : 0.032
    metarea_841 ( beaumont-port arthur, tx ) : 0.083
    metarea_860 ( bellingham, wa ) : 0.041
    metarea_880 ( billings, mt ) : -0.039
    metarea_920 ( biloxi-gulfport, ms ) : -0.039
    metarea_960 ( binghamton, ny ) : -0.032
    metarea_1081 ( boise city-nampa, id ) : -0.078
    metarea_1124 ( boston-cambridge-quincy, ma-nh ) : 0.016
    metarea_1280 ( buffalo-niagara falls, ny ) : -0.047
    metarea_1360 ( cedar rapids, ia ) : -0.048
    metarea_1440 ( charleston-north charleston, sc ) : -0.031
    metarea_1480 ( charleston, wv ) : -0.087
    metarea_1605 ( chicago-naperville-joliet, il-in-wi ) : 0.060
    metarea_1700 ( coeur d'alene, id ) : -0.091
    metarea_1720 ( colorado springs, co ) : -0.017
    metarea_1800 ( columbus, ga/al ) : -0.148
    metarea_1922 ( dallas-fort worth-arlington, tx ) : 0.025
    metarea_1930 ( danbury, ct ) : 0.132
    metarea_2001 ( springfield, oh ) : -0.051
    metarea_2002 ( dayton, oh ) : -0.145
    metarea_2030 ( decatur, al ) : -0.046
    metarea_2082 ( boulder, co ) : 0.012
    metarea_2083 ( denver-aurora, co ) : 0.035
    metarea_2190 ( dover, de ) : -0.003
    metarea_2241 ( duluth, mn/wi ) : -0.140
    metarea_2300 ( el centro, ca ) : -0.145
    metarea_2310 ( el paso, tx ) : -0.086
    metarea_2360 ( erie, pa ) : -0.151
    metarea_2400 ( eugene-springfield, or ) : -0.032
    metarea_2581 ( fayetteville-springdale-rogers, ar-mo ) : 0.060
    metarea_2640 ( flint, mi ) : -0.146
    metarea_2670 ( fort collins-loveland, co ) : -0.055
    metarea_2760 ( fort wayne, in ) : -0.019
    metarea_2840 ( fresno, ca ) : -0.084
    metarea_2900 ( gainesville, fl ) : -0.090
    metarea_3060 ( greeley, co ) : -0.042
    metarea_3162 ( greenville, sc ) : -0.035
    metarea_3181 ( hagerstown-martinsburg, md-wv ) : 0.034
    metarea_3362 ( houston-baytown-sugar land, tx ) : 0.081
    metarea_3440 ( huntsville,al ) : -0.067
    metarea_3480 ( indianapolis, in ) : 0.034
    metarea_3520 ( jackson, mi ) : -0.072
    metarea_3560 ( jackson, ms ) : -0.036
    metarea_3590 ( jacksonville,fl ) : 0.010
    metarea_3600 ( jacksonville, nc ) : -0.034
    metarea_3621 ( janvesville, wi ) : -0.024
    metarea_3661 ( johnson city, tn ) : -0.066
    metarea_3720 ( kalamazoo-portage, mi ) : -0.019
    metarea_3760 ( kansas city, mo/ks ) : 0.069
    metarea_3830 ( kingston, ny ) : 0.039
    metarea_4000 ( lancaster, pa ) : 0.089
    metarea_4040 ( lansing-east lansing, mi ) : -0.035
    metarea_4080 ( laredo, tx ) : -0.020
    metarea_4100 ( las cruces, nm ) : -0.059
    metarea_4130 ( las vegas-paradise, nv ) : 0.023
    metarea_4150 ( lawrence, ks ) : 0.064
    metarea_4200 ( lawton, ok ) : -0.041
    metarea_4280 ( lexington-fayette, ky ) : -0.051
    metarea_4483 ( los angeles-long beach-santa ana, ca ) : 0.020
    metarea_4600 ( lubbock, tx ) : -0.098
    metarea_4640 ( lynchburg, va ) : -0.035
    metarea_4681 ( macon, ga ) : -0.082
    metarea_4720 ( madison, wi ) : 0.019
    metarea_4940 ( merced, ca ) : -0.054
    metarea_5001 ( miami-fort lauderdale-miami beach, fl ) : 0.044
    metarea_5081 ( milwaukee-waukesha-west allis, wi ) : -0.007
    metarea_5121 ( minneapolis-st. paul-bloomington, mn/wi ) : 0.043
    metarea_5160 ( mobile, al ) : 0.006
    metarea_5170 ( modesto, ca ) : -0.007
    metarea_5200 ( monroe, la ) : -0.021
    metarea_5220 ( monroe, mi ) : 0.118
    metarea_5321 ( muskegon-norton shores, mi ) : -0.076
    metarea_5331 ( myrtle beach-conway-north myrtle beach, sc ) : -0.087
    metarea_5361 ( nashville-davidson-murfreesboro, tn ) : 0.007
    metarea_5481 ( new haven, ct ) : 0.016
    metarea_5606 ( new york-northern new jersey-long island, ny-nj-pa ) : 0.198
    metarea_5790 ( ocala, fl ) : -0.105
    metarea_5801 ( midland, tx ) : 0.123
    metarea_5840 ( ocean city, nj ) : -0.356
    metarea_5910 ( olympia, wa ) : -0.091
    metarea_5960 ( orlando, fl ) : -0.061
    metarea_6011 ( panama city-lynn haven, fl ) : 0.010
    metarea_6081 ( pensacola-ferry pass-brent, fl ) : -0.107
    metarea_6161 ( philadelphia-camden-wilmington, pa/nj/de ) : 0.059
    metarea_6201 ( phoenix-mesa-scottsdale, az ) : 0.017
    metarea_6280 ( pittsburg, pa ) : -0.015
    metarea_6401 ( portland-south portland, me ) : 0.053
    metarea_6442 ( portland-vancouver-beaverton, or/wa ) : 0.001
    metarea_6520 ( provo-orem, ut ) : -0.028
    metarea_6642 ( raleigh-carey, nc ) : 0.005
    metarea_6680 ( reading, pa ) : -0.099
    metarea_6880 ( rockford, il ) : -0.001
    metarea_6980 ( st. cloud, mn ) : -0.062
    metarea_7080 ( salem, or ) : -0.014
    metarea_7130 ( salisbury, md ) : -0.097
    metarea_7321 ( san diego-carlsbad-san marcos, ca ) : 0.044
    metarea_7364 ( napa, ca ) : 0.068
    metarea_7365 ( san francisco-oakland-fremont, ca ) : 0.127
    metarea_7401 ( san jose-sunnyvale-santa clara, ca ) : 0.158
    metarea_7461 ( san luis obispo-paso robles, ca ) : 0.096
    metarea_7471 ( santa barbara-santa maria-goleta, ca ) : 0.080
    metarea_7481 ( santa cruz-watsonville, ca ) : 0.073
    metarea_7490 ( santa fe, nm ) : 0.014
    metarea_7511 ( sarasota-bradenton-venice, fl ) : 0.020
    metarea_7520 ( savannah, ga ) : 0.043
    metarea_7560 ( scranton-wilkes-barre, pa ) : -0.008
    metarea_7601 ( seattle-tacoma-bellevue, wa ) : 0.032
    metarea_7681 ( shreveport-bossier city, la ) : 0.022
    metarea_7760 ( sioux falls, sd ) : -0.028
    metarea_7920 ( springfield, mo ) : -0.033
    metarea_8160 ( syracuse, ny ) : -0.024
    metarea_8240 ( tallahassee, fl ) : -0.030
    metarea_8440 ( topeka, ks ) : 0.061
    metarea_8520 ( tucson, az ) : -0.002
    metarea_8600 ( tuscaloosa, al ) : -0.073
    metarea_8700 ( valdosta, ga ) : -0.024
    metarea_8731 ( oxnard-thousand oaks-ventura, ca ) : 0.074
    metarea_8740 ( vero beach, fl ) : -0.111
    metarea_8750 ( victoria, tx ) : -0.025
    metarea_8760 ( vineland-milville-bridgetown, nj ) : 0.088
    metarea_8781 ( visalia-porterville, ca ) : -0.037
    metarea_8840 ( washington, dc/md/va ) : 0.157
    metarea_8920 ( waterloo-cedar falls, ia ) : -0.055
    metarea_8940 ( wausau, wi ) : -0.057
    metarea_9040 ( wichita, ks ) : -0.031
    metarea_9321 ( youngstown-warren-boardman, oh ) : -0.107
    metarea_9997 ( other metropolitan areas, unidentified ) : -0.050
    metarea_9998 ( niu, household not in a metropolitan area ) : -0.066
    metarea_9999 ( missing data ) : -0.022
    unitsstr_1 ( mobile home or trailer ) : -0.027
    unitsstr_7 ( 5-9 family building ) : -0.009
    unitsstr_11 ( one unit, unspecified type ) : 0.027
    nfams_1 ( 1 family or n/a ) : 0.007
    nfams_3 ( 3 ) : -0.002
    nfams_4 ( 4 ) : -0.008
    nfams_6 ( 6 ) : -0.096
    nfams_8 ( 8 ) : 0.180
    ncouples_2 ( 2 ) : -0.058
    nmothers_2 ( 2 ) : -0.021
    nmothers_3 ( 3 ) : -0.091
    nfathers_1 ( 1 ) : 0.002
    nfathers_2 ( 2 ) : -0.020
    nfathers_3 ( 3 ) : -0.054
    marst_1 ( married, spouse present ) : 0.134
    marst_3 ( separated ) : -0.027
    marst_5 ( widowed ) : -0.046
    marst_6 ( never married/single ) : -0.073
    famsize_3 ( 3 family members present ) : 0.001
    famsize_6 ( 6 family members present ) : -0.010
    famsize_7 ( 7 family members present ) : -0.015
    famsize_8 ( 8 family members present ) : -0.034
    famsize_14 ( 14 family members present ) : -0.103
    famsize_15 ( 15 family members present ) : -0.323
    ftype_2 ( nonfamily householder ) : 0.045
    ftype_3 ( related subfamily ) : -0.063
    ftype_4 ( unrelated subfamily ) : -0.029
    famkind_1 ( husband/wife family ) : -0.068
    famkind_3 ( female reference person ) : 0.130
    yrimmig_0 ( niu ) : 0.003
    yrimmig_1985 ( 1984-1985 ) : 0.012
    yrimmig_1989 ( 1988-1989 ) : 0.000
    yrimmig_2001 ( 2000-2001 (2001 cps: 1998-2001) ) : -0.017
    yrimmig_2003 ( 2002-2003 (2003 cps: 2000-2003) ) : -0.021
    yrimmig_2005 ( 2004-2005 (2005 cps: 2002-2005) ) : -0.046
    yrimmig_2007 ( 2004-2007 ) : -0.028
    yrimmig_2009 ( 2006-2009 ) : -0.030
    yrimmig_2012 ( 2010-2012 (2014 cps: 2010-2011) ) : -0.074
    citizen_1 ( born in u.s ) : 0.000
    citizen_3 ( born abroad of american parents ) : 0.018
    citizen_5 ( not a citizen ) : -0.054
    nativity_4 ( both parents foreign ) : 0.001
    hispan_0 ( not hispanic ) : 0.009
    hispan_410 ( central/south american ) : -0.013
    occ_0 ( Missing data? ) : -0.279
    occ_10 ( chief executives and legislators/public administration ) : 0.078
    occ_20 ( general and operations managers ) : 0.083
    occ_40 (  ) : 0.006
    occ_135 (  ) : 0.023
    occ_136 (  ) : 0.089
    occ_150 ( purchasing managers ) : 0.039
    occ_220 ( constructions managers ) : 0.094
    occ_325 (  ) : 0.208
    occ_340 (  ) : -0.022
    occ_350 ( medical and health services managers ) : 0.123
    occ_420 ( social and community service managers ) : 0.028
    occ_500 ( agents and business managers of artists, performers, and athletes ) : 0.368
    occ_565 (  ) : 0.112
    occ_600 ( cost estimators ) : 0.270
    occ_630 (  ) : 0.008
    occ_640 (  ) : 0.041
    occ_650 (  ) : 0.067
    occ_725 (  ) : 0.090
    occ_726 (  ) : 0.013
    occ_735 (  ) : 0.191
    occ_810 ( appraisers and assessors of real estate ) : 0.096
    occ_830 ( credit analysts ) : 0.094
    occ_850 ( personal financial advisors ) : 0.098
    occ_860 ( insurance underwriters ) : 0.034
    occ_940 ( tax preparers ) : -0.160
    occ_950 ( financial specialists, nec ) : 0.055
    occ_1005 (  ) : 0.089
    occ_1007 (  ) : 0.023
    occ_1010 ( computer programmers ) : 0.007
    occ_1020 ( software developers, applications and systems software ) : 0.068
    occ_1060 ( database administrators ) : 0.226
    occ_1105 (  ) : 0.113
    occ_1106 (  ) : 0.000
    occ_1240 ( mathematical science occupations, nec ) : 0.099
    occ_1320 ( aerospace engineers ) : 0.108
    occ_1330 (  ) : 0.166
    occ_1340 (  ) : 0.012
    occ_1350 ( chemical engineers ) : 0.199
    occ_1430 ( industrial engineers, including health and safety ) : 0.085
    occ_1460 ( mechanical engineers ) : 0.173
    occ_1510 (  ) : 0.038
    occ_1520 ( petroleum, mining and geological engineers, including mining safety engineers ) : 0.341
    occ_1530 ( engineers, nec ) : 0.017
    occ_1540 ( drafters ) : 0.027
    occ_1560 ( surveying and mapping technicians ) : -0.016
    occ_1640 ( conservation scientists and foresters ) : -0.057
    occ_1660 (  ) : 0.309
    occ_1700 ( astronomers and physicists ) : 0.143
    occ_1720 ( chemists and materials scientists ) : 0.099
    occ_1800 ( economists and market researchers ) : 0.277
    occ_1820 ( psychologists ) : 0.070
    occ_1860 (  ) : -0.013
    occ_1910 ( biological technicians ) : -0.143
    occ_1930 ( geological and petroleum technicians, and nuclear technicians ) : -0.220
    occ_1965 (  ) : -0.028
    occ_2000 ( counselors ) : -0.007
    occ_2060 ( religious workers, nec ) : -0.424
    occ_2100 ( lawyers, and judges, magistrates, and other judicial workers ) : 0.069
    occ_2160 (  ) : -0.031
    occ_2200 ( postsecondary teachers ) : 0.059
    occ_2300 ( preschool and kindergarten teachers ) : -0.023
    occ_2430 ( librarians ) : -0.032
    occ_2440 ( library technicians ) : -0.339
    occ_2540 ( teacher assistants ) : -0.052
    occ_2710 (  ) : 0.117
    occ_2720 ( athletes, coaches, umpires, and related workers ) : 0.121
    occ_2750 ( musicians, singers, and related workers ) : -0.270
    occ_2760 ( entertainers and performers, sports and related workers, all other ) : 0.118
    occ_2825 ( public relations specialists ) : 0.097
    occ_2830 (  ) : 0.032
    occ_2850 ( writers and authors ) : -0.019
    occ_2960 (  ) : -0.804
    occ_3000 ( chiropractors ) : -0.023
    occ_3010 ( dentists ) : 0.219
    occ_3060 ( physicians and surgeons ) : 0.194
    occ_3110 ( physician assistants ) : 0.097
    occ_3160 ( physical therapists ) : 0.047
    occ_3200 ( radiation therapists ) : 0.142
    occ_3210 ( recreational therapists ) : -0.021
    occ_3230 ( speech language pathologists ) : 0.112
    occ_3235 (  ) : -1.063
    occ_3255 (  ) : 0.151
    occ_3257 (  ) : 0.194
    occ_3420 (  ) : -0.093
    occ_3600 ( nursing, psychiatric, and home health aides ) : -0.014
    occ_3620 ( physical therapist assistants and aides ) : 0.059
    occ_3645 (  ) : -0.040
    occ_3646 (  ) : -0.020
    occ_3700 ( first-line supervisors of correctional officers ) : 0.024
    occ_3740 ( firefighters ) : 0.069
    occ_3800 ( sheriffs, bailiffs, correctional officers, and jailers ) : -0.038
    occ_3850 (  ) : 0.065
    occ_3860 (  ) : 0.288
    occ_3900 ( animal control ) : -0.275
    occ_3940 ( crossing guards ) : -0.035
    occ_4000 ( chefs and cooks ) : -0.050
    occ_4020 (  ) : -0.080
    occ_4040 ( bartenders ) : -0.223
    occ_4050 ( combined food preparation and serving workers, including fast food ) : -0.183
    occ_4060 ( counter attendant, cafeteria, food concession, and coffee shop ) : -0.271
    occ_4120 ( food servers, nonrestaurant ) : -0.090
    occ_4140 ( dishwashers ) : -0.217
    occ_4220 ( janitors and building cleaners ) : -0.036
    occ_4230 ( maids and housekeeping cleaners ) : -0.063
    occ_4240 ( pest control workers ) : -0.003
    occ_4250 ( grounds maintenance workers ) : -0.036
    occ_4350 ( nonfarm animal caretakers ) : -0.127
    occ_4400 ( gaming services workers ) : 0.009
    occ_4420 ( ushers, lobby attendants, and ticket takers ) : 0.022
    occ_4430 ( entertainment attendants and related workers, nec ) : -0.192
    occ_4460 ( funeral service workers and embalmers ) : -0.253
    occ_4530 ( baggage porters, bellhops, and concierges ) : -0.041
    occ_4540 ( tour and travel guides ) : 0.294
    occ_4600 ( childcare workers ) : -0.247
    occ_4610 ( personal care aides ) : -0.058
    occ_4640 ( residential advisors ) : -0.082
    occ_4650 ( personal care and service workers, all other ) : 0.014
    occ_4700 ( first-line supervisors of sales workers ) : 0.013
    occ_4720 ( cashiers ) : -0.037
    occ_4760 ( retail salespersons ) : -0.010
    occ_4800 ( advertising sales agents ) : 0.008
    occ_4840 ( sales representatives, services, all other ) : 0.006
    occ_4850 ( sales representatives, wholesale and manufacturing ) : 0.110
    occ_4900 ( models, demonstrators, and product promoters ) : -0.162
    occ_4920 ( real estate brokers and sales agents ) : 0.170
    occ_4950 ( door-to-door sales workers, news and street vendors, and related workers ) : -0.217
    occ_5000 ( first-line supervisors of office and administrative support workers ) : 0.025
    occ_5010 ( switchboard operators, including answering service ) : -0.145
    occ_5110 ( billing and posting clerks ) : -0.093
    occ_5120 ( bookkeeping, accounting, and auditing clerks ) : -0.091
    occ_5160 ( bank tellers ) : -0.053
    occ_5220 ( court, municipal, and license clerks ) : -0.119
    occ_5310 ( interviewers, except eligibility and loan ) : -0.052
    occ_5360 ( human resources assistants, except payroll and timekeeping ) : -0.048
    occ_5400 ( receptionists and information clerks ) : -0.062
    occ_5530 ( meter readers, utilities ) : -0.100
    occ_5540 ( postal service clerks ) : -0.041
    occ_5610 ( shipping, receiving, and traffic clerks ) : -0.181
    occ_5800 ( computer operators ) : -0.005
    occ_5820 ( word processors and typists ) : -0.199
    occ_5840 ( insurance claims and policy processing clerks ) : -0.058
    occ_5920 ( statistical assistants ) : -0.069
    occ_5940 ( office and administrative support workers, nec ) : -0.062
    occ_6220 ( brickmasons, blockmasons, and stonemasons ) : -0.052
    occ_6260 ( construction laborers ) : -0.077
    occ_6320 ( construction equipment operators except paving, surfacing, and tamping equipment operators ) : 0.067
    occ_6330 ( drywall installers, ceiling tile installers, and tapers ) : -0.143
    occ_6460 ( plasterers and stucco masons ) : -0.003
    occ_6500 ( reinforcing iron and rebar workers ) : -0.233
    occ_6530 ( structural iron and steel workers ) : 0.004
    occ_6730 ( highway maintenance workers ) : -0.082
    occ_6750 (  ) : -0.374
    occ_6800 ( derrick, rotary drill, and service unit operators, and roustabouts, oil, gas, and mining ) : 0.029
    occ_6840 ( mining machine operators ) : 0.016
    occ_6910 (  ) : -0.179
    occ_6920 (  ) : -0.351
    occ_7000 ( first-line supervisors of mechanics, installers, and repairers ) : 0.082
    occ_7130 ( security and fire alarm systems installers ) : 0.102
    occ_7140 ( aircraft mechanics and service technicians ) : 0.000
    occ_7150 ( automotive body and related repairers ) : 0.016
    occ_7260 ( vehicle and mobile equipment mechanics, installers, and repairers, nec ) : -0.183
    occ_7360 ( millwrights ) : 0.048
    occ_7410 ( electrical power-line installers and repairers ) : 0.087
    occ_7440 (  ) : -0.365
    occ_7510 ( coin, vending, and amusement machine servicers and repairers ) : -0.167
    occ_7540 ( locksmiths and safe repairers ) : -0.012
    occ_7550 ( manufactured building and mobile home installers ) : 0.061
    occ_7560 ( riggers ) : 0.027
    occ_7630 ( other installation, maintenance, and repair workers including wind turbine service technicians, and commercial divers, and signal and track switch repairers ) : -0.019
    occ_7700 ( first-line supervisors of production and operating workers ) : 0.061
    occ_7710 ( aircraft structure, surfaces, rigging, and systems assemblers ) : -0.034
    occ_7720 ( electrical, electronics, and electromechanical assemblers ) : -0.008
    occ_7750 ( assemblers and fabricators, nec ) : -0.055
    occ_7800 ( bakers ) : -0.136
    occ_7855 ( food processing, nec ) : -0.043
    occ_8000 ( grinding, lapping, polishing, and buffing machine tool setters, operators, and tenders, metal and plastic ) : -0.145
    occ_8100 ( molders and molding machine setters, operators, and tenders, metal and plastic ) : -0.100
    occ_8120 (  ) : -0.106
    occ_8250 ( prepress technicians and workers ) : 0.058
    occ_8255 (  ) : -0.153
    occ_8300 ( laundry and dry-cleaning workers ) : -0.028
    occ_8330 ( shoe and leather workers and repairers ) : -0.265
    occ_8350 ( tailors, dressmakers, and sewers ) : -0.141
    occ_8440 (  ) : 1.013
    occ_8540 ( woodworking machine setters, operators, and tenders, except sawing ) : -0.016
    occ_8550 ( woodworkers including model makers and patternmakers, nec ) : -0.179
    occ_8610 ( stationary engineers and boiler operators ) : 0.007
    occ_8620 ( water wastewater treatment plant and system operators ) : 0.011
    occ_8630 ( plant and system operators, nec ) : 0.144
    occ_8650 ( crushing, grinding, polishing, mixing, and blending workers ) : -0.111
    occ_8710 ( cutting workers ) : -0.012
    occ_8740 ( inspectors, testers, sorters, samplers, and weighers ) : -0.036
    occ_8760 ( medical, dental, and ophthalmic laboratory technicians ) : -0.123
    occ_8800 ( packaging and filling machine operators and tenders ) : -0.037
    occ_8810 ( painting workers and dyers ) : -0.081
    occ_8830 ( photographic process workers and processing machine operators ) : -0.055
    occ_8840 (  ) : -0.075
    occ_8930 ( paper goods machine setters, operators, and tenders ) : 0.019
    occ_8950 ( helpers--production workers ) : -0.124
    occ_8965 ( other production workers including semiconductor processors and cooling and freezing equipment operators ) : -0.104
    occ_9110 (  ) : -0.403
    occ_9120 (  ) : -0.246
    occ_9150 ( motor vehicle operators, all other ) : -0.199
    occ_9200 ( locomotive engineers and operators ) : 0.137
    occ_9240 ( railroad conductors and yardmasters ) : 0.134
    occ_9330 (  ) : 0.220
    occ_9350 ( parking lot attendants ) : -0.113
    occ_9600 ( industrial truck and tractor operators ) : -0.122
    occ_9620 ( laborers and freight, stock, and material movers, hand ) : -0.083
    occ_9640 ( packers and packagers, hand ) : -0.319
    occ_9720 ( refuse and recyclable material collectors ) : -0.083
    occ_9730 (  ) : 0.004
    occ_9840 (  ) : -0.316
    ind_0 (  ) : -0.027
    ind_280 (  ) : 0.101
    ind_370 (  ) : 0.070
    ind_380 (  ) : 0.109
    ind_390 (  ) : 0.031
    ind_470 (  ) : 0.126
    ind_570 (  ) : 0.043
    ind_580 (  ) : 0.154
    ind_680 (  ) : 0.042
    ind_690 (  ) : 0.185
    ind_770 (  ) : 0.000
    ind_1190 (  ) : -0.038
    ind_1280 (  ) : -0.004
    ind_1390 (  ) : 0.033
    ind_1480 (  ) : -0.133
    ind_1670 (  ) : -0.053
    ind_1680 (  ) : -0.090
    ind_1790 (  ) : 0.142
    ind_1870 (  ) : 0.031
    ind_1880 (  ) : -0.024
    ind_2290 (  ) : 0.014
    ind_2380 (  ) : 0.016
    ind_2390 (  ) : 0.076
    ind_2470 (  ) : -0.133
    ind_2480 (  ) : -0.023
    ind_2670 (  ) : 0.098
    ind_2680 (  ) : 0.054
    ind_2790 (  ) : -0.146
    ind_2870 (  ) : 0.007
    ind_2890 (  ) : 0.012
    ind_3090 (  ) : 0.028
    ind_3170 (  ) : 0.131
    ind_3360 (  ) : 0.043
    ind_3370 (  ) : 0.005
    ind_3380 (  ) : 0.012
    ind_3390 (  ) : 0.036
    ind_3570 (  ) : 0.048
    ind_3580 (  ) : 0.012
    ind_3670 (  ) : 0.056
    ind_3690 (  ) : -0.025
    ind_3790 (  ) : -0.005
    ind_3970 (  ) : 0.009
    ind_3990 (  ) : 0.005
    ind_4090 (  ) : 0.041
    ind_4170 (  ) : 0.102
    ind_4190 (  ) : 0.010
    ind_4380 (  ) : 0.071
    ind_4470 (  ) : 0.014
    ind_4570 (  ) : -0.010
    ind_4670 (  ) : 0.043
    ind_4770 (  ) : -0.047
    ind_4870 (  ) : -0.044
    ind_4880 (  ) : -0.078
    ind_4990 (  ) : -0.136
    ind_5070 (  ) : -0.035
    ind_5170 (  ) : -0.007
    ind_5190 (  ) : -0.078
    ind_5380 (  ) : -0.020
    ind_5590 (  ) : 0.083
    ind_5690 (  ) : -0.048
    ind_6080 (  ) : 0.145
    ind_6270 (  ) : 0.142
    ind_6480 (  ) : 0.027
    ind_6490 (  ) : 0.127
    ind_6570 (  ) : 0.053
    ind_6670 (  ) : 0.002
    ind_6680 (  ) : 0.007
    ind_6780 (  ) : 0.003
    ind_6970 (  ) : 0.072
    ind_6990 (  ) : 0.034
    ind_7080 (  ) : -0.041
    ind_7190 (  ) : 0.115
    ind_7380 (  ) : 0.034
    ind_7470 (  ) : 0.027
    ind_7570 (  ) : 0.041
    ind_7680 (  ) : -0.019
    ind_7770 (  ) : -0.058
    ind_7780 (  ) : 0.002
    ind_7860 (  ) : -0.012
    ind_7890 (  ) : -0.092
    ind_7980 (  ) : 0.009
    ind_8170 (  ) : -0.047
    ind_8190 (  ) : 0.028
    ind_8370 (  ) : -0.040
    ind_8380 (  ) : -0.029
    ind_8470 (  ) : -0.040
    ind_8570 (  ) : -0.029
    ind_8580 (  ) : -0.269
    ind_8590 (  ) : -0.059
    ind_8660 (  ) : -0.028
    ind_8670 (  ) : -0.063
    ind_8870 (  ) : 0.057
    ind_8880 (  ) : -0.058
    ind_8980 (  ) : -0.034
    ind_9090 (  ) : -0.097
    ind_9290 (  ) : -0.042
    ind_9370 (  ) : -0.010
    ind_9890 (  ) : -0.006
    educ_10 ( grades 1, 2, 3, or 4 ) : -0.058
    educ_20 ( grades 5 or 6 ) : -0.028
    educ_30 ( grades 7 or 8 ) : -0.010
    educ_50 ( grade 10 ) : -0.003
    educ_71 ( 12th grade, no diploma ) : 0.012
    educ_73 ( high school diploma or equivalent ) : -0.000
    educ_81 ( some college but no degree ) : -0.005
    educ_91 ( associate's degree, occupational/vocational program ) : 0.008
    educ_111 ( bachelor's degree ) : 0.074
    educ_124 ( professional school degree ) : 0.015
    educ_125 ( doctorate degree ) : 0.104
    occly_10 ( chief executives and legislators/public administration ) : 0.527
    occly_20 ( general and operations managers ) : 0.291
    occly_40 (  ) : 0.295
    occly_50 (  ) : 0.370
    occly_60 (  ) : 0.239
    occly_100 ( administrative services managers ) : 0.074
    occly_110 ( computer and information systems managers ) : 0.408
    occly_120 ( financial managers ) : 0.275
    occly_136 (  ) : 0.165
    occly_137 (  ) : 0.111
    occly_140 ( industrial production managers ) : 0.277
    occly_150 ( purchasing managers ) : 0.143
    occly_160 ( transportation, storage, and distribution managers ) : 0.061
    occly_205 ( farmers, ranchers, and other agricultural managers ) : -0.046
    occly_220 ( constructions managers ) : 0.259
    occly_230 ( education administrators ) : 0.236
    occly_300 ( architectural and engineering managers ) : 0.398
    occly_310 ( food service and lodging managers ) : 0.028
    occly_350 ( medical and health services managers ) : 0.160
    occly_360 ( natural science managers ) : 0.115
    occly_410 ( property, real estate, and community association managers ) : 0.134
    occly_420 ( social and community service managers ) : 0.064
    occly_425 (  ) : 0.038
    occly_430 ( managers, nec (including postmasters) ) : 0.245
    occly_500 ( agents and business managers of artists, performers, and athletes ) : 0.016
    occly_520 ( wholesale and retail buyers, except farm products ) : 0.064
    occly_630 (  ) : 0.151
    occly_710 ( management analysts ) : 0.178
    occly_726 (  ) : 0.055
    occly_740 (  ) : 0.044
    occly_800 ( accountants and auditors ) : 0.150
    occly_820 ( budget analysts ) : 0.111
    occly_840 ( financial analysts ) : 0.254
    occly_850 ( personal financial advisors ) : 0.095
    occly_910 ( credit counselors and loan officers ) : 0.053
    occly_940 ( tax preparers ) : -0.175
    occly_1006 (  ) : 0.277
    occly_1010 ( computer programmers ) : 0.190
    occly_1020 ( software developers, applications and systems software ) : 0.267
    occly_1030 (  ) : 0.070
    occly_1050 ( computer support specialists ) : 0.005
    occly_1105 (  ) : 0.003
    occly_1106 (  ) : 0.386
    occly_1107 (  ) : 0.097
    occly_1200 ( actuaries ) : 0.629
    occly_1220 ( operations research analysts ) : 0.112
    occly_1300 ( architects, except naval ) : 0.121
    occly_1320 ( aerospace engineers ) : 0.226
    occly_1330 (  ) : 0.000
    occly_1340 (  ) : 0.009
    occly_1360 ( civil engineers ) : 0.236
    occly_1400 ( computer hardware engineers ) : 0.208
    occly_1410 ( electrical and electronics engineers ) : 0.254
    occly_1420 ( environmental engineers ) : 0.202
    occly_1430 ( industrial engineers, including health and safety ) : 0.025
    occly_1440 ( marine engineers and naval architects ) : 0.343
    occly_1500 (  ) : 0.329
    occly_1510 (  ) : 0.007
    occly_1530 ( engineers, nec ) : 0.268
    occly_1550 ( engineering technicians, except drafters ) : 0.003
    occly_1560 ( surveying and mapping technicians ) : -0.017
    occly_1640 ( conservation scientists and foresters ) : 0.076
    occly_1660 (  ) : 0.033
    occly_1700 ( astronomers and physicists ) : 0.030
    occly_1710 ( atmospheric and space scientists ) : -0.124
    occly_1800 ( economists and market researchers ) : 0.059
    occly_1860 (  ) : -0.136
    occly_1930 ( geological and petroleum technicians, and nuclear technicians ) : -0.001
    occly_1965 (  ) : -0.077
    occly_2000 ( counselors ) : -0.003
    occly_2016 (  ) : -0.025
    occly_2025 (  ) : -0.033
    occly_2060 ( religious workers, nec ) : -0.097
    occly_2100 ( lawyers, and judges, magistrates, and other judicial workers ) : 0.284
    occly_2300 ( preschool and kindergarten teachers ) : -0.018
    occly_2320 ( secondary school teachers ) : 0.070
    occly_2330 ( special education teachers ) : 0.048
    occly_2340 ( other teachers and instructors ) : -0.201
    occly_2430 ( librarians ) : -0.019
    occly_2540 ( teacher assistants ) : -0.411
    occly_2550 ( education, training, and library workers, nec ) : -0.018
    occly_2600 ( artists and related workers ) : -0.004
    occly_2630 ( designers ) : -0.012
    occly_2700 ( actors, producers, and directors ) : 0.103
    occly_2720 ( athletes, coaches, umpires, and related workers ) : -0.288
    occly_2740 ( dancers and choreographers ) : -0.458
    occly_2760 ( entertainers and performers, sports and related workers, all other ) : 0.159
    occly_2800 ( announcers ) : 0.252
    occly_2825 ( public relations specialists ) : 0.138
    occly_2840 ( technical writers ) : 0.087
    occly_2850 ( writers and authors ) : 0.216
    occly_2910 ( photographers ) : -0.135
    occly_2960 (  ) : -0.148
    occly_3000 ( chiropractors ) : -0.173
    occly_3010 ( dentists ) : 0.332
    occly_3030 ( dieticians and nutritionists ) : -0.052
    occly_3040 ( optometrists ) : 0.188
    occly_3050 ( pharmacists ) : 0.565
    occly_3060 ( physicians and surgeons ) : 0.382
    occly_3110 ( physician assistants ) : 0.115
    occly_3120 ( podiatrists ) : 0.856
    occly_3150 ( occupational therapists ) : 0.168
    occly_3160 ( physical therapists ) : 0.086
    occly_3200 ( radiation therapists ) : 0.079
    occly_3210 ( recreational therapists ) : -0.013
    occly_3220 ( respiratory therapists ) : 0.120
    occly_3230 ( speech language pathologists ) : 0.032
    occly_3235 (  ) : -0.052
    occly_3250 ( veterinarians ) : 0.354
    occly_3255 (  ) : 0.084
    occly_3256 (  ) : 0.678
    occly_3257 (  ) : 0.039
    occly_3258 (  ) : 0.332
    occly_3310 ( dental hygienists ) : 0.199
    occly_3320 ( diagnostic related technologists and technicians ) : 0.166
    occly_3420 (  ) : -0.007
    occly_3500 ( licensed practical and licensed vocational nurses ) : 0.042
    occly_3510 ( medical records and health information technicians ) : -0.223
    occly_3520 ( opticians, dispensing ) : -0.011
    occly_3600 ( nursing, psychiatric, and home health aides ) : -0.259
    occly_3610 ( occupational therapy assistants and aides ) : 0.223
    occly_3630 ( massage therapists ) : -0.173
    occly_3645 (  ) : -0.207
    occly_3647 (  ) : -0.171
    occly_3649 (  ) : -0.196
    occly_3655 (  ) : -0.296
    occly_3710 ( first-line supervisors of police and detectives ) : 0.179
    occly_3720 ( first-line supervisors of fire fighting and prevention workers ) : 0.235
    occly_3750 ( fire inspectors ) : 0.026
    occly_3820 ( police officers and detectives ) : 0.165
    occly_3840 (  ) : -0.320
    occly_3850 (  ) : 0.060
    occly_3860 (  ) : 0.116
    occly_3900 ( animal control ) : 0.931
    occly_3930 ( security guards and gaming surveillance officers ) : -0.244
    occly_3940 ( crossing guards ) : -1.023
    occly_3955 (  ) : -0.506
    occly_4010 ( first-line supervisors of food preparation and serving workers ) : -0.096
    occly_4020 (  ) : -0.269
    occly_4030 ( food preparation workers ) : -0.415
    occly_4050 ( combined food preparation and serving workers, including fast food ) : -0.332
    occly_4060 ( counter attendant, cafeteria, food concession, and coffee shop ) : -0.278
    occly_4110 ( waiters and waitresses ) : -0.349
    occly_4120 ( food servers, nonrestaurant ) : -0.402
    occly_4130 ( food preparation and serving related workers, nec ) : -0.354
    occly_4140 ( dishwashers ) : -0.450
    occly_4150 ( host and hostesses, restaurant, lounge, and coffee shop ) : -0.576
    occly_4200 ( first-line supervisors of housekeeping and janitorial workers ) : -0.055
    occly_4220 ( janitors and building cleaners ) : -0.277
    occly_4230 ( maids and housekeeping cleaners ) : -0.346
    occly_4250 ( grounds maintenance workers ) : -0.216
    occly_4300 ( first-line supervisors of gaming workers ) : 0.136
    occly_4320 ( first-line supervisors of personal service workers ) : 0.009
    occly_4350 ( nonfarm animal caretakers ) : -0.067
    occly_4430 ( entertainment attendants and related workers, nec ) : -0.205
    occly_4465 (  ) : 0.022
    occly_4500 ( barbers ) : -0.022
    occly_4520 ( personal appearance workers, nec ) : -0.267
    occly_4530 ( baggage porters, bellhops, and concierges ) : -0.338
    occly_4540 ( tour and travel guides ) : -1.227
    occly_4600 ( childcare workers ) : -0.098
    occly_4610 ( personal care aides ) : -0.342
    occly_4620 ( recreation and fitness workers ) : -0.372
    occly_4650 ( personal care and service workers, all other ) : -0.299
    occly_4700 ( first-line supervisors of sales workers ) : 0.080
    occly_4710 (  ) : 0.176
    occly_4720 ( cashiers ) : -0.388
    occly_4760 ( retail salespersons ) : -0.232
    occly_4800 ( advertising sales agents ) : 0.045
    occly_4810 ( insurance sales agents ) : 0.014
    occly_4820 ( securities, commodities, and financial services sales agents ) : 0.086
    occly_4840 ( sales representatives, services, all other ) : 0.022
    occly_4850 ( sales representatives, wholesale and manufacturing ) : 0.063
    occly_4900 ( models, demonstrators, and product promoters ) : -0.287
    occly_4920 ( real estate brokers and sales agents ) : 0.020
    occly_4930 ( sales engineers ) : 0.215
    occly_4940 ( telemarketers ) : -0.443
    occly_4950 ( door-to-door sales workers, news and street vendors, and related workers ) : -0.218
    occly_4965 ( sales and related workers, all other ) : 0.003
    occly_5000 ( first-line supervisors of office and administrative support workers ) : 0.043
    occly_5010 ( switchboard operators, including answering service ) : -0.226
    occly_5100 ( bill and account collectors ) : -0.101
    occly_5110 ( billing and posting clerks ) : -0.009
    occly_5130 ( gaming cage workers ) : 0.013
    occly_5160 ( bank tellers ) : -0.270
    occly_5165 ( financial clerks, nec ) : -0.009
    occly_5240 ( customer service representatives ) : -0.149
    occly_5260 ( file clerks ) : -0.182
    occly_5300 ( hotel, motel, and resort desk clerks ) : -0.213
    occly_5310 ( interviewers, except eligibility and loan ) : -0.193
    occly_5320 ( library assistants, clerical ) : -0.608
    occly_5330 ( loan interviewers and clerks ) : 0.006
    occly_5340 ( new account clerks ) : -0.169
    occly_5350 ( correspondent clerks and order clerks ) : -0.114
    occly_5400 ( receptionists and information clerks ) : -0.187
    occly_5410 ( reservation and transportation ticket agents and travel clerks ) : -0.102
    occly_5420 ( information and record clerks, all other ) : -0.192
    occly_5510 ( couriers and messengers ) : -0.088
    occly_5560 ( postal service mail sorters, processors, and processing machine operators ) : -0.255
    occly_5610 ( shipping, receiving, and traffic clerks ) : -0.030
    occly_5620 ( stock clerks and order fillers ) : -0.349
    occly_5630 ( weighers, measurers, checkers, and samplers, recordkeeping ) : -0.117
    occly_5700 ( secretaries and administrative assistants ) : -0.071
    occly_5810 ( data entry keyers ) : -0.204
    occly_5840 ( insurance claims and policy processing clerks ) : -0.072
    occly_5850 ( mail clerks and mail machine operators, except postal service ) : -0.481
    occly_5860 ( office clerks, general ) : -0.216
    occly_6005 ( first-line supervisors of farming, fishing, and forestry workers ) : 0.038
    occly_6040 ( graders and sorters, agricultural products ) : -0.306
    occly_6050 ( agricultural workers, nec ) : -0.161
    occly_6100 ( fishing and hunting workers ) : 0.204
    occly_6200 ( first-line supervisors of construction trades and extraction workers ) : 0.216
    occly_6210 ( boilermakers ) : -0.170
    occly_6230 ( carpenters ) : -0.093
    occly_6240 ( carpet, floor, and tile installers and finishers ) : -0.069
    occly_6250 ( cement masons, concrete finishers, and terrazzo workers ) : -0.058
    occly_6260 ( construction laborers ) : -0.086
    occly_6300 ( paving, surfacing, and tamping equipment operators ) : 0.113
    occly_6320 ( construction equipment operators except paving, surfacing, and tamping equipment operators ) : 0.004
    occly_6355 ( electricians ) : 0.079
    occly_6420 ( painters, construction and maintenance ) : -0.288
    occly_6440 ( pipelayers, plumbers, pipefitters, and steamfitters ) : 0.040
    occly_6460 ( plasterers and stucco masons ) : -0.236
    occly_6515 ( roofers ) : -0.104
    occly_6520 ( sheet metal workers, metal-working ) : -0.029
    occly_6600 ( helpers, construction trades ) : -0.275
    occly_6700 ( elevator installers and repairers ) : 0.153
    occly_6710 ( fence erectors ) : -0.420
    occly_6800 ( derrick, rotary drill, and service unit operators, and roustabouts, oil, gas, and mining ) : 0.321
    occly_6820 ( earth drillers, except oil and gas ) : 0.247
    occly_6920 (  ) : 0.247
    occly_6940 ( extraction workers, nec ) : 0.083
    occly_7010 ( computer, automated teller, and office machine repairers ) : -0.058
    occly_7040 ( electric motor, power tool, and related repairers ) : 0.019
    occly_7100 ( electrical and electronics repairers, transportation equipment, and industrial and utility ) : 0.081
    occly_7130 ( security and fire alarm systems installers ) : 0.049
    occly_7140 ( aircraft mechanics and service technicians ) : 0.058
    occly_7160 ( automotive glass installers and repairers ) : -0.183
    occly_7200 ( automotive service technicians and mechanics ) : -0.025
    occly_7220 ( heavy vehicle and mobile equipment service technicians and mechanics ) : 0.070
    occly_7340 ( maintenance and repair workers, general ) : -0.014
    occly_7360 ( millwrights ) : 0.107
    occly_7420 ( telecommunications line installers and repairers ) : 0.064
    occly_7510 ( coin, vending, and amusement machine servicers and repairers ) : -0.045
    occly_7550 ( manufactured building and mobile home installers ) : 0.049
    occly_7560 ( riggers ) : 0.079
    occly_7600 (  ) : 0.100
    occly_7610 ( helpers--installation, maintenance, and repair workers ) : -0.470
    occly_7700 ( first-line supervisors of production and operating workers ) : 0.038
    occly_7710 ( aircraft structure, surfaces, rigging, and systems assemblers ) : -0.197
    occly_7720 ( electrical, electronics, and electromechanical assemblers ) : -0.153
    occly_7730 ( engine and other machine assemblers ) : -0.134
    occly_7750 ( assemblers and fabricators, nec ) : -0.167
    occly_7800 ( bakers ) : -0.226
    occly_7810 ( butchers and other meat, poultry, and fish processing workers ) : -0.134
    occly_7830 ( food and tobacco roasting, baking, and drying machine operators and tenders ) : -0.137
    occly_7840 ( food batchmakers ) : -0.313
    occly_7855 ( food processing, nec ) : -0.044
    occly_7950 ( cutting, punching, and press machine setters, operators, and tenders, metal and plastic ) : -0.194
    occly_8000 ( grinding, lapping, polishing, and buffing machine tool setters, operators, and tenders, metal and plastic ) : -0.086
    occly_8220 ( metal workers and plastic workers, nec ) : -0.103
    occly_8256 (  ) : -0.006
    occly_8300 ( laundry and dry-cleaning workers ) : -0.178
    occly_8310 ( pressers, textile, garment, and related materials ) : -0.412
    occly_8320 ( sewing machine operators ) : -0.303
    occly_8340 ( shoe machine operators and tenders ) : -0.069
    occly_8400 ( textile bleaching and dyeing, and cutting machine setters, operators, and tenders ) : -0.142
    occly_8410 ( textile knitting and weaving machine setters, operators, and tenders ) : -0.358
    occly_8440 (  ) : 0.097
    occly_8460 ( textile, apparel, and furnishings workers, nec ) : -0.130
    occly_8500 ( cabinetmakers and bench carpenters ) : -0.028
    occly_8510 ( furniture finishers ) : -0.266
    occly_8530 ( sawing machine setters, operators, and tenders, wood ) : -0.016
    occly_8600 ( power plant operators, distributors, and dispatchers ) : 0.322
    occly_8630 ( plant and system operators, nec ) : 0.108
    occly_8710 ( cutting workers ) : -0.195
    occly_8740 ( inspectors, testers, sorters, samplers, and weighers ) : -0.029
    occly_8800 ( packaging and filling machine operators and tenders ) : -0.153
    occly_8830 ( photographic process workers and processing machine operators ) : -0.027
    occly_8850 ( adhesive bonding machine operators and tenders ) : -0.095
    occly_8910 ( etchers, engravers, and lithographers ) : -0.523
    occly_8920 ( molders, shapers, and casters, except metal and plastic ) : 0.076
    occly_8965 ( other production workers including semiconductor processors and cooling and freezing equipment operators ) : -0.093
    occly_9030 ( aircraft pilots and flight engineers ) : 0.589
    occly_9040 ( air traffic controllers and airfield operations specialists ) : 0.394
    occly_9110 (  ) : -0.041
    occly_9130 ( driver/sales workers and truck drivers ) : -0.049
    occly_9140 ( taxi drivers and chauffeurs ) : -0.316
    occly_9200 ( locomotive engineers and operators ) : 0.044
    occly_9310 ( ship and boat captains and operators ) : 0.339
    occly_9330 (  ) : 0.000
    occly_9350 ( parking lot attendants ) : -0.324
    occly_9360 ( automotive and watercraft service attendants ) : -0.300
    occly_9415 (  ) : -0.354
    occly_9510 ( crane and tower operators ) : 0.058
    occly_9600 ( industrial truck and tractor operators ) : -0.042
    occly_9610 ( cleaners of vehicles and equipment ) : -0.375
    occly_9620 ( laborers and freight, stock, and material movers, hand ) : -0.246
    occly_9630 ( machine feeders and offbearers ) : -0.149
    occly_9640 ( packers and packagers, hand ) : -0.107
    occly_9650 ( pumping station operators ) : 0.020
    occly_9730 (  ) : 0.231
    occly_9750 ( material moving workers, nec ) : -0.199
    occly_9840 (  ) : 0.207
    indly_170 (  ) : -0.037
    indly_280 ( other primary metal industries ) : 0.071
    indly_290 ( screw machine products ) : -0.026
    indly_370 ( cycles and miscellaneous transportation equipment ) : 0.173
    indly_380 ( photographic equipment and supplies ) : 0.254
    indly_390 ( toys, amusement, and sporting goods ) : 0.327
    indly_480 (  ) : 0.051
    indly_490 (  ) : 0.419
    indly_570 (  ) : 0.180
    indly_590 ( mobile home dealers ) : 0.280
    indly_670 ( vending machine operators ) : 0.074
    indly_1070 (  ) : 0.014
    indly_1090 (  ) : 0.029
    indly_1170 (  ) : 0.116
    indly_1190 (  ) : -0.013
    indly_1270 (  ) : -0.031
    indly_1290 (  ) : -0.049
    indly_1370 (  ) : -0.001
    indly_1480 (  ) : -0.077
    indly_1670 (  ) : -0.608
    indly_1680 (  ) : -0.119
    indly_1690 (  ) : 0.404
    indly_1790 (  ) : 0.001
    indly_1870 (  ) : 0.161
    indly_1890 (  ) : 0.086
    indly_2070 (  ) : 0.302
    indly_2090 (  ) : 0.248
    indly_2190 (  ) : 0.262
    indly_2280 (  ) : 0.128
    indly_2290 (  ) : 0.096
    indly_2470 (  ) : 0.066
    indly_2490 (  ) : 0.067
    indly_2590 (  ) : -0.114
    indly_2780 (  ) : -0.318
    indly_2790 (  ) : 0.158
    indly_2880 (  ) : 0.053
    indly_2970 (  ) : 0.067
    indly_3080 (  ) : 0.031
    indly_3190 (  ) : 0.053
    indly_3360 (  ) : 0.073
    indly_3380 (  ) : 0.135
    indly_3390 (  ) : 0.099
    indly_3490 (  ) : 0.064
    indly_3570 (  ) : 0.050
    indly_3580 (  ) : 0.066
    indly_3590 (  ) : 0.077
    indly_3680 (  ) : 0.041
    indly_3770 (  ) : -0.000
    indly_3870 (  ) : -0.124
    indly_3890 (  ) : -0.012
    indly_3970 (  ) : 0.101
    indly_3980 (  ) : -0.052
    indly_4070 (  ) : -0.006
    indly_4080 (  ) : 0.039
    indly_4170 (  ) : 0.005
    indly_4180 (  ) : 0.095
    indly_4270 (  ) : 0.068
    indly_4370 (  ) : -0.001
    indly_4380 (  ) : 0.143
    indly_4390 (  ) : 0.025
    indly_4470 (  ) : 0.004
    indly_4480 (  ) : 0.036
    indly_4490 (  ) : 0.156
    indly_4560 (  ) : 0.023
    indly_4585 (  ) : 0.085
    indly_4590 (  ) : -0.260
    indly_4670 (  ) : 0.132
    indly_4690 (  ) : -0.076
    indly_4770 (  ) : 0.053
    indly_4780 (  ) : -0.045
    indly_4790 (  ) : 0.116
    indly_4880 (  ) : -0.151
    indly_4970 (  ) : -0.153
    indly_4980 (  ) : -0.132
    indly_5070 (  ) : -0.016
    indly_5090 (  ) : -0.051
    indly_5170 (  ) : -0.164
    indly_5180 (  ) : -0.248
    indly_5270 (  ) : -0.285
    indly_5280 (  ) : -0.133
    indly_5290 (  ) : -0.138
    indly_5370 (  ) : -0.427
    indly_5380 (  ) : -0.232
    indly_5390 (  ) : -0.157
    indly_5470 (  ) : -0.269
    indly_5490 (  ) : -0.356
    indly_5570 (  ) : -0.266
    indly_5580 (  ) : -0.074
    indly_5590 (  ) : -0.021
    indly_5591 (  ) : 0.029
    indly_5670 (  ) : -0.229
    indly_5690 (  ) : -0.090
    indly_6070 (  ) : 0.011
    indly_6090 (  ) : 0.142
    indly_6170 (  ) : 0.119
    indly_6180 (  ) : -0.058
    indly_6190 (  ) : -0.211
    indly_6280 (  ) : 0.158
    indly_6290 (  ) : 0.029
    indly_6380 (  ) : -0.039
    indly_6470 (  ) : -0.171
    indly_6672 (  ) : 0.297
    indly_6680 (  ) : 0.134
    indly_6690 (  ) : 0.051
    indly_6695 (  ) : 0.067
    indly_6770 (  ) : -0.082
    indly_6780 (  ) : 0.011
    indly_6970 (  ) : 0.076
    indly_6990 (  ) : 0.061
    indly_7070 (  ) : 0.017
    indly_7170 (  ) : -0.217
    indly_7190 (  ) : 0.071
    indly_7270 (  ) : 0.140
    indly_7290 (  ) : 0.121
    indly_7370 (  ) : 0.037
    indly_7380 (  ) : 0.130
    indly_7390 (  ) : 0.116
    indly_7460 (  ) : 0.080
    indly_7470 (  ) : 0.116
    indly_7490 (  ) : -0.034
    indly_7570 (  ) : 0.011
    indly_7580 (  ) : -0.409
    indly_7590 (  ) : -0.062
    indly_7680 (  ) : -0.088
    indly_7690 (  ) : -0.093
    indly_7860 (  ) : -0.105
    indly_7870 (  ) : -0.123
    indly_7880 (  ) : -0.083
    indly_7970 (  ) : 0.058
    indly_7980 (  ) : 0.009
    indly_8170 (  ) : -0.112
    indly_8180 (  ) : 0.029
    indly_8270 (  ) : -0.029
    indly_8370 (  ) : -0.111
    indly_8380 (  ) : -0.065
    indly_8390 (  ) : -0.371
    indly_8470 (  ) : -0.206
    indly_8560 (  ) : -0.108
    indly_8570 (  ) : -0.099
    indly_8660 (  ) : -0.068
    indly_8670 (  ) : -0.160
    indly_8680 (  ) : -0.129
    indly_8690 (  ) : -0.081
    indly_8770 (  ) : -0.015
    indly_8780 (  ) : -0.139
    indly_8790 (  ) : -0.010
    indly_8870 (  ) : 0.053
    indly_8880 (  ) : -0.032
    indly_8890 (  ) : -1.339
    indly_8980 (  ) : -0.066
    indly_9070 (  ) : -0.035
    indly_9090 (  ) : -0.002
    indly_9160 (  ) : -0.248
    indly_9170 (  ) : -0.077
    indly_9290 (  ) : -0.017
    indly_9370 (  ) : -0.015
    indly_9380 (  ) : -0.014
    indly_9470 (  ) : 0.062
    indly_9480 (  ) : -0.031
    indly_9590 (  ) : 0.038
    indly_9890 (  ) : 0.000
    classwly_13 ( self-employed, not incorporated ) : -1.111
    classwly_14 ( self-employed, incorporated ) : 0.220
    classwly_25 ( federal government employee ) : 0.128
    classwly_27 ( state government employee ) : -0.093
    classwly_28 ( local government employee ) : -0.021
    pension_at_w_ly_2 ( pension plan at work, but not included ) : -0.033
    pension_at_w_ly_3 ( included in pension plan at work ) : 0.309
    firmsize_ly_1 ( under 10 ) : -0.213
    firmsize_ly_4 ( 10 to 49 ) : -0.075
    firmsize_ly_6 ( 50 to 99 ) : -0.013
    firmsize_ly_8 ( 500 to 999 ) : 0.021
    firmsize_ly_9 ( 1000+ ) : 0.035
    actnlfly_0 ( niu ) : 0.387
    actnlfly_10 ( ill or disabled ) : -0.010
    actnlfly_20 ( taking care of home/family ) : -0.342
    actnlfly_30 ( going to school ) : -0.484
    actnlfly_40 ( retired ) : -0.228
    actnlfly_50 ( other ) : 0.130
    spmmort_1 ( owners with a mortgage ) : 0.067
    statefip_2 ( alaska ) : 0.137
    statefip_5 ( arkansas ) : -0.020
    statefip_6 ( california ) : 0.058
    statefip_9 ( connecticut ) : 0.079
    statefip_11 ( district of columbia ) : 0.035
    statefip_15 ( hawaii ) : 0.079
    statefip_16 ( idaho ) : -0.044
    statefip_20 ( kansas ) : -0.072
    statefip_21 ( kentucky ) : -0.012
    statefip_23 ( maine ) : -0.074
    statefip_25 ( massachusetts ) : 0.051
    statefip_29 ( missouri ) : -0.063
    statefip_30 ( montana ) : -0.020
    statefip_31 ( nebraska ) : 0.006
    statefip_32 ( nevada ) : 0.039
    statefip_33 ( new hampshire ) : 0.031
    statefip_35 ( new mexico ) : -0.033
    statefip_37 ( north carolina ) : -0.010
    statefip_38 ( north dakota ) : 0.002
    statefip_39 ( ohio ) : -0.000
    statefip_40 ( oklahoma ) : -0.019
    statefip_41 ( oregon ) : -0.007
    statefip_42 ( pennsylvania ) : -0.007
    statefip_44 ( rhode island ) : 0.031
    statefip_45 ( south carolina ) : -0.029
    statefip_46 ( south dakota ) : -0.036
    statefip_47 ( tennessee ) : -0.025
    statefip_54 ( west virginia ) : -0.047
    statefip_56 ( wyoming ) : 0.063
    state_ly_2 ( alaska ) : 0.003
    state_ly_6 ( california ) : -0.027
    state_ly_10 ( delaware ) : -0.104
    state_ly_12 ( florida ) : 0.015
    state_ly_16 ( idaho ) : -0.033
    state_ly_23 ( maine ) : -0.068
    state_ly_24 ( maryland ) : 0.024
    state_ly_25 ( massachusetts ) : 0.134
    state_ly_34 ( new jersey ) : -0.036
    state_ly_36 ( new york ) : -0.004
    state_ly_37 ( north carolina ) : 0.038
    state_ly_40 ( oklahoma ) : -0.043
    state_ly_49 ( utah ) : -0.060
    state_ly_51 ( virginia ) : 0.052
    state_ly_91 ( abroad ) : -0.097
    whymove_1 ( change in marital status ) : -0.033
    whymove_2 ( to establish own household ) : -0.071
    whymove_3 ( other family reason ) : 0.009
    whymove_4 ( new job or job transfer ) : -0.003
    whymove_5 ( to look for work or lost job ) : -0.259
    whymove_10 ( wanted new or better housing ) : 0.015
    whymove_11 ( wanted better neighborhood ) : 0.053
    whymove_12 ( for cheaper housing ) : -0.035
    whymove_14 ( attend/leave college ) : -0.319
    whymove_18 ( natural disaster ) : 0.163
    whymove_19 ( foreclosure or eviction ) : 0.034
    mig_stat_ly_4 ( moved within state, different county ) : 0.009
    mig_stat_ly_5 ( moved between states ) : -0.000
    mig_stat_ly_6 ( abroad ) : -0.006
    health_1 ( excellent ) : 0.026
    health_3 ( good ) : -0.054
    health_4 ( fair ) : -0.129
    health_5 ( poor ) : -0.175
    vet1_1 ( september 2001 or later ) : -0.000
    vet1_2 ( august 1990 to august 2001 ) : 0.005
    vet1_3 ( may 1975 to july 1990 ) : 0.003
    vet1_4 ( vietnam era (august 1964 to april 1975) ) : -0.069
    vet2_1 ( september 2001 or later ) : -0.007
    csvisleg_1 ( no ) : 0.015
    csvisleg_2 ( yes ) : 0.003
    csvisleg_98 ( blank ) : -0.015
    paidhour_1 ( no ) : 0.109
    paidhour_2 ( yes ) : -0.030
    union_1 ( no union coverage ) : -0.013
    union_2 ( member of labor union ) : 0.074
    bpl_1.0 ( usa, canada & dependent ) : 0.003
    bpl_8.0 ( developed asia ) : 0.023
    fbpl_5.0 ( central and caribean ) : -0.014
    fbpl_7.0 ( europe ) : 0.006
    fbpl_9.0 ( east asia ) : -0.006

### grid: 
    grid: [1.45096612e-03 1.35317586e-03 1.26197633e-03 1.17692335e-03
    1.09760266e-03 1.02362791e-03 9.54638815e-04 8.90299354e-04
    8.30296157e-04 7.74336975e-04 7.22149255e-04 6.73478812e-04
    6.28088594e-04 5.85757525e-04 5.46279428e-04 5.09462023e-04
    4.75125988e-04 4.43104086e-04 4.13240354e-04 3.85389337e-04
    3.59415386e-04 3.35191992e-04 3.12601173e-04 2.91532900e-04
    2.71884559e-04 2.53560449e-04 2.36471324e-04 2.20533948e-04
    2.05670698e-04 1.91809181e-04 1.78881884e-04 1.66825844e-04
    1.55582341e-04 1.45096612e-04 1.35317586e-04 1.26197633e-04
    1.17692335e-04 1.09760266e-04 1.02362791e-04 9.54638815e-05
    8.90299354e-05 8.30296157e-05 7.74336975e-05 7.22149255e-05
    6.73478812e-05 6.28088594e-05 5.85757525e-05 5.46279428e-05
    5.09462023e-05 4.75125988e-05 4.43104086e-05 4.13240354e-05
    3.85389337e-05 3.59415386e-05 3.35191992e-05 3.12601173e-05
    2.91532900e-05 2.71884559e-05 2.53560449e-05 2.36471324e-05
    2.20533948e-05 2.05670698e-05 1.91809181e-05 1.78881884e-05
    1.66825844e-05 1.55582341e-05 1.45096612e-05 1.35317586e-05
    1.26197633e-05 1.17692335e-05 1.09760266e-05 1.02362791e-05
    9.54638815e-06 8.90299354e-06 8.30296157e-06 7.74336975e-06
    7.22149255e-06 6.73478812e-06 6.28088594e-06 5.85757525e-06
    5.46279428e-06 5.09462023e-06 4.75125988e-06 4.43104086e-06
    4.13240354e-06 3.85389337e-06 3.59415386e-06 3.35191992e-06
    3.12601173e-06 2.91532900e-06 2.71884559e-06 2.53560449e-06
    2.36471324e-06 2.20533948e-06 2.05670698e-06 1.91809181e-06
    1.78881884e-06 1.66825844e-06 1.55582341e-06 1.45096612e-06]
















































































## LassoCV5 with manual gridpoints (100)

### Code


### Results

Time to run: 177.47615122795105 to run
\lambda:  (9.546388151822239e-06,) log10: [-5.02016091] ln: [-11.55934768]
Coefficients: 
 [ 0.00400128 -0.         -0.12686468 ... -0.00622842  0.
 -0.        ]
Mean squared error: 0.29
Coefficient of determination: 0.57
age ( age ) : 0.004
educ_cat_1.0 (  ) : -0.127
educ_cat_2.0 (  ) : -0.033
educ_cat_4.0 (  ) : 0.066
educ_cat_5.0 (  ) : 0.287
race_cat_1.0 (  ) : 0.042
race_cat_2.0 (  ) : -0.013
male_0.0 (  ) : -0.274
male_1.0 (  ) : 0.000
hhtenure_1 ( owned or being bought ) : 0.051
hhtenure_3 ( occupied without payment of cash rent ) : -0.024
region_11 ( new england division ) : 0.027
region_21 ( east north central division ) : -0.009
region_32 ( east south central division ) : -0.036
region_42 ( pacific division ) : 0.027
metarea_120 ( albany, ga ) : -0.112
metarea_200 ( albuquerque, nm ) : -0.004
metarea_280 ( altoona, pa msa ) : -0.038
metarea_320 ( amarillo, tx ) : -0.016
metarea_440 ( ann arbor, mi ) : 0.090
metarea_462 ( oshkosh-neenah, wi ) : -0.177
metarea_480 ( asheville, nc ) : -0.089
metarea_521 ( atlanta-sandy springs-marietta, ga ) : 0.009
metarea_641 ( austin-round rock, tx ) : 0.050
metarea_680 ( bakersfield, ca ) : -0.129
metarea_721 ( baltimore-towson, md ) : 0.068
metarea_730 ( bangor, me ) : -0.038
metarea_741 ( barnstable town, ma ) : -0.057
metarea_760 ( baton rouge, la ) : 0.026
metarea_841 ( beaumont-port arthur, tx ) : 0.073
metarea_860 ( bellingham, wa ) : 0.020
metarea_880 ( billings, mt ) : -0.033
metarea_920 ( biloxi-gulfport, ms ) : -0.025
metarea_960 ( binghamton, ny ) : -0.017
metarea_1081 ( boise city-nampa, id ) : -0.075
metarea_1124 ( boston-cambridge-quincy, ma-nh ) : 0.017
metarea_1280 ( buffalo-niagara falls, ny ) : -0.043
metarea_1360 ( cedar rapids, ia ) : -0.041
metarea_1440 ( charleston-north charleston, sc ) : -0.024
metarea_1480 ( charleston, wv ) : -0.081
metarea_1605 ( chicago-naperville-joliet, il-in-wi ) : 0.057
metarea_1700 ( coeur d'alene, id ) : -0.081
metarea_1720 ( colorado springs, co ) : -0.011
metarea_1800 ( columbus, ga/al ) : -0.133
metarea_1922 ( dallas-fort worth-arlington, tx ) : 0.023
metarea_1930 ( danbury, ct ) : 0.122
metarea_2001 ( springfield, oh ) : -0.029
metarea_2002 ( dayton, oh ) : -0.140
metarea_2030 ( decatur, al ) : -0.030
metarea_2082 ( boulder, co ) : 0.005
metarea_2083 ( denver-aurora, co ) : 0.033
metarea_2241 ( duluth, mn/wi ) : -0.129
metarea_2300 ( el centro, ca ) : -0.130
metarea_2310 ( el paso, tx ) : -0.080
metarea_2360 ( erie, pa ) : -0.136
metarea_2400 ( eugene-springfield, or ) : -0.026
metarea_2581 ( fayetteville-springdale-rogers, ar-mo ) : 0.047
metarea_2640 ( flint, mi ) : -0.127
metarea_2670 ( fort collins-loveland, co ) : -0.048
metarea_2760 ( fort wayne, in ) : -0.010
metarea_2840 ( fresno, ca ) : -0.079
metarea_2900 ( gainesville, fl ) : -0.075
metarea_3060 ( greeley, co ) : -0.034
metarea_3162 ( greenville, sc ) : -0.026
metarea_3181 ( hagerstown-martinsburg, md-wv ) : 0.024
metarea_3362 ( houston-baytown-sugar land, tx ) : 0.079
metarea_3440 ( huntsville,al ) : -0.055
metarea_3480 ( indianapolis, in ) : 0.028
metarea_3520 ( jackson, mi ) : -0.061
metarea_3560 ( jackson, ms ) : -0.027
metarea_3590 ( jacksonville,fl ) : 0.007
metarea_3600 ( jacksonville, nc ) : -0.025
metarea_3621 ( janvesville, wi ) : -0.015
metarea_3661 ( johnson city, tn ) : -0.058
metarea_3720 ( kalamazoo-portage, mi ) : -0.008
metarea_3760 ( kansas city, mo/ks ) : 0.059
metarea_3830 ( kingston, ny ) : 0.026
metarea_4000 ( lancaster, pa ) : 0.079
metarea_4040 ( lansing-east lansing, mi ) : -0.027
metarea_4080 ( laredo, tx ) : -0.007
metarea_4100 ( las cruces, nm ) : -0.048
metarea_4130 ( las vegas-paradise, nv ) : 0.019
metarea_4150 ( lawrence, ks ) : 0.043
metarea_4200 ( lawton, ok ) : -0.031
metarea_4280 ( lexington-fayette, ky ) : -0.046
metarea_4483 ( los angeles-long beach-santa ana, ca ) : 0.017
metarea_4600 ( lubbock, tx ) : -0.083
metarea_4640 ( lynchburg, va ) : -0.026
metarea_4681 ( macon, ga ) : -0.067
metarea_4720 ( madison, wi ) : 0.011
metarea_4940 ( merced, ca ) : -0.043
metarea_5001 ( miami-fort lauderdale-miami beach, fl ) : 0.040
metarea_5081 ( milwaukee-waukesha-west allis, wi ) : -0.004
metarea_5121 ( minneapolis-st. paul-bloomington, mn/wi ) : 0.041
metarea_5160 ( mobile, al ) : 0.001
metarea_5170 ( modesto, ca ) : -0.000
metarea_5200 ( monroe, la ) : -0.010
metarea_5220 ( monroe, mi ) : 0.106
metarea_5321 ( muskegon-norton shores, mi ) : -0.066
metarea_5331 ( myrtle beach-conway-north myrtle beach, sc ) : -0.078
metarea_5481 ( new haven, ct ) : 0.013
metarea_5606 ( new york-northern new jersey-long island, ny-nj-pa ) : 0.196
metarea_5790 ( ocala, fl ) : -0.091
metarea_5801 ( midland, tx ) : 0.108
metarea_5840 ( ocean city, nj ) : -0.331
metarea_5910 ( olympia, wa ) : -0.087
metarea_5960 ( orlando, fl ) : -0.057
metarea_6081 ( pensacola-ferry pass-brent, fl ) : -0.096
metarea_6161 ( philadelphia-camden-wilmington, pa/nj/de ) : 0.056
metarea_6201 ( phoenix-mesa-scottsdale, az ) : 0.013
metarea_6280 ( pittsburg, pa ) : -0.012
metarea_6401 ( portland-south portland, me ) : 0.045
metarea_6520 ( provo-orem, ut ) : -0.022
metarea_6680 ( reading, pa ) : -0.090
metarea_6980 ( st. cloud, mn ) : -0.053
metarea_7080 ( salem, or ) : -0.008
metarea_7130 ( salisbury, md ) : -0.083
metarea_7321 ( san diego-carlsbad-san marcos, ca ) : 0.039
metarea_7364 ( napa, ca ) : 0.052
metarea_7365 ( san francisco-oakland-fremont, ca ) : 0.123
metarea_7401 ( san jose-sunnyvale-santa clara, ca ) : 0.154
metarea_7461 ( san luis obispo-paso robles, ca ) : 0.081
metarea_7471 ( santa barbara-santa maria-goleta, ca ) : 0.068
metarea_7481 ( santa cruz-watsonville, ca ) : 0.059
metarea_7511 ( sarasota-bradenton-venice, fl ) : 0.011
metarea_7520 ( savannah, ga ) : 0.036
metarea_7560 ( scranton-wilkes-barre, pa ) : -0.001
metarea_7601 ( seattle-tacoma-bellevue, wa ) : 0.023
metarea_7681 ( shreveport-bossier city, la ) : 0.007
metarea_7760 ( sioux falls, sd ) : -0.024
metarea_7920 ( springfield, mo ) : -0.027
metarea_8160 ( syracuse, ny ) : -0.016
metarea_8240 ( tallahassee, fl ) : -0.018
metarea_8440 ( topeka, ks ) : 0.042
metarea_8600 ( tuscaloosa, al ) : -0.058
metarea_8700 ( valdosta, ga ) : -0.010
metarea_8731 ( oxnard-thousand oaks-ventura, ca ) : 0.068
metarea_8740 ( vero beach, fl ) : -0.093
metarea_8750 ( victoria, tx ) : -0.016
metarea_8760 ( vineland-milville-bridgetown, nj ) : 0.074
metarea_8781 ( visalia-porterville, ca ) : -0.027
metarea_8840 ( washington, dc/md/va ) : 0.156
metarea_8920 ( waterloo-cedar falls, ia ) : -0.045
metarea_8940 ( wausau, wi ) : -0.045
metarea_9040 ( wichita, ks ) : -0.035
metarea_9321 ( youngstown-warren-boardman, oh ) : -0.097
metarea_9997 ( other metropolitan areas, unidentified ) : -0.047
metarea_9998 ( niu, household not in a metropolitan area ) : -0.066
metarea_9999 ( missing data ) : -0.020
unitsstr_1 ( mobile home or trailer ) : -0.028
unitsstr_7 ( 5-9 family building ) : -0.007
unitsstr_11 ( one unit, unspecified type ) : 0.026
nfams_1 ( 1 family or n/a ) : 0.007
nfams_4 ( 4 ) : -0.004
nfams_6 ( 6 ) : -0.082
nfams_8 ( 8 ) : 0.152
ncouples_2 ( 2 ) : -0.058
nmothers_2 ( 2 ) : -0.022
nmothers_3 ( 3 ) : -0.089
nfathers_1 ( 1 ) : 0.001
nfathers_2 ( 2 ) : -0.021
nfathers_3 ( 3 ) : -0.051
marst_1 ( married, spouse present ) : 0.119
marst_3 ( separated ) : -0.025
marst_5 ( widowed ) : -0.043
marst_6 ( never married/single ) : -0.073
famsize_3 ( 3 family members present ) : 0.000
famsize_6 ( 6 family members present ) : -0.009
famsize_7 ( 7 family members present ) : -0.014
famsize_8 ( 8 family members present ) : -0.031
famsize_14 ( 14 family members present ) : -0.084
famsize_15 ( 15 family members present ) : -0.293
ftype_2 ( nonfamily householder ) : 0.044
ftype_3 ( related subfamily ) : -0.061
ftype_4 ( unrelated subfamily ) : -0.024
famkind_1 ( husband/wife family ) : -0.053
famkind_3 ( female reference person ) : 0.128
yrimmig_0 ( niu ) : 0.002
yrimmig_1985 ( 1984-1985 ) : 0.009
yrimmig_2001 ( 2000-2001 (2001 cps: 1998-2001) ) : -0.015
yrimmig_2003 ( 2002-2003 (2003 cps: 2000-2003) ) : -0.018
yrimmig_2005 ( 2004-2005 (2005 cps: 2002-2005) ) : -0.043
yrimmig_2007 ( 2004-2007 ) : -0.025
yrimmig_2009 ( 2006-2009 ) : -0.027
yrimmig_2012 ( 2010-2012 (2014 cps: 2010-2011) ) : -0.070
citizen_1 ( born in u.s ) : 0.000
citizen_3 ( born abroad of american parents ) : 0.015
citizen_5 ( not a citizen ) : -0.056
hispan_0 ( not hispanic ) : 0.010
hispan_410 ( central/south american ) : -0.012
occ_0 ( Missing data? ) : -0.276
occ_10 ( chief executives and legislators/public administration ) : 0.077
occ_20 ( general and operations managers ) : 0.082
occ_40 (  ) : 0.001
occ_135 (  ) : 0.002
occ_136 (  ) : 0.084
occ_150 ( purchasing managers ) : 0.038
occ_220 ( constructions managers ) : 0.092
occ_325 (  ) : 0.173
occ_340 (  ) : -0.013
occ_350 ( medical and health services managers ) : 0.122
occ_420 ( social and community service managers ) : 0.025
occ_500 ( agents and business managers of artists, performers, and athletes ) : 0.357
occ_565 (  ) : 0.107
occ_600 ( cost estimators ) : 0.262
occ_630 (  ) : 0.005
occ_640 (  ) : 0.033
occ_650 (  ) : 0.059
occ_725 (  ) : 0.079
occ_735 (  ) : 0.186
occ_810 ( appraisers and assessors of real estate ) : 0.080
occ_830 ( credit analysts ) : 0.076
occ_850 ( personal financial advisors ) : 0.096
occ_860 ( insurance underwriters ) : 0.027
occ_940 ( tax preparers ) : -0.154
occ_950 ( financial specialists, nec ) : 0.044
occ_1005 (  ) : 0.067
occ_1007 (  ) : 0.006
occ_1010 ( computer programmers ) : 0.007
occ_1020 ( software developers, applications and systems software ) : 0.066
occ_1060 ( database administrators ) : 0.217
occ_1105 (  ) : 0.109
occ_1240 ( mathematical science occupations, nec ) : 0.055
occ_1320 ( aerospace engineers ) : 0.105
occ_1330 (  ) : 0.118
occ_1350 ( chemical engineers ) : 0.189
occ_1430 ( industrial engineers, including health and safety ) : 0.078
occ_1460 ( mechanical engineers ) : 0.170
occ_1510 (  ) : 0.004
occ_1520 ( petroleum, mining and geological engineers, including mining safety engineers ) : 0.321
occ_1530 ( engineers, nec ) : 0.018
occ_1540 ( drafters ) : 0.021
occ_1560 ( surveying and mapping technicians ) : -0.006
occ_1660 (  ) : 0.247
occ_1700 ( astronomers and physicists ) : 0.112
occ_1720 ( chemists and materials scientists ) : 0.092
occ_1800 ( economists and market researchers ) : 0.260
occ_1820 ( psychologists ) : 0.060
occ_1860 (  ) : -0.013
occ_1910 ( biological technicians ) : -0.119
occ_1930 ( geological and petroleum technicians, and nuclear technicians ) : -0.192
occ_1965 (  ) : -0.017
occ_2000 ( counselors ) : -0.006
occ_2060 ( religious workers, nec ) : -0.418
occ_2100 ( lawyers, and judges, magistrates, and other judicial workers ) : 0.068
occ_2160 (  ) : -0.021
occ_2200 ( postsecondary teachers ) : 0.049
occ_2300 ( preschool and kindergarten teachers ) : -0.020
occ_2430 ( librarians ) : -0.027
occ_2440 ( library technicians ) : -0.320
occ_2540 ( teacher assistants ) : -0.049
occ_2710 (  ) : 0.107
occ_2720 ( athletes, coaches, umpires, and related workers ) : 0.063
occ_2750 ( musicians, singers, and related workers ) : -0.260
occ_2760 ( entertainers and performers, sports and related workers, all other ) : 0.061
occ_2825 ( public relations specialists ) : 0.095
occ_2830 (  ) : 0.022
occ_2960 (  ) : -0.738
occ_3000 ( chiropractors ) : -0.010
occ_3010 ( dentists ) : 0.213
occ_3060 ( physicians and surgeons ) : 0.193
occ_3110 ( physician assistants ) : 0.096
occ_3160 ( physical therapists ) : 0.045
occ_3200 ( radiation therapists ) : 0.120
occ_3210 ( recreational therapists ) : -0.005
occ_3230 ( speech language pathologists ) : 0.107
occ_3235 (  ) : -0.990
occ_3255 (  ) : 0.151
occ_3257 (  ) : 0.149
occ_3420 (  ) : -0.091
occ_3600 ( nursing, psychiatric, and home health aides ) : -0.012
occ_3620 ( physical therapist assistants and aides ) : 0.045
occ_3645 (  ) : -0.036
occ_3646 (  ) : -0.004
occ_3700 ( first-line supervisors of correctional officers ) : 0.012
occ_3740 ( firefighters ) : 0.063
occ_3800 ( sheriffs, bailiffs, correctional officers, and jailers ) : -0.032
occ_3850 (  ) : 0.061
occ_3860 (  ) : 0.238
occ_3900 ( animal control ) : -0.172
occ_3940 ( crossing guards ) : -0.032
occ_4000 ( chefs and cooks ) : -0.042
occ_4020 (  ) : -0.077
occ_4040 ( bartenders ) : -0.216
occ_4050 ( combined food preparation and serving workers, including fast food ) : -0.179
occ_4060 ( counter attendant, cafeteria, food concession, and coffee shop ) : -0.263
occ_4120 ( food servers, nonrestaurant ) : -0.088
occ_4140 ( dishwashers ) : -0.214
occ_4220 ( janitors and building cleaners ) : -0.034
occ_4230 ( maids and housekeeping cleaners ) : -0.062
occ_4250 ( grounds maintenance workers ) : -0.037
occ_4350 ( nonfarm animal caretakers ) : -0.124
occ_4430 ( entertainment attendants and related workers, nec ) : -0.189
occ_4460 ( funeral service workers and embalmers ) : -0.221
occ_4530 ( baggage porters, bellhops, and concierges ) : -0.037
occ_4540 ( tour and travel guides ) : 0.186
occ_4600 ( childcare workers ) : -0.245
occ_4610 ( personal care aides ) : -0.055
occ_4640 ( residential advisors ) : -0.070
occ_4700 ( first-line supervisors of sales workers ) : 0.011
occ_4720 ( cashiers ) : -0.035
occ_4760 ( retail salespersons ) : -0.012
occ_4800 ( advertising sales agents ) : 0.003
occ_4840 ( sales representatives, services, all other ) : 0.006
occ_4850 ( sales representatives, wholesale and manufacturing ) : 0.111
occ_4900 ( models, demonstrators, and product promoters ) : -0.152
occ_4920 ( real estate brokers and sales agents ) : 0.169
occ_4950 ( door-to-door sales workers, news and street vendors, and related workers ) : -0.211
occ_5000 ( first-line supervisors of office and administrative support workers ) : 0.026
occ_5010 ( switchboard operators, including answering service ) : -0.137
occ_5110 ( billing and posting clerks ) : -0.088
occ_5120 ( bookkeeping, accounting, and auditing clerks ) : -0.086
occ_5160 ( bank tellers ) : -0.048
occ_5220 ( court, municipal, and license clerks ) : -0.107
occ_5310 ( interviewers, except eligibility and loan ) : -0.048
occ_5360 ( human resources assistants, except payroll and timekeeping ) : -0.033
occ_5400 ( receptionists and information clerks ) : -0.059
occ_5530 ( meter readers, utilities ) : -0.074
occ_5540 ( postal service clerks ) : -0.029
occ_5610 ( shipping, receiving, and traffic clerks ) : -0.175
occ_5820 ( word processors and typists ) : -0.187
occ_5840 ( insurance claims and policy processing clerks ) : -0.052
occ_5920 ( statistical assistants ) : -0.042
occ_5940 ( office and administrative support workers, nec ) : -0.057
occ_6220 ( brickmasons, blockmasons, and stonemasons ) : -0.041
occ_6260 ( construction laborers ) : -0.074
occ_6320 ( construction equipment operators except paving, surfacing, and tamping equipment operators ) : 0.066
occ_6330 ( drywall installers, ceiling tile installers, and tapers ) : -0.127
occ_6500 ( reinforcing iron and rebar workers ) : -0.198
occ_6730 ( highway maintenance workers ) : -0.069
occ_6750 (  ) : -0.330
occ_6800 ( derrick, rotary drill, and service unit operators, and roustabouts, oil, gas, and mining ) : 0.020
occ_6840 ( mining machine operators ) : 0.013
occ_6910 (  ) : -0.136
occ_6920 (  ) : -0.166
occ_7000 ( first-line supervisors of mechanics, installers, and repairers ) : 0.080
occ_7130 ( security and fire alarm systems installers ) : 0.093
occ_7140 ( aircraft mechanics and service technicians ) : 0.001
occ_7150 ( automotive body and related repairers ) : 0.007
occ_7260 ( vehicle and mobile equipment mechanics, installers, and repairers, nec ) : -0.168
occ_7360 ( millwrights ) : 0.041
occ_7410 ( electrical power-line installers and repairers ) : 0.081
occ_7440 (  ) : -0.268
occ_7510 ( coin, vending, and amusement machine servicers and repairers ) : -0.145
occ_7550 ( manufactured building and mobile home installers ) : 0.000
occ_7560 ( riggers ) : 0.000
occ_7630 ( other installation, maintenance, and repair workers including wind turbine service technicians, and commercial divers, and signal and track switch repairers ) : -0.009
occ_7700 ( first-line supervisors of production and operating workers ) : 0.063
occ_7710 ( aircraft structure, surfaces, rigging, and systems assemblers ) : -0.023
occ_7720 ( electrical, electronics, and electromechanical assemblers ) : -0.004
occ_7750 ( assemblers and fabricators, nec ) : -0.051
occ_7800 ( bakers ) : -0.136
occ_7855 ( food processing, nec ) : -0.034
occ_8000 ( grinding, lapping, polishing, and buffing machine tool setters, operators, and tenders, metal and plastic ) : -0.137
occ_8100 ( molders and molding machine setters, operators, and tenders, metal and plastic ) : -0.081
occ_8120 (  ) : -0.037
occ_8250 ( prepress technicians and workers ) : 0.041
occ_8255 (  ) : -0.143
occ_8300 ( laundry and dry-cleaning workers ) : -0.025
occ_8330 ( shoe and leather workers and repairers ) : -0.243
occ_8350 ( tailors, dressmakers, and sewers ) : -0.131
occ_8440 (  ) : 0.944
occ_8550 ( woodworkers including model makers and patternmakers, nec ) : -0.152
occ_8610 ( stationary engineers and boiler operators ) : 0.001
occ_8620 ( water wastewater treatment plant and system operators ) : 0.009
occ_8630 ( plant and system operators, nec ) : 0.139
occ_8650 ( crushing, grinding, polishing, mixing, and blending workers ) : -0.094
occ_8710 ( cutting workers ) : -0.006
occ_8740 ( inspectors, testers, sorters, samplers, and weighers ) : -0.034
occ_8760 ( medical, dental, and ophthalmic laboratory technicians ) : -0.109
occ_8800 ( packaging and filling machine operators and tenders ) : -0.036
occ_8810 ( painting workers and dyers ) : -0.070
occ_8830 ( photographic process workers and processing machine operators ) : -0.049
occ_8840 (  ) : -0.019
occ_8930 ( paper goods machine setters, operators, and tenders ) : 0.008
occ_8950 ( helpers--production workers ) : -0.101
occ_8965 ( other production workers including semiconductor processors and cooling and freezing equipment operators ) : -0.099
occ_9110 (  ) : -0.389
occ_9120 (  ) : -0.241
occ_9150 ( motor vehicle operators, all other ) : -0.179
occ_9200 ( locomotive engineers and operators ) : 0.124
occ_9240 ( railroad conductors and yardmasters ) : 0.117
occ_9330 (  ) : 0.187
occ_9350 ( parking lot attendants ) : -0.105
occ_9600 ( industrial truck and tractor operators ) : -0.119
occ_9620 ( laborers and freight, stock, and material movers, hand ) : -0.082
occ_9640 ( packers and packagers, hand ) : -0.317
occ_9720 ( refuse and recyclable material collectors ) : -0.069
occ_9730 (  ) : 0.001
occ_9840 (  ) : -0.280
ind_0 (  ) : -0.028
ind_280 (  ) : 0.084
ind_370 (  ) : 0.045
ind_380 (  ) : 0.106
ind_390 (  ) : 0.023
ind_470 (  ) : 0.120
ind_570 (  ) : 0.042
ind_580 (  ) : 0.142
ind_680 (  ) : 0.029
ind_690 (  ) : 0.159
ind_1190 (  ) : -0.034
ind_1480 (  ) : -0.126
ind_1670 (  ) : -0.044
ind_1680 (  ) : -0.087
ind_1790 (  ) : 0.110
ind_1870 (  ) : 0.027
ind_1880 (  ) : -0.016
ind_2290 (  ) : 0.011
ind_2390 (  ) : 0.064
ind_2470 (  ) : -0.081
ind_2480 (  ) : -0.005
ind_2670 (  ) : 0.090
ind_2680 (  ) : 0.038
ind_2790 (  ) : -0.097
ind_3090 (  ) : 0.017
ind_3170 (  ) : 0.121
ind_3360 (  ) : 0.040
ind_3380 (  ) : 0.011
ind_3390 (  ) : 0.034
ind_3570 (  ) : 0.044
ind_3580 (  ) : 0.010
ind_3670 (  ) : 0.033
ind_3690 (  ) : -0.012
ind_3970 (  ) : 0.007
ind_4090 (  ) : 0.032
ind_4170 (  ) : 0.099
ind_4190 (  ) : 0.004
ind_4380 (  ) : 0.068
ind_4470 (  ) : 0.010
ind_4670 (  ) : 0.043
ind_4770 (  ) : -0.020
ind_4870 (  ) : -0.039
ind_4880 (  ) : -0.073
ind_4990 (  ) : -0.123
ind_5070 (  ) : -0.032
ind_5170 (  ) : -0.002
ind_5190 (  ) : -0.065
ind_5380 (  ) : -0.018
ind_5590 (  ) : 0.060
ind_5690 (  ) : -0.046
ind_6080 (  ) : 0.148
ind_6270 (  ) : 0.131
ind_6480 (  ) : 0.023
ind_6490 (  ) : 0.116
ind_6570 (  ) : 0.047
ind_6670 (  ) : 0.002
ind_6680 (  ) : 0.005
ind_6970 (  ) : 0.071
ind_6990 (  ) : 0.033
ind_7080 (  ) : -0.033
ind_7190 (  ) : 0.112
ind_7380 (  ) : 0.034
ind_7470 (  ) : 0.025
ind_7570 (  ) : 0.034
ind_7680 (  ) : -0.014
ind_7770 (  ) : -0.053
ind_7860 (  ) : -0.011
ind_7890 (  ) : -0.084
ind_7980 (  ) : 0.007
ind_8170 (  ) : -0.045
ind_8190 (  ) : 0.028
ind_8370 (  ) : -0.039
ind_8380 (  ) : -0.021
ind_8470 (  ) : -0.038
ind_8570 (  ) : -0.023
ind_8580 (  ) : -0.250
ind_8590 (  ) : -0.055
ind_8660 (  ) : -0.026
ind_8670 (  ) : -0.056
ind_8870 (  ) : 0.053
ind_8880 (  ) : -0.050
ind_8980 (  ) : -0.031
ind_9090 (  ) : -0.092
ind_9290 (  ) : -0.041
ind_9370 (  ) : -0.007
ind_9890 (  ) : -0.005
educ_10 ( grades 1, 2, 3, or 4 ) : -0.053
educ_20 ( grades 5 or 6 ) : -0.026
educ_30 ( grades 7 or 8 ) : -0.007
educ_71 ( 12th grade, no diploma ) : 0.011
educ_73 ( high school diploma or equivalent ) : -0.000
educ_81 ( some college but no degree ) : -0.005
educ_91 ( associate's degree, occupational/vocational program ) : 0.007
educ_111 ( bachelor's degree ) : 0.076
educ_124 ( professional school degree ) : 0.016
educ_125 ( doctorate degree ) : 0.106
occly_10 ( chief executives and legislators/public administration ) : 0.525
occly_20 ( general and operations managers ) : 0.289
occly_40 (  ) : 0.289
occly_50 (  ) : 0.368
occly_60 (  ) : 0.222
occly_100 ( administrative services managers ) : 0.065
occly_110 ( computer and information systems managers ) : 0.405
occly_120 ( financial managers ) : 0.273
occly_136 (  ) : 0.164
occly_137 (  ) : 0.094
occly_140 ( industrial production managers ) : 0.273
occly_150 ( purchasing managers ) : 0.141
occly_160 ( transportation, storage, and distribution managers ) : 0.057
occly_205 ( farmers, ranchers, and other agricultural managers ) : -0.039
occly_220 ( constructions managers ) : 0.258
occly_230 ( education administrators ) : 0.229
occly_300 ( architectural and engineering managers ) : 0.390
occly_310 ( food service and lodging managers ) : 0.027
occly_350 ( medical and health services managers ) : 0.156
occly_360 ( natural science managers ) : 0.088
occly_410 ( property, real estate, and community association managers ) : 0.131
occly_420 ( social and community service managers ) : 0.058
occly_430 ( managers, nec (including postmasters) ) : 0.245
occly_500 ( agents and business managers of artists, performers, and athletes ) : 0.001
occly_520 ( wholesale and retail buyers, except farm products ) : 0.047
occly_630 (  ) : 0.149
occly_710 ( management analysts ) : 0.175
occly_726 (  ) : 0.052
occly_740 (  ) : 0.039
occly_800 ( accountants and auditors ) : 0.148
occly_820 ( budget analysts ) : 0.098
occly_840 ( financial analysts ) : 0.240
occly_850 ( personal financial advisors ) : 0.092
occly_910 ( credit counselors and loan officers ) : 0.049
occly_940 ( tax preparers ) : -0.168
occly_1006 (  ) : 0.272
occly_1010 ( computer programmers ) : 0.186
occly_1020 ( software developers, applications and systems software ) : 0.266
occly_1030 (  ) : 0.064
occly_1050 ( computer support specialists ) : 0.001
occly_1106 (  ) : 0.380
occly_1107 (  ) : 0.092
occly_1200 ( actuaries ) : 0.613
occly_1220 ( operations research analysts ) : 0.103
occly_1300 ( architects, except naval ) : 0.111
occly_1320 ( aerospace engineers ) : 0.224
occly_1360 ( civil engineers ) : 0.230
occly_1400 ( computer hardware engineers ) : 0.198
occly_1410 ( electrical and electronics engineers ) : 0.251
occly_1420 ( environmental engineers ) : 0.186
occly_1430 ( industrial engineers, including health and safety ) : 0.026
occly_1440 ( marine engineers and naval architects ) : 0.322
occly_1500 (  ) : 0.299
occly_1510 (  ) : 0.012
occly_1530 ( engineers, nec ) : 0.263
occly_1550 ( engineering technicians, except drafters ) : 0.001
occly_1560 ( surveying and mapping technicians ) : -0.011
occly_1640 ( conservation scientists and foresters ) : 0.012
occly_1660 (  ) : 0.036
occly_1700 ( astronomers and physicists ) : 0.034
occly_1710 ( atmospheric and space scientists ) : -0.110
occly_1800 ( economists and market researchers ) : 0.059
occly_1860 (  ) : -0.128
occly_1930 ( geological and petroleum technicians, and nuclear technicians ) : -0.001
occly_1965 (  ) : -0.077
occly_2000 ( counselors ) : -0.002
occly_2016 (  ) : -0.019
occly_2025 (  ) : -0.023
occly_2060 ( religious workers, nec ) : -0.080
occly_2100 ( lawyers, and judges, magistrates, and other judicial workers ) : 0.281
occly_2300 ( preschool and kindergarten teachers ) : -0.018
occly_2320 ( secondary school teachers ) : 0.064
occly_2330 ( special education teachers ) : 0.041
occly_2340 ( other teachers and instructors ) : -0.198
occly_2430 ( librarians ) : -0.019
occly_2540 ( teacher assistants ) : -0.410
occly_2550 ( education, training, and library workers, nec ) : -0.013
occly_2630 ( designers ) : -0.005
occly_2700 ( actors, producers, and directors ) : 0.077
occly_2720 ( athletes, coaches, umpires, and related workers ) : -0.238
occly_2740 ( dancers and choreographers ) : -0.410
occly_2760 ( entertainers and performers, sports and related workers, all other ) : 0.161
occly_2800 ( announcers ) : 0.234
occly_2825 ( public relations specialists ) : 0.130
occly_2840 ( technical writers ) : 0.077
occly_2850 ( writers and authors ) : 0.189
occly_2910 ( photographers ) : -0.127
occly_2960 (  ) : -0.138
occly_3000 ( chiropractors ) : -0.163
occly_3010 ( dentists ) : 0.323
occly_3030 ( dieticians and nutritionists ) : -0.041
occly_3040 ( optometrists ) : 0.157
occly_3050 ( pharmacists ) : 0.552
occly_3060 ( physicians and surgeons ) : 0.377
occly_3110 ( physician assistants ) : 0.107
occly_3120 ( podiatrists ) : 0.807
occly_3150 ( occupational therapists ) : 0.157
occly_3160 ( physical therapists ) : 0.079
occly_3200 ( radiation therapists ) : 0.081
occly_3220 ( respiratory therapists ) : 0.111
occly_3230 ( speech language pathologists ) : 0.026
occly_3235 (  ) : -0.053
occly_3250 ( veterinarians ) : 0.339
occly_3255 (  ) : 0.083
occly_3256 (  ) : 0.646
occly_3257 (  ) : 0.042
occly_3258 (  ) : 0.322
occly_3310 ( dental hygienists ) : 0.193
occly_3320 ( diagnostic related technologists and technicians ) : 0.163
occly_3420 (  ) : -0.004
occly_3500 ( licensed practical and licensed vocational nurses ) : 0.039
occly_3510 ( medical records and health information technicians ) : -0.209
occly_3600 ( nursing, psychiatric, and home health aides ) : -0.257
occly_3610 ( occupational therapy assistants and aides ) : 0.200
occly_3630 ( massage therapists ) : -0.160
occly_3645 (  ) : -0.201
occly_3647 (  ) : -0.159
occly_3649 (  ) : -0.181
occly_3655 (  ) : -0.285
occly_3710 ( first-line supervisors of police and detectives ) : 0.172
occly_3720 ( first-line supervisors of fire fighting and prevention workers ) : 0.223
occly_3750 ( fire inspectors ) : 0.003
occly_3820 ( police officers and detectives ) : 0.157
occly_3840 (  ) : -0.280
occly_3850 (  ) : 0.060
occly_3860 (  ) : 0.118
occly_3900 ( animal control ) : 0.754
occly_3930 ( security guards and gaming surveillance officers ) : -0.242
occly_3940 ( crossing guards ) : -1.007
occly_3955 (  ) : -0.494
occly_4010 ( first-line supervisors of food preparation and serving workers ) : -0.089
occly_4020 (  ) : -0.266
occly_4030 ( food preparation workers ) : -0.407
occly_4050 ( combined food preparation and serving workers, including fast food ) : -0.325
occly_4060 ( counter attendant, cafeteria, food concession, and coffee shop ) : -0.266
occly_4110 ( waiters and waitresses ) : -0.342
occly_4120 ( food servers, nonrestaurant ) : -0.391
occly_4130 ( food preparation and serving related workers, nec ) : -0.343
occly_4140 ( dishwashers ) : -0.443
occly_4150 ( host and hostesses, restaurant, lounge, and coffee shop ) : -0.560
occly_4200 ( first-line supervisors of housekeeping and janitorial workers ) : -0.048
occly_4220 ( janitors and building cleaners ) : -0.274
occly_4230 ( maids and housekeeping cleaners ) : -0.342
occly_4250 ( grounds maintenance workers ) : -0.213
occly_4300 ( first-line supervisors of gaming workers ) : 0.125
occly_4350 ( nonfarm animal caretakers ) : -0.061
occly_4430 ( entertainment attendants and related workers, nec ) : -0.197
occly_4465 (  ) : 0.001
occly_4500 ( barbers ) : -0.003
occly_4520 ( personal appearance workers, nec ) : -0.258
occly_4530 ( baggage porters, bellhops, and concierges ) : -0.324
occly_4540 ( tour and travel guides ) : -1.144
occly_4600 ( childcare workers ) : -0.095
occly_4610 ( personal care aides ) : -0.340
occly_4620 ( recreation and fitness workers ) : -0.368
occly_4650 ( personal care and service workers, all other ) : -0.271
occly_4700 ( first-line supervisors of sales workers ) : 0.078
occly_4710 (  ) : 0.175
occly_4720 ( cashiers ) : -0.387
occly_4760 ( retail salespersons ) : -0.230
occly_4800 ( advertising sales agents ) : 0.044
occly_4810 ( insurance sales agents ) : 0.010
occly_4820 ( securities, commodities, and financial services sales agents ) : 0.079
occly_4840 ( sales representatives, services, all other ) : 0.019
occly_4850 ( sales representatives, wholesale and manufacturing ) : 0.064
occly_4900 ( models, demonstrators, and product promoters ) : -0.280
occly_4920 ( real estate brokers and sales agents ) : 0.018
occly_4930 ( sales engineers ) : 0.199
occly_4940 ( telemarketers ) : -0.431
occly_4950 ( door-to-door sales workers, news and street vendors, and related workers ) : -0.216
occly_5000 ( first-line supervisors of office and administrative support workers ) : 0.041
occly_5010 ( switchboard operators, including answering service ) : -0.212
occly_5100 ( bill and account collectors ) : -0.091
occly_5110 ( billing and posting clerks ) : -0.004
occly_5160 ( bank tellers ) : -0.265
occly_5240 ( customer service representatives ) : -0.144
occly_5260 ( file clerks ) : -0.174
occly_5300 ( hotel, motel, and resort desk clerks ) : -0.198
occly_5310 ( interviewers, except eligibility and loan ) : -0.188
occly_5320 ( library assistants, clerical ) : -0.598
occly_5340 ( new account clerks ) : -0.135
occly_5350 ( correspondent clerks and order clerks ) : -0.099
occly_5400 ( receptionists and information clerks ) : -0.184
occly_5410 ( reservation and transportation ticket agents and travel clerks ) : -0.087
occly_5420 ( information and record clerks, all other ) : -0.179
occly_5510 ( couriers and messengers ) : -0.078
occly_5560 ( postal service mail sorters, processors, and processing machine operators ) : -0.237
occly_5610 ( shipping, receiving, and traffic clerks ) : -0.026
occly_5620 ( stock clerks and order fillers ) : -0.345
occly_5630 ( weighers, measurers, checkers, and samplers, recordkeeping ) : -0.100
occly_5700 ( secretaries and administrative assistants ) : -0.066
occly_5810 ( data entry keyers ) : -0.195
occly_5840 ( insurance claims and policy processing clerks ) : -0.068
occly_5850 ( mail clerks and mail machine operators, except postal service ) : -0.469
occly_5860 ( office clerks, general ) : -0.211
occly_6005 ( first-line supervisors of farming, fishing, and forestry workers ) : 0.024
occly_6040 ( graders and sorters, agricultural products ) : -0.290
occly_6050 ( agricultural workers, nec ) : -0.156
occly_6100 ( fishing and hunting workers ) : 0.194
occly_6200 ( first-line supervisors of construction trades and extraction workers ) : 0.216
occly_6210 ( boilermakers ) : -0.148
occly_6230 ( carpenters ) : -0.087
occly_6240 ( carpet, floor, and tile installers and finishers ) : -0.056
occly_6250 ( cement masons, concrete finishers, and terrazzo workers ) : -0.042
occly_6260 ( construction laborers ) : -0.082
occly_6300 ( paving, surfacing, and tamping equipment operators ) : 0.094
occly_6320 ( construction equipment operators except paving, surfacing, and tamping equipment operators ) : 0.003
occly_6355 ( electricians ) : 0.078
occly_6420 ( painters, construction and maintenance ) : -0.278
occly_6440 ( pipelayers, plumbers, pipefitters, and steamfitters ) : 0.040
occly_6460 ( plasterers and stucco masons ) : -0.218
occly_6515 ( roofers ) : -0.093
occly_6520 ( sheet metal workers, metal-working ) : -0.013
occly_6600 ( helpers, construction trades ) : -0.258
occly_6700 ( elevator installers and repairers ) : 0.135
occly_6710 ( fence erectors ) : -0.411
occly_6800 ( derrick, rotary drill, and service unit operators, and roustabouts, oil, gas, and mining ) : 0.318
occly_6820 ( earth drillers, except oil and gas ) : 0.237
occly_6920 (  ) : 0.063
occly_6940 ( extraction workers, nec ) : 0.073
occly_7010 ( computer, automated teller, and office machine repairers ) : -0.050
occly_7040 ( electric motor, power tool, and related repairers ) : 0.003
occly_7100 ( electrical and electronics repairers, transportation equipment, and industrial and utility ) : 0.065
occly_7130 ( security and fire alarm systems installers ) : 0.041
occly_7140 ( aircraft mechanics and service technicians ) : 0.054
occly_7160 ( automotive glass installers and repairers ) : -0.159
occly_7200 ( automotive service technicians and mechanics ) : -0.020
occly_7220 ( heavy vehicle and mobile equipment service technicians and mechanics ) : 0.067
occly_7340 ( maintenance and repair workers, general ) : -0.006
occly_7360 ( millwrights ) : 0.106
occly_7420 ( telecommunications line installers and repairers ) : 0.061
occly_7510 ( coin, vending, and amusement machine servicers and repairers ) : -0.034
occly_7550 ( manufactured building and mobile home installers ) : 0.024
occly_7560 ( riggers ) : 0.059
occly_7600 (  ) : 0.047
occly_7610 ( helpers--installation, maintenance, and repair workers ) : -0.443
occly_7700 ( first-line supervisors of production and operating workers ) : 0.038
occly_7710 ( aircraft structure, surfaces, rigging, and systems assemblers ) : -0.170
occly_7720 ( electrical, electronics, and electromechanical assemblers ) : -0.138
occly_7730 ( engine and other machine assemblers ) : -0.105
occly_7750 ( assemblers and fabricators, nec ) : -0.162
occly_7800 ( bakers ) : -0.218
occly_7810 ( butchers and other meat, poultry, and fish processing workers ) : -0.127
occly_7830 ( food and tobacco roasting, baking, and drying machine operators and tenders ) : -0.119
occly_7840 ( food batchmakers ) : -0.302
occly_7855 ( food processing, nec ) : -0.040
occly_7950 ( cutting, punching, and press machine setters, operators, and tenders, metal and plastic ) : -0.176
occly_8000 ( grinding, lapping, polishing, and buffing machine tool setters, operators, and tenders, metal and plastic ) : -0.075
occly_8220 ( metal workers and plastic workers, nec ) : -0.091
occly_8300 ( laundry and dry-cleaning workers ) : -0.170
occly_8310 ( pressers, textile, garment, and related materials ) : -0.400
occly_8320 ( sewing machine operators ) : -0.294
occly_8340 ( shoe machine operators and tenders ) : -0.042
occly_8400 ( textile bleaching and dyeing, and cutting machine setters, operators, and tenders ) : -0.109
occly_8410 ( textile knitting and weaving machine setters, operators, and tenders ) : -0.328
occly_8440 (  ) : 0.095
occly_8460 ( textile, apparel, and furnishings workers, nec ) : -0.101
occly_8500 ( cabinetmakers and bench carpenters ) : -0.012
occly_8510 ( furniture finishers ) : -0.236
occly_8600 ( power plant operators, distributors, and dispatchers ) : 0.309
occly_8630 ( plant and system operators, nec ) : 0.104
occly_8710 ( cutting workers ) : -0.185
occly_8740 ( inspectors, testers, sorters, samplers, and weighers ) : -0.023
occly_8800 ( packaging and filling machine operators and tenders ) : -0.143
occly_8830 ( photographic process workers and processing machine operators ) : -0.016
occly_8850 ( adhesive bonding machine operators and tenders ) : -0.064
occly_8910 ( etchers, engravers, and lithographers ) : -0.479
occly_8920 ( molders, shapers, and casters, except metal and plastic ) : 0.058
occly_8965 ( other production workers including semiconductor processors and cooling and freezing equipment operators ) : -0.090
occly_9030 ( aircraft pilots and flight engineers ) : 0.582
occly_9040 ( air traffic controllers and airfield operations specialists ) : 0.384
occly_9110 (  ) : -0.025
occly_9130 ( driver/sales workers and truck drivers ) : -0.042
occly_9140 ( taxi drivers and chauffeurs ) : -0.309
occly_9200 ( locomotive engineers and operators ) : 0.038
occly_9310 ( ship and boat captains and operators ) : 0.326
occly_9330 (  ) : 0.000
occly_9350 ( parking lot attendants ) : -0.316
occly_9360 ( automotive and watercraft service attendants ) : -0.284
occly_9415 (  ) : -0.325
occly_9510 ( crane and tower operators ) : 0.051
occly_9600 ( industrial truck and tractor operators ) : -0.037
occly_9610 ( cleaners of vehicles and equipment ) : -0.366
occly_9620 ( laborers and freight, stock, and material movers, hand ) : -0.241
occly_9630 ( machine feeders and offbearers ) : -0.121
occly_9640 ( packers and packagers, hand ) : -0.098
occly_9650 ( pumping station operators ) : 0.004
occly_9730 (  ) : 0.191
occly_9750 ( material moving workers, nec ) : -0.179
occly_9840 (  ) : 0.200
indly_170 (  ) : -0.035
indly_280 ( other primary metal industries ) : 0.075
indly_290 ( screw machine products ) : -0.019
indly_370 ( cycles and miscellaneous transportation equipment ) : 0.196
indly_380 ( photographic equipment and supplies ) : 0.252
indly_390 ( toys, amusement, and sporting goods ) : 0.324
indly_480 (  ) : 0.034
indly_490 (  ) : 0.419
indly_570 (  ) : 0.180
indly_590 ( mobile home dealers ) : 0.268
indly_670 ( vending machine operators ) : 0.067
indly_1070 (  ) : 0.004
indly_1090 (  ) : 0.015
indly_1170 (  ) : 0.105
indly_1190 (  ) : -0.011
indly_1270 (  ) : -0.028
indly_1290 (  ) : -0.037
indly_1480 (  ) : -0.076
indly_1670 (  ) : -0.593
indly_1680 (  ) : -0.114
indly_1690 (  ) : 0.338
indly_1870 (  ) : 0.155
indly_1890 (  ) : 0.070
indly_2070 (  ) : 0.298
indly_2090 (  ) : 0.229
indly_2190 (  ) : 0.258
indly_2280 (  ) : 0.119
indly_2290 (  ) : 0.092
indly_2470 (  ) : 0.019
indly_2490 (  ) : 0.054
indly_2590 (  ) : -0.102
indly_2780 (  ) : -0.301
indly_2790 (  ) : 0.111
indly_2880 (  ) : 0.045
indly_2970 (  ) : 0.047
indly_3080 (  ) : 0.020
indly_3190 (  ) : 0.048
indly_3360 (  ) : 0.071
indly_3380 (  ) : 0.129
indly_3390 (  ) : 0.097
indly_3490 (  ) : 0.056
indly_3570 (  ) : 0.047
indly_3580 (  ) : 0.059
indly_3590 (  ) : 0.073
indly_3680 (  ) : 0.033
indly_3870 (  ) : -0.121
indly_3890 (  ) : -0.012
indly_3970 (  ) : 0.092
indly_3980 (  ) : -0.047
indly_4080 (  ) : 0.025
indly_4170 (  ) : 0.002
indly_4180 (  ) : 0.078
indly_4270 (  ) : 0.063
indly_4380 (  ) : 0.137
indly_4390 (  ) : 0.014
indly_4470 (  ) : 0.001
indly_4480 (  ) : 0.022
indly_4490 (  ) : 0.147
indly_4560 (  ) : 0.009
indly_4585 (  ) : 0.072
indly_4590 (  ) : -0.237
indly_4670 (  ) : 0.128
indly_4690 (  ) : -0.070
indly_4770 (  ) : 0.030
indly_4780 (  ) : -0.026
indly_4790 (  ) : 0.112
indly_4880 (  ) : -0.146
indly_4970 (  ) : -0.150
indly_4980 (  ) : -0.122
indly_5070 (  ) : -0.012
indly_5090 (  ) : -0.045
indly_5170 (  ) : -0.161
indly_5180 (  ) : -0.234
indly_5270 (  ) : -0.278
indly_5280 (  ) : -0.110
indly_5290 (  ) : -0.122
indly_5370 (  ) : -0.415
indly_5380 (  ) : -0.231
indly_5390 (  ) : -0.151
indly_5470 (  ) : -0.254
indly_5490 (  ) : -0.346
indly_5570 (  ) : -0.252
indly_5580 (  ) : -0.066
indly_5591 (  ) : 0.008
indly_5670 (  ) : -0.216
indly_5690 (  ) : -0.086
indly_6070 (  ) : 0.006
indly_6090 (  ) : 0.134
indly_6170 (  ) : 0.113
indly_6180 (  ) : -0.052
indly_6190 (  ) : -0.204
indly_6280 (  ) : 0.139
indly_6290 (  ) : 0.025
indly_6380 (  ) : -0.038
indly_6470 (  ) : -0.164
indly_6672 (  ) : 0.285
indly_6680 (  ) : 0.134
indly_6690 (  ) : 0.050
indly_6695 (  ) : 0.059
indly_6770 (  ) : -0.081
indly_6970 (  ) : 0.077
indly_6990 (  ) : 0.062
indly_7070 (  ) : 0.017
indly_7170 (  ) : -0.188
indly_7190 (  ) : 0.063
indly_7270 (  ) : 0.139
indly_7290 (  ) : 0.121
indly_7370 (  ) : 0.028
indly_7380 (  ) : 0.131
indly_7390 (  ) : 0.116
indly_7460 (  ) : 0.078
indly_7470 (  ) : 0.116
indly_7490 (  ) : -0.028
indly_7570 (  ) : 0.012
indly_7580 (  ) : -0.405
indly_7590 (  ) : -0.059
indly_7680 (  ) : -0.086
indly_7690 (  ) : -0.090
indly_7860 (  ) : -0.104
indly_7870 (  ) : -0.118
indly_7880 (  ) : -0.067
indly_7970 (  ) : 0.055
indly_7980 (  ) : 0.011
indly_8170 (  ) : -0.109
indly_8180 (  ) : 0.028
indly_8270 (  ) : -0.025
indly_8370 (  ) : -0.109
indly_8380 (  ) : -0.060
indly_8390 (  ) : -0.362
indly_8470 (  ) : -0.203
indly_8560 (  ) : -0.098
indly_8570 (  ) : -0.097
indly_8660 (  ) : -0.069
indly_8670 (  ) : -0.154
indly_8680 (  ) : -0.129
indly_8690 (  ) : -0.074
indly_8770 (  ) : -0.012
indly_8780 (  ) : -0.130
indly_8870 (  ) : 0.052
indly_8880 (  ) : -0.026
indly_8890 (  ) : -1.294
indly_8980 (  ) : -0.060
indly_9070 (  ) : -0.032
indly_9160 (  ) : -0.246
indly_9170 (  ) : -0.070
indly_9290 (  ) : -0.013
indly_9370 (  ) : -0.014
indly_9380 (  ) : -0.007
indly_9470 (  ) : 0.062
indly_9480 (  ) : -0.027
indly_9590 (  ) : 0.036
indly_9890 (  ) : 0.000
classwly_13 ( self-employed, not incorporated ) : -1.108
classwly_14 ( self-employed, incorporated ) : 0.220
classwly_25 ( federal government employee ) : 0.128
classwly_27 ( state government employee ) : -0.093
classwly_28 ( local government employee ) : -0.020
pension_at_w_ly_2 ( pension plan at work, but not included ) : -0.032
pension_at_w_ly_3 ( included in pension plan at work ) : 0.312
firmsize_ly_1 ( under 10 ) : -0.212
firmsize_ly_4 ( 10 to 49 ) : -0.073
firmsize_ly_6 ( 50 to 99 ) : -0.011
firmsize_ly_8 ( 500 to 999 ) : 0.020
firmsize_ly_9 ( 1000+ ) : 0.035
actnlfly_0 ( niu ) : 0.388
actnlfly_10 ( ill or disabled ) : -0.008
actnlfly_20 ( taking care of home/family ) : -0.340
actnlfly_30 ( going to school ) : -0.482
actnlfly_40 ( retired ) : -0.224
actnlfly_50 ( other ) : 0.128
spmmort_1 ( owners with a mortgage ) : 0.068
statefip_2 ( alaska ) : 0.128
statefip_5 ( arkansas ) : -0.015
statefip_6 ( california ) : 0.052
statefip_9 ( connecticut ) : 0.077
statefip_11 ( district of columbia ) : 0.032
statefip_15 ( hawaii ) : 0.068
statefip_16 ( idaho ) : -0.044
statefip_20 ( kansas ) : -0.063
statefip_21 ( kentucky ) : -0.008
statefip_23 ( maine ) : -0.070
statefip_25 ( massachusetts ) : 0.045
statefip_29 ( missouri ) : -0.059
statefip_30 ( montana ) : -0.018
statefip_31 ( nebraska ) : 0.003
statefip_32 ( nevada ) : 0.038
statefip_33 ( new hampshire ) : 0.027
statefip_35 ( new mexico ) : -0.031
statefip_37 ( north carolina ) : -0.007
statefip_39 ( ohio ) : -0.000
statefip_40 ( oklahoma ) : -0.017
statefip_41 ( oregon ) : -0.011
statefip_42 ( pennsylvania ) : -0.005
statefip_44 ( rhode island ) : 0.026
statefip_45 ( south carolina ) : -0.029
statefip_46 ( south dakota ) : -0.035
statefip_47 ( tennessee ) : -0.019
statefip_54 ( west virginia ) : -0.045
statefip_56 ( wyoming ) : 0.062
state_ly_6 ( california ) : -0.022
state_ly_10 ( delaware ) : -0.090
state_ly_12 ( florida ) : 0.010
state_ly_16 ( idaho ) : -0.029
state_ly_23 ( maine ) : -0.061
state_ly_24 ( maryland ) : 0.018
state_ly_25 ( massachusetts ) : 0.127
state_ly_34 ( new jersey ) : -0.030
state_ly_37 ( north carolina ) : 0.030
state_ly_40 ( oklahoma ) : -0.038
state_ly_49 ( utah ) : -0.052
state_ly_51 ( virginia ) : 0.047
state_ly_91 ( abroad ) : -0.091
whymove_1 ( change in marital status ) : -0.029
whymove_2 ( to establish own household ) : -0.068
whymove_3 ( other family reason ) : 0.004
whymove_4 ( new job or job transfer ) : -0.000
whymove_5 ( to look for work or lost job ) : -0.254
whymove_10 ( wanted new or better housing ) : 0.013
whymove_11 ( wanted better neighborhood ) : 0.048
whymove_12 ( for cheaper housing ) : -0.034
whymove_14 ( attend/leave college ) : -0.287
whymove_18 ( natural disaster ) : 0.146
whymove_19 ( foreclosure or eviction ) : 0.026
mig_stat_ly_4 ( moved within state, different county ) : 0.006
mig_stat_ly_6 ( abroad ) : -0.007
health_1 ( excellent ) : 0.027
health_3 ( good ) : -0.054
health_4 ( fair ) : -0.129
health_5 ( poor ) : -0.174
vet1_2 ( august 1990 to august 2001 ) : 0.004
vet1_3 ( may 1975 to july 1990 ) : 0.001
vet1_4 ( vietnam era (august 1964 to april 1975) ) : -0.067
csvisleg_1 ( no ) : 0.013
csvisleg_2 ( yes ) : 0.002
csvisleg_98 ( blank ) : -0.015
paidhour_1 ( no ) : 0.109
paidhour_2 ( yes ) : -0.031
union_1 ( no union coverage ) : -0.011
union_2 ( member of labor union ) : 0.073
bpl_1.0 ( usa, canada & dependent ) : 0.004
bpl_8.0 ( developed asia ) : 0.021
fbpl_5.0 ( central and caribean ) : -0.013
fbpl_7.0 ( europe ) : 0.005
fbpl_9.0 ( east asia ) : -0.006


### Grid:

grid: [1.45096612e-03 1.35317586e-03 1.26197633e-03 1.17692335e-03
 1.09760266e-03 1.02362791e-03 9.54638815e-04 8.90299354e-04
 8.30296157e-04 7.74336975e-04 7.22149255e-04 6.73478812e-04
 6.28088594e-04 5.85757525e-04 5.46279428e-04 5.09462023e-04
 4.75125988e-04 4.43104086e-04 4.13240354e-04 3.85389337e-04
 3.59415386e-04 3.35191992e-04 3.12601173e-04 2.91532900e-04
 2.71884559e-04 2.53560449e-04 2.36471324e-04 2.20533948e-04
 2.05670698e-04 1.91809181e-04 1.78881884e-04 1.66825844e-04
 1.55582341e-04 1.45096612e-04 1.35317586e-04 1.26197633e-04
 1.17692335e-04 1.09760266e-04 1.02362791e-04 9.54638815e-05
 8.90299354e-05 8.30296157e-05 7.74336975e-05 7.22149255e-05
 6.73478812e-05 6.28088594e-05 5.85757525e-05 5.46279428e-05
 5.09462023e-05 4.75125988e-05 4.43104086e-05 4.13240354e-05
 3.85389337e-05 3.59415386e-05 3.35191992e-05 3.12601173e-05
 2.91532900e-05 2.71884559e-05 2.53560449e-05 2.36471324e-05
 2.20533948e-05 2.05670698e-05 1.91809181e-05 1.78881884e-05
 1.66825844e-05 1.55582341e-05 1.45096612e-05 1.35317586e-05
 1.26197633e-05 1.17692335e-05 1.09760266e-05 1.02362791e-05
 9.54638815e-06 8.90299354e-06 8.30296157e-06 7.74336975e-06
 7.22149255e-06 6.73478812e-06 6.28088594e-06 5.85757525e-06
 5.46279428e-06 5.09462023e-06 4.75125988e-06 4.43104086e-06
 4.13240354e-06 3.85389337e-06 3.59415386e-06 3.35191992e-06
 3.12601173e-06 2.91532900e-06 2.71884559e-06 2.53560449e-06
 2.36471324e-06 2.20533948e-06 2.05670698e-06 1.91809181e-06
 1.78881884e-06 1.66825844e-06 1.55582341e-06 1.45096612e-06]





















#%% Show results...
Time to run: 1205.65895986557 to run
\lambda:  (1.023531021899027e-05,) log10: [-4.98989899] ln: [-11.48966703]
Coefficients: 
 [ 0.0039944  -0.         -0.12838535 ... -0.00625428  0.
 -0.        ]
Mean squared error: 0.29
Coefficient of determination: 0.57
age ( age ) : 0.004
educ_cat_1.0 (  ) : -0.128
educ_cat_2.0 (  ) : -0.034
educ_cat_4.0 (  ) : 0.065
educ_cat_5.0 (  ) : 0.289
race_cat_1.0 (  ) : 0.042
race_cat_2.0 (  ) : -0.013
male_0.0 (  ) : -0.275
hhtenure_1 ( owned or being bought ) : 0.051
hhtenure_3 ( occupied without payment of cash rent ) : -0.023
region_11 ( new england division ) : 0.028
region_21 ( east north central division ) : -0.008
region_32 ( east south central division ) : -0.037
region_42 ( pacific division ) : 0.031
metarea_120 ( albany, ga ) : -0.105
metarea_200 ( albuquerque, nm ) : -0.001
metarea_280 ( altoona, pa msa ) : -0.030
metarea_320 ( amarillo, tx ) : -0.010
metarea_440 ( ann arbor, mi ) : 0.083
metarea_462 ( oshkosh-neenah, wi ) : -0.172
metarea_480 ( asheville, nc ) : -0.083
metarea_521 ( atlanta-sandy springs-marietta, ga ) : 0.008
metarea_641 ( austin-round rock, tx ) : 0.047
metarea_680 ( bakersfield, ca ) : -0.127
metarea_721 ( baltimore-towson, md ) : 0.066
metarea_730 ( bangor, me ) : -0.036
metarea_741 ( barnstable town, ma ) : -0.048
metarea_760 ( baton rouge, la ) : 0.022
metarea_841 ( beaumont-port arthur, tx ) : 0.068
metarea_860 ( bellingham, wa ) : 0.008
metarea_880 ( billings, mt ) : -0.029
metarea_920 ( biloxi-gulfport, ms ) : -0.017
metarea_960 ( binghamton, ny ) : -0.010
metarea_1081 ( boise city-nampa, id ) : -0.073
metarea_1124 ( boston-cambridge-quincy, ma-nh ) : 0.018
metarea_1280 ( buffalo-niagara falls, ny ) : -0.041
metarea_1360 ( cedar rapids, ia ) : -0.037
metarea_1440 ( charleston-north charleston, sc ) : -0.020
metarea_1480 ( charleston, wv ) : -0.077
metarea_1605 ( chicago-naperville-joliet, il-in-wi ) : 0.055
metarea_1700 ( coeur d'alene, id ) : -0.076
metarea_1720 ( colorado springs, co ) : -0.007
metarea_1800 ( columbus, ga/al ) : -0.125
metarea_1922 ( dallas-fort worth-arlington, tx ) : 0.022
metarea_1930 ( danbury, ct ) : 0.117
metarea_2001 ( springfield, oh ) : -0.016
metarea_2002 ( dayton, oh ) : -0.137
metarea_2030 ( decatur, al ) : -0.022
metarea_2082 ( boulder, co ) : 0.001
metarea_2083 ( denver-aurora, co ) : 0.031
metarea_2241 ( duluth, mn/wi ) : -0.123
metarea_2300 ( el centro, ca ) : -0.122
metarea_2310 ( el paso, tx ) : -0.077
metarea_2360 ( erie, pa ) : -0.127
metarea_2400 ( eugene-springfield, or ) : -0.022
metarea_2581 ( fayetteville-springdale-rogers, ar-mo ) : 0.040
metarea_2640 ( flint, mi ) : -0.118
metarea_2670 ( fort collins-loveland, co ) : -0.044
metarea_2760 ( fort wayne, in ) : -0.004
metarea_2840 ( fresno, ca ) : -0.077
metarea_2900 ( gainesville, fl ) : -0.067
metarea_3060 ( greeley, co ) : -0.029
metarea_3162 ( greenville, sc ) : -0.021
metarea_3181 ( hagerstown-martinsburg, md-wv ) : 0.019
metarea_3362 ( houston-baytown-sugar land, tx ) : 0.078
metarea_3440 ( huntsville,al ) : -0.048
metarea_3480 ( indianapolis, in ) : 0.024
metarea_3520 ( jackson, mi ) : -0.054
metarea_3560 ( jackson, ms ) : -0.021
metarea_3590 ( jacksonville,fl ) : 0.004
metarea_3600 ( jacksonville, nc ) : -0.019
metarea_3621 ( janvesville, wi ) : -0.009
metarea_3661 ( johnson city, tn ) : -0.053
metarea_3720 ( kalamazoo-portage, mi ) : -0.001
metarea_3760 ( kansas city, mo/ks ) : 0.053
metarea_3830 ( kingston, ny ) : 0.018
metarea_4000 ( lancaster, pa ) : 0.073
metarea_4040 ( lansing-east lansing, mi ) : -0.023
metarea_4080 ( laredo, tx ) : -0.000
metarea_4100 ( las cruces, nm ) : -0.042
metarea_4130 ( las vegas-paradise, nv ) : 0.017
metarea_4150 ( lawrence, ks ) : 0.031
metarea_4200 ( lawton, ok ) : -0.025
metarea_4280 ( lexington-fayette, ky ) : -0.043
metarea_4483 ( los angeles-long beach-santa ana, ca ) : 0.015
metarea_4600 ( lubbock, tx ) : -0.075
metarea_4640 ( lynchburg, va ) : -0.021
metarea_4681 ( macon, ga ) : -0.058
metarea_4720 ( madison, wi ) : 0.006
metarea_4940 ( merced, ca ) : -0.037
metarea_5001 ( miami-fort lauderdale-miami beach, fl ) : 0.039
metarea_5081 ( milwaukee-waukesha-west allis, wi ) : -0.003
metarea_5121 ( minneapolis-st. paul-bloomington, mn/wi ) : 0.040
metarea_5200 ( monroe, la ) : -0.004
metarea_5220 ( monroe, mi ) : 0.100
metarea_5321 ( muskegon-norton shores, mi ) : -0.061
metarea_5331 ( myrtle beach-conway-north myrtle beach, sc ) : -0.072
metarea_5481 ( new haven, ct ) : 0.011
metarea_5606 ( new york-northern new jersey-long island, ny-nj-pa ) : 0.194
metarea_5790 ( ocala, fl ) : -0.083
metarea_5801 ( midland, tx ) : 0.101
metarea_5840 ( ocean city, nj ) : -0.318
metarea_5910 ( olympia, wa ) : -0.085
metarea_5960 ( orlando, fl ) : -0.054
metarea_6081 ( pensacola-ferry pass-brent, fl ) : -0.090
metarea_6161 ( philadelphia-camden-wilmington, pa/nj/de ) : 0.054
metarea_6201 ( phoenix-mesa-scottsdale, az ) : 0.011
metarea_6280 ( pittsburg, pa ) : -0.011
metarea_6401 ( portland-south portland, me ) : 0.040
metarea_6520 ( provo-orem, ut ) : -0.019
metarea_6680 ( reading, pa ) : -0.086
metarea_6980 ( st. cloud, mn ) : -0.049
metarea_7080 ( salem, or ) : -0.004
metarea_7130 ( salisbury, md ) : -0.075
metarea_7321 ( san diego-carlsbad-san marcos, ca ) : 0.037
metarea_7364 ( napa, ca ) : 0.042
metarea_7365 ( san francisco-oakland-fremont, ca ) : 0.120
metarea_7401 ( san jose-sunnyvale-santa clara, ca ) : 0.151
metarea_7461 ( san luis obispo-paso robles, ca ) : 0.072
metarea_7471 ( santa barbara-santa maria-goleta, ca ) : 0.060
metarea_7481 ( santa cruz-watsonville, ca ) : 0.051
metarea_7511 ( sarasota-bradenton-venice, fl ) : 0.006
metarea_7520 ( savannah, ga ) : 0.033
metarea_7601 ( seattle-tacoma-bellevue, wa ) : 0.018
metarea_7760 ( sioux falls, sd ) : -0.022
metarea_7920 ( springfield, mo ) : -0.024
metarea_8160 ( syracuse, ny ) : -0.012
metarea_8240 ( tallahassee, fl ) : -0.011
metarea_8440 ( topeka, ks ) : 0.032
metarea_8600 ( tuscaloosa, al ) : -0.050
metarea_8700 ( valdosta, ga ) : -0.002
metarea_8731 ( oxnard-thousand oaks-ventura, ca ) : 0.064
metarea_8740 ( vero beach, fl ) : -0.083
metarea_8750 ( victoria, tx ) : -0.010
metarea_8760 ( vineland-milville-bridgetown, nj ) : 0.067
metarea_8781 ( visalia-porterville, ca ) : -0.021
metarea_8840 ( washington, dc/md/va ) : 0.156
metarea_8920 ( waterloo-cedar falls, ia ) : -0.039
metarea_8940 ( wausau, wi ) : -0.038
metarea_9040 ( wichita, ks ) : -0.037
metarea_9321 ( youngstown-warren-boardman, oh ) : -0.092
metarea_9997 ( other metropolitan areas, unidentified ) : -0.045
metarea_9998 ( niu, household not in a metropolitan area ) : -0.066
metarea_9999 ( missing data ) : -0.020
unitsstr_1 ( mobile home or trailer ) : -0.029
unitsstr_7 ( 5-9 family building ) : -0.007
unitsstr_11 ( one unit, unspecified type ) : 0.025
nfams_1 ( 1 family or n/a ) : 0.006
nfams_4 ( 4 ) : -0.002
nfams_6 ( 6 ) : -0.075
nfams_8 ( 8 ) : 0.137
ncouples_2 ( 2 ) : -0.057
nmothers_2 ( 2 ) : -0.022
nmothers_3 ( 3 ) : -0.088
nfathers_2 ( 2 ) : -0.022
nfathers_3 ( 3 ) : -0.049
marst_1 ( married, spouse present ) : 0.111
marst_3 ( separated ) : -0.024
marst_5 ( widowed ) : -0.041
marst_6 ( never married/single ) : -0.073
famsize_6 ( 6 family members present ) : -0.008
famsize_7 ( 7 family members present ) : -0.013
famsize_8 ( 8 family members present ) : -0.030
famsize_14 ( 14 family members present ) : -0.074
famsize_15 ( 15 family members present ) : -0.276
ftype_2 ( nonfamily householder ) : 0.044
ftype_3 ( related subfamily ) : -0.060
ftype_4 ( unrelated subfamily ) : -0.021
famkind_1 ( husband/wife family ) : -0.045
famkind_3 ( female reference person ) : 0.128
yrimmig_0 ( niu ) : 0.001
yrimmig_1985 ( 1984-1985 ) : 0.008
yrimmig_2001 ( 2000-2001 (2001 cps: 1998-2001) ) : -0.013
yrimmig_2003 ( 2002-2003 (2003 cps: 2000-2003) ) : -0.016
yrimmig_2005 ( 2004-2005 (2005 cps: 2002-2005) ) : -0.042
yrimmig_2007 ( 2004-2007 ) : -0.023
yrimmig_2009 ( 2006-2009 ) : -0.025
yrimmig_2012 ( 2010-2012 (2014 cps: 2010-2011) ) : -0.068
citizen_1 ( born in u.s ) : 0.000
citizen_3 ( born abroad of american parents ) : 0.013
citizen_5 ( not a citizen ) : -0.057
hispan_0 ( not hispanic ) : 0.010
hispan_410 ( central/south american ) : -0.011
occ_0 ( Missing data? ) : -0.276
occ_10 ( chief executives and legislators/public administration ) : 0.077
occ_20 ( general and operations managers ) : 0.082
occ_136 (  ) : 0.082
occ_150 ( purchasing managers ) : 0.037
occ_220 ( constructions managers ) : 0.092
occ_325 (  ) : 0.153
occ_340 (  ) : -0.009
occ_350 ( medical and health services managers ) : 0.121
occ_420 ( social and community service managers ) : 0.023
occ_500 ( agents and business managers of artists, performers, and athletes ) : 0.347
occ_565 (  ) : 0.104
occ_600 ( cost estimators ) : 0.257
occ_630 (  ) : 0.004
occ_640 (  ) : 0.029
occ_650 (  ) : 0.054
occ_725 (  ) : 0.073
occ_735 (  ) : 0.183
occ_810 ( appraisers and assessors of real estate ) : 0.071
occ_830 ( credit analysts ) : 0.067
occ_850 ( personal financial advisors ) : 0.095
occ_860 ( insurance underwriters ) : 0.023
occ_940 ( tax preparers ) : -0.151
occ_950 ( financial specialists, nec ) : 0.038
occ_1005 (  ) : 0.056
occ_1010 ( computer programmers ) : 0.007
occ_1020 ( software developers, applications and systems software ) : 0.065
occ_1060 ( database administrators ) : 0.212
occ_1105 (  ) : 0.105
occ_1240 ( mathematical science occupations, nec ) : 0.031
occ_1320 ( aerospace engineers ) : 0.104
occ_1330 (  ) : 0.092
occ_1350 ( chemical engineers ) : 0.183
occ_1430 ( industrial engineers, including health and safety ) : 0.074
occ_1460 ( mechanical engineers ) : 0.168
occ_1520 ( petroleum, mining and geological engineers, including mining safety engineers ) : 0.311
occ_1530 ( engineers, nec ) : 0.018
occ_1540 ( drafters ) : 0.018
occ_1560 ( surveying and mapping technicians ) : -0.001
occ_1660 (  ) : 0.213
occ_1700 ( astronomers and physicists ) : 0.094
occ_1720 ( chemists and materials scientists ) : 0.088
occ_1800 ( economists and market researchers ) : 0.251
occ_1820 ( psychologists ) : 0.054
occ_1860 (  ) : -0.012
occ_1910 ( biological technicians ) : -0.106
occ_1930 ( geological and petroleum technicians, and nuclear technicians ) : -0.176
occ_1965 (  ) : -0.011
occ_2000 ( counselors ) : -0.005
occ_2060 ( religious workers, nec ) : -0.414
occ_2100 ( lawyers, and judges, magistrates, and other judicial workers ) : 0.067
occ_2160 (  ) : -0.015
occ_2200 ( postsecondary teachers ) : 0.045
occ_2300 ( preschool and kindergarten teachers ) : -0.019
occ_2430 ( librarians ) : -0.024
occ_2440 ( library technicians ) : -0.309
occ_2540 ( teacher assistants ) : -0.046
occ_2710 (  ) : 0.102
occ_2720 ( athletes, coaches, umpires, and related workers ) : 0.031
occ_2750 ( musicians, singers, and related workers ) : -0.255
occ_2760 ( entertainers and performers, sports and related workers, all other ) : 0.029
occ_2825 ( public relations specialists ) : 0.092
occ_2830 (  ) : 0.017
occ_2960 (  ) : -0.700
occ_3000 ( chiropractors ) : -0.002
occ_3010 ( dentists ) : 0.210
occ_3060 ( physicians and surgeons ) : 0.192
occ_3110 ( physician assistants ) : 0.094
occ_3160 ( physical therapists ) : 0.044
occ_3200 ( radiation therapists ) : 0.109
occ_3230 ( speech language pathologists ) : 0.103
occ_3235 (  ) : -0.951
occ_3255 (  ) : 0.152
occ_3257 (  ) : 0.124
occ_3420 (  ) : -0.089
occ_3600 ( nursing, psychiatric, and home health aides ) : -0.010
occ_3620 ( physical therapist assistants and aides ) : 0.038
occ_3645 (  ) : -0.034
occ_3700 ( first-line supervisors of correctional officers ) : 0.006
occ_3740 ( firefighters ) : 0.060
occ_3800 ( sheriffs, bailiffs, correctional officers, and jailers ) : -0.028
occ_3850 (  ) : 0.059
occ_3860 (  ) : 0.209
occ_3900 ( animal control ) : -0.115
occ_3940 ( crossing guards ) : -0.031
occ_4000 ( chefs and cooks ) : -0.037
occ_4020 (  ) : -0.075
occ_4040 ( bartenders ) : -0.212
occ_4050 ( combined food preparation and serving workers, including fast food ) : -0.177
occ_4060 ( counter attendant, cafeteria, food concession, and coffee shop ) : -0.258
occ_4120 ( food servers, nonrestaurant ) : -0.087
occ_4140 ( dishwashers ) : -0.212
occ_4220 ( janitors and building cleaners ) : -0.033
occ_4230 ( maids and housekeeping cleaners ) : -0.061
occ_4250 ( grounds maintenance workers ) : -0.037
occ_4350 ( nonfarm animal caretakers ) : -0.122
occ_4430 ( entertainment attendants and related workers, nec ) : -0.187
occ_4460 ( funeral service workers and embalmers ) : -0.203
occ_4530 ( baggage porters, bellhops, and concierges ) : -0.033
occ_4540 ( tour and travel guides ) : 0.128
occ_4600 ( childcare workers ) : -0.244
occ_4610 ( personal care aides ) : -0.054
occ_4640 ( residential advisors ) : -0.063
occ_4700 ( first-line supervisors of sales workers ) : 0.009
occ_4720 ( cashiers ) : -0.034
occ_4760 ( retail salespersons ) : -0.012
occ_4840 ( sales representatives, services, all other ) : 0.005
occ_4850 ( sales representatives, wholesale and manufacturing ) : 0.111
occ_4900 ( models, demonstrators, and product promoters ) : -0.146
occ_4920 ( real estate brokers and sales agents ) : 0.168
occ_4950 ( door-to-door sales workers, news and street vendors, and related workers ) : -0.208
occ_5000 ( first-line supervisors of office and administrative support workers ) : 0.026
occ_5010 ( switchboard operators, including answering service ) : -0.133
occ_5110 ( billing and posting clerks ) : -0.086
occ_5120 ( bookkeeping, accounting, and auditing clerks ) : -0.083
occ_5160 ( bank tellers ) : -0.046
occ_5220 ( court, municipal, and license clerks ) : -0.099
occ_5310 ( interviewers, except eligibility and loan ) : -0.046
occ_5360 ( human resources assistants, except payroll and timekeeping ) : -0.025
occ_5400 ( receptionists and information clerks ) : -0.058
occ_5530 ( meter readers, utilities ) : -0.059
occ_5540 ( postal service clerks ) : -0.022
occ_5610 ( shipping, receiving, and traffic clerks ) : -0.173
occ_5820 ( word processors and typists ) : -0.181
occ_5840 ( insurance claims and policy processing clerks ) : -0.050
occ_5920 ( statistical assistants ) : -0.027
occ_5940 ( office and administrative support workers, nec ) : -0.054
occ_6220 ( brickmasons, blockmasons, and stonemasons ) : -0.034
occ_6260 ( construction laborers ) : -0.072
occ_6320 ( construction equipment operators except paving, surfacing, and tamping equipment operators ) : 0.066
occ_6330 ( drywall installers, ceiling tile installers, and tapers ) : -0.119
occ_6500 ( reinforcing iron and rebar workers ) : -0.178
occ_6730 ( highway maintenance workers ) : -0.062
occ_6750 (  ) : -0.306
occ_6800 ( derrick, rotary drill, and service unit operators, and roustabouts, oil, gas, and mining ) : 0.016
occ_6840 ( mining machine operators ) : 0.012
occ_6910 (  ) : -0.113
occ_6920 (  ) : -0.096
occ_7000 ( first-line supervisors of mechanics, installers, and repairers ) : 0.078
occ_7130 ( security and fire alarm systems installers ) : 0.087
occ_7140 ( aircraft mechanics and service technicians ) : 0.002
occ_7150 ( automotive body and related repairers ) : 0.002
occ_7260 ( vehicle and mobile equipment mechanics, installers, and repairers, nec ) : -0.160
occ_7360 ( millwrights ) : 0.038
occ_7410 ( electrical power-line installers and repairers ) : 0.078
occ_7440 (  ) : -0.216
occ_7510 ( coin, vending, and amusement machine servicers and repairers ) : -0.132
occ_7560 ( riggers ) : 0.000
occ_7630 ( other installation, maintenance, and repair workers including wind turbine service technicians, and commercial divers, and signal and track switch repairers ) : -0.003
occ_7700 ( first-line supervisors of production and operating workers ) : 0.064
occ_7710 ( aircraft structure, surfaces, rigging, and systems assemblers ) : -0.016
occ_7720 ( electrical, electronics, and electromechanical assemblers ) : -0.002
occ_7750 ( assemblers and fabricators, nec ) : -0.048
occ_7800 ( bakers ) : -0.135
occ_7855 ( food processing, nec ) : -0.028
occ_8000 ( grinding, lapping, polishing, and buffing machine tool setters, operators, and tenders, metal and plastic ) : -0.133
occ_8100 ( molders and molding machine setters, operators, and tenders, metal and plastic ) : -0.071
occ_8250 ( prepress technicians and workers ) : 0.032
occ_8255 (  ) : -0.138
occ_8300 ( laundry and dry-cleaning workers ) : -0.023
occ_8330 ( shoe and leather workers and repairers ) : -0.231
occ_8350 ( tailors, dressmakers, and sewers ) : -0.125
occ_8440 (  ) : 0.905
occ_8550 ( woodworkers including model makers and patternmakers, nec ) : -0.136
occ_8620 ( water wastewater treatment plant and system operators ) : 0.008
occ_8630 ( plant and system operators, nec ) : 0.135
occ_8650 ( crushing, grinding, polishing, mixing, and blending workers ) : -0.084
occ_8710 ( cutting workers ) : -0.003
occ_8740 ( inspectors, testers, sorters, samplers, and weighers ) : -0.033
occ_8760 ( medical, dental, and ophthalmic laboratory technicians ) : -0.101
occ_8800 ( packaging and filling machine operators and tenders ) : -0.035
occ_8810 ( painting workers and dyers ) : -0.063
occ_8830 ( photographic process workers and processing machine operators ) : -0.046
occ_8930 ( paper goods machine setters, operators, and tenders ) : 0.002
occ_8950 ( helpers--production workers ) : -0.088
occ_8965 ( other production workers including semiconductor processors and cooling and freezing equipment operators ) : -0.097
occ_9110 (  ) : -0.382
occ_9120 (  ) : -0.239
occ_9150 ( motor vehicle operators, all other ) : -0.168
occ_9200 ( locomotive engineers and operators ) : 0.117
occ_9240 ( railroad conductors and yardmasters ) : 0.108
occ_9330 (  ) : 0.169
occ_9350 ( parking lot attendants ) : -0.102
occ_9600 ( industrial truck and tractor operators ) : -0.117
occ_9620 ( laborers and freight, stock, and material movers, hand ) : -0.081
occ_9640 ( packers and packagers, hand ) : -0.315
occ_9720 ( refuse and recyclable material collectors ) : -0.062
occ_9730 (  ) : 0.000
occ_9840 (  ) : -0.259
ind_0 (  ) : -0.027
ind_280 (  ) : 0.075
ind_370 (  ) : 0.035
ind_380 (  ) : 0.105
ind_390 (  ) : 0.019
ind_470 (  ) : 0.117
ind_570 (  ) : 0.041
ind_580 (  ) : 0.136
ind_680 (  ) : 0.022
ind_690 (  ) : 0.146
ind_1190 (  ) : -0.032
ind_1480 (  ) : -0.121
ind_1670 (  ) : -0.038
ind_1680 (  ) : -0.085
ind_1790 (  ) : 0.092
ind_1870 (  ) : 0.024
ind_1880 (  ) : -0.012
ind_2290 (  ) : 0.010
ind_2390 (  ) : 0.058
ind_2470 (  ) : -0.054
ind_2670 (  ) : 0.085
ind_2680 (  ) : 0.029
ind_2790 (  ) : -0.070
ind_3090 (  ) : 0.011
ind_3170 (  ) : 0.116
ind_3360 (  ) : 0.038
ind_3380 (  ) : 0.010
ind_3390 (  ) : 0.033
ind_3570 (  ) : 0.042
ind_3580 (  ) : 0.009
ind_3670 (  ) : 0.021
ind_3690 (  ) : -0.004
ind_3970 (  ) : 0.004
ind_4090 (  ) : 0.027
ind_4170 (  ) : 0.097
ind_4190 (  ) : 0.001
ind_4380 (  ) : 0.066
ind_4470 (  ) : 0.007
ind_4670 (  ) : 0.044
ind_4770 (  ) : -0.005
ind_4870 (  ) : -0.036
ind_4880 (  ) : -0.069
ind_4990 (  ) : -0.115
ind_5070 (  ) : -0.029
ind_5190 (  ) : -0.059
ind_5380 (  ) : -0.017
ind_5590 (  ) : 0.055
ind_5690 (  ) : -0.044
ind_6080 (  ) : 0.149
ind_6270 (  ) : 0.124
ind_6480 (  ) : 0.021
ind_6490 (  ) : 0.110
ind_6570 (  ) : 0.043
ind_6670 (  ) : 0.002
ind_6680 (  ) : 0.004
ind_6970 (  ) : 0.070
ind_6990 (  ) : 0.033
ind_7080 (  ) : -0.029
ind_7190 (  ) : 0.110
ind_7380 (  ) : 0.035
ind_7470 (  ) : 0.023
ind_7570 (  ) : 0.031
ind_7680 (  ) : -0.011
ind_7770 (  ) : -0.050
ind_7860 (  ) : -0.011
ind_7890 (  ) : -0.080
ind_7980 (  ) : 0.006
ind_8170 (  ) : -0.044
ind_8190 (  ) : 0.028
ind_8370 (  ) : -0.038
ind_8380 (  ) : -0.018
ind_8470 (  ) : -0.037
ind_8570 (  ) : -0.021
ind_8580 (  ) : -0.241
ind_8590 (  ) : -0.053
ind_8660 (  ) : -0.025
ind_8670 (  ) : -0.051
ind_8870 (  ) : 0.051
ind_8880 (  ) : -0.046
ind_8980 (  ) : -0.030
ind_9090 (  ) : -0.089
ind_9290 (  ) : -0.040
ind_9370 (  ) : -0.006
ind_9890 (  ) : -0.004
educ_10 ( grades 1, 2, 3, or 4 ) : -0.051
educ_20 ( grades 5 or 6 ) : -0.026
educ_30 ( grades 7 or 8 ) : -0.006
educ_71 ( 12th grade, no diploma ) : 0.009
educ_73 ( high school diploma or equivalent ) : -0.000
educ_81 ( some college but no degree ) : -0.005
educ_91 ( associate's degree, occupational/vocational program ) : 0.006
educ_111 ( bachelor's degree ) : 0.079
educ_124 ( professional school degree ) : 0.017
educ_125 ( doctorate degree ) : 0.106
occly_10 ( chief executives and legislators/public administration ) : 0.525
occly_20 ( general and operations managers ) : 0.289
occly_40 (  ) : 0.284
occly_50 (  ) : 0.367
occly_60 (  ) : 0.214
occly_100 ( administrative services managers ) : 0.061
occly_110 ( computer and information systems managers ) : 0.403
occly_120 ( financial managers ) : 0.272
occly_136 (  ) : 0.163
occly_137 (  ) : 0.085
occly_140 ( industrial production managers ) : 0.271
occly_150 ( purchasing managers ) : 0.140
occly_160 ( transportation, storage, and distribution managers ) : 0.055
occly_205 ( farmers, ranchers, and other agricultural managers ) : -0.035
occly_220 ( constructions managers ) : 0.258
occly_230 ( education administrators ) : 0.224
occly_300 ( architectural and engineering managers ) : 0.386
occly_310 ( food service and lodging managers ) : 0.027
occly_350 ( medical and health services managers ) : 0.155
occly_360 ( natural science managers ) : 0.073
occly_410 ( property, real estate, and community association managers ) : 0.130
occly_420 ( social and community service managers ) : 0.054
occly_430 ( managers, nec (including postmasters) ) : 0.245
occly_520 ( wholesale and retail buyers, except farm products ) : 0.038
occly_630 (  ) : 0.148
occly_710 ( management analysts ) : 0.173
occly_726 (  ) : 0.044
occly_740 (  ) : 0.037
occly_800 ( accountants and auditors ) : 0.148
occly_820 ( budget analysts ) : 0.092
occly_840 ( financial analysts ) : 0.232
occly_850 ( personal financial advisors ) : 0.090
occly_910 ( credit counselors and loan officers ) : 0.047
occly_940 ( tax preparers ) : -0.164
occly_1006 (  ) : 0.270
occly_1010 ( computer programmers ) : 0.185
occly_1020 ( software developers, applications and systems software ) : 0.266
occly_1030 (  ) : 0.061
occly_1106 (  ) : 0.377
occly_1107 (  ) : 0.090
occly_1200 ( actuaries ) : 0.605
occly_1220 ( operations research analysts ) : 0.099
occly_1300 ( architects, except naval ) : 0.107
occly_1320 ( aerospace engineers ) : 0.224
occly_1360 ( civil engineers ) : 0.227
occly_1400 ( computer hardware engineers ) : 0.193
occly_1410 ( electrical and electronics engineers ) : 0.250
occly_1420 ( environmental engineers ) : 0.178
occly_1430 ( industrial engineers, including health and safety ) : 0.027
occly_1440 ( marine engineers and naval architects ) : 0.310
occly_1500 (  ) : 0.282
occly_1530 ( engineers, nec ) : 0.260
occly_1550 ( engineering technicians, except drafters ) : 0.001
occly_1560 ( surveying and mapping technicians ) : -0.007
occly_1660 (  ) : 0.038
occly_1700 ( astronomers and physicists ) : 0.036
occly_1710 ( atmospheric and space scientists ) : -0.100
occly_1800 ( economists and market researchers ) : 0.058
occly_1860 (  ) : -0.124
occly_1930 ( geological and petroleum technicians, and nuclear technicians ) : -0.000
occly_1965 (  ) : -0.076
occly_2000 ( counselors ) : -0.001
occly_2016 (  ) : -0.015
occly_2025 (  ) : -0.017
occly_2060 ( religious workers, nec ) : -0.070
occly_2100 ( lawyers, and judges, magistrates, and other judicial workers ) : 0.279
occly_2300 ( preschool and kindergarten teachers ) : -0.018
occly_2320 ( secondary school teachers ) : 0.061
occly_2330 ( special education teachers ) : 0.037
occly_2340 ( other teachers and instructors ) : -0.196
occly_2430 ( librarians ) : -0.019
occly_2540 ( teacher assistants ) : -0.409
occly_2550 ( education, training, and library workers, nec ) : -0.010
occly_2630 ( designers ) : -0.001
occly_2700 ( actors, producers, and directors ) : 0.062
occly_2720 ( athletes, coaches, umpires, and related workers ) : -0.210
occly_2740 ( dancers and choreographers ) : -0.384
occly_2760 ( entertainers and performers, sports and related workers, all other ) : 0.162
occly_2800 ( announcers ) : 0.224
occly_2825 ( public relations specialists ) : 0.128
occly_2840 ( technical writers ) : 0.072
occly_2850 ( writers and authors ) : 0.183
occly_2910 ( photographers ) : -0.122
occly_2960 (  ) : -0.135
occly_3000 ( chiropractors ) : -0.157
occly_3010 ( dentists ) : 0.318
occly_3030 ( dieticians and nutritionists ) : -0.035
occly_3040 ( optometrists ) : 0.139
occly_3050 ( pharmacists ) : 0.545
occly_3060 ( physicians and surgeons ) : 0.374
occly_3110 ( physician assistants ) : 0.103
occly_3120 ( podiatrists ) : 0.780
occly_3150 ( occupational therapists ) : 0.152
occly_3160 ( physical therapists ) : 0.075
occly_3200 ( radiation therapists ) : 0.082
occly_3220 ( respiratory therapists ) : 0.106
occly_3230 ( speech language pathologists ) : 0.023
occly_3235 (  ) : -0.055
occly_3250 ( veterinarians ) : 0.332
occly_3255 (  ) : 0.082
occly_3256 (  ) : 0.628
occly_3257 (  ) : 0.045
occly_3258 (  ) : 0.317
occly_3310 ( dental hygienists ) : 0.189
occly_3320 ( diagnostic related technologists and technicians ) : 0.161
occly_3420 (  ) : -0.002
occly_3500 ( licensed practical and licensed vocational nurses ) : 0.037
occly_3510 ( medical records and health information technicians ) : -0.202
occly_3600 ( nursing, psychiatric, and home health aides ) : -0.256
occly_3610 ( occupational therapy assistants and aides ) : 0.188
occly_3630 ( massage therapists ) : -0.152
occly_3645 (  ) : -0.197
occly_3647 (  ) : -0.152
occly_3649 (  ) : -0.173
occly_3655 (  ) : -0.278
occly_3710 ( first-line supervisors of police and detectives ) : 0.169
occly_3720 ( first-line supervisors of fire fighting and prevention workers ) : 0.217
occly_3820 ( police officers and detectives ) : 0.153
occly_3840 (  ) : -0.257
occly_3850 (  ) : 0.060
occly_3860 (  ) : 0.121
occly_3900 ( animal control ) : 0.657
occly_3930 ( security guards and gaming surveillance officers ) : -0.240
occly_3940 ( crossing guards ) : -0.998
occly_3955 (  ) : -0.486
occly_4010 ( first-line supervisors of food preparation and serving workers ) : -0.085
occly_4020 (  ) : -0.264
occly_4030 ( food preparation workers ) : -0.403
occly_4050 ( combined food preparation and serving workers, including fast food ) : -0.322
occly_4060 ( counter attendant, cafeteria, food concession, and coffee shop ) : -0.259
occly_4110 ( waiters and waitresses ) : -0.338
occly_4120 ( food servers, nonrestaurant ) : -0.386
occly_4130 ( food preparation and serving related workers, nec ) : -0.337
occly_4140 ( dishwashers ) : -0.438
occly_4150 ( host and hostesses, restaurant, lounge, and coffee shop ) : -0.551
occly_4200 ( first-line supervisors of housekeeping and janitorial workers ) : -0.044
occly_4220 ( janitors and building cleaners ) : -0.273
occly_4230 ( maids and housekeeping cleaners ) : -0.339
occly_4250 ( grounds maintenance workers ) : -0.210
occly_4300 ( first-line supervisors of gaming workers ) : 0.119
occly_4350 ( nonfarm animal caretakers ) : -0.057
occly_4430 ( entertainment attendants and related workers, nec ) : -0.192
occly_4520 ( personal appearance workers, nec ) : -0.253
occly_4530 ( baggage porters, bellhops, and concierges ) : -0.318
occly_4540 ( tour and travel guides ) : -1.098
occly_4600 ( childcare workers ) : -0.094
occly_4610 ( personal care aides ) : -0.339
occly_4620 ( recreation and fitness workers ) : -0.365
occly_4650 ( personal care and service workers, all other ) : -0.261
occly_4700 ( first-line supervisors of sales workers ) : 0.077
occly_4710 (  ) : 0.175
occly_4720 ( cashiers ) : -0.386
occly_4760 ( retail salespersons ) : -0.229
occly_4800 ( advertising sales agents ) : 0.043
occly_4810 ( insurance sales agents ) : 0.008
occly_4820 ( securities, commodities, and financial services sales agents ) : 0.076
occly_4840 ( sales representatives, services, all other ) : 0.018
occly_4850 ( sales representatives, wholesale and manufacturing ) : 0.066
occly_4900 ( models, demonstrators, and product promoters ) : -0.277
occly_4920 ( real estate brokers and sales agents ) : 0.017
occly_4930 ( sales engineers ) : 0.191
occly_4940 ( telemarketers ) : -0.424
occly_4950 ( door-to-door sales workers, news and street vendors, and related workers ) : -0.214
occly_5000 ( first-line supervisors of office and administrative support workers ) : 0.040
occly_5010 ( switchboard operators, including answering service ) : -0.204
occly_5100 ( bill and account collectors ) : -0.086
occly_5110 ( billing and posting clerks ) : -0.002
occly_5160 ( bank tellers ) : -0.262
occly_5240 ( customer service representatives ) : -0.142
occly_5260 ( file clerks ) : -0.170
occly_5300 ( hotel, motel, and resort desk clerks ) : -0.189
occly_5310 ( interviewers, except eligibility and loan ) : -0.184
occly_5320 ( library assistants, clerical ) : -0.592
occly_5340 ( new account clerks ) : -0.117
occly_5350 ( correspondent clerks and order clerks ) : -0.090
occly_5400 ( receptionists and information clerks ) : -0.182
occly_5410 ( reservation and transportation ticket agents and travel clerks ) : -0.079
occly_5420 ( information and record clerks, all other ) : -0.172
occly_5510 ( couriers and messengers ) : -0.073
occly_5560 ( postal service mail sorters, processors, and processing machine operators ) : -0.227
occly_5610 ( shipping, receiving, and traffic clerks ) : -0.024
occly_5620 ( stock clerks and order fillers ) : -0.343
occly_5630 ( weighers, measurers, checkers, and samplers, recordkeeping ) : -0.091
occly_5700 ( secretaries and administrative assistants ) : -0.064
occly_5810 ( data entry keyers ) : -0.191
occly_5840 ( insurance claims and policy processing clerks ) : -0.066
occly_5850 ( mail clerks and mail machine operators, except postal service ) : -0.463
occly_5860 ( office clerks, general ) : -0.209
occly_6005 ( first-line supervisors of farming, fishing, and forestry workers ) : 0.016
occly_6040 ( graders and sorters, agricultural products ) : -0.281
occly_6050 ( agricultural workers, nec ) : -0.153
occly_6100 ( fishing and hunting workers ) : 0.189
occly_6200 ( first-line supervisors of construction trades and extraction workers ) : 0.216
occly_6210 ( boilermakers ) : -0.136
occly_6230 ( carpenters ) : -0.083
occly_6240 ( carpet, floor, and tile installers and finishers ) : -0.049
occly_6250 ( cement masons, concrete finishers, and terrazzo workers ) : -0.034
occly_6260 ( construction laborers ) : -0.080
occly_6300 ( paving, surfacing, and tamping equipment operators ) : 0.084
occly_6320 ( construction equipment operators except paving, surfacing, and tamping equipment operators ) : 0.002
occly_6355 ( electricians ) : 0.078
occly_6420 ( painters, construction and maintenance ) : -0.273
occly_6440 ( pipelayers, plumbers, pipefitters, and steamfitters ) : 0.040
occly_6460 ( plasterers and stucco masons ) : -0.206
occly_6515 ( roofers ) : -0.086
occly_6520 ( sheet metal workers, metal-working ) : -0.005
occly_6600 ( helpers, construction trades ) : -0.248
occly_6700 ( elevator installers and repairers ) : 0.125
occly_6710 ( fence erectors ) : -0.403
occly_6800 ( derrick, rotary drill, and service unit operators, and roustabouts, oil, gas, and mining ) : 0.316
occly_6820 ( earth drillers, except oil and gas ) : 0.231
occly_6940 ( extraction workers, nec ) : 0.069
occly_7010 ( computer, automated teller, and office machine repairers ) : -0.045
occly_7100 ( electrical and electronics repairers, transportation equipment, and industrial and utility ) : 0.056
occly_7130 ( security and fire alarm systems installers ) : 0.036
occly_7140 ( aircraft mechanics and service technicians ) : 0.052
occly_7160 ( automotive glass installers and repairers ) : -0.146
occly_7200 ( automotive service technicians and mechanics ) : -0.017
occly_7220 ( heavy vehicle and mobile equipment service technicians and mechanics ) : 0.066
occly_7340 ( maintenance and repair workers, general ) : -0.001
occly_7360 ( millwrights ) : 0.104
occly_7420 ( telecommunications line installers and repairers ) : 0.059
occly_7510 ( coin, vending, and amusement machine servicers and repairers ) : -0.028
occly_7560 ( riggers ) : 0.033
occly_7600 (  ) : 0.017
occly_7610 ( helpers--installation, maintenance, and repair workers ) : -0.428
occly_7700 ( first-line supervisors of production and operating workers ) : 0.038
occly_7710 ( aircraft structure, surfaces, rigging, and systems assemblers ) : -0.154
occly_7720 ( electrical, electronics, and electromechanical assemblers ) : -0.130
occly_7730 ( engine and other machine assemblers ) : -0.089
occly_7750 ( assemblers and fabricators, nec ) : -0.159
occly_7800 ( bakers ) : -0.215
occly_7810 ( butchers and other meat, poultry, and fish processing workers ) : -0.123
occly_7830 ( food and tobacco roasting, baking, and drying machine operators and tenders ) : -0.109
occly_7840 ( food batchmakers ) : -0.296
occly_7855 ( food processing, nec ) : -0.038
occly_7950 ( cutting, punching, and press machine setters, operators, and tenders, metal and plastic ) : -0.166
occly_8000 ( grinding, lapping, polishing, and buffing machine tool setters, operators, and tenders, metal and plastic ) : -0.069
occly_8220 ( metal workers and plastic workers, nec ) : -0.085
occly_8300 ( laundry and dry-cleaning workers ) : -0.166
occly_8310 ( pressers, textile, garment, and related materials ) : -0.393
occly_8320 ( sewing machine operators ) : -0.289
occly_8340 ( shoe machine operators and tenders ) : -0.027
occly_8400 ( textile bleaching and dyeing, and cutting machine setters, operators, and tenders ) : -0.090
occly_8410 ( textile knitting and weaving machine setters, operators, and tenders ) : -0.311
occly_8440 (  ) : 0.095
occly_8460 ( textile, apparel, and furnishings workers, nec ) : -0.085
occly_8500 ( cabinetmakers and bench carpenters ) : -0.003
occly_8510 ( furniture finishers ) : -0.220
occly_8600 ( power plant operators, distributors, and dispatchers ) : 0.302
occly_8630 ( plant and system operators, nec ) : 0.102
occly_8710 ( cutting workers ) : -0.180
occly_8740 ( inspectors, testers, sorters, samplers, and weighers ) : -0.020
occly_8800 ( packaging and filling machine operators and tenders ) : -0.137
occly_8830 ( photographic process workers and processing machine operators ) : -0.010
occly_8850 ( adhesive bonding machine operators and tenders ) : -0.047
occly_8910 ( etchers, engravers, and lithographers ) : -0.454
occly_8920 ( molders, shapers, and casters, except metal and plastic ) : 0.046
occly_8965 ( other production workers including semiconductor processors and cooling and freezing equipment operators ) : -0.088
occly_9030 ( aircraft pilots and flight engineers ) : 0.579
occly_9040 ( air traffic controllers and airfield operations specialists ) : 0.379
occly_9110 (  ) : -0.016
occly_9130 ( driver/sales workers and truck drivers ) : -0.038
occly_9140 ( taxi drivers and chauffeurs ) : -0.305
occly_9200 ( locomotive engineers and operators ) : 0.035
occly_9310 ( ship and boat captains and operators ) : 0.318
occly_9330 (  ) : 0.000
occly_9350 ( parking lot attendants ) : -0.311
occly_9360 ( automotive and watercraft service attendants ) : -0.275
occly_9415 (  ) : -0.309
occly_9510 ( crane and tower operators ) : 0.047
occly_9600 ( industrial truck and tractor operators ) : -0.034
occly_9610 ( cleaners of vehicles and equipment ) : -0.361
occly_9620 ( laborers and freight, stock, and material movers, hand ) : -0.239
occly_9630 ( machine feeders and offbearers ) : -0.106
occly_9640 ( packers and packagers, hand ) : -0.094
occly_9730 (  ) : 0.168
occly_9750 ( material moving workers, nec ) : -0.168
occly_9840 (  ) : 0.196
indly_170 (  ) : -0.035
indly_280 ( other primary metal industries ) : 0.076
indly_290 ( screw machine products ) : -0.016
indly_370 ( cycles and miscellaneous transportation equipment ) : 0.204
indly_380 ( photographic equipment and supplies ) : 0.250
indly_390 ( toys, amusement, and sporting goods ) : 0.322
indly_480 (  ) : 0.024
indly_490 (  ) : 0.419
indly_570 (  ) : 0.179
indly_590 ( mobile home dealers ) : 0.261
indly_670 ( vending machine operators ) : 0.063
indly_1090 (  ) : 0.008
indly_1170 (  ) : 0.099
indly_1190 (  ) : -0.010
indly_1270 (  ) : -0.026
indly_1290 (  ) : -0.031
indly_1480 (  ) : -0.075
indly_1670 (  ) : -0.584
indly_1680 (  ) : -0.112
indly_1690 (  ) : 0.301
indly_1870 (  ) : 0.152
indly_1890 (  ) : 0.061
indly_2070 (  ) : 0.296
indly_2090 (  ) : 0.219
indly_2190 (  ) : 0.256
indly_2280 (  ) : 0.113
indly_2290 (  ) : 0.090
indly_2490 (  ) : 0.048
indly_2590 (  ) : -0.096
indly_2780 (  ) : -0.292
indly_2790 (  ) : 0.085
indly_2880 (  ) : 0.041
indly_2970 (  ) : 0.036
indly_3080 (  ) : 0.014
indly_3190 (  ) : 0.045
indly_3360 (  ) : 0.070
indly_3380 (  ) : 0.125
indly_3390 (  ) : 0.096
indly_3490 (  ) : 0.051
indly_3570 (  ) : 0.045
indly_3580 (  ) : 0.056
indly_3590 (  ) : 0.071
indly_3680 (  ) : 0.028
indly_3870 (  ) : -0.119
indly_3890 (  ) : -0.012
indly_3970 (  ) : 0.088
indly_3980 (  ) : -0.045
indly_4080 (  ) : 0.016
indly_4180 (  ) : 0.068
indly_4270 (  ) : 0.060
indly_4380 (  ) : 0.134
indly_4390 (  ) : 0.009
indly_4480 (  ) : 0.014
indly_4490 (  ) : 0.142
indly_4560 (  ) : 0.002
indly_4585 (  ) : 0.064
indly_4590 (  ) : -0.225
indly_4670 (  ) : 0.126
indly_4690 (  ) : -0.066
indly_4770 (  ) : 0.017
indly_4780 (  ) : -0.016
indly_4790 (  ) : 0.110
indly_4880 (  ) : -0.144
indly_4970 (  ) : -0.148
indly_4980 (  ) : -0.117
indly_5070 (  ) : -0.010
indly_5090 (  ) : -0.041
indly_5170 (  ) : -0.158
indly_5180 (  ) : -0.227
indly_5270 (  ) : -0.274
indly_5280 (  ) : -0.097
indly_5290 (  ) : -0.112
indly_5370 (  ) : -0.409
indly_5380 (  ) : -0.230
indly_5390 (  ) : -0.148
indly_5470 (  ) : -0.247
indly_5490 (  ) : -0.340
indly_5570 (  ) : -0.244
indly_5580 (  ) : -0.062
indly_5670 (  ) : -0.209
indly_5690 (  ) : -0.083
indly_6070 (  ) : 0.004
indly_6090 (  ) : 0.130
indly_6170 (  ) : 0.110
indly_6180 (  ) : -0.049
indly_6190 (  ) : -0.200
indly_6280 (  ) : 0.128
indly_6290 (  ) : 0.023
indly_6380 (  ) : -0.038
indly_6470 (  ) : -0.160
indly_6672 (  ) : 0.279
indly_6680 (  ) : 0.134
indly_6690 (  ) : 0.049
indly_6695 (  ) : 0.054
indly_6770 (  ) : -0.081
indly_6970 (  ) : 0.078
indly_6990 (  ) : 0.062
indly_7070 (  ) : 0.017
indly_7170 (  ) : -0.172
indly_7190 (  ) : 0.059
indly_7270 (  ) : 0.138
indly_7290 (  ) : 0.121
indly_7370 (  ) : 0.024
indly_7380 (  ) : 0.131
indly_7390 (  ) : 0.116
indly_7460 (  ) : 0.077
indly_7470 (  ) : 0.116
indly_7490 (  ) : -0.025
indly_7570 (  ) : 0.012
indly_7580 (  ) : -0.403
indly_7590 (  ) : -0.057
indly_7680 (  ) : -0.085
indly_7690 (  ) : -0.089
indly_7860 (  ) : -0.103
indly_7870 (  ) : -0.115
indly_7880 (  ) : -0.057
indly_7970 (  ) : 0.053
indly_7980 (  ) : 0.012
indly_8170 (  ) : -0.107
indly_8180 (  ) : 0.027
indly_8270 (  ) : -0.023
indly_8370 (  ) : -0.108
indly_8380 (  ) : -0.057
indly_8390 (  ) : -0.357
indly_8470 (  ) : -0.202
indly_8560 (  ) : -0.092
indly_8570 (  ) : -0.095
indly_8660 (  ) : -0.069
indly_8670 (  ) : -0.151
indly_8680 (  ) : -0.129
indly_8690 (  ) : -0.070
indly_8770 (  ) : -0.010
indly_8780 (  ) : -0.125
indly_8870 (  ) : 0.051
indly_8880 (  ) : -0.023
indly_8890 (  ) : -1.269
indly_8980 (  ) : -0.057
indly_9070 (  ) : -0.030
indly_9160 (  ) : -0.245
indly_9170 (  ) : -0.067
indly_9290 (  ) : -0.011
indly_9370 (  ) : -0.014
indly_9380 (  ) : -0.004
indly_9470 (  ) : 0.062
indly_9480 (  ) : -0.025
indly_9590 (  ) : 0.035
indly_9890 (  ) : 0.000
classwly_13 ( self-employed, not incorporated ) : -1.106
classwly_14 ( self-employed, incorporated ) : 0.221
classwly_25 ( federal government employee ) : 0.128
classwly_27 ( state government employee ) : -0.093
classwly_28 ( local government employee ) : -0.020
pension_at_w_ly_2 ( pension plan at work, but not included ) : -0.031
pension_at_w_ly_3 ( included in pension plan at work ) : 0.313
firmsize_ly_1 ( under 10 ) : -0.212
firmsize_ly_4 ( 10 to 49 ) : -0.073
firmsize_ly_6 ( 50 to 99 ) : -0.011
firmsize_ly_8 ( 500 to 999 ) : 0.020
firmsize_ly_9 ( 1000+ ) : 0.035
actnlfly_0 ( niu ) : 0.389
actnlfly_10 ( ill or disabled ) : -0.006
actnlfly_20 ( taking care of home/family ) : -0.339
actnlfly_30 ( going to school ) : -0.481
actnlfly_40 ( retired ) : -0.222
actnlfly_50 ( other ) : 0.128
spmmort_1 ( owners with a mortgage ) : 0.068
statefip_2 ( alaska ) : 0.123
statefip_5 ( arkansas ) : -0.012
statefip_6 ( california ) : 0.049
statefip_9 ( connecticut ) : 0.076
statefip_11 ( district of columbia ) : 0.031
statefip_15 ( hawaii ) : 0.062
statefip_16 ( idaho ) : -0.044
statefip_20 ( kansas ) : -0.057
statefip_21 ( kentucky ) : -0.005
statefip_23 ( maine ) : -0.069
statefip_25 ( massachusetts ) : 0.042
statefip_29 ( missouri ) : -0.056
statefip_30 ( montana ) : -0.018
statefip_31 ( nebraska ) : 0.002
statefip_32 ( nevada ) : 0.037
statefip_33 ( new hampshire ) : 0.025
statefip_35 ( new mexico ) : -0.031
statefip_37 ( north carolina ) : -0.006
statefip_40 ( oklahoma ) : -0.015
statefip_41 ( oregon ) : -0.013
statefip_42 ( pennsylvania ) : -0.003
statefip_44 ( rhode island ) : 0.024
statefip_45 ( south carolina ) : -0.029
statefip_46 ( south dakota ) : -0.035
statefip_47 ( tennessee ) : -0.016
statefip_54 ( west virginia ) : -0.044
statefip_56 ( wyoming ) : 0.061
state_ly_6 ( california ) : -0.020
state_ly_10 ( delaware ) : -0.083
state_ly_12 ( florida ) : 0.008
state_ly_16 ( idaho ) : -0.026
state_ly_23 ( maine ) : -0.057
state_ly_24 ( maryland ) : 0.015
state_ly_25 ( massachusetts ) : 0.123
state_ly_34 ( new jersey ) : -0.026
state_ly_37 ( north carolina ) : 0.025
state_ly_40 ( oklahoma ) : -0.035
state_ly_49 ( utah ) : -0.048
state_ly_51 ( virginia ) : 0.045
state_ly_91 ( abroad ) : -0.088
whymove_1 ( change in marital status ) : -0.027
whymove_2 ( to establish own household ) : -0.066
whymove_3 ( other family reason ) : 0.002
whymove_5 ( to look for work or lost job ) : -0.251
whymove_10 ( wanted new or better housing ) : 0.012
whymove_11 ( wanted better neighborhood ) : 0.045
whymove_12 ( for cheaper housing ) : -0.033
whymove_14 ( attend/leave college ) : -0.270
whymove_18 ( natural disaster ) : 0.136
whymove_19 ( foreclosure or eviction ) : 0.022
mig_stat_ly_4 ( moved within state, different county ) : 0.005
mig_stat_ly_6 ( abroad ) : -0.006
health_1 ( excellent ) : 0.027
health_3 ( good ) : -0.054
health_4 ( fair ) : -0.128
health_5 ( poor ) : -0.173
vet1_2 ( august 1990 to august 2001 ) : 0.003
vet1_3 ( may 1975 to july 1990 ) : 0.000
vet1_4 ( vietnam era (august 1964 to april 1975) ) : -0.065
csvisleg_1 ( no ) : 0.011
csvisleg_2 ( yes ) : 0.001
csvisleg_98 ( blank ) : -0.014
paidhour_1 ( no ) : 0.108
paidhour_2 ( yes ) : -0.032
union_1 ( no union coverage ) : -0.011
union_2 ( member of labor union ) : 0.072
bpl_1.0 ( usa, canada & dependent ) : 0.005
bpl_8.0 ( developed asia ) : 0.020
fbpl_5.0 ( central and caribean ) : -0.012
fbpl_7.0 ( europe ) : 0.005
fbpl_9.0 ( east asia ) : -0.006
grid: [1.00000000e-02 8.30217568e-03 6.89261210e-03 5.72236766e-03
 4.75081016e-03 3.94420606e-03 3.27454916e-03 2.71858824e-03
 2.25701972e-03 1.87381742e-03 1.55567614e-03 1.29154967e-03
 1.07226722e-03 8.90215085e-04 7.39072203e-04 6.13590727e-04
 5.09413801e-04 4.22924287e-04 3.51119173e-04 2.91505306e-04
 2.42012826e-04 2.00923300e-04 1.66810054e-04 1.38488637e-04
 1.14975700e-04 9.54548457e-05 7.92482898e-05 6.57933225e-05
 5.46227722e-05 4.53487851e-05 3.76493581e-05 3.12571585e-05
 2.59502421e-05 2.15443469e-05 1.78864953e-05 1.48496826e-05
 1.23284674e-05 1.02353102e-05 8.49753436e-06 7.05480231e-06
 5.85702082e-06 4.86260158e-06 4.03701726e-06 3.35160265e-06
 2.78255940e-06 2.31012970e-06 1.91791026e-06 1.59228279e-06
 1.32194115e-06 1.09749877e-06 9.11162756e-07 7.56463328e-07
 6.28029144e-07 5.21400829e-07 4.32876128e-07 3.59381366e-07
 2.98364724e-07 2.47707636e-07 2.05651231e-07 1.70735265e-07
 1.41747416e-07 1.17681195e-07 9.77009957e-08 8.11130831e-08
 6.73415066e-08 5.59081018e-08 4.64158883e-08 3.85352859e-08
 3.19926714e-08 2.65608778e-08 2.20513074e-08 1.83073828e-08
 1.51991108e-08 1.26185688e-08 1.04761575e-08 8.69749003e-09
 7.22080902e-09 5.99484250e-09 4.97702356e-09 4.13201240e-09
 3.43046929e-09 2.84803587e-09 2.36448941e-09 1.96304065e-09
 1.62975083e-09 1.35304777e-09 1.12332403e-09 9.32603347e-10
 7.74263683e-10 6.42807312e-10 5.33669923e-10 4.43062146e-10
 3.67837977e-10 3.05385551e-10 2.53536449e-10 2.10490414e-10
 1.74752840e-10 1.45082878e-10 1.20450354e-10 1.00000000e-10]
























