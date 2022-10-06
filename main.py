from SeqAnalyzer import sequenceData

file_path = '/Users/oriolnavarro/Desktop/PersonalDev/Bioinformatics/CrashCourse/Week4/SeqAnalysis/raw.fastq.rtf'
output_path = '/Users/oriolnavarro/Desktop/PersonalDev/Bioinformatics/CrashCourse/Week4/SeqAnalysis/'
sequence = sequenceData(filePath=file_path, outputPath=output_path)
sequence.usableReads(lowestQualScore=50, thresholdAverageScore=68)
sequence.GCContent()
#sequence.extractDNAReads(fname="X")
sequence.translateDNA2RNA(fname="X")
#sequence.generateReport()