---
layout: default
title: Coarse-to-Fine Learning of Dynamic Causal Structures
---

# Coarse-to-Fine Learning of Dynamic Causal Structures
**arXiv**：[2602.22532v1](https://arxiv.org/abs/2602.22532) · [PDF](https://arxiv.org/pdf/2602.22532.pdf)  
**作者**：Dezhi Yang, Qiaoyu Tan, Carlotta Domeniconi, Jun Wang, Lizhen Cui, Guoxian Yu  

**一句话要点**：提出DyCausal框架，通过粗到细学习解决全动态因果结构识别问题。

**关键词**：动态因果结构学习, 时间序列分析, 卷积网络, 线性插值, 无环约束

## 3 点简述
- 核心问题：现有方法依赖分布或结构不变性，难以处理现实世界中完全动态、时变的因果关系。
- 方法要点：利用卷积网络捕获粗粒度时间窗口的因果模式，再通过线性插值细化每个时间步的因果图。
- 实验或效果：在合成和真实数据集上评估，DyCausal相比现有方法表现更优，提供稳定高效的解决方案。

## 摘要（原文）

> Learning the dynamic causal structure of time series is a challenging problem. Most existing approaches rely on distributional or structural invariance to uncover underlying causal dynamics, assuming stationary or partially stationary causality. However, these assumptions often conflict with the complex, time-varying causal relationships observed in real-world systems. This motivates the need for methods that address fully dynamic causality, where both instantaneous and lagged dependencies evolve over time. Such a setting poses significant challenges for the efficiency and stability of causal discovery. To address these challenges, we introduce DyCausal, a dynamic causal structure learning framework. DyCausal leverages convolutional networks to capture causal patterns within coarse-grained time windows, and then applies linear interpolation to refine causal structures at each time step, thereby recovering fine-grained and time-varying causal graphs. In addition, we propose an acyclic constraint based on matrix norm scaling, which improves efficiency while effectively constraining loops in evolving causal structures. Comprehensive evaluations on both synthetic and real-world datasets demonstrate that DyCausal achieves superior performance compared to existing methods, offering a stable and efficient approach for identifying fully dynamic causal structures from coarse to fine.

