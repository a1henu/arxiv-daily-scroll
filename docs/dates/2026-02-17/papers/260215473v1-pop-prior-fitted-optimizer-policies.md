---
layout: default
title: POP: Prior-fitted Optimizer Policies
---

# POP: Prior-fitted Optimizer Policies
**arXiv**：[2602.15473v1](https://arxiv.org/abs/2602.15473) · [PDF](https://arxiv.org/pdf/2602.15473.pdf)  
**作者**：Jan Kobiolka, Christian Frey, Gresa Shala, Arlind Kadra, Erind Bedalli, Josif Grabocka  

**一句话要点**：提出POP元学习优化器，通过先验拟合预测步长以提升非凸优化性能。

**关键词**：元学习优化器, 非凸优化, 先验拟合, 步长预测, 合成数据集

## 3 点简述
- 核心问题：梯度优化器对超参数敏感，在非凸场景中性能依赖精细调参。
- 方法要点：基于先验采样百万合成问题，元学习条件步长预测策略。
- 实验或效果：在47个函数基准上优于梯度方法、进化策略和贝叶斯优化。

## 摘要（原文）

> Optimization refers to the task of finding extrema of an objective function. Classical gradient-based optimizers are highly sensitive to hyperparameter choices. In highly non-convex settings their performance relies on carefully tuned learning rates, momentum, and gradient accumulation. To address these limitations, we introduce POP (Prior-fitted Optimizer Policies), a meta-learned optimizer that predicts coordinate-wise step sizes conditioned on the contextual information provided in the optimization trajectory. Our model is learned on millions of synthetic optimization problems sampled from a novel prior spanning both convex and non-convex objectives. We evaluate POP on an established benchmark including 47 optimization functions of various complexity, where it consistently outperforms first-order gradient-based methods, non-convex optimization approaches (e.g., evolutionary strategies), Bayesian optimization, and a recent meta-learned competitor under matched budget constraints. Our evaluation demonstrates strong generalization capabilities without task-specific tuning.

