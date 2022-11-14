# Overview

This repository contains my solution for Conway's Game of Life that I developed after attending the [Gloabl Day of Coderetreat in Madrid](https://www.eventbrite.co.uk/e/entradas-global-day-of-coderetreat-madrid-431835300007) in Python 

# Game of Life Kata

This Kata is about calculating the next generation of Conway’s Game of Life, given any starting state.

You start with a two dimensional grid of cells, where each cell is either alive or dead. In this version of the problem, the grid is finite, and no life can exist off the edges. When calculating the next generation of the grid, follow these rules:

* Any live cell with fewer than two live neighbours dies (referred to as underpopulation or exposure).
* Any live cell with more than three live neighbours dies (referred to as overpopulation or overcrowding).
* Any live cell with two or three live neighbours lives, unchanged, to the next generation.
* Any dead cell with exactly three live neighbours will come to life.

The code should allow for the board/world to be created with a valid initial state, or a randomly generated state.
