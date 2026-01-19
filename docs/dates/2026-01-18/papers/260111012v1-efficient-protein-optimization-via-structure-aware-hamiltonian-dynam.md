---
layout: default
title: Efficient Protein Optimization via Structure-aware Hamiltonian Dynamics
---

# Efficient Protein Optimization via Structure-aware Hamiltonian Dynamics
**arXiv**：[2601.11012v1](https://arxiv.org/abs/2601.11012) · [PDF](https://arxiv.org/pdf/2601.11012.pdf)  
**作者**：Jiahao Wang, Shuangjia Zheng  

**一句话要点**：提出HADES方法，利用哈密顿动力学进行结构感知的蛋白质序列优化，以解决高维复杂性和结构约束问题。

**关键词**：蛋白质优化, 哈密顿动力学, 贝叶斯优化, 结构感知, 序列设计, 编码器-解码器

## 3 点简述
- 核心问题：蛋白质优化面临高维复杂性，现有序列方法忽略结构约束和上位效应。
- 方法要点：采用贝叶斯优化，结合哈密顿动力学采样，通过两阶段编码器-解码器学习结构-功能关系。
- 实验或效果：在硅评估中优于基线，能设计结构相似且性质优化的蛋白质序列。

## 摘要（原文）

> The ability to engineer optimized protein variants has transformative potential for biotechnology and medicine. Prior sequence-based optimization methods struggle with the high-dimensional complexities due to the epistasis effect and the disregard for structural constraints. To address this, we propose HADES, a Bayesian optimization method utilizing Hamiltonian dynamics to efficiently sample from a structure-aware approximated posterior. Leveraging momentum and uncertainty in the simulated physical movements, HADES enables rapid transition of proposals toward promising areas. A position discretization procedure is introduced to propose discrete protein sequences from such a continuous state system. The posterior surrogate is powered by a two-stage encoder-decoder framework to determine the structure and function relationships between mutant neighbors, consequently learning a smoothed landscape to sample from. Extensive experiments demonstrate that our method outperforms state-of-the-art baselines in in-silico evaluations across most metrics. Remarkably, our approach offers a unique advantage by leveraging the mutual constraints between protein structure and sequence, facilitating the design of protein sequences with similar structures and optimized properties. The code and data are publicly available at https://github.com/GENTEL-lab/HADES.

