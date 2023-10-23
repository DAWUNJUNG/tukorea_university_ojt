library(descr)

ex_data <- read.csv("C:/tukorea_university_ojt/Junior/secondSemester/week_8/testdata.csv", fileEncoding = "UTF-8")

pie(table(ex_data$평일운영시작시각))
