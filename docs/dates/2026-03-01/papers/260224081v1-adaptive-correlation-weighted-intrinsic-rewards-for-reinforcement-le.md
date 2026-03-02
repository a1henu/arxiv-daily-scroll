---
layout: default
title: Adaptive Correlation-Weighted Intrinsic Rewards for Reinforcement Learning
---

# Adaptive Correlation-Weighted Intrinsic Rewards for Reinforcement Learning
**arXiv**：[2602.24081v1](https://arxiv.org/abs/2602.24081) · [PDF](https://arxiv.org/pdf/2602.24081.pdf)  
**作者**：Viet Bac Nguyen, Phuong Thai Nguyen  

**一句话要点**：提出ACWI框架，通过自适应相关加权内在奖励解决稀疏奖励强化学习中的探索问题。

**关键词**：稀疏奖励强化学习, 内在奖励, 自适应探索, 相关加权, Beta网络, MiniGrid环境

## 3 点简述
- 核心问题：传统方法依赖手动调整内在奖励权重，导致跨任务性能不稳定或次优。
- 方法要点：引入轻量级Beta网络，基于状态预测内在奖励权重，并通过相关目标优化对齐内在奖励与未来外在回报。
- 实验或效果：在MiniGrid稀疏奖励环境中，ACWI提升样本效率和训练稳定性，优于固定内在奖励基线。

## 摘要（原文）

> We propose ACWI (Adaptive Correlation Weighted Intrinsic), an adaptive intrinsic reward scaling framework designed to dynamically balance intrinsic and extrinsic rewards for improved exploration in sparse reward reinforcement learning. Unlike conventional approaches that rely on manually tuned scalar coefficients, which often result in unstable or suboptimal performance across tasks, ACWI learns a state dependent scaling coefficient online. Specifically, ACWI introduces a lightweight Beta Network that predicts the intrinsic reward weight directly from the agent state through an encoder based architecture. The scaling mechanism is optimized using a correlation based objective that encourages alignment between the weighted intrinsic rewards and discounted future extrinsic returns. This formulation enables task adaptive exploration incentives while preserving computational efficiency and training stability. We evaluate ACWI on a suite of sparse reward environments in MiniGrid. Experimental results demonstrate that ACWI consistently improves sample efficiency and learning stability compared to fixed intrinsic reward baselines, achieving superior performance with minimal computational overhead.

