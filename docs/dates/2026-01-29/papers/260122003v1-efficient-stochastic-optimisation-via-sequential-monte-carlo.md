---
layout: default
title: Efficient Stochastic Optimisation via Sequential Monte Carlo
---

# Efficient Stochastic Optimisation via Sequential Monte Carlo
**arXiv**：[2601.22003v1](https://arxiv.org/abs/2601.22003) · [PDF](https://arxiv.org/pdf/2601.22003.pdf)  
**作者**：James Cuin, Davide Carbone, Yanbo Tang, O. Deniz Akyildiz  

**一句话要点**：提出基于序贯蒙特卡洛的优化方法，以高效解决梯度难处理函数优化问题。

**关键词**：序贯蒙特卡洛, 梯度难处理优化, 随机近似, 能量模型, 计算效率

## 3 点简述
- 核心问题：机器学习中梯度难处理函数优化，如最大边际似然估计和生成模型微调，现有方法需内层采样循环，计算成本高。
- 方法要点：开发序贯蒙特卡洛采样器替代昂贵内层采样，提供高效近似，建立收敛性理论。
- 实验或效果：在基于能量模型的奖励调优中验证有效性，实现显著计算增益。

## 摘要（原文）

> The problem of optimising functions with intractable gradients frequently arise in machine learning and statistics, ranging from maximum marginal likelihood estimation procedures to fine-tuning of generative models. Stochastic approximation methods for this class of problems typically require inner sampling loops to obtain (biased) stochastic gradient estimates, which rapidly becomes computationally expensive. In this work, we develop sequential Monte Carlo (SMC) samplers for optimisation of functions with intractable gradients. Our approach replaces expensive inner sampling methods with efficient SMC approximations, which can result in significant computational gains. We establish convergence results for the basic recursions defined by our methodology which SMC samplers approximate. We demonstrate the effectiveness of our approach on the reward-tuning of energy-based models within various settings.

