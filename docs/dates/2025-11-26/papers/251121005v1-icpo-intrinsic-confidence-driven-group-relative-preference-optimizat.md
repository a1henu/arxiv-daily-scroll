---
layout: default
title: ICPO: Intrinsic Confidence-Driven Group Relative Preference Optimization for Efficient Reinforcement Learning
---

# ICPO: Intrinsic Confidence-Driven Group Relative Preference Optimization for Efficient Reinforcement Learning
**arXiv**：[2511.21005v1](https://arxiv.org/abs/2511.21005) · [PDF](https://arxiv.org/pdf/2511.21005.pdf)  
**作者**：Jinpeng Wang, Chao Li, Ting Ye, Mengyuan Zhang, Wei Liu, Jian Luan  

**一句话要点**：提出ICPO方法以解决强化学习中奖励粗糙、噪声和不稳定训练问题。

**关键词**：强化学习, 偏好优化, 大语言模型, 推理增强, 奖励建模, 探索策略

## 3 点简述
- 核心问题：现有RLVR方法存在奖励粗糙、噪声和探索效率低，导致训练不稳定和熵崩溃。
- 方法要点：利用LLM生成概率计算偏好优势分，结合可验证奖励指导探索，提升推理质量。
- 实验或效果：在多个基准测试中，ICPO稳定提升推理能力，优于GRPO方法。

## 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) demonstrates significant potential in enhancing the reasoning capabilities of Large Language Models (LLMs). However, existing RLVR methods are often constrained by issues such as coarse-grained rewards, reward noise, and inefficient exploration, which lead to unstable training and entropy collapse. To address this challenge, we propose the Intrinsic Confidence-Driven Group Relative Preference Optimization method (ICPO). The intuition behind it lies in the fact that the probabilities of an LLM generating different responses can inherently and directly reflect its self-assessment of the reasoning process. Inspired by the idea of preference modeling, ICPO calculates a preference advantage score for each response by comparing the relative generation probabilities of multiple responses under the same input prompt, and integrates this score with verifiable rewards to guide the exploration process. We have discovered that the preference advantage score not only alleviates the issues of coarse-grained rewards and reward noise but also effectively curbs overconfident errors, enhances the relative superiority of undervalued high-quality responses, and prevents the model from overfitting to specific strategies, thereby facilitating more thorough exploration. Comprehensive experiments across four general-domain benchmarks and three mathematical benchmarks demonstrate that ICPO steadily boosts reasoning compared to GRPO.

