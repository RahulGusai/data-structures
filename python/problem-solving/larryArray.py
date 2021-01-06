#! /usr/lib/python3


A = [826,399,308,449,954,899,214,239,326,988,989,760,887,199,206,137,406,162,174,15,850,919,953,290,343,166,986,860,730,774,701,857,257,405,379,531,286,511,781,770,620,171,431,55,648,36,114,264,931,
613,163,529,344,668,862,155,968,353,389,113,885,335,732,979,72,743,480,268,765,52,557,647,283,423,809,112,188,385,24,616,284,658,440,252,493,715,870,172,939,707,703,959,785,581,515,970,346,874,410,
600,622,425,943,152,822,520,98,911,877,839,74,685,369,261,512,237,77,66,679,937,922,778,617,216,602,759,106,159,197,475,803,962,916,905,655,277,966,107,747,122,392,923,735,63,427,640,921,40,831,523,82,821,802,949,504,27,501,84,194,636,179,2,444,761,319,510,408,888,323,868,
934,51,146,551,591,677,574,401,347,443,263,890,269,700,514,717,67,883,961,200,266,329,631,638,176,828,855,265,864,375,341,378,298,981,987,422,60,880,660,753,561,892,542,126,132,92,478,47,593,429,886,594
,231,321,782,629,226,503,491,248,976,294,111,967,141,128,990,370,914,813,325,461,739,120,738,29,209,681,675,830,618,330,519,570,589,90,835,479,663,592,721,251,566,787,595,562,124,489,609,
88,327,94,673,750,526,381,23,245,946,869,374,20,457,866,964,22,580,30,476,313,722,867,807,980,695,288,256,644,614,873,123,394,314,637,49,466,702,929,621,513,952,768,282,470,453,96,400,579
,509,280,549,19,12,775,468,848,553,190,7,664,334,836,859,464,764,59,806,434,521,734,368,773,823,827,499,158,56,160,376,41,428,13,666,42,295,611,484,89,395,289,452,240,273,560,718,4,688,712,917
,404,548,612,44,972,211,527,1,362,437,139,878,645,133,336,127,61,299,978,228,625,669,203,881,810,757,147,856,924,360,697,584,844,506,725,301,630,741,537,804,302,267,205,518,799,704,789,598,365,798
,971,278,615,692,843,279,258,852,193,210,875,31,793,445,340,5,982,91,597,975,454,441,525,100,790,64,254,435,135,543,944,635,547,626,642,140,608,583,315,590,766,311,472,492,322,576,545,481,39,117,109,255,902,711,746,795,384,246,933,253,678,699,693,709,755,185,786,863,544,524,473,145,386,409,196,984,189,351,25,585,9,373,477,57,920,241,87,538,355,104,303,671,134,891,913,950,411,872,854,220,716,110,497,115,686,54,354,672,958,451,415,230,508,192,357,935,35,50,455,490,740,751,691,467,610,260,623,359,897,507,603,649,496,356,414,901,763,641,500,586,559,670,974,393,130,396,505,300,287,772,168,153,367,683,834,910,165,936,533,291,651,469,532,432,270,784,601,312,568,963,38,175,324,421,462,244,474,426,6,575,639,748,889,177,101,706,412,81,380,448,720,569,659,794,125,486,942,849,727,788,342,898,652,654,46,293,320,714,215,965,225,903,204,460,37,154,908,516,599,687,865,530,183,397,926,938,350,382,805,348,337,723,808,816,33,217,32,129,169,11,450,820,416,792,628,403,845,941,121,234,439,587,517,696,102,606,148,632,219,14,332,674,76,724,488,955,48,304,71,136,18,358,331,222,99,540,149,676,847,567,419,68,242,829,339,212,388,947,383,957,170,75,181,213,436,58,28,928,184,698,777,767,43,948,93,235,535,390,243,236,70,783,208,195,832,182,983,879,371,745,951,552,361,430,762,973,418,656,558,65,915,841,459,550,904,690,861,202,960,541,776,729,605,604,157,662,281,846,233,694,105,812,818,607,446,858,619,108,498,79,927,482,118,728,918,985,912,736,201,572,689,896,292,564,992,731,801,851,447,756,814,726,296,398,232,250,310,708,463,555,333,26,144,167,578,69,930,588,522,187,86,554,800,779,713,274,749,969,363,577,45,21,657,438,791,318,207,8,186,465,238,53,932,627,116,909,364,840,705,221,539,907,83,494,433,653,85,62,925,229,900,307,224,345,143,906,247,352,556,780,424,719,815,684,420,305,131,563,34,227,103,297,945,876,275,16,667,833,442,571,825,10,838,744,151,573,646,272,262,546,178,142,596,796,661,842,191,161,317,665,817,771,306,276,940,487,309,80,797,991,956,752,884,650,316,285,95,458,73,893,349,758,471,417,837,536,633,634,138,3,710,97,643,485,565,218,502,977,624,391,366,495,769,894,819,338,871,150,387,483,180,156,372,164,534,377,528,824,402,882,680,811,223,271,582,407,17,853,249,198,733,737,119,259,456,328,413,754,742,682,173,895,78]

def larrysArray(A):
    n = len(A)
    pIndex=0
    cIndex = 0
    diff=0
    element = 1

    while( pIndex<n ):
        cIndex = A.index(element)        
        diff = cIndex - pIndex

        ret = rotateArray(A,n,pIndex,cIndex,element,diff)

        if ret==True:
            pIndex = pIndex + 1
            element = element + 1    
            continue
        
        else:
            return "NO"

    return "YES"


def rotateArray(A,n,pIndex,cIndex,element,diff):
    if ( pIndex==cIndex ):
        return True

    else:
        if( diff==1 ):
            if ( pIndex==n-2 ):
                return False
            temp = A[cIndex-1]
            A[cIndex-1] = A[cIndex]
            A[cIndex]= A[cIndex+1]
            A[cIndex+1] = temp
            cIndex = A.index(element)
            diff = cIndex - pIndex
            if rotateArray(A,n,pIndex,cIndex,element,diff)==True:
                return True
            else:
                return False
        else:
            A[cIndex]=A[cIndex-1]
            A[cIndex-1]=A[cIndex-2]
            A[cIndex-2] = element
            cIndex = A.index(element)
            diff = cIndex - pIndex
            if rotateArray(A,n,pIndex,cIndex,element,diff)==True:
                return True
            else:
                return False


print( larrysArray(A) )

