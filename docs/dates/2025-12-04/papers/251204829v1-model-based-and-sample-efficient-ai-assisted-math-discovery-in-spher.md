---
layout: default
title: Model-Based and Sample-Efficient AI-Assisted Math Discovery in Sphere Packing
---

# Model-Based and Sample-Efficient AI-Assisted Math Discovery in Sphere Packing
**arXiv**：[2512.04829v1](https://arxiv.org/abs/2512.04829) · [PDF](https://arxiv.org/pdf/2512.04829.pdf)  
**作者**：Rasul Tutunov, Alexandre Maraval, Antoine Grosnit, Xihan Li, Jun Wang, Haitham Bou-Ammar  

**一句话要点**：提出基于模型的样本高效AI辅助方法，在球体堆积问题中实现新上限

**关键词**：球体堆积, 半定规划, 贝叶斯优化, 蒙特卡洛树搜索, 样本高效学习, AI辅助数学发现

## 3 点简述
- 核心问题：解决高维球体堆积的密度上限问题，传统方法计算成本高。
- 方法要点：将SDP构建建模为序列决策过程，结合贝叶斯优化与蒙特卡洛树搜索。
- 实验或效果：在4-16维获得新的最优上限，验证模型在计算受限几何问题中的有效性。

## 摘要（原文）

> Sphere packing, Hilbert's eighteenth problem, asks for the densest arrangement of congruent spheres in n-dimensional Euclidean space. Although relevant to areas such as cryptography, crystallography, and medical imaging, the problem remains unresolved: beyond a few special dimensions, neither optimal packings nor tight upper bounds are known. Even a major breakthrough in dimension $n=8$, later recognised with a Fields Medal, underscores its difficulty. A leading technique for upper bounds, the three-point method, reduces the problem to solving large, high-precision semidefinite programs (SDPs). Because each candidate SDP may take days to evaluate, standard data-intensive AI approaches are infeasible. We address this challenge by formulating SDP construction as a sequential decision process, the SDP game, in which a policy assembles SDP formulations from a set of admissible components. Using a sample-efficient model-based framework that combines Bayesian optimisation with Monte Carlo Tree Search, we obtain new state-of-the-art upper bounds in dimensions $4-16$, showing that model-based search can advance computational progress in longstanding geometric problems. Together, these results demonstrate that sample-efficient, model-based search can make tangible progress on mathematically rigid, evaluation limited problems, pointing towards a complementary direction for AI-assisted discovery beyond large-scale LLM-driven exploration.

