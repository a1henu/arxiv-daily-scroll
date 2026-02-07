---
layout: default
title: Accelerated Sequential Flow Matching: A Bayesian Filtering Perspective
---

# Accelerated Sequential Flow Matching: A Bayesian Filtering Perspective
**arXiv**：[2602.05319v1](https://arxiv.org/abs/2602.05319) · [PDF](https://arxiv.org/pdf/2602.05319.pdf)  
**作者**：Yinan Huang, Hans Hao-Hsun Hsu, Junran Wang, Bo Dai, Pan Li  

**一句话要点**：提出基于贝叶斯滤波的序列流匹配框架，以加速实时流环境中的多模态轨迹预测。

**关键词**：序列预测, 贝叶斯滤波, 流匹配模型, 实时推理, 多模态轨迹, 采样加速

## 3 点简述
- 核心问题：流观测序列预测中，扩散和流匹配模型因重复采样导致推理延迟和系统积压。
- 方法要点：将流推理视为概率流学习，利用贝叶斯滤波递归更新，从前一后验初始化生成以加速采样。
- 实验或效果：在预测、决策和状态估计任务中，性能媲美全步扩散，仅需少量采样步骤，实现更快采样。

## 摘要（原文）

> Sequential prediction from streaming observations is a fundamental problem in stochastic dynamical systems, where inherent uncertainty often leads to multiple plausible futures. While diffusion and flow-matching models are capable of modeling complex, multi-modal trajectories, their deployment in real-time streaming environments typically relies on repeated sampling from a non-informative initial distribution, incurring substantial inference latency and potential system backlogs. In this work, we introduce Sequential Flow Matching, a principled framework grounded in Bayesian filtering. By treating streaming inference as learning a probability flow that transports the predictive distribution from one time step to the next, our approach naturally aligns with the recursive structure of Bayesian belief updates. We provide theoretical justification that initializing generation from the previous posterior offers a principled warm start that can accelerate sampling compared to naïve re-sampling. Across a wide range of forecasting, decision-making and state estimation tasks, our method achieves performance competitive with full-step diffusion while requiring only one or very few sampling steps, therefore with faster sampling. It suggests that framing sequential inference via Bayesian filtering provides a new and principled perspective towards efficient real-time deployment of flow-based models.

