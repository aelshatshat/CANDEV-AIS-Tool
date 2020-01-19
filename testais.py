import ais, csv, time, shutil



def parser(filepath):

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


    parsedData = {"MMSI": {"region": "Region", "stationLocation": "Station Location", "channel": "Channel", "date": "Date", "time": "Time",
                                          "imoNum": "IMO Number", "callsign": "Callsign", "vesselName": "Vessel Name", "cargoType": "CargoType",
                            "dimBow": "Dimension Bow", "dimStern": "Dimension Stern", "dimPort": "Dimension Port", "dimStar": "Dimension Starbord",
                                          "draught": "Draught", "destination": "Destination"}}

    errorCount = 0
    time1 = time.time()
    with open('CCG_AIS_Log_2018-05-01.csv', newline='\n') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        count = 0
        MMSIArray = []
        for row in csv_reader:
            count += 1

            # if count == 10000:
            #     break
            try:
                #print(text)
                #print(len(row))
                if (len(row) < 8):
                    rowPos = 5
                    text = str(row[rowPos])
                    sentencePos = 1
                    channel = str(row[4])
                    stationLocation = "NA"
                    region = 'NA'

                else:
                    rowPos = 7
                    text = str(row[rowPos])
                    sentencePos = 3
                    tempRegion = (str(row[2]))
                    region = tempRegion[2]
                    stationLocation = tempRegion[tempRegion.rindex("-") + 1:tempRegion.rindex("*")]
                    channel = str(row[6])

                if(row[sentencePos] == "1"):
                    decodeTxt = ais.decode(text, 0)

                else:
                    for j in range(int(row[sentencePos]) - 1):
                        count += 1
                        row = csv_reader.__next__()
                        text += str(row[rowPos])
                        ##print(text)
                    decodeTxt = ais.decode(text, int(row[sentencePos]))


                ## STATIC INFO
                mmsi = decodeTxt.get('mmsi')
                year = decodeTxt.get('year')
                month = decodeTxt.get('month')
                day = decodeTxt.get('day')
                hour = decodeTxt.get('hour')
                minute = decodeTxt.get('minute')
                second = decodeTxt.get('second')
                imoNum = decodeTxt.get('imo_num')
                callsign = decodeTxt.get('callsign')
                vesselName = decodeTxt.get('name')
                typeCargo = decodeTxt.get('type_and_cargo')
                dimBow = decodeTxt.get('dim_a')
                dimStern = decodeTxt.get('dim_b')
                dimPort = decodeTxt.get('dim_c')
                dimStarbord = decodeTxt.get('dim_d')
                draught = decodeTxt.get('draught')
                destination = decodeTxt.get('destination')


                # with open('test.csv', mode='a', newline="") as test:
                #     test_writer = csv.writer(test, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                #     test_writer.writerow([region, stationLocation, channel, year, month, day, hour, minute, second, mmsi,
                #                           imoNum, callsign, vesselName, typeCargo, dimBow, dimStern, dimPort, dimStarbord,
                #                           draught, destination])



                listKey = ["region", "stationLocation", "channel", "date",
                                            "time", "imoNum", "callsign", "vesselName", "cargoType",
                            "dimBow", "dimStern", "dimPort", "dimStar",
                                          "draught","destination"]

                dicKey = {"region": region, "stationLocation": stationLocation, "channel": channel, "date": (str(day) + "/" + str(month) + "/" + str(year)),
                                            "time": (str(hour) + ":" + str(minute) + ":" + str(second)), "imoNum": imoNum, "callsign": callsign, "vesselName": vesselName, "cargoType": typeCargo,
                            "dimBow": dimBow, "dimStern": dimStern, "dimPort": dimPort, "dimStar": dimStarbord,
                                          "draught": draught, "destination": destination}

                try:
                    if mmsi not in parsedData.keys():

                        MMSIArray.append(mmsi)
                        parsedData[mmsi] = {"region": region, "stationLocation": stationLocation, "channel": channel, "date": (str(day) + "/" + str(month) + "/" + str(year)),
                                            "time": (str(hour) + ":" + str(minute) + ":" + str(second)), "imoNum": imoNum, "callsign": callsign, "vesselName": vesselName, "cargoType": typeCargo,
                                            "dimBow": dimBow, "dimStern": dimStern, "dimPort": dimPort, "dimStar": dimStarbord,
                                            "draught": draught, "destination": destination}
                    else:
                        for tempVar in listKey:
                            if(parsedData[mmsi][tempVar] == ""):
                                parsedData[mmsi][tempVar] = dicKey[tempVar]

                except:
                   print("Fuck")

                # print(decodeTxt)


                ##print(str(mmsi))
            except:
                errorCount += 1
                ##print("error")
                ##print(count)
                ##print(text)
                ##print(len(row))
    with open('test.csv', mode='w', newline="") as test:
        test_writer = csv.writer(test, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        test_writer.writerow(
            ["MMSI", parsedData["MMSI"]["region"], parsedData["MMSI"]["stationLocation"],
             parsedData["MMSI"]["channel"], parsedData["MMSI"]["date"],
             parsedData["MMSI"]["time"],
             parsedData["MMSI"]["imoNum"], parsedData["MMSI"]["callsign"],
             parsedData["MMSI"]["vesselName"], parsedData["MMSI"]["cargoType"],
             parsedData["MMSI"]["dimBow"], parsedData["MMSI"]["dimStern"],
             parsedData["MMSI"]["dimPort"], parsedData["MMSI"]["dimStar"],
             parsedData["MMSI"]["draught"], parsedData["MMSI"]["destination"]])

    with open('test.csv', mode='a', newline="") as test:
        test_writer = csv.writer(test, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for i in range(len(MMSIArray)):
            test_writer.writerow(
                [MMSIArray[i], parsedData[MMSIArray[i]]["region"], parsedData[MMSIArray[i]]["stationLocation"],
                 parsedData[MMSIArray[i]]["channel"], parsedData[MMSIArray[i]]["date"],
                 parsedData[MMSIArray[i]]["time"],
                 parsedData[MMSIArray[i]]["imoNum"], parsedData[MMSIArray[i]]["callsign"],
                 parsedData[MMSIArray[i]]["vesselName"], parsedData[MMSIArray[i]]["cargoType"],
                 parsedData[MMSIArray[i]]["dimBow"], parsedData[MMSIArray[i]]["dimStern"],
                 parsedData[MMSIArray[i]]["dimPort"], parsedData[MMSIArray[i]]["dimStar"],
                 parsedData[MMSIArray[i]]["draught"], parsedData[MMSIArray[i]]["destination"]])
    time2 = time.time()
    timefinal = time2 - time1
    print("end ", timefinal)
    print(errorCount)
    print(count)
    print(errorCount/count)



def filter(region, sMin, sMax, x, y, xSelect, ySelect):

    regionCheck = False
    speedCheck = False
    locationCheck = False

    time1 = time.time()

    with open('CCG_AIS_Dynamic_Data_2018-05-01.csv', newline='\n') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")



        filteredRows = []
        count = 0
        for row in csv_reader:
            if (region != ""):
                regionCheck = True

            if (sMin != "" and sMax != ""):
                speedCheck = True

            if (x != "" and y != "" and xSelect != "" and ySelect != ""):
                locationCheck = True

            if(count == 0):
                count += 1
                filteredRows.append(row)
                row = csv_reader.__next__()

            #print(count)
            count += 1
            textSpeed = str(row[15])
            textLocationX = str(row[18])
            textLocationY = str(row[17])

            if(textSpeed == "NA" and speedCheck):
                row = csv_reader.__next__()

            elif(textLocationX == "NA" and locationCheck):
                locationCheck = False
                row = csv_reader.__next__()

            if(regionCheck):
                textRegion = str(row[0])

            if(speedCheck):
                textSpeed = float(row[15])

            if(locationCheck):
                textLocationX = float(row[18])
                textLocationY = float(row[17])


            if(regionCheck and speedCheck and locationCheck):
                if (textRegion == region):
                    if(sMin <= textSpeed <= sMax):

                        if(ySelect == "S" and xSelect == "E"):
                            #print(float(x))
                            if(textLocationY <= float(y) and textLocationX >= float(x)):
                             #   print("X: " + str(textLocationX) + " Y: " + str(textLocationY))
                                filteredRows.append(row)


            elif(regionCheck and speedCheck and not(locationCheck)):
                if (textRegion == region):
                    if(sMin <= textSpeed <= sMax):

                        filteredRows.append(row)


            elif(regionCheck):
                if(textRegion == region):

                    filteredRows.append(row)

        with open('filtered.csv', mode='w', newline="") as test:
            test_writer = csv.writer(test, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for i in range(len(filteredRows)):
                test_writer.writerow(filteredRows[i])

        print("done")
        time2 = time.time()
        timefinal = time2 - time1
        print("end ", timefinal)



filter("M", 5, 10, -64.0, 47.0, "", "")
##parser("test")