# Conway
Conway is a dataset containing 100,000 instances that of Conway's game of life. 

### Data 
Inside of the compressed `data` folder, there are folders for each game 
instance. Each of these folders contains a `start.npy` and 
`end.npy`, which contain NumPy arrays of the game's initial 
and ending conditions. 
- Each grid is 50x50, and the grid boundaries are concrete 
(e.g. left/right top/bottom boundaries do not connect like an 
infinite plain).
- The games follow the traditional rules

The compressed `data` folder also contains a `games.csv`, which contains the
following (each row represents 1 game):
- Paths to `start.npy` and `end.npy`
- Number of living cells at the start of the game. This should 
average around 10% of the map size, or around 250 cells.
- Number of living cells at the end of the game.
- Steps performed (will be 100,000 unless all cells have died)
