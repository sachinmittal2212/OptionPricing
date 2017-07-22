from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
import matplotlib.pyplot as plt
import datetime
import plot_util as pu
import numpy as np
import math

dates         		= 	[datetime.date(2015, 7, 20), datetime.date(2015, 8, 3), datetime.date(2015, 8, 10), datetime.date(2015, 8, 17), datetime.date(2015, 8, 24), datetime.date(2015, 9, 7), datetime.date(2015, 9, 14), datetime.date(2015, 9, 21), datetime.date(2015, 10, 8), datetime.date(2015, 10, 15), datetime.date(2015, 11, 5), datetime.date(2015, 11, 12), datetime.date(2015, 11, 19), datetime.date(2015, 12, 3), datetime.date(2015, 12, 10), datetime.date(2015, 12, 17), datetime.date(2016, 1, 7), datetime.date(2016, 1, 14), datetime.date(2016, 1, 21), datetime.date(2016, 2, 4), datetime.date(2016, 2, 15), datetime.date(2016, 2, 22), datetime.date(2016, 3, 7), datetime.date(2016, 3, 14), datetime.date(2016, 3, 21), datetime.date(2016, 4, 5), datetime.date(2016, 4, 12), datetime.date(2016, 4, 19), datetime.date(2016, 4, 26), datetime.date(2016, 5, 3), datetime.date(2016, 5, 10), datetime.date(2016, 5, 17), datetime.date(2016, 5, 24), datetime.date(2016, 6, 7), datetime.date(2016, 6, 14), datetime.date(2016, 6, 21), datetime.date(2016, 7, 5), datetime.date(2016, 7, 12), datetime.date(2016, 7, 19), datetime.date(2016, 7, 26), datetime.date(2016, 8, 2), datetime.date(2016, 8, 9), datetime.date(2016, 8, 16), datetime.date(2016, 8, 23), datetime.date(2016, 9, 6), datetime.date(2016, 9, 13), datetime.date(2016, 9, 20), datetime.date(2016, 9, 27), datetime.date(2016, 10, 10), datetime.date(2016, 10, 17), datetime.date(2016, 10, 24), datetime.date(2016, 11, 7), datetime.date(2016, 11, 14), datetime.date(2016, 11, 21), datetime.date(2016, 12, 5), datetime.date(2016, 12, 12), datetime.date(2016, 12, 19), datetime.date(2016, 12, 26), datetime.date(2017, 1, 3), datetime.date(2017, 1, 10), datetime.date(2017, 1, 17), datetime.date(2017, 1, 24), datetime.date(2017, 2, 3), datetime.date(2017, 2, 10), datetime.date(2017, 2, 17), datetime.date(2017, 3, 3), datetime.date(2017, 3, 10), datetime.date(2017, 3, 17), datetime.date(2017, 4, 7), datetime.date(2017, 4, 14), datetime.date(2017, 4, 21), datetime.date(2017, 5, 5), datetime.date(2017, 5, 12), datetime.date(2017, 5, 19), datetime.date(2017, 6, 2), datetime.date(2017, 6, 9), datetime.date(2017, 6, 16), datetime.date(2017, 6, 23), datetime.date(2017, 7, 7), datetime.date(2017, 7, 14)]
underlying_chg     	= 	[-0.029699510831586312, -0.10767014764133952, 0.055690072639225006, -0.025993883792048974, -0.19662480376766073, 0.04543234000977024, 0.03878504672897186, -0.0049482681061626625, -0.007233273056057974, 0.049180327868852375, 0.06119791666666666, 0.010224948875255825, 0.00040485829959500995, -0.004451639012545549, -0.04268292682926825, 0.01953290870488304, -0.09329446064139933, -0.021129995406522745, -0.04129516658845601, -0.03181595692608918, -0.014661274014155647, 0.05387378142637244, 0.027750730282376106, -0.01657981999052601, 0.05587668593448937, -0.007755474452554706, -0.015172413793103521, 0.008870214752567775, -0.004164738546968901, 0.0032527881040890043, -0.041222788327929645, 0.003381642512077511, -0.0038517091959557634, 0.03576607056549057, -0.019598693420438615, 0.005235602094240862, 0.03456439393939387, 0.021967963386727813, -0.007613076578593781, 0.004963898916967327, -0.016614279299505957, 0.014155251141552465, 0.03827104907699236, -0.006938421509106783, -0.0017467248908295226, -0.019247594050743746, -0.0013380909901873023, -0.004466279589102244, 0.014804845222072545, -0.0053050397877982885, 0.032888888888888676, 0.0025817555938039234, 0.01888412017167391, 0.006739679865206313, 0.014749531886450437, 0.0054782975136957015, -0.03897736797988263, 0.002180549498473569, 0.003916449086161835, 0.0026007802340703196, 0.006917423259835717, 0.010734220695577463, -0.005097706032285476, 0.010247651579846294, -0.0021132713440405295, -0.0076238881829734165, -0.0034144259496372204, 0.003426124197002144, 0.017498932991890707, -0.014261744966442873, -0.003829787234042509, -0.01196070055531825, 0.024643320363164693, -0.006329113924050685, 0.04883227176220816, 0.01902834008097154, -0.022646007151370655, 0.03373983739837406, 0.007078254030672353, 0.0406091370558376]
spread_next_month  	= 	[0.0776327343216128, 0.1835236719224059, -0.1775139651249635, 0.19018205028594884, 0.053315443538049206, 0.18945869028782028, 0.34592460607837033, -0.07266194079594207, -0.05537268719226716, -0.10464383725505674, -0.13553702973338494, -0.31507670217922945, -0.2007432170638516, -0.040302471347905974, -0.04776198893469943, -0.1168474743768798, 0.06343884335566366, -0.17936088320254692, -0.01421461282781683, -0.15404587026598715, -0.2753295818090075, -0.24820094407066073, 0.0007166417081051549, -0.04490943466659707, -0.1640585656170372, -0.10553395154715672, -0.17516983479954176, -0.1974416069505814, -0.18367476854023848, -0.19343328481825203, -0.2055929747623945, -0.22735453162618363, -0.2537850138635447, -0.16276552951153503, -0.1416430272723432, -0.1657976650033603, -0.13945975219262263, -0.1789848708382742, -0.2118331389716106, -0.2363342454165828, -0.18165391508553705, -0.1904682864974595, -0.2821342876761358, -0.2803005059228164, -0.1737802105586789, -0.17571142529850436, -0.18162666631545069, -0.20119786017773506, -0.17084304419342544, -0.16090586373481228, -0.20166676166752875, 0.11956943546105397, 0.14476593360958986, 0.15853380346635063, 0.029421375233046377, 0.04854703793785462, 0.06208317239557218, 0.06146211931479165, 0.026316519688489977, 0.023143144680273068, 0.04723972461240349, 0.03300412853935592, -0.0018759641985278195, 0.06681640393957161, 0.0638901743627384, 0.03212522062844476, 0.051388022676994737, 0.05115638584314666, 0.0625190226494642, 0.02575156047450212, 0.0642121759413387, 0.059391183431922526, 0.08816188727539717, 0.061662735069545595, 0.06542619292344075, 0.05231166567710064, 0.049162388155512056, 0.09537509422108206, 0.04616758475827858, 0.08993237462388057]
spread_far_month   	=  	[-0.02422610364194225, 0.009251246546500025, 0.03084632462006559, 0.04099585471655751, 0.05395854108750396, 0.20462121572506153, 0.18257191761791308, 0.10131315116245096, 0.026199151675872043, -0.008133900451770846, 0.07774905702178309, -0.06284715201414545, 0.018511577284982015, 0.01564056469938903, 0.03222415843112756, 0.033196005354107404, 0.06995636870795748, 0.10993152966679265, 0.16164993784316298, 0.1265271912917059, 0.0860919153971303, 0.14760934927463812, 0.1714860883192592, 0.13464955453583263, 0.04175385517677928, 0.03282388381923449, 0.014374813022840731, -0.023434621721406323, 0.028459008440693403, 0.10155566077810776, 0.09732979920707664, 0.13238457339692586, 0.131984883945884, 0.08160042435384136, 0.1106563415498401, 0.13807355837292296, 0.12304815420120277, 0.13573349361566536, 0.0906489799813234, 0.07994156320135021, 0.055428015002701315, 0.061642651438976535, 0.023009142340721253, 0.04664095269312896, 0.04213939263788506, 0.052920260315386346, 0.06771784642101994, 0.05498363538723565, 0.054807390284849364, 0.06603343999875028, 0.09803393038314885, 0.0657002030757753, 0.07342698379869743, 0.10281704228750588, 0.04812430002475256, 0.06051875366006534, 0.06318189659360932, 0.07629691029171184, 0.037207684920671516, 0.03781214403281051, 0.06534088887056998, 0.044089277768900974, 0.031689824248302315, 0.03843585895039668, 0.03474389599314299, 0.025915980804261524, 0.054196888481268045, 0.05182809517188963, 0.06759733617151831, 0.05130228706902165, 0.07498339622910342, 0.07361614630194424, 0.09249191835201624, 0.07630070188106243, 0.08061844262234691, 0.0944068167715997, 0.08003018387243416, 0.09857754298718824, 0.09094508236130056, 0.11374898299563047]
spread_this_month  	=	[-0.7488781810047951, 0.06977613083724374, -0.30587667379930644, -0.25991526849917845, -1.1130842147264282, 0.34972782219577825, 0.7230179949911647, -1.183521056659992, -0.240446670624735, -0.4027934964380026, -0.18620899612676867, -0.43195994968232115, -0.5999045892354012, -0.3897517608039881, -0.4853627944801319, -0.7335741594433611, -0.22749196452435194, -0.4148539517490555, -0.5108137646384558, -0.31465151183324747, -0.48015586538350374, -0.8468982213874761, -0.3830390472096145, -0.5136584340773657, -1.0314115728019273, -0.31952934139058403, -0.39413132469338824, -0.5123615029027935, -1.2535696869055404, -0.24263809468069653, -0.2658817951843744, -0.32888737705078913, -0.807738945050719, -0.38181544170191867, -0.4680505781257653, -1.2604696807034514, -0.2392380098452455, -0.3584721417195337, -0.4457844882893721, -1.1365882590259144, -0.24998052620235867, -0.2843584618874078, -0.4848142656261493, -1.181931907748545, -0.37947743245275706, -0.4124277283962897, -0.5373085457112999, -1.171077287430592, -0.2623228056218328, -0.29334319919676294, -0.7934749271545446, -0.28314354843649087, -0.3981419183814738, -0.8709081062860442, 0.11455955575449107, 0.12341956825881115, 0.15803035553370984, 0.28054370507009996, 0.010727131470223628, 0.02781752588426625, -0.0025597121057482682, 0.072641755791015, -0.013478812278092443, 0.072332115918413, -0.08811330285191822, 0.08152831916774375, 0.07812706651106406, 0.12248411597607103, 0.072626244115235, 0.0030802399129388224, 0.07105424685552574, 0.06355372913909374, 0.11444364942501407, 0.07606968650383993, 0.10184913113027023, 0.1323724700306134, 0.12019079955216604, 0.2310890670839579, 0.08839860301979427, 0.16698209210666717]
spread_next_season 	=  	[0.00772991658584797, 0.07492185821485833, 0.028716158188933895, 0.11265945556143095, 0.10232443593918912, 0.21675221712868578, 0.32041747101476703, 0.08721845662448141, -0.15510353863651996, -0.17966919234605702, 0.06502823163904674, -0.10395975304558913, 0.00037590654467972717, -0.027954275990402712, -0.020116229361996116, -0.046410205235562656, -0.0719597992371527, -0.03133799952571843, 0.12319801587740396, 0.08979153708559785, 0.08901665039236979, 0.13155190183661514, 0.14211973681245818, 0.07806850014642774, -0.024231372695143652, -0.08741308853731306, -0.15635657164369268, -0.1783906665576132, -0.12750286346141818, -0.004271653155945811, -0.0014594213611464396, 0.020116991737854174, 0.008090496030251436, -0.06780989021171775, -0.02036901617849726, -0.015984745583561024, -0.07795625772941103, -0.11635165670648656, -0.14945514426511752, -0.16751470484733777, 0.08210492403730571, 0.08278529821056646, 0.014523467280221858, 0.07983861034616835, 0.053819791483533504, 0.07052602874554405, 0.07967054794918908, 0.0680917259678449, 0.07755971038482952, 0.09728725547876328, 0.10662292104759728, 0.10193767426250458, 0.11013103960302999, 0.12218848271479542, 0.06034758328393498, 0.08107793797938087, 0.07516034938297272, 0.09325819469783261, 0.052512252092331645, 0.042489486696354106, 0.08055599751703348, 0.04086665471745871, 0.02649908844541542, 0.04201709503489717, 0.03763630130924285, 0.030747026107450448, 0.05938359082271908, 0.05688218147714841, 0.06947713982700378, 0.04518926379612552, 0.06538436742980086, 0.06732118074041507, 0.08266971440641051, 0.06721305326503899, 0.07083474387884924, 0.08564261569293101, 0.07175007901605597, 0.093843751084482, 0.0986300556260544, 0.12218136141869297]

x = [1,2,3,4,5]
a = [-1,-2,-1,-3,-4]
b = [1,2,3,1,2]

host = host_subplot(111, axes_class=AA.Axes)
plt.subplots_adjust(right=0.75)
par1 = host.twinx()
####git 
#### qqq
host.set_ylim(0,10)
host.set_xlim(min(x),max(x))
par1.set_ylim(-5,0)
host.set_xlabel("Date")
host.set_ylabel("Underlying")
par1.set_ylabel("Spread")

line1, = host.plot(x, b, color = pu.c1,linestyle = pu.l1,linewidth = 2,label="Underlying")
line2, = par1.plot(x, a, color = pu.c2,linestyle = pu.l2,linewidth = 2,label="Spread next month")

par1.fill_between(x,a,0,color = pu.c2)
host.axis["left"].label.set_color(line1.get_color())
par1.axis["right"].label.set_color(line2.get_color())

plt.show()