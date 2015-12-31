d <- read.csv(commandArgs(trailingOnly = FALSE)[6],sep =',',stringsAsFactors=FALSE)
# Remove first 5 rows
d <- d[-(0:4),]
# Company name as row name
names <- t(d[,1])
# remove company names
d <- d[,-c(1)]
# change string to numeric
d <- as.data.frame(sapply(d,as.numeric))
d[is.na(d)] <- 0
for (j in seq(1:4)){
	ret <- (d[,5]-d[,5-j])/d[,5-j]
	ret <- ret[complete.cases(ret),]
	for(k in seq(1:4)){

	}
}
