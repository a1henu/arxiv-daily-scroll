---
layout: default
title: STAPO: Stabilizing Reinforcement Learning for LLMs by Silencing Rare Spurious Tokens
---

# STAPO: Stabilizing Reinforcement Learning for LLMs by Silencing Rare Spurious Tokens
**arXiv**：[2602.15620v1](https://arxiv.org/abs/2602.15620) · [PDF](https://arxiv.org/pdf/2602.15620.pdf)  
**作者**：Shiqi Liu, Zeyu He, Guojian Zhan, Letian Tao, Zhilong Zheng, Jiang Wu, Yinuo Wang, Yang Guan, Kehua Sheng, Bo Zhang, Keqiang Li, Jingliang Duan, Shengbo Eben Li  

**一句话要点**：提出STAPO方法以解决大语言模型强化学习中的训练不稳定问题

**关键词**：强化学习, 大语言模型微调, 训练稳定性, 虚假令牌, 策略优化, 数学推理

## 3 点简述
- 核心问题：现有RL微调方法依赖启发式技术，常出现后期性能崩溃，导致推理质量下降和不稳定训练
- 方法要点：基于策略梯度与令牌概率负相关的推导，识别并屏蔽约0.01%的虚假令牌更新，重新归一化有效令牌损失
- 实验或效果：在六个数学推理基准测试中，STAPO展示出更优的熵稳定性，平均性能比基线方法提升7.13%

## 摘要（原文）

> Reinforcement Learning (RL) has significantly improved large language model reasoning, but existing RL fine-tuning methods rely heavily on heuristic techniques such as entropy regularization and reweighting to maintain stability. In practice, they often experience late-stage performance collapse, leading to degraded reasoning quality and unstable training. We derive that the magnitude of token-wise policy gradients in RL is negatively correlated with token probability and local policy entropy. Building on this result, we prove that training instability is driven by a tiny fraction of tokens, approximately 0.01\%, which we term \emph{spurious tokens}. When such tokens appear in correct responses, they contribute little to the reasoning outcome but inherit the full sequence-level reward, leading to abnormally amplified gradient updates. Motivated by this observation, we propose Spurious-Token-Aware Policy Optimization (STAPO) for large-scale model refining, which selectively masks such updates and renormalizes the loss over valid tokens. Across six mathematical reasoning benchmarks using Qwen 1.7B, 8B, and 14B base models, STAPO consistently demonstrates superior entropy stability and achieves an average performance improvement of 7.13\% over GRPO, 20-Entropy and JustRL.

