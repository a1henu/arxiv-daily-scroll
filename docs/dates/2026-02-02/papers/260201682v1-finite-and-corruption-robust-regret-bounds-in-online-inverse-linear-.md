---
layout: default
title: Finite and Corruption-Robust Regret Bounds in Online Inverse Linear Optimization under M-Convex Action Sets
---

# Finite and Corruption-Robust Regret Bounds in Online Inverse Linear Optimization under M-Convex Action Sets
**arXiv**：[2602.01682v1](https://arxiv.org/abs/2602.01682) · [PDF](https://arxiv.org/pdf/2602.01682.pdf)  
**作者**：Taihei Oki, Shinsaku Sakaue  

**一句话要点**：提出基于M凸集的在线逆线性优化方法，实现有限且抗扰动的遗憾界

**关键词**：在线逆线性优化, M凸集, 遗憾界分析, 对抗性扰动, 上下文推荐, 优化理论

## 3 点简述
- 研究在线逆线性优化问题，旨在从动态可行集中推断代理隐藏目标向量
- 结合M凸集的结构特性与几何体积论证，获得O(d log d)的有限遗憾界
- 扩展至对抗性扰动反馈，自适应检测扰动，实现O((C+1)d log d)的遗憾界

## 摘要（原文）

> We study online inverse linear optimization, also known as contextual recommendation, where a learner sequentially infers an agent's hidden objective vector from observed optimal actions over feasible sets that change over time. The learner aims to recommend actions that perform well under the agent's true objective, and the performance is measured by the regret, defined as the cumulative gap between the agent's optimal values and those achieved by the learner's recommended actions. Prior work has established a regret bound of $O(d\log T)$, as well as a finite but exponentially large bound of $\exp(O(d\log d))$, where $d$ is the dimension of the optimization problem and $T$ is the time horizon, while a regret lower bound of $Ω(d)$ is known (Gollapudi et al. 2021; Sakaue et al. 2025). Whether a finite regret bound polynomial in $d$ is achievable or not has remained an open question. We partially resolve this by showing that when the feasible sets are M-convex -- a broad class that includes matroids -- a finite regret bound of $O(d\log d)$ is possible. We achieve this by combining a structural characterization of optimal solutions on M-convex sets with a geometric volume argument. Moreover, we extend our approach to adversarially corrupted feedback in up to $C$ rounds. We obtain a regret bound of $O((C+1)d\log d)$ without prior knowledge of $C$, by monitoring directed graphs induced by the observed feedback to detect corruptions adaptively.

