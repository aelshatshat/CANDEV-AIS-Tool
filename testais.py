import ais, csv, time

##print(ais.decode('55NBjP01mtGIL@CW;SM<D60P5Ld000000000000P0`<3557l0<50@kk@K5h@00000000000', 2))
##
##print(ais.decode('15O<@N001sG:hgHL6F?m;T6D00S@', 0))
##
##print(ais.decode('D030p<QoDN?b<`N00A=O6D0', 0)



##print(ais.decode('15O<@N001sG:hgHL6F?m;T6D00S@', 0))
##print(ais.decode('8@30oni?0@=@Rh2531>3Boep75Cn7P4dh01@RhkeB9F00ode?UCJ604lh000', 0))
##print(ais.decode('D030p<QoDN?b<`N00A=O6D0', 2))


#print(ais.decode('54eGUdT1r?uAH63OS7@M9DF0@E>0ThE>222222152hH7576B052@Ap3CkU3@AkVH888888034eGP`UP00JBhV`HhM=tbwvB0000',2))
#print(ais.decode('54eGUdT1r?uAH63OS7@M9DF0@E>0ThE>222222152hH7576B052@Ap3CkU3@AkVH8888880',2))

with open('test.csv', mode='w') as test:
    test_writer = csv.writer(test, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    test_writer.writerow(['MMSI'])


errorCount = 0
time1 = time.time()
with open('CCG_AIS_Log_2018-05-01.csv', newline='\n') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    count = 0
    for row in csv_reader:
        count += 1

        if count > 50:
            break

        try:
            #print(text)
            #print(len(row))
            if (len(row) < 8):
                rowPos = 5
                text = str(row[rowPos])
                sentencePos = 1
                
            else:
                rowPos = 7
                text = str(row[rowPos])
                sentencePos = 3

            if(row[sentencePos] == "1"):
                decodeTxt = ais.decode(text, 0)

            else:
                for j in range(int(row[sentencePos]) - 1):
                    count += 1
                    row = csv_reader.__next__()
                    text += str(row[rowPos])
                    ##print(text)
                decodeTxt = ais.decode(text, int(row[sentencePos]))

            mmsi = decodeTxt.get('mmsi')
            with open('test.csv', mode='a', newline="") as test:
                test_writer = csv.writer(test, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                test_writer.writerow([mmsi])

            ##print(str(mmsi))
        except:
            errorCount += 1
            ##print("error")
            ##print(count)
            ##print(text)
            ##print(len(row))


time2 = time.time()
timefinal = time2 - time1
print("end ", timefinal)
print(errorCount)
print(count)
print(errorCount/count)
