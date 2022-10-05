
class sequenceData():
    def __init__(self, filePath, teardown=False):
        self.filePath = filePath    # fastq.rtf file location
        self.teardown = teardown    # teardown flag 

    def __exit__(self):
        if self.teardown:
            self.quit()

    def loadFile(self):
        # Load file
        self.fastaqFile = open(self.filePath, 'r').readlines()[7:]
    
    def usableReads(self, lowestQualScore=50, thresholdAverageScore=68):
        # Determine number of usable reads based on predefine thresholds
        asciiFlag = False
        numberUsableReads = 0
        readsCounter = 0
        
        for line in self.fastaqFile:
            if "length=" in line:
                # Extract length of the read
                readLength = line.split("length=")[-1]
                readLength = int(readLength.split("\\")[0])
                continue
            elif line == '+\\\n':
                asciiFlag = True #  Flag to determine if next line contains ASCII scores
                readsCounter += 1
                continue
            elif asciiFlag:
                tooLowScore = False
                asciiScores = line[:readLength]    # Extraction of ASCII Scores
                runCount = 0
                for score in asciiScores:
                    indScore = ord(score)           # Score conversion to int value
                    if indScore < lowestQualScore:
                        tooLowScore = True
                        break
                    else:
                        runCount += indScore
                asciiFlag = False
            else:
                continue
        
            averageScore = runCount/len(asciiScores)    # Avg Score calculated

            # Read Analysis to determine if min requirements are met
            if (tooLowScore == False) & (averageScore > thresholdAverageScore):
                numberUsableReads += 1  
        
        # Output Results
        print(f"Number of reads that meet quality requirements: {numberUsableReads}")
        print(f"Reads analyzed: {readsCounter}")

        








