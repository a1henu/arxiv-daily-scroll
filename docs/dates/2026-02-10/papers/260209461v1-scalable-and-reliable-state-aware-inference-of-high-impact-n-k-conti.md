---
layout: default
title: Scalable and Reliable State-Aware Inference of High-Impact N-k Contingencies
---

# Scalable and Reliable State-Aware Inference of High-Impact N-k Contingencies
**arXiv**：[2602.09461v1](https://arxiv.org/abs/2602.09461) · [PDF](https://arxiv.org/pdf/2602.09461.pdf)  
**作者**：Lihao Mai, Chenhan Xiao, Yang Weng  

**一句话要点**：提出可扩展的状态感知推理框架以高效评估高影响N-k故障场景

**关键词**：N-k故障评估, 条件扩散模型, 图神经网络, 状态感知推理, 可控覆盖保证, 电力系统安全

## 3 点简述
- 核心问题：高渗透率可再生能源和快速变化工况下，N-k故障评估计算成本高，传统启发式方法无法保证覆盖所有关键故障。
- 方法要点：采用条件扩散模型生成状态感知的候选故障，结合图神经网络离线构建高风险训练样本，并提供可控覆盖保证。
- 实验或效果：在IEEE基准系统上，相比均匀采样，该方法在有限评估预算下能更可靠地识别高严重性故障。

## 摘要（原文）

> Increasing penetration of inverter-based resources, flexible loads, and rapidly changing operating conditions make higher-order $N\!-\!k$ contingency assessment increasingly important but computationally prohibitive. Exhaustive evaluation of all outage combinations using AC power-flow or ACOPF is infeasible in routine operation. This fact forces operators to rely on heuristic screening methods whose ability to consistently retain all critical contingencies is not formally established. This paper proposes a scalable, state-aware contingency inference framework designed to directly generate high-impact $N\!-\!k$ outage scenarios without enumerating the combinatorial contingency space. The framework employs a conditional diffusion model to produce candidate contingencies tailored to the current operating state, while a topology-aware graph neural network trained only on base and $N\!-\!1$ cases efficiently constructs high-risk training samples offline. Finally, the framework is developed to provide controllable coverage guarantees for severe contingencies, allowing operators to explicitly manage the risk of missing critical events under limited AC power-flow evaluation budgets. Experiments on IEEE benchmark systems show that, for a given evaluation budget, the proposed approach consistently evaluates higher-severity contingencies than uniform sampling. This allows critical outages to be identified more reliably with reduced computational effort.

