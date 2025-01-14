## Plotting with Pylab and Matplotlib

Over the past few weeks we have explored different computational methods and processes.  In those said methods and processes we generated data in the form of lists, tuples, and libraries.  But simply looking at those data types is not very useful.  We now need the ability to take the data and to put it into a figure of some kind.

Pylab contains a _plot_ module that allows the plotting of data.  Pylab utilizes the _matplotlib_ library.  The greatest thing about _matplotlib_ is there is an enormous set of resources online and many pre-made figures that can be adapted to your needs.  

One confusing thing is that you can use _pylab_ or you can use the _matplotlib_ library directly.  

```python

import pylab

import matplotlib.pyplot as plt 
```

[According to this](https://stackoverflow.com/questions/16849483/which-is-the-recommended-way-to-plot-matplotlib-or-pylab) StackOverflow post, pylab and matplotlib do the exact same thing it is simply a different way to use it.  Let's first explore _pylab_ then we can explore plotting use _matplotlib_.

### Pylab

In order to start plotting, we will first need some data.  Run the following code to generate a list of numbers.

```python
l = []
for i in range(1,100):
    l.append((i**3)/2.0)
```
The previous script generated a list of numbers.  Remember that lists are ordered so we can simply plot these numbers and they will be plotted in order.  To plot, first import pylab and then use the _plot_ method.

```python
import pylab

pylab.plot(l)
pylab.show()
```
If it worked correctly, a separate window should have opened with the list plotted as a line graph.  Pretty cool, huh?  It really is that easy for a basic line graph.  If you like, you can modify the plot to look different.

```python
pylab.plot(l, linewidth = 10, color='r')
pylab.show()
```
The above code actually changed the plot to have a thicker line width and a different color.  

But figures are useless unless they have labels.  Consider, adding y- and x-labels to your figures.  Try typing, pylab.y and hit tab to bring up options.  When you choose a method, open parenthesis and Canopy will open a dialog box showing what can be added.

You can find other basic tutorial [here](http://jakevdp.github.io/mpl_tutorial/tutorial_pages/tut1.html) which also includes some basic examples of _numpy_.

### Quick exercise: Trying a pie chart

pylab has numerous method for plotting different chart types -- _bar_, _barh_, etc.  Let's try _pie_ for a pie chart.  Consider the following data:

```python
grades = [30, 40, 20, 5, 5]
letters = ['A', 'B', 'C', 'D', 'F']
```
These are obviously the percenages of different letter grades with percentages in one list and the corresponding letter grade in the other list.  Plot these _pylab.pie_ and generate a legend and title to go with the figure.  See the [pie chart demo](https://matplotlib.org/gallery/pie_and_polar_charts/pie_demo2.html#sphx-glr-gallery-pie-and-polar-charts-pie-demo2-py) on the matplotlib demo page to see tips like exploding wedges.  Remember this is _matplotlib_ syntax so _pylab_ will be slightly different.  

### Using matplotlib

As you will see, using _matplotlib_ it is essentially the same as using _pylab_.  Let's start off with [a simple line graph](https://matplotlib.org/gallery/pyplots/pyplot_simple.html#sphx-glr-gallery-pyplots-pyplot-simple-py) as demonstration.  But instead of the demonstration data, let's use the data generated from above.

```python
l = []
for i in range(1,100):
    l.append((i**3)/2.0)

import matplotlib.pyplot as plt

plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()
```

### Problem #1 

Write a function or procedural code to calculate yearly compounding interest with a specific annual percentage rate.  Here is some static variables to start you off in solving this problem.  

```python
principal = 10000 #initial investment
interestRate = 0.05
years = 20
```

After you have calcualted the interest for 20 to 30 years, plot the results in a line graph.  Make sure to give it a title, legend, and x/y labels.