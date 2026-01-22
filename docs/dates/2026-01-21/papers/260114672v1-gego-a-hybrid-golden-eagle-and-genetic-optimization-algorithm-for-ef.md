---
layout: default
title: GEGO: A Hybrid Golden Eagle and Genetic Optimization Algorithm for Efficient Hyperparameter Tuning in Resource-Constrained Environments
---

# GEGO: A Hybrid Golden Eagle and Genetic Optimization Algorithm for Efficient Hyperparameter Tuning in Resource-Constrained Environments
**arXiv**：[2601.14672v1](https://arxiv.org/abs/2601.14672) · [PDF](https://arxiv.org/pdf/2601.14672.pdf)  
**作者**：Amaras Nazarians, Sachin Kumar  

**一句话要点**：提出GEGO混合元启发式算法，用于资源受限环境下的高效超参数调优

**关键词**：超参数调优, 元启发式算法, 混合优化, 神经网络训练, 资源受限环境

## 3 点简述
- 核心问题：超参数调优计算成本高，搜索空间高维非凸，易陷入局部最优
- 方法要点：将遗传算子嵌入金鹰优化迭代过程，增强种群多样性，减少早熟收敛
- 实验或效果：在CEC2017基准函数和MNIST数据集上优于基础算法，提升分类精度和收敛稳定性

## 摘要（原文）

> Hyperparameter tuning is a critical yet computationally expensive step in training neural networks, particularly when the search space is high dimensional and nonconvex. Metaheuristic optimization algorithms are often used for this purpose due to their derivative free nature and robustness against local optima. In this work, we propose Golden Eagle Genetic Optimization (GEGO), a hybrid metaheuristic that integrates the population movement strategy of Golden Eagle Optimization with the genetic operators of selection, crossover, and mutation.
>   The main novelty of GEGO lies in embedding genetic operators directly into the iterative search process of GEO, rather than applying them as a separate evolutionary stage. This design improves population diversity during search and reduces premature convergence while preserving the exploration behavior of GEO.
>   GEGO is evaluated on standard unimodal, multimodal, and composite benchmark functions from the CEC2017 suite, where it consistently outperforms its constituent algorithms and several classical metaheuristics in terms of solution quality and robustness. The algorithm is further applied to hyperparameter tuning of artificial neural networks on the MNIST dataset, where GEGO achieves improved classification accuracy and more stable convergence compared to GEO and GA. These results indicate that GEGO provides a balanced exploration-exploitation tradeoff and is well suited for hyperparameter optimization under constrained computational settings.

