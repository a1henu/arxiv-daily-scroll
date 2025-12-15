---
layout: default
title: Three methods, one problem: Classical and AI approaches to no-three-in-line
---

# Three methods, one problem: Classical and AI approaches to no-three-in-line
**arXiv**：[2512.11469v1](https://arxiv.org/abs/2512.11469) · [PDF](https://arxiv.org/pdf/2512.11469.pdf)  
**作者**：Pranav Ramanathan, Thomas Prellberg, Matthew Lewis, Prathamesh Dinesh Joshi, Raj Abhijit Dandekar, Rajat Dandekar, Sreedath Panat  

**一句话要点**：比较经典优化与AI方法解决无三点共线问题，提出混合方法以扩展规模

**关键词**：无三点共线问题, 整数线性规划, 变换器学习, 强化学习, 组合几何, 混合优化

## 3 点简述
- 研究无三点共线问题，寻求n×n网格中最大非共线点集
- 应用整数线性规划、PatternBoost变换器学习和PPO强化学习三种方法
- ILP在19×19网格内最优，PatternBoost在14×14网格内匹配最优，PPO在10×10网格内完美但11×11失败

## 摘要（原文）

> The No-Three-In-Line problem asks for the maximum number of points that can be placed on an n by n grid with no three collinear, representing a famous problem in combinatorial geometry. While classical methods like Integer Linear Programming (ILP) guarantee optimal solutions, they face exponential scaling with grid size, and recent advances in machine learning offer promising alternatives for pattern-based approximation. This paper presents the first systematic comparison of classical optimization and AI approaches to this problem, evaluating their performance against traditional algorithms. We apply PatternBoost transformer learning and reinforcement learning (PPO) to this problem for the first time, comparing them against ILP. ILP achieves provably optimal solutions up to 19 by 19 grids, while PatternBoost matches optimal performance up to 14 by 14 grids with 96% test loss reduction. PPO achieves perfect solutions on 10 by 10 grids but fails at 11 by 11 grids, where constraint violations prevent valid configurations. These results demonstrate that classical optimization remains essential for exact solutions while AI methods offer competitive performance on smaller instances, with hybrid approaches presenting the most promising direction for scaling to larger problem sizes.

