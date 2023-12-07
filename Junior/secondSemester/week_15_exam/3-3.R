library(ggplot2)
library(scales)

data <- read.csv("C:/tukorea_university_ojt/Junior/secondSemester/week_15_exam/count.csv")

data_subset <- head(data, 30)

ggplot(data_subset, aes(x = factor(trycount))) +
  geom_bar(aes(fill = factor(successcount)))
