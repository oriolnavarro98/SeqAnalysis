from SeqAnalyzer import sequenceData

file_path = '/Users/oriolnavarro/Desktop/PersonalDev/Bioinformatics/CrashCourse/Week4/raw.fastq.rtf'

sequence = sequenceData(filePath=file_path)
sequence.loadFile()
sequence.usableReads(lowestQualScore=50, thresholdAverageScore=68)