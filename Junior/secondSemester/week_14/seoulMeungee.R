library(extrafont)
font_import()
theme_set(theme_grey(base_family="AppleGothic"))

# 엑셀 파일 가져오기
library(readxl)
dustdata <- read_excel("/Users/lacy/tukorea/ojt/tukorea_university_ojt/Junior/secondSemester/week_14/dustdata.xlsx")

View(dustdata)
str(dustdata)


# 성북구와 중구 데이터만 추출
library(dplyr)
dustdata_anal <- dustdata[, c("날짜", "성북구", "중구") ]
View(dustdata_anal)


# 결측치 확인
is.na(dustdata_anal)

sum(is.na(dustdata_anal))


# 지역별 미세먼지 농도의 기술통계량 도출
library(psych)

describe(dustdata_anal$성북구)
describe(dustdata_anal$중구)


# 성북구와 중구 미세먼지 농도 상자 그림 출력
boxplot(dustdata_anal$성북구, dustdata_anal$중구,
        main = "finedust_compare", xlab = "AREA", names = c("성북구", "중구"),
        ylab = "FINEDUST_PM", col = c("blue", "green"))


# f 검정으로 지역별 미세먼지 농도의 분산 차이를 검정
var.test(dustdata_anal$중구, dustdata_anal$성북구)


# t 검정으로 지역별 미세먼지 농도의 평균 차이를 검정
t.test(dustdata_anal$중구, dustdata_anal$성북구, var.equal = T)


# 엑셀 파일 호출
library(readxl)
exdata1 <- read_excel("/Users/lacy/tukorea/ojt/tukorea_university_ojt/Junior/secondSemester/week_14/Sample1.xlsx")
exdata1


# 경기, 서울, 제주 지역 Y20_CNT를 상자 그림으로 출력
boxplot(formula = Y20_CNT ~ AREA, data = exdata1)


# 분산분석으로 세 집단 간 평균 차이 검정 - 1
anova(lm(Y20_CNT ~ AREA, data = exdata1))
      
      
# 분산분석으로 세 집단 간 평균 차이 검정 - 2
oneway.test(data = exdata1, Y20_CNT ~ AREA, var.equal = T)


