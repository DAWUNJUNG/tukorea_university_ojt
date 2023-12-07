library(dplyr)
library(readxl)

jeju_y21_history <- read_excel("C:/tukorea_university_ojt/Junior/secondSemester/week_15_exam/Sample4_y21_history.xlsx")
jeju_y20_history <- read_excel("C:/tukorea_university_ojt/Junior/secondSemester/week_15_exam/Sample5_y20_history.xlsx")

bind_col <- left_join(jeju_y21_history, jeju_y20_history, by = "ID")
bind_col