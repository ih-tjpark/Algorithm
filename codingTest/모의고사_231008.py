# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# 각 목적지의 최소거리를 구하고 더하기
from collections import deque
N, K = map(int,input().split())

board = [list(map(int,input().split()))for _ in range(N)]


def bfs(sx, sy, goal):
	row, col = len(board), len(board[0])
	visited = [[0]*col for _ in range(row)]
	
	dir = [(0,1),(0,-1),(1,0),(-1,0)]
	#print(sx,sy)
	que = deque([[sx, sy]])
	
	visited[sx][sy] = 0
	
	while que:
		bx, by = que.popleft()
		for dx, dy in dir:
			x = bx + dx
			y = by + dy
			
			if 0<=x<col and 0<=y<row and visited[y][x]<1:
				visited[y][x] = visited[by][bx] + 1
				que.append([x,y])
				
				if board[y][x] == goal:
					return x, y, visited[y][x]
	
start_x, start_y = 0, 0
result_move = 0
for i in range(K):
	goal = i+1
	
	start_x, start_y, move = bfs(start_x, start_y, goal)
	
	if goal > 1:
		result_move += move
		
	print(result_move)
