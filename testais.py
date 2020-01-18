import ais, csv, time

##print(ais.decode('55NBjP01mtGIL@CW;SM<D60P5Ld000000000000P0`<3557l0<50@kk@K5h@00000000000', 2))
##
##print(ais.decode('15O<@N001sG:hgHL6F?m;T6D00S@', 0))
##
##print(ais.decode('D030p<QoDN?b<`N00A=O6D0', 0)



##print(ais.decode('15O<@N001sG:hgHL6F?m;T6D00S@', 0))
##print(ais.decode('D030p<QoDN?b<`N00A=O6D0', 0))
##print(ais.decode('D030p<QoDN?b<`N00A=O6D0', 2))

time1 = time.time()
with open('CCG_AIS_Log_2018-05-01.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    for row in csv_reader:
        
        try:
            text = str(row[7])
            ##print(text)
            ##print(ais.decode(text, 0))

            ais.decode(text, 0)
            
        except:
            ##print("error")
            1+1


time2 = time.time()
timefinal = time2 - time1
print("end ", timefinal)
        
        
