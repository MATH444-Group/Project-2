DATA_DIR <- "../data/cleaned/"
DATA_FILE <- "cleaned car details v4.csv"
DATA_PATH <- paste0(DATA_DIR, DATA_FILE)

MODEL_DIR <- "../models/"


if (!file.exists(DATA_PATH)) {
  stop(message(paste0("[[ CRITICAL ERROR ]]\nData \"", DATA_FILE, "\" not found in data directory \"", DATA_DIR, "\"\n")))
}

data <- read.csv(DATA_PATH)

source("reduction.r")
reducedData <- dropUncorrelatedPredictors(data = data, responseVariable = "Price")
reducedData <- dropHighCollinearPredictors(data = reducedData, responseVariable = "Price")





source("aic.r")
runAIC(data = reducedData, summarize = TRUE, counts = TRUE)

source("bic.r")
runBIC(data = reducedData, summarize = TRUE, counts = TRUE)