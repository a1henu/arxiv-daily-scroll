---
layout: default
title: Your Group-Relative Advantage Is Biased
---

# Your Group-Relative Advantage Is Biased
**arXiv**：[2601.08521v1](https://arxiv.org/abs/2601.08521) · [PDF](https://arxiv.org/pdf/2601.08521.pdf)  
**作者**：Fengkai Yang, Zherui Chen, Xiaohan Wang, Xiaodong Lu, Jiajun Chai, Guojun Yin, Wei Lin, Shuai Ma, Fuzhen Zhuang, Deqing Wang, Yaodong Yang, Jianxin Li, Yikun Ban  

**一句话要点**：提出历史感知自适应难度加权以解决基于组的强化学习中优势估计偏差问题

**关键词**：强化学习验证奖励, 优势估计偏差, 自适应难度加权, 数学推理, 后训练优化

## 3 点简述
- 揭示基于组的强化学习中组相对优势估计器存在固有偏差，导致探索与利用失衡
- 提出HA-DW方法，通过动态难度锚点和训练动态自适应调整优势估计权重
- 在五个数学推理基准上实验验证HA-DW能稳定提升GRPO及其变体的性能

## 摘要（原文）

> Reinforcement Learning from Verifier Rewards (RLVR) has emerged as a widely used approach for post-training large language models on reasoning tasks, with group-based methods such as GRPO and its variants gaining broad adoption. These methods rely on group-relative advantage estimation to avoid learned critics, yet its theoretical properties remain poorly understood.
>   In this work, we uncover a fundamental issue of group-based RL: the group-relative advantage estimator is inherently biased relative to the true (expected) advantage. We provide the first theoretical analysis showing that it systematically underestimates advantages for hard prompts and overestimates them for easy prompts, leading to imbalanced exploration and exploitation. To address this issue, we propose History-Aware Adaptive Difficulty Weighting (HA-DW), an adaptive reweighting scheme that adjusts advantage estimates based on an evolving difficulty anchor and training dynamics. Both theoretical analysis and experiments on five mathematical reasoning benchmarks demonstrate that HA-DW consistently improves performance when integrated into GRPO and its variants. Our results suggest that correcting biased advantage estimation is critical for robust and efficient RLVR training.

