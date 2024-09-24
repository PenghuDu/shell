#!/usr/bin/env python
#function: write sbatch shell script of slurm job system in PKU. 
#edited by Dupenghu, 20210803

f = open('job.sh', 'w')
print('#!/bin/sh', file=f)
print('#SBATCH -J *		#--job-name', file=f)
print('#SBATCH -o %x.o%j	#--output', file=f)
print('#SBATCH -e %x.e%j	#--error', file=f)
print('#SBATCH -p C032M0256G	#--partition', file=f)
print('#SBATCH -q low		#--qos', file=f)
print('#SBATCH -N 1		#--nodes', file=f)
print('#SBATCH --ntasks-per-node=4', file=f)
print('#SBATCH -c 1		#--cpu-per-task', file=f)
print('#SBATCH -t 05-00:00:00	#--time\n', file=f)

print('#导入运行环境', file=f)
print('module purge', file=f)
print('module load intel/2018.1\n', file=f)

print('#mpi跨节点运行', file=f)
print('#mpirun -n 32 *', file=f)
print('python *.py', file=f)

f.close()
