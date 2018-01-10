from Tkinter import *
import string
import random
global gameover
gameover= False
def reveal_blank_blocks(row,col):
	print 'reveal_blank_blocks---'

def show_grid(grid,grid_size):

	for i in range(grid_size):
		for j in range(grid_size):
			if grid[i][j]=='X':
				# photo=PhotoImage(file="root.png")
				# button=Button(image=photo,width="40",height="40",compound=RIGHT,command=lambda row=i,col=j: btn_callback(row,col))
				button=Button(width="3",height="3",bg='Red',state=NORMAL,command=lambda row=i,col=j: btn_callback(row,col))
			elif grid[i][j]==0:
				button=Button(width="3",height="3",bg='Grey',state=NORMAL,command=lambda row=i,col=j: btn_callback(row,col))
			else:
				button=Button(width="3",height="3",state=NORMAL,text=grid[i][j],command=lambda row=i,col=j: btn_callback(row,col))
			# button.bind('<ButtonPress-1>', lambda event, row=i,col=j: btn_callback(row,col))
			button.grid(row=i,column=j)
	mainloop()

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
		global gameover
		global grid_size
		global flags_set
		global bomb_cells
		global grid
		global grid1
		global curr_grid
		gameover= False
		grid_size = 8
		bombs_no = 10
		#initialize the playing grid
		curr_grid = [[' ' for i in range(grid_size)] for i in range(grid_size)]
		flags_set=[]
		grid=[[' ' for i in range(grid_size)] for i in range(grid_size)]
		grid1=[[' ' for i in range(grid_size)] for i in range(grid_size)]
		bomb_cells = get_grid(grid_size,bombs_no,grid,grid1)
		show_grid(curr_grid,grid_size)
	except:
		print '---------------ERROR:::UNFORTUNATELY STOPPED---------------'
	return 0

def btn_callback(row,col):
	# if not gameover:
	flag=False
	if row>grid_size or col>grid_size:
		print '---------------ERROR:::Enter valid grid values---------------\n'
	else:
		if flag=='T' or flag=='t':
			flag=True
		else:
			flag = False
		cell=(row,col)#in coord-syste
		if flag:
			if cell in flags_set:
				print '---------------INFO:::Flag already set---------------\n'
			else:
				curr_grid[row][col] = 'F'
				flags_set.append((row,col))
		else:
			if cell not in flags_set and cell in bomb_cells:
				show_grid(grid,grid_size)
				print 'GAME OVER'
				gameover = True
				return -1
			elif grid[row][col]==0:
				reveal_blank_blocks(row,col)
			elif cell not in flags_set:
				curr_grid[row][col] = grid[row][col]
			elif cell in flags_set:#remove F
				curr_grid[row][col] = ''
				flags_set.remove(cell)
	show_grid(curr_grid,grid_size)

gameover= False
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