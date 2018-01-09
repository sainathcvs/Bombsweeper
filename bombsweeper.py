import string
import random
def show_grid(grid,grid_size):
	horizontal = '   ' + (4 * grid_size * '-') + '-'
	# Print top column letters
	toplabel = '     '
	for i in string. ascii_lowercase[:grid_size]:
	    toplabel = toplabel + i + '   '

	print(toplabel + '\n' + horizontal)

	# Print left row numbers
	for cnt, i in enumerate(grid):
	    row = '{0:2} |'.format(cnt + 1)
	    for j in i:
	        row = row + ' ' + str(j) + ' |'

	    print(row + '\n' + horizontal)
	print('')

def sel_random_cell(len_grid):
	return(random.randint(0,len_grid-1),random.randint(0,len_grid-1))
	
def select_bombs(len_grid,bombs_no,grid):
	bomb_cells=[]
	while len(bomb_cells)<bombs_no:
		bomb_cell = sel_random_cell(len_grid)
		while bomb_cell in bomb_cells:
			bomb_cell = sel_random_cell(len_grid)
		bomb_cells.append(bomb_cell)
	return bomb_cells

def get_counts(bomb_cells,len_grid,grid,grid1):
	val_arr={}
	for i in range(len_grid):
		for j in range(len_grid):
			if (i,j) not in bomb_cells:
				val_ij = 0
				if (i-1,j+1) in bomb_cells:
					val_ij+=1
				if (i,j+1) in bomb_cells:
					val_ij+=1
				if (i+1,j+1) in bomb_cells:
					val_ij+=1
				if (i-1,j) in bomb_cells:
					val_ij+=1
				if (i+1,j) in bomb_cells:
					val_ij+=1
				if (i-1,j-1) in bomb_cells:
					val_ij+=1
				if (i,j-1) in bomb_cells:
					val_ij+=1
				if (i+1,j-1) in bomb_cells:
					val_ij+=1
				grid[i][j]=val_ij
			else:
				grid[i][j] = 'X'
				grid1[i][j] = 'X'
	return val_arr

def get_grid(grid_size,bombs_no,grid,grid1):
    bomb_cells = select_bombs(grid_size,bombs_no,grid)
    val_arr=get_counts(bomb_cells,grid_size,grid,grid1)
    # show_grid(grid,grid_size)
    #original grid done
    return bomb_cells

def play_game():
	try:
		print '\nStarting GAME'
		print '------------------------------------------\n'
		grid_size = 8
		bombs_no = 10
		#initialize the playing grid
		curr_grid = [[' ' for i in range(grid_size)] for i in range(grid_size)]
		show_grid(curr_grid,grid_size)
		flags_set=[]
		grid=[[' ' for i in range(grid_size)] for i in range(grid_size)]
		grid1=[[' ' for i in range(grid_size)] for i in range(grid_size)]
		bomb_cells = get_grid(grid_size,bombs_no,grid,grid1)
		while 1:
			bombs_left = bombs_no-len(flags_set)
			input_cell = input('Enter the next cell ({} bombs left): '.format(bombs_left))
			rowno,colno,flag = input_cell
			if rowno>grid_size or colno>grid_size:
				print '---------------ERROR:::Enter valid grid values---------------\n'
			else:
				if flag=='T' or flag=='t':
					flag=True
				else:
					flag = False
				cell=(rowno-1,colno-1)#in coord-syste
				if flag:
					if cell in flags_set:
						print '---------------INFO:::Flag already set---------------\n'
					else:
						curr_grid[rowno-1][colno-1] = 'F'
						flags_set.append((rowno-1,colno-1))
				else:
					if cell not in flags_set and cell in bomb_cells:
						show_grid(grid,grid_size)
						print 'GAME OVER'
						return -1
					elif cell not in flags_set:
						curr_grid[rowno-1][colno-1] = grid[rowno-1][colno-1]
					elif cell in flags_set:#remove F
						curr_grid[rowno-1][colno-1] = ''
						flags_set.remove(cell)
				show_grid(curr_grid,grid_size)
	except:
		print '---------------ERROR:::UNFORTUNATELY STOPPED---------------'
	return 0

status = play_game()
while status==-1:
	prompt = input('Want to restart?(1/0):')
	if prompt==1:
		status=play_game()
	else:
		exit(0)

#grid-0 to 7
#curr_grid-0 to 7
#bomb_cells 0 to 7
#input 1-8