---
layout: default
title: Efficient Stochastic Optimisation via Sequential Monte Carlo
---

# Efficient Stochastic Optimisation via Sequential Monte Carlo
**arXiv**：[2601.22003v1](https://arxiv.org/abs/2601.22003) · [PDF](https://arxiv.org/pdf/2601.22003.pdf)  
**作者**：James Cuin, Davide Carbone, Yanbo Tang, O. Deniz Akyildiz  

**一句话要点**：提出基于序贯蒙特卡洛的优化方法，以高效解决梯度难处理函数的优化问题。

**关键词**：序贯蒙特卡洛, 梯度难处理优化, 随机优化, 计算效率, 基于能量的模型

## 3 点简述
- 核心问题：机器学习中梯度难处理函数的优化，如最大边际似然估计和生成模型微调，现有方法计算成本高。
- 方法要点：用序贯蒙特卡洛采样器替代昂贵的内层采样，近似梯度，建立收敛理论，降低计算开销。
- 实验或效果：在基于能量的模型奖励调优中验证有效性，展示显著计算增益。

## 摘要（原文）

> The problem of optimising functions with intractable gradients frequently arise in machine learning and statistics, ranging from maximum marginal likelihood estimation procedures to fine-tuning of generative models. Stochastic approximation methods for this class of problems typically require inner sampling loops to obtain (biased) stochastic gradient estimates, which rapidly becomes computationally expensive. In this work, we develop sequential Monte Carlo (SMC) samplers for optimisation of functions with intractable gradients. Our approach replaces expensive inner sampling methods with efficient SMC approximations, which can result in significant computational gains. We establish convergence results for the basic recursions defined by our methodology which SMC samplers approximate. We demonstrate the effectiveness of our approach on the reward-tuning of energy-based models within various settings.

