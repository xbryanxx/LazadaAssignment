
1. Before run, need to make some local changes in LazadaAuto.py, make sure web drive is in this path, '~/automation/LazadaAutoPython/chromedriver'

2. There are an video in the reports folder to demonstrate the first scenario

3. Areas to improve
-> an error occurs after slider button is performed, during the login. Tentative walk-around is choose google login manually

-> to handle relative path for webdriver

-> Makes use of json to store all elements	

-> to screen capture when fails

-> create helper files to handle web driver or explicit wait

-> to generate better reports
	brew install allure

	pip install allure-behave

	behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features