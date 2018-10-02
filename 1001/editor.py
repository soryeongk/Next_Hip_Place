un_hip = un_hip.dropna()
changes_un_hip = un_hip[un_hip['구분'].str.contains(r'(총전입-전출|구내전입-전출|구간전입-전출|시/도간전입-전출)')]
changes_un_hip
