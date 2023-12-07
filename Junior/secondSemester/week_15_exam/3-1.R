library(ggplot2)

data <- read.csv("C:/tukorea_university_ojt/Junior/secondSemester/week_15_exam/count.csv")

ggplot(data, aes(x = trycount, y = successcount)) +
  geom_point()
