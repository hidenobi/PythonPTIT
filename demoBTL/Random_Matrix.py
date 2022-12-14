import sys
from random import choice as ch
import pygame

def generate_maze(screen, N, M, printmtx):
	a = [[1 for i in range(M)] for j in range(N)]
	# 0->3 = down,right,up,left
	dy = [1, 0, -1, 0]
	dx = [0, 1, 0, -1]
	stck = []
	check_y = [[0, 0, 1, 1, 1], [-1, -1, 0, 1, 1], [-1, -1, -1, 0, 0], [-1, -1, 0, 1, 1]]
	check_x = [[-1, 1, -1, 0, 1], [0, 1, 1, 1, 0], [-1, 0, 1, -1, 1], [-1, 0, -1, -1, 0]]

	def oob(y, x):
		return y <= 0 or y >= N - 1 or x <= 0 or x >= M - 1

	def check(y, x, choice):
		new_y = y + dy[choice]
		new_x = x + dx[choice]
		if oob(new_y, new_x): return False
		for i in range(5):
			if not a[new_y + check_y[choice][i]][new_x + check_x[choice][i]]: return False
		return True

	def print_mtx(screen, N, M,stck,a):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		vis = [[False for i in range(M)] for j in range(N)]
		for i in stck:
			y = i[0]
			x = i[1]
			pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(40 + x * 30, 30 + y * 30, 30, 30))
			vis[y][x] = True
		for i in range(N):
			for j in range(M):
				if not vis[i][j]:
					if a[i][j] == 1:
						pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(40 + j * 30, 30 + i * 30, 30, 30))
					else:
						pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(40 + j * 30, 30 + i * 30, 30, 30))
		pygame.display.update()

	# outer layer is wall, generate maze inside first then add entrance-exit
	a[1][1] = 0
	st = []
	stck = []
	st.append([1, 1, [0, 1, 2, 3]])
	stck.append([1, 1])
	while len(st) > 0:
		p = st[-1]
		# print(p[0],p[1])
		a[p[0]][p[1]] = 0
		if printmtx == 1:
			# pygame.time.delay(10)
			print_mtx(screen,N,M,stck,a)
		if len(p[2]) > 0:
			option = ch(p[2])
			# print("options:",p[2])
			# print("option:", option)
			p[2].remove(option)
			if check(p[0], p[1], option):
				st.append([p[0] + dy[option], p[1] + dx[option], [0, 1, 2, 3]])
				stck.append([p[0] + dy[option], p[1] + dx[option]])
		else:
			st.pop()
			stck.pop()
	# done generating inside of matrix, now add entrance-exit
	# entrance has x = 0 and y range from 1 to N-1
	# exit has x = M-1 and y range from 1 to N-1
	scope = [i+1 for i in range(N-1)]
	while True:
		start_y = ch(scope)
		if not a[start_y][1]:
			a[start_y][0] = 8
			break
	while True:
		end_y = ch(scope)
		if not a[end_y][M-2]:
			a[end_y][M-1] = 9
			break
	return a

def output_to_file(N, M, a):
	f = open("assets/Matrix/Matrix_level_5.txt",'w')
	for i in range(N):
		for j in range(M):
			f.write(str(a[i][j]) + ' ')
		f.write('\n')
	f.close()


