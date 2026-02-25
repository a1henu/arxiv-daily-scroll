---
layout: default
title: Upper-Linearizability of Online Non-Monotone DR-Submodular Maximization over Down-Closed Convex Sets
---

# Upper-Linearizability of Online Non-Monotone DR-Submodular Maximization over Down-Closed Convex Sets
**arXiv**：[2602.20578v1](https://arxiv.org/abs/2602.20578) · [PDF](https://arxiv.org/pdf/2602.20578.pdf)  
**作者**：Yiyang Lu, Haresh Jadav, Mohammad Pedramfar, Ranveer Singh, Vaneet Aggarwal  

**一句话要点**：提出1/e-线性化方法以优化在线非单调DR-次模最大化问题

**关键词**：在线优化, DR-次模函数, 线性化, 遗憾分析, 反馈模型, 凸集约束

## 3 点简述
- 研究在线非单调DR-次模函数在向下闭凸集上的最大化问题
- 通过指数重参数化、缩放参数和代理势实现1/e-线性化，转化为在线线性优化
- 在多种反馈模型下获得改进的遗憾保证，包括静态、自适应和动态遗憾

## 摘要（原文）

> We study online maximization of non-monotone Diminishing-Return(DR)-submodular functions over down-closed convex sets, a regime where existing projection-free online methods suffer from suboptimal regret and limited feedback guarantees. Our main contribution is a new structural result showing that this class is $1/e$-linearizable under carefully designed exponential reparametrization, scaling parameter, and surrogate potential, enabling a reduction to online linear optimization. As a result, we obtain $O(T^{1/2})$ static regret with a single gradient query per round and unlock adaptive and dynamic regret guarantees, together with improved rates under semi-bandit, bandit, and zeroth-order feedback. Across all feedback models, our bounds strictly improve the state of the art.

