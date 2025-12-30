---
layout: default
title: A Simple, Optimal and Efficient Algorithm for Online Exp-Concave Optimization
---

# A Simple, Optimal and Efficient Algorithm for Online Exp-Concave Optimization
**arXiv**：[2512.23190v1](https://arxiv.org/abs/2512.23190) · [PDF](https://arxiv.org/pdf/2512.23190.pdf)  
**作者**：Yi-Han Wang, Peng Zhao, Zhi-Hua Zhou  

**一句话要点**：提出LightONS算法以降低在线指数凹优化的计算成本，同时保持最优遗憾界。

**关键词**：在线学习, 指数凹优化, 计算效率, 遗憾最小化, 随机优化, 算法设计

## 3 点简述
- 核心问题：在线指数凹优化中，标准算法ONS因每轮Mahalanobis投影导致高计算成本，总运行时间可达Ω(d^ωT)。
- 方法要点：LightONS通过引入滞后机制延迟昂贵投影，将总运行时间降至O(d^2T + d^ω√(T log T))，保持O(d log T)遗憾。
- 实验或效果：LightONS解决了COLT'13开放问题，为随机指数凹优化提供运行时间Õ(d^3/ε)的算法，适用于更广泛场景如自适应遗憾和参数化随机赌博机。

## 摘要（原文）

> Online eXp-concave Optimization (OXO) is a fundamental problem in online learning. The standard algorithm, Online Newton Step (ONS), balances statistical optimality and computational practicality, guaranteeing an optimal regret of $O(d \log T)$, where $d$ is the dimension and $T$ is the time horizon. ONS faces a computational bottleneck due to the Mahalanobis projections at each round. This step costs $Ω(d^ω)$ arithmetic operations for bounded domains, even for the unit ball, where $ω\in (2,3]$ is the matrix-multiplication exponent. As a result, the total runtime can reach $\tilde{O}(d^ωT)$, particularly when iterates frequently oscillate near the domain boundary. For Stochastic eXp-concave Optimization (SXO), computational cost is also a challenge. Deploying ONS with online-to-batch conversion for SXO requires $T = \tilde{O}(d/ε)$ rounds to achieve an excess risk of $ε$, and thereby necessitates an $\tilde{O}(d^{ω+1}/ε)$ runtime. A COLT'13 open problem posed by Koren [2013] asks for an SXO algorithm with runtime less than $\tilde{O}(d^{ω+1}/ε)$.
>   This paper proposes a simple variant of ONS, LightONS, which reduces the total runtime to $O(d^2 T + d^ω\sqrt{T \log T})$ while preserving the optimal $O(d \log T)$ regret. LightONS implies an SXO method with runtime $\tilde{O}(d^3/ε)$, thereby answering the open problem. Importantly, LightONS preserves the elegant structure of ONS by leveraging domain-conversion techniques from parameter-free online learning to introduce a hysteresis mechanism that delays expensive Mahalanobis projections until necessary. This design enables LightONS to serve as an efficient plug-in replacement of ONS in broader scenarios, even beyond regret minimization, including gradient-norm adaptive regret, parametric stochastic bandits, and memory-efficient online learning.

