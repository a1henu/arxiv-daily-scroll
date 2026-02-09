---
layout: default
title: On the Plasticity and Stability for Post-Training Large Language Models
---

# On the Plasticity and Stability for Post-Training Large Language Models
**arXiv**：[2602.06453v1](https://arxiv.org/abs/2602.06453) · [PDF](https://arxiv.org/pdf/2602.06453.pdf)  
**作者**：Wenwen Qiang, Ziyin Gu, Jiahuan Zhou, Jie Hu, Jingyao Wang, Changwen Zheng, Hui Xiong  

**一句话要点**：提出概率冲突解决以优化GRPO训练稳定性与推理可塑性

**关键词**：大语言模型后训练, 训练稳定性, 梯度冲突, 贝叶斯优化, 推理任务

## 3 点简述
- 核心问题：GRPO训练稳定性差，源于可塑性与稳定性梯度间的几何冲突。
- 方法要点：引入概率冲突解决，建模梯度为随机变量，实现不确定性感知软投影。
- 实验或效果：实验显示PCR平滑训练轨迹，在多种推理任务中性能优越。

## 摘要（原文）

> Training stability remains a critical bottleneck for Group Relative Policy Optimization (GRPO), often manifesting as a trade-off between reasoning plasticity and general capability retention. We identify a root cause as the geometric conflict between plasticity and stability gradients, which leads to destructive interference. Crucially, we argue that deterministic projection methods are suboptimal for GRPO as they overlook the intrinsic stochasticity of group-based gradient estimates. To address this, we propose Probabilistic Conflict Resolution (PCR), a Bayesian framework that models gradients as random variables. PCR dynamically arbitrates conflicts via an uncertainty-aware ``soft projection'' mechanism, optimizing the signal-to-noise ratio. Extensive experiments demonstrate that PCR significantly smooths the training trajectory and achieves superior performance in various reasoning tasks.

