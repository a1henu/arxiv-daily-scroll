---
layout: default
title: Contribution-aware Token Compression for Efficient Video Understanding via Reinforcement Learning
---

# Contribution-aware Token Compression for Efficient Video Understanding via Reinforcement Learning
**arXiv**：[2602.01649v1](https://arxiv.org/abs/2602.01649) · [PDF](https://arxiv.org/pdf/2602.01649.pdf)  
**作者**：Yinchao Ma, Qiang Zhou, Zhibin Wang, Xianing Chen, Hanqing Yang, Jun Song, Bo Zheng  

**一句话要点**：提出基于强化学习的贡献感知令牌压缩算法CaCoVID，以优化视频理解中的令牌选择策略。

**关键词**：视频理解, 令牌压缩, 强化学习, 贡献感知, 组合优化, 计算效率

## 3 点简述
- 核心问题：视频令牌冗余导致计算开销大，现有方法依赖注意力分数，但分数与正确预测贡献相关性未知。
- 方法要点：使用强化学习框架优化策略网络，主动选择对正确预测贡献最大的令牌组合，并引入组合策略优化算法加速收敛。
- 实验或效果：在多个视频理解基准测试中验证了CaCoVID的有效性，代码将开源。

## 摘要（原文）

> Video large language models have demonstrated remarkable capabilities in video understanding tasks. However, the redundancy of video tokens introduces significant computational overhead during inference, limiting their practical deployment. Many compression algorithms are proposed to prioritize retaining features with the highest attention scores to minimize perturbations in attention computations. However, the correlation between attention scores and their actual contribution to correct answers remains ambiguous. To address the above limitation, we propose a novel \textbf{C}ontribution-\textbf{a}ware token \textbf{Co}mpression algorithm for \textbf{VID}eo understanding (\textbf{CaCoVID}) that explicitly optimizes the token selection policy based on the contribution of tokens to correct predictions. First, we introduce a reinforcement learning-based framework that optimizes a policy network to select video token combinations with the greatest contribution to correct predictions. This paradigm shifts the focus from passive token preservation to active discovery of optimal compressed token combinations. Secondly, we propose a combinatorial policy optimization algorithm with online combination space sampling, which dramatically reduces the exploration space for video token combinations and accelerates the convergence speed of policy optimization. Extensive experiments on diverse video understanding benchmarks demonstrate the effectiveness of CaCoVID. Codes will be released.

