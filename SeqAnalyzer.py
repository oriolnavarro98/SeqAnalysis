
class sequenceData():
    def __init__(self, filePath, teardown=False):
        self.filePath = filePath    # fastq.rtf file location
        self.teardown = teardown    # teardown flag 
        self.usableReadsExecuted = False

    def __exit__(self):
        if self.teardown:
            self.quit()

    def loadFile(self):
        # Load file
        self.fastaqFile = open(self.filePath, 'r').readlines()[7:]
    
    def usableReads(self, lowestQualScore=50, thresholdAverageScore=68):
        self.usableReadsExecuted = True
        self.lowestQualScore = lowestQualScore
        self.thresholdAverageScore = thresholdAverageScore
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
        
        # Output results
        self.numberUsableReads = numberUsableReads
        self.readsCounter = readsCounter
    
    def GCContent(self):
        self.GCContentExecuted = True

        seqFlag = False
        runningLength = 0
        totalCCount = 0
        totalGCount = 0

        for line in self.fastaqFile:
            if "length" in line:
                # Extract length of the read
                readLength = line.split("length=")[-1]
                readLength = int(readLength.split("\\")[0])
                SeqFlag = True
            elif SeqFlag:
                # Analyze read
                indRead = line[:readLength]
                indCCount = indRead.count('C')  # Count number of Cs
                indGCount = indRead.count('G')  # Count number of Gs
                totalCCount += indCCount
                totalGCount += indGCount
                runningLength += readLength
                SeqFlag = False
            else:
                continue
        
        # Calculate total GC Content % and Output Result
        self.runningLenth = runningLength
        self.totalCCount = totalCCount
        self.totalGCount = totalGCount
        self.totalGCContent = (totalCCount + totalGCount)/runningLength

    def SequencePresenceTest(self):
        pass

    
    def generateReport(self):
        # Generate a report based on the analysis performed on the loaded sequencing data
        print("\n")
        print("##### REPORT #####")
        #print(f"Date: {}")
        
        if self.usableReadsExecuted:
            # Output Results
            print("\n")
            print("------------------")
            print("# USABLE READS REPORT: ")
            print("User input thresholds: ")
            print(f"Highest Quality Score Not Admissible: {self.lowestQualScore}")
            print(f"Highest Average Score Not Admissible: {self.thresholdAverageScore}")
            print("-------------------------------------------------------")
            print("Results obtained: ")
            print(f"Number of reads that meet quality requirements: {self.numberUsableReads}")
            print(f"Reads analyzed: {self.readsCounter}")
            print(f"Percentage of admissible reads: {self.numberUsableReads/self.readsCounter*100}%")
        
        if self.GCContentExecuted:
            # Output Results
            print("\n")
            print("------------------")
            print("# GC CONTENT REPORT: ")
            print("-------------------------------------------------------")
            print("Results obtained: ")
            print(f"Total number of bases: {self.runningLenth}")
            print(f"Total number of C bases: {self.totalCCount}")
            print(f"Total number of G bases: {self.totalGCount}")
            print(f"GC Content Percentage: {self.totalGCContent*100}%")
            print(f"Total GC Content: {self.totalCCount + self.totalGCount} / {self.runningLenth}")

        print("\n")
        print("###################")
        print("\n")


        








