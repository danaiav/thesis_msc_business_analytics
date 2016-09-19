loading_times <- read.csv("F:/Dropbox/Dani/Spinellis - Diplwmatiki/Python Scripts/infos/loading_times.csv", sep=";")
loading_times$loading.time <- format(loading_times$loading.time, decimal.mark=",")
str(loading_times)
loading_times$X <- NULL
write.csv2(loading_times, file = "F:/Dropbox/Dani/Spinellis - Diplwmatiki/Python Scripts/infos/loading_time.csv", sep=";")
