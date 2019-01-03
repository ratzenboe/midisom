# Midisom

Self Organizing Maps
--------------------

Midisom is a a fork to the [MiniSom](https://github.com/JustGlowing/minisom) package which is a minimalistic and Numpy based implementation of the Self Organizing Maps (SOM) 
created by Giuseppe Vettigli. 
The Midisom package adds minor extensions such as the [tqdm](https://tqdm.github.io/) status bar for training the SOM and also adds multiple plotting member function for easy, convenient, and fast
results.

Installation
---------------------

Download MidiSom to a directory of your choice via
```
  git clone https://github.com/ratzenboe/midisom
```
change into the created directory and execute the setup script

```
  python setup.py install
```

How to use it
---------------------

In constrast to the original Minisom package Midisom works with `pandas` DataFrames as well as with `numpy` arrays. The newly added plotting functions in fact currently rely on 
the input data to be `pandas` DataFrames. 

```python
from midisom import MidiSom    
som = MidiSom(20, 20, df_data.shape[-1], sigma=2.0, learning_rate=0.5) # initialization of 20x20 SOM
q_error,iter_x = som.train_error(df_data, init=True, rand=True, err_update=df_data.shape[0]//100) # trains the SOM and calculates the quantisation error 100 times

# plotting the quantisation error
from matplotlib import pyplot as plt
plt.plot(iter_x, q_error)

# Plotting the distance map (if target is available, else target=None)
som.plot_distance_map(df_data, target, n_samples=-1) # plots all n_samples onto the som grid - this may take a while (value should be below 10^5 for sensible run times); for unsupervised: target=None
# Plotting the individual feature distributions
som.plot_feat_dist(df_data)
# Plotting the most important features per cell 
som.plot_most_imp_feat(df_data)
# (Supervised) Plotting a map where the individual classes have landed
som.plot_label_map(df_data, target)
# Plotting activation response (count where the most instances lie)
som.plot_activation_response(df_data, target, n_samples=-1) # for unsupervised: target=None
```
## Licence 
Midisom builds upon the Minisom package developed by Giuseppe Vettigli which is licensed under the Creative Commons Attribution 3.0 Unported License. 
Therefore, the use of the Midisom package also falls under the same terms of use, do not fall short to give credit to Giuseppe Vettigli if you use this software!
To view a copy of this license, visit http://creativecommons.org/licenses/by/3.0/.
![License]( http://i.creativecommons.org/l/by/3.0/88x31.png "Creative Commons Attribution 3.0 Unported License")
