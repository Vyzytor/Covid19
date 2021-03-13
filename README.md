# Covid19
Project contains a flask app that queries google big query storage (holds two arima models and etl of NYT Covid19 dataset) and returns latest cases/deaths stats for US and territories, along with prediction for cases/deaths 30 days out.
Vyzytor-patch-1 is the development environment, subject to linting from both CircleCI and GitActions. Master is the production environment that is linked to Google Cloud Platform.
