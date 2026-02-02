---
layout: default
title: An Efficient Algorithm for Thresholding Monte Carlo Tree Search
---

# An Efficient Algorithm for Thresholding Monte Carlo Tree Search
**arXiv**：[2601.22600v1](https://arxiv.org/abs/2601.22600) · [PDF](https://arxiv.org/pdf/2601.22600.pdf)  
**作者**：Shoma Nameki, Atsuyoshi Nakamura, Junpei Komiyama, Koji Tabata  

**一句话要点**：提出基于Track-and-Stop的阈值蒙特卡洛树搜索算法，以解决树根节点值是否超过阈值的判定问题。

**关键词**：蒙特卡洛树搜索, 顺序采样, 渐近最优性, 计算复杂度优化, 阈值判定

## 3 点简述
- 核心问题：阈值蒙特卡洛树搜索问题，需判定给定树根节点值是否至少为阈值θ。
- 方法要点：开发δ-正确顺序采样算法，基于Track-and-Stop策略，具有渐近最优样本复杂度。
- 实验或效果：通过比率修正D-Tracking策略，显著降低经验样本复杂度和每轮计算成本。

## 摘要（原文）

> We introduce the Thresholding Monte Carlo Tree Search problem, in which, given a tree $\mathcal{T}$ and a threshold $θ$, a player must answer whether the root node value of $\mathcal{T}$ is at least $θ$ or not. In the given tree, `MAX' or `MIN' is labeled on each internal node, and the value of a `MAX'-labeled (`MIN'-labeled) internal node is the maximum (minimum) of its child values. The value of a leaf node is the mean reward of an unknown distribution, from which the player can sample rewards. For this problem, we develop a $δ$-correct sequential sampling algorithm based on the Track-and-Stop strategy that has asymptotically optimal sample complexity. We show that a ratio-based modification of the D-Tracking arm-pulling strategy leads to a substantial improvement in empirical sample complexity, as well as reducing the per-round computational cost from linear to logarithmic in the number of arms.

