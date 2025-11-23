#Initialize/Load
setwd("/Users/mheinen/Documents/Bellevue/DSC 530 /Heinen530FinalProject/Build_DataSet")
tj <- read.csv('tj_list1.csv')
savant_up <- read.csv('tj_savant_up.csv')

#Data Cleaning
library('dplyr')
library('stringr')
library('ggplot2')
library('caTools')
library('randomForest')
library('caret')
library('rpart')
library('rpart.plot')
library('ROCR')
library('mice')
library('huxtable')
library('DT')

#Display Original Data
tj_hux <-
  hux(tj) %>%
  add_colnames() %>%
  set_bold(row = 1, col = everywhere, value = TRUE) %>%
  set_all_borders(TRUE)
head(tj_hux)

sav_hux <-
  hux(savant_up) %>%
  add_colnames() %>%
  set_bold(row = 1, col = everywhere, value = TRUE) %>%
  set_all_borders(TRUE)
head(sav_hux)

#Print head of TJ
head(tj)

#Filter Neccessary Variables

tj <- select(tj, select = c(Player, Position, Level, Year))

#Only Take Pitchers
library(dplyr)
tj <- filter(tj, Select2 == 'P')

#Only Take Players from MLB
tj <- subset(tj, select3 == 'MLB')

#Subset Greater or Equal to 2015 due to Statcast data
tj <- subset(tj, select4 >= 2015)

#Split First and Last Name
tj_1 <- str_split(tj$select1,' ')
data <- do.call(rbind, tj_1)
tj <- cbind(data, tj)

#Select Variables for Updated Frame
tj <- select(tj, select = c(1, 2))

#Rename Variables
names(tj)[1] <- "first_name"
names(tj)[2] <- "last_name"

#Add Binary TJ Feature -> 1 stands for YES 0 for NO
tj$tj_history <- 1

#Updated TJ Frame
tj_up_hux <-
  hux(tj) %>%
  add_colnames() %>%
  set_bold(row = 1, col = everywhere, value = TRUE) %>%
  set_all_borders(TRUE)

tj_up_hux

#Merge Data Frames
data <- merge(x = tj, y = savant_up, by = c("last_name"), all=TRUE)

#Replace NA's with 0
data$tj_history[is.na(data$tj_history)] <- 0

data$first_name.x <- NULL

names(data)[3] <- "first_name"
data$tj_history <- as.factor(data$tj_history)
sum(is.na(data))
summary(data)

#Replace NA values with Mean
for(i in 1:ncol(data)){
  data[is.na(data[,i]), i] <- mean(data[,i], na.rm = TRUE)
}

#Remove Remainder NA Values
data <- na.omit(data)
summary(data)
colnames(data)

#Rename Variables
names(data)[5] <- "age"
names(data)[6] <- "games_pitched"
names(data)[7] <- "innings_pitched"
names(data)[8] <- "k_percent"
names(data)[9] <- "bb_percent"
names(data)[13] <- "zone_swing_percent"
names(data)[14] <- "zone_swing_miss_percent"
names(data)[15] <- "out_zone_swing_percent"
names(data)[17] <- "pitches_thrown"
names(data)[18] <- "fastballs_thrown"
names(data)[24] <- "breaking_thrown"
names(data)[30] <- "offspeed_thrown"

#Reorder Variables
colnames(data)
data <- data[,c(1,3,2,5,6,7,8,9,10,11,12,13,14,
                15,16,17,18,19,20,21,22,23,24,25,26,27,4,28,29,30,31,32,33,34,35)]

#Cleaned Frame
data_hux <-
  hux(data) %>%
  add_colnames() %>%
  set_bold(row = 1, col = everywhere, value = TRUE) %>%
  set_all_borders(TRUE)
head(data_hux)

#Data Exploration
data$year <- as.factor(data$year)
summary(data)

# Remove Duplicates
data_no_duplicates <- distinct(data)

write.csv(data,"/Users/mheinen/Documents/Bellevue/DSC 530 /Heinen530FinalProject/tj_combines_data1.csv", row.names = FALSE) 

print ('CSV created Successfully')
