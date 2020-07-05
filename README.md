<p align="center">
  <a href="" rel="noopener">
 <img height=100px src="./img/dino.png" alt="dino-logo"></a>
</p>
<h1 align="center">teachable dinosaur</h1>


<div align="center">
<img src="https://img.shields.io/github/license/sushantPatrikar/teachable-dinosaur">	
<img src="https://www.codefactor.io/repository/github/sushantpatrikar/teachable-dinosaur/badge?s=47db980d7cbdc347f8775087b22eee938231b691">
<img src="https://img.shields.io/github/issues/sushantPatrikar/teachable-dinosaur">
<img src="https://img.shields.io/github/stars/sushantPatrikar/teachable-dinosaur">
<img src="https://img.shields.io/github/forks/sushantPatrikar/teachable-dinosaur">
<img src="https://img.shields.io/github/issues/sushantPatrikar/teachable-dinosaur">
<img src="https://img.shields.io/badge/PRs-welcome-informational">
</div>

<h4 align="center">Dinosaur game, but in a Machine Learning way</h4>

<hr>

<p align="center">
<img src = "./img/demo-lite.gif" height=400 width=800>
</p>

<h2>How to use:</h2>

Clone this repsitory using the following command:
```
$ git clone https://github.com/sushantPatrikar/teachable-dinosaur.git
```

After cloning, run "train.py" file.

When you run the file, an opencv frame will pop up, here you have to give the dataset for training.

<p align="center">
<img src = "./img/demo_run.gif" height=200 width=200>
</p>

Make a gesture which will tell the dinosaur to run. For example, in my case, it was a closed fist. When you are ready with the gesture, press the 's' key on your keyboard. This will capture 1500 burst shots of your gesture.

<p align="center">
<img src = "./img/demo_jump.gif" height=200 width=200>
</p>

After this step, the similar opencv window will pop up, now make another gesture that will tell the dinosaur to jump. In my case, it was the open palm. Again press 's' key on your keyborad when you are ready. This will take another 1500 burst shots. 

Note: Don't keep your gesture as it is for all the 1500 burst shots. Keep the gesture moving little after some interval. This is to avoid overfitting of the model.

After doing this, the program will train the convolutional neural network on your dataset. Once the cnn is trained you will have a new file "weights.h5"

Now you are ready to play the game. Run "game.py" and enjoy!
