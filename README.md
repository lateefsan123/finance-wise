# finance-wise

FinanceWise is a desktop and android application. The app is intended to allow users to be more organised with their finances and spending. The app is to be downloaded onto a mobile phone via apk uploaded on mediafire (further plans for Google Play Store).
Upon download, a user can sign up and create an account using an email address and suitable password.

FinanceWise can accept new users into the system via a sign up page, using an email address and a password. It can also recognise existing users and grant them access to the interface if the login information is correct. 
FinanceWise is capable of providing graph representation of the users income and expenses over the last 3 years and also provides a pie chart showing the user which expense category is using up the most of their money.
You can add an expense to your account by manually entering the expense or via ocr, the ocr feature has a daily quota because the price of the api is very costly($400 a month) so we had to settle with  the free trial..
The app allows you to check how much you spent on a specific date.
The system can allow users to write down notes and store them in the notes scrollview,
FinanceWise is also capable of storing files and receipts in the users database. 
FinanceWise can provide charting such as bar charts, line charts and pie charts for further user analysis. 

The frontend was designed using kivy, and the backend was developed using python and firebase. The Kivy frontend communicates with the python backend by sending functions to the kivy widgets. We also used the aspire api for the receipt parsing. 
