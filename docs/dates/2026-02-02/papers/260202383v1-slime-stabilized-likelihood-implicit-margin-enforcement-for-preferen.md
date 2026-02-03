---
layout: default
title: SLIME: Stabilized Likelihood Implicit Margin Enforcement for Preference Optimization
---

# SLIME: Stabilized Likelihood Implicit Margin Enforcement for Preference Optimization
**arXiv**：[2602.02383v1](https://arxiv.org/abs/2602.02383) · [PDF](https://arxiv.org/pdf/2602.02383.pdf)  
**作者**：Maksim Afanasyev, Illarion Iov  

**一句话要点**：提出SLIME方法以解决偏好优化中的目标不匹配问题，提升大语言模型对齐的稳定性。

**关键词**：偏好优化, 大语言模型对齐, 目标不匹配, 生成稳定性, 隐式奖励函数

## 3 点简述
- 核心问题：现有偏好优化方法因目标不匹配导致模型遗忘高质量输出或格式崩溃。
- 方法要点：SLIME通过锚定项、稳定惩罚和双边界机制，解耦偏好学习与生成质量。
- 实验或效果：SLIME在基准测试中优于现有方法，同时保持更高的生成稳定性。

## 摘要（原文）

> Direct preference optimization methods have emerged as a computationally efficient alternative to Reinforcement Learning from Human Feedback (RLHF) for aligning Large Language Models (LLMs). Latest approaches have streamlined the alignment process by deriving implicit reward functions, yet they often suffer from a critical objective mismatch: optimizing the relative margin between chosen and rejected responses does not guarantee the preservation of the chosen response's absolute likelihood. This can lead to ``unlearning'', where the model degrades the probability of high-quality outputs to satisfy margin constraints, and ``formatting collapse'' caused by the over-penalization of rejected sequences. In this work, we introduce SLIME (Stabilized Likelihood Implicit Margin Enforcement), a reference-free alignment objective designed to decouple preference learning from generation quality. SLIME incorporates a three-pronged objective: (1) an anchoring term to maximize the likelihood of preferred responses; (2) a stabilizing penalty that prevents the probabilities of rejected tokens from collapsing to zero; and (3) a dual-margin mechanism that combines hard and soft constraints for precise boundary shaping. Our results demonstrate that SLIME achieves superior performance compared to state-of-the-art baselines while maintaining higher generation stability.

