# M-SHAPE PROJECT 

### Objectives 
Detect Forehead baldness by calculating the ratio between vertical lines length on 
- central forehead  
- left forehead  
- right forehead  

### Hypothesis
If the ratio between central & left & right is imbalanced (and passed our defined threshold), we could classify that the user has forehead baldness

### Challenges
- Picture orientation (object is skewed to an axis,  not centered)<br>
![face cropped]
(bad_examples\6.jpg)


- Bad Contrast (can be overcomed by performing gamma correction)<br>

- Too Close<br>
![tooclose](bad_examples\1.jpg)

- Over Exposed (on bangs)<br>
![Over Exposed](bad_examples\8.jpg)


### Procedure

![reference](81_points_reference.jpg)

### Commands
for a list of images <br>
`python main.py`<br>
for single images
`python main.py --single=<PATH>`

# FNC (Receding Hairline) PROJECT

### Commands
`python main.py --m_shape=False`