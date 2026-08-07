# Settlers of Catan Dice Tracker
Have you eved wondered just how much you are getting screwed over by the dice in your Catan games? Well, wonder no longer! Because now you can use this handy tool (_which I initially smashed out in a couple of hours in a state of exasperated catharsis and now doing it to procrastinate work_) to find out! It's janky and hastly made and looks terrible and uses questionable maths and was probably a waste of time, but hey!,... ummm... I'm not sure what's the silver lining here. 

![screenshot](/assets/example.png)

## Quick guide
1. Run `cdt.py`.
2. Click on checkboxes in the Roll statistics table to 'build' settlements. 
3. Enter your dice rolls in 'New roll'.
4. Click 'Roll for me' if you cannot be bothered rolling and entering the dice yourself. The roll is weighted for 2d6.
5. Look at ~pretty~ numbers and colours! You can change colours and gradient limits in `config.toml`.
6. You can 'build' more settlements as you're rolling new dice. The program remembers which turn the settlement was built and will account for that when calculating stats. 
7. Click 'Delete last roll' to... delete last roll. This will also 'unbuild' any settlements built that turn. 
8. Click 'Reset everything' to start from scratch.

## Todo list:
- [ ] add robber functionality
- [x] add colour config so you can choose your own _prettier_ colours
- [x] add clear all button w warning
- [x] fix delete last roll behaving funky with later build settlements
- [ ] save game record?
- [ ] anything else I can think of and bother doing
