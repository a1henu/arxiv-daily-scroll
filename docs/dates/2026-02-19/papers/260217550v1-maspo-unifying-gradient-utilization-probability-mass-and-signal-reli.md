---
layout: default
title: MASPO: Unifying Gradient Utilization, Probability Mass, and Signal Reliability for Robust and Sample-Efficient LLM Reasoning
---

# MASPO: Unifying Gradient Utilization, Probability Mass, and Signal Reliability for Robust and Sample-Efficient LLM Reasoning
**arXiv**：[2602.17550v1](https://arxiv.org/abs/2602.17550) · [PDF](https://arxiv.org/pdf/2602.17550.pdf)  
**作者**：Xiaoliang Fu, Jiaye Lin, Yangyi Fang, Binbin Zheng, Chaowen Hu, Zekai Shao, Cong Qin, Lu Pan, Ke Zeng, Xunliang Cai  

**一句话要点**：提出MASPO框架，通过统一梯度利用、概率质量和信号可靠性，提升LLM推理的鲁棒性和样本效率。

**关键词**：强化学习, 大语言模型推理, 策略优化, 梯度利用, 信号可靠性, 样本效率

## 3 点简述
- 核心问题：现有RLVR方法存在梯度利用低效、概率质量不敏感和信号可靠性不对称的挑战。
- 方法要点：集成软高斯门控、质量自适应限制器和非对称风险控制器，以优化策略更新。
- 实验或效果：在广泛评估中显著优于基线，提供稳健的RLVR解决方案。

## 摘要（原文）

> Existing Reinforcement Learning with Verifiable Rewards (RLVR) algorithms, such as GRPO, rely on rigid, uniform, and symmetric trust region mechanisms that are fundamentally misaligned with the complex optimization dynamics of Large Language Models (LLMs). In this paper, we identify three critical challenges in these methods: (1) inefficient gradient utilization caused by the binary cutoff of hard clipping, (2) insensitive probability mass arising from uniform ratio constraints that ignore the token distribution, and (3) asymmetric signal reliability stemming from the disparate credit assignment ambiguity between positive and negative samples. To bridge these gaps, we propose Mass-Adaptive Soft Policy Optimization (MASPO), a unified framework designed to harmonize these three dimensions. MASPO integrates a differentiable soft Gaussian gating to maximize gradient utility, a mass-adaptive limiter to balance exploration across the probability spectrum, and an asymmetric risk controller to align update magnitudes with signal confidence. Extensive evaluations demonstrate that MASPO serves as a robust, all-in-one RLVR solution, significantly outperforming strong baselines. Our code is available at: https://anonymous.4open.science/r/ma1/README.md.

