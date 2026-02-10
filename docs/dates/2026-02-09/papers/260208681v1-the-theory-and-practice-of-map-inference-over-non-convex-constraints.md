---
layout: default
title: The Theory and Practice of MAP Inference over Non-Convex Constraints
---

# The Theory and Practice of MAP Inference over Non-Convex Constraints
**arXiv**：[2602.08681v1](https://arxiv.org/abs/2602.08681) · [PDF](https://arxiv.org/pdf/2602.08681.pdf)  
**作者**：Leander Kurscheidt, Gabriele Masina, Roberto Sebastiani, Antonio Vergari  

**一句话要点**：提出约束MAP推理的理论与算法，以处理非凸约束下的连续变量预测问题。

**关键词**：约束MAP推理, 非凸优化, 消息传递算法, 连续变量预测, 安全关键系统

## 3 点简述
- 核心问题：在安全关键场景中，概率ML系统需在非凸代数约束下进行高效可靠的MAP预测。
- 方法要点：研究约束MAP推理的精确高效条件，并设计可扩展的消息传递算法和通用分区优化策略。
- 实验或效果：在合成和真实基准测试中，方法优于无视约束的基线，并能扩展到复杂密度问题。

## 摘要（原文）

> In many safety-critical settings, probabilistic ML systems have to make predictions subject to algebraic constraints, e.g., predicting the most likely trajectory that does not cross obstacles.
>   These real-world constraints are rarely convex, nor the densities considered are (log-)concave.
>   This makes computing this constrained maximum a posteriori (MAP) prediction efficiently and reliably extremely challenging.
>   In this paper, we first investigate under which conditions we can perform constrained MAP inference over continuous variables exactly and efficiently and devise a scalable message-passing algorithm for this tractable fragment.
>   Then, we devise a general constrained MAP strategy that interleaves partitioning the domain into convex feasible regions with numerical constrained optimization.
>   We evaluate both methods on synthetic and real-world benchmarks, showing our %
>   approaches outperform constraint-agnostic baselines, and scale to complex densities intractable for SoTA exact solvers.

