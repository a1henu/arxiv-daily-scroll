---
layout: default
title: BandPO: Bridging Trust Regions and Ratio Clipping via Probability-Aware Bounds for LLM Reinforcement Learning
---

# BandPO: Bridging Trust Regions and Ratio Clipping via Probability-Aware Bounds for LLM Reinforcement Learning
**arXiv**：[2603.04918v1](https://arxiv.org/abs/2603.04918) · [PDF](https://arxiv.org/pdf/2603.04918.pdf)  
**作者**：Yuan Li, Bo Wang, Yufei Gao, Yuqian Yao, Xinyuan Wang, Zhangyue Yin, Xipeng Qiu  

**一句话要点**：提出BandPO以解决LLM强化学习中固定裁剪限制探索瓶颈的问题

**关键词**：大语言模型强化学习, 信任区域优化, 概率感知裁剪, 探索瓶颈, 熵崩溃缓解

## 3 点简述
- 核心问题：PPO固定裁剪限制低概率动作的向上更新，抑制高优势策略并导致熵快速崩溃
- 方法要点：引入Band算子，将f-散度信任区域映射为动态概率感知裁剪区间，理论分析解决探索瓶颈
- 实验或效果：在多种模型和数据集上实验，BandPO优于标准裁剪和Clip-Higher，有效缓解熵崩溃

## 摘要（原文）

> Proximal constraints are fundamental to the stability of the Large Language Model reinforcement learning. While the canonical clipping mechanism in PPO serves as an efficient surrogate for trust regions, we identify a critical bottleneck: fixed bounds strictly constrain the upward update margin of low-probability actions, disproportionately suppressing high-advantage tail strategies and inducing rapid entropy collapse. To address this, we introduce Band-constrained Policy Optimization (BandPO). BandPO replaces canonical clipping with Band, a unified theoretical operator that projects trust regions defined by f-divergences into dynamic, probability-aware clipping intervals. Theoretical analysis confirms that Band effectively resolves this exploration bottleneck. We formulate this mapping as a convex optimization problem, guaranteeing a globally optimal numerical solution while deriving closed-form solutions for specific divergences. Extensive experiments across diverse models and datasets demonstrate that BandPO consistently outperforms canonical clipping and Clip-Higher, while robustly mitigating entropy collapse.

