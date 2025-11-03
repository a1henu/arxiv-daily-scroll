---
layout: default
title: EBT-Policy: Energy Unlocks Emergent Physical Reasoning Capabilities
---

# EBT-Policy: Energy Unlocks Emergent Physical Reasoning Capabilities
**arXiv**：[2510.27545v1](https://arxiv.org/abs/2510.27545) · [PDF](https://arxiv.org/pdf/2510.27545.pdf)  
**作者**：Travis Davies, Yiqi Huang, Alexi Gladstone, Yunxin Liu, Xiang Chen, Heng Ji, Huxian Liu, Luhui Hu  

**一句话要点**：提出EBT-Policy能量模型以解决机器人策略学习中的计算成本高和鲁棒性差问题

**关键词**：能量模型, 机器人策略学习, 分布偏移鲁棒性, 计算效率, 零样本恢复

## 3 点简述
- 核心问题：基于生成模型的策略存在高计算成本、曝光偏差和推理不稳定，导致分布偏移下性能下降
- 方法要点：利用能量模型学习端到端能量景观，建模平衡动态，提升鲁棒性和减少曝光偏差
- 实验或效果：在模拟和真实任务中优于扩散策略，计算需求更低，部分任务仅需两步推理

## 摘要（原文）

> Implicit policies parameterized by generative models, such as Diffusion
> Policy, have become the standard for policy learning and Vision-Language-Action
> (VLA) models in robotics. However, these approaches often suffer from high
> computational cost, exposure bias, and unstable inference dynamics, which lead
> to divergence under distribution shifts. Energy-Based Models (EBMs) address
> these issues by learning energy landscapes end-to-end and modeling equilibrium
> dynamics, offering improved robustness and reduced exposure bias. Yet, policies
> parameterized by EBMs have historically struggled to scale effectively. Recent
> work on Energy-Based Transformers (EBTs) demonstrates the scalability of EBMs
> to high-dimensional spaces, but their potential for solving core challenges in
> physically embodied models remains underexplored. We introduce a new
> energy-based architecture, EBT-Policy, that solves core issues in robotic and
> real-world settings. Across simulated and real-world tasks, EBT-Policy
> consistently outperforms diffusion-based policies, while requiring less
> training and inference computation. Remarkably, on some tasks it converges
> within just two inference steps, a 50x reduction compared to Diffusion Policy's
> 100. Moreover, EBT-Policy exhibits emergent capabilities not seen in prior
> models, such as zero-shot recovery from failed action sequences using only
> behavior cloning and without explicit retry training. By leveraging its scalar
> energy for uncertainty-aware inference and dynamic compute allocation,
> EBT-Policy offers a promising path toward robust, generalizable robot behavior
> under distribution shifts.

