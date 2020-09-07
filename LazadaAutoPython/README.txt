
1. Before run, 
	need to make some local changes in LazadaAuto.py, make sure web drive is in this path, '~/automation/LazadaAutoPython/chromedriver'
	need to install behave, selenium and python3
	
2. Run the scripts via command line, behave features/LazadaAuto.feature

3. I have included an video to demonstrate the first scenario in this link, https://drive.google.com/file/d/1R6-4-l91UHNT_twxDnQMmPqiRdVaWPVN/view?usp=sharing

4. Areas to improve
-> an error occurs after slider button is performed, during the login. Tentative walk-around is choose google login manually

-> to handle relative path for webdriver

-> Makes use of json to store all elements	

-> to screen capture when fails

-> create helper files to handle web driver or explicit wait

-> to generate better reports
	brew install allure

	pip install allure-behave

	behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features
