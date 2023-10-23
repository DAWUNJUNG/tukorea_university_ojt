library(descr)

ex_data <- read.csv("C:/tukorea_university_ojt/Junior/secondSemester/week_8/testdata.csv", fileEncoding = "UTF-8")

freq(ex_data$사업장구분, plot=T, main='사업장 구분 별 개수')
