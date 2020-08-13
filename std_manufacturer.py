#--This code standardizes the names of all the phone manufacturers in the dataframes
import re, string

#--import data--
std_manuf = pd.read_csv('pd_anon_standardize_manufacturers.csv')

#--drop empty column--
std_manuf = std_manuf.drop(columns='Unnamed: 8')

std_manuf['Manufacturer'] = std_manuf['Manufacturer'].str.lower()

#--list of standardized manufacturers--
manuf_str = 'Acer,alcatel,Allview,Amazon,Amoi,Apple,Archos,Asus,AT&T,Benefon,BenQ,BenQ-Siemens,Bird,BlackBerry,BLU,Bosch,BQ,Casio,Cat,chiun mai communication,Celkon,Chea,Coolpad,Dell,Edup International,Emporia,Energizer,Ericsson,Eten,Fujitsu Siemens,Garmin-Asus,Gigabyte,Gionee,Google,Haier,HP,HTC,Huawei,i-mate,i-mobile,Icemobile,Innostream,iNQ,Inpro Comm,Intel,Intex,Jolla,Karbonn,Kyocera,Lava,LeEco,Lenovo,LG,Maxon,Maxwest,Meizu,Microcom,Micromax,Microsoft,Mitac,Mitsubishi,Modu,Motorola,Murata,MWg,NEC,Neonode,NIU,Nokia,Nvidia,O2,OnePlus,Oppo,Orange,Palm,Panasonic,Pantech,Parla,Philips,Plum,Posh,Prestigio,QMobile,Qtek,Rebound Telecom,Sagem,Samsung,Sendo,Sewon,Sharp,Siemens,Sonim,Sony,Sony Ericsson,Spice,T-Mobile,TCT,Tel.Me.,Telit,Thuraya,Toshiba,Unnecto,Vertu,verykool,vivo,VKMobile,Vodafone,Wiko,Wisol,WND,XCute,Xiaomi,XOLO,Yezz,Yota,YU,ZTE'
manuf_str = manuf_str.lower()
manuf_lst = re.split(',', manuf_str)

std_manuf['Manufacturer_std'] = std_manuf['Manufacturer']

#--match substring of Manufacturer column with std manufacturer list--
s = '(' + '|'.join(manuf_lst) + ')'
std_manuf['Manufacturer_std'] =std_manuf['Manufacturer'].str.extract(s, expand=False)

std_manuf.to_csv('Standardized_Anon_Manufacturers.csv')
