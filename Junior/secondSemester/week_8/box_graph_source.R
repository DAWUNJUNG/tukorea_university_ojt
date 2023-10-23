library(descr)

ex_data <- read.csv("C:/tukorea_university_ojt/Junior/secondSemester/week_8/testdata.csv", fileEncoding = "UTF-8")

boxplot(ex_data$보유차고지수용능력, ex_data$자동차총보유대수, ylim = c(0, 1000), main="차고지 수용능력에 따른 보유대수 비교", names=c("보유차고지수용능력", "자동차총보유대수"))