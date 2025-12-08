---
layout: default
title: On Dynamic Programming Theory for Leader-Follower Stochastic Games
---

# On Dynamic Programming Theory for Leader-Follower Stochastic Games
**arXiv**：[2512.05667v1](https://arxiv.org/abs/2512.05667) · [PDF](https://arxiv.org/pdf/2512.05667.pdf)  
**作者**：Jilles Steeve Dibangoye, Thibaut Le Marre, Ocan Sankur, François Schwarzentruber  

**一句话要点**：提出基于可信集的动态规划框架，以计算领导者-追随者随机博弈的强Stackelberg均衡。

**关键词**：领导者-追随者博弈, 动态规划, 可信集, Stackelberg均衡, 随机博弈, NP难问题

## 3 点简述
- 研究领导者-追随者随机博弈，其中领导者承诺策略，追随者最优响应，形成强Stackelberg均衡。
- 引入动态规划框架，通过可信集上的Bellman递归，将博弈无损约简为马尔可夫决策过程。
- 证明最优无记忆确定性策略合成是NP难的，开发ε-最优算法，实验显示在标准基准上优于现有方法。

## 摘要（原文）

> Leader-follower general-sum stochastic games (LF-GSSGs) model sequential decision-making under asymmetric commitment, where a leader commits to a policy and a follower best responds, yielding a strong Stackelberg equilibrium (SSE) with leader-favourable tie-breaking. This paper introduces a dynamic programming (DP) framework that applies Bellman recursion over credible sets-state abstractions formally representing all rational follower best responses under partial leader commitments-to compute SSEs. We first prove that any LF-GSSG admits a lossless reduction to a Markov decision process (MDP) over credible sets. We further establish that synthesising an optimal memoryless deterministic leader policy is NP-hard, motivating the development of ε-optimal DP algorithms with provable guarantees on leader exploitability. Experiments on standard mixed-motive benchmarks-including security games, resource allocation, and adversarial planning-demonstrate empirical gains in leader value and runtime scalability over state-of-the-art methods.

