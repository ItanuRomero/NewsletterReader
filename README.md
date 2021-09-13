# NewsletterReader
You really do NOT have time for read a newsletter? Now you can listen to it

The [Newsletter of Filipe Deschamps](https://filipedeschamps.com.br/newsletter)
is a great place to read the most recent news about technologies and do not spend much time on it


The problem to me is: **I forget**, I'm **feeling lazy**, or maybe **I really don't have time**,
even the most simple and summed up content can be a little hard to read, so...

## I create this text-to-speach bot
The bot will open your gmail account with [easyimap](https://pypi.org/project/easyimap/) and get one of the newsletters send by Filipe.

Then it will transform the email to speach with [pyttsx3](https://pypi.org/project/pyttsx3/)

## how use it:
- Subscribe to the newsletter [clicking here](https://filipedeschamps.com.br/newsletter)
- Install the dependencies
- Create a txt file with the name "userAndPassword.txt"
- Write on this txt your gmail and your password
  - Like: 
  ``` 
  yourAccount@gmail.com
  yourPassword    
  ```
- Run the program and listen the news :)
