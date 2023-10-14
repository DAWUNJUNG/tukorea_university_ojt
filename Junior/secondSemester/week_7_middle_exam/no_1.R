sum <- 0
for (i in 1:100) {
  sum <- sum + i
  i <- i + 1
}
cat(sum)