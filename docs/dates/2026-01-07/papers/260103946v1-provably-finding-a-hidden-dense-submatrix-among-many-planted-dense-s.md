---
layout: default
title: Provably Finding a Hidden Dense Submatrix among Many Planted Dense Submatrices via Convex Programming
---

# Provably Finding a Hidden Dense Submatrix among Many Planted Dense Submatrices via Convex Programming
**arXiv**：[2601.03946v1](https://arxiv.org/abs/2601.03946) · [PDF](https://arxiv.org/pdf/2601.03946.pdf)  
**作者**：Valentine Olanubi, Phineas Agar, Brendan Ames  

**一句话要点**：提出凸规划方法，在含多个稠密子矩阵的随机或对抗性矩阵中可证明找到隐藏稠密子矩阵。

**关键词**：稠密子矩阵问题, 凸规划, 随机块模型, 图论优化, 网络分析

## 3 点简述
- 研究稠密子矩阵问题，扩展至含多个稠密子矩阵的现实场景。
- 建立多项式时间可解和完美恢复的充分条件，基于随机块模型推广。
- 通过随机生成实例和真实网络实验验证理论相变。

## 摘要（原文）

> We consider the densest submatrix problem, which seeks the submatrix of fixed size of a given binary matrix that contains the most nonzero entries. This problem is a natural generalization of fundamental problems in combinatorial optimization, e.g., the densest subgraph, maximum clique, and maximum edge biclique problems, and has wide application the study of complex networks. Much recent research has focused on the development of sufficient conditions for exact solution of the densest submatrix problem via convex relaxation. The vast majority of these sufficient conditions establish identification of the densest submatrix within a graph containing exactly one large dense submatrix hidden by noise. The assumptions of these underlying models are not observed in real-world networks, where the data may correspond to a matrix containing many dense submatrices of varying sizes.
>   We extend and generalize these results to the more realistic setting where the input matrix may contain \emph{many} large dense subgraphs. Specifically, we establish sufficient conditions under which we can expect to solve the densest submatrix problem in polynomial time for random input matrices sampled from a generalization of the stochastic block model. Moreover, we also provide sufficient conditions for perfect recovery under a deterministic adversarial. Numerical experiments involving randomly generated problem instances and real-world collaboration and communication networks are used empirically to verify the theoretical phase-transitions to perfect recovery given by these sufficient conditions.

