---
layout: default
title: Scalable Power Sampling: Unlocking Efficient, Training-Free Reasoning for LLMs via Distribution Sharpening
---

# Scalable Power Sampling: Unlocking Efficient, Training-Free Reasoning for LLMs via Distribution Sharpening
**arXiv**：[2601.21590v1](https://arxiv.org/abs/2601.21590) · [PDF](https://arxiv.org/pdf/2601.21590.pdf)  
**作者**：Xiaotong Ji, Rasul Tutunov, Matthieu Zimmer, Haitham Bou Ammar  

**一句话要点**：提出可扩展功率采样方法，通过分布锐化实现LLMs高效免训练推理

**关键词**：大语言模型推理, 分布锐化, 免训练方法, 功率采样, 推理效率, 自回归生成

## 3 点简述
- 核心问题：强化学习后训练依赖外部奖励且计算成本高，MCMC采样效率低。
- 方法要点：理论推导全局功率分布近似为令牌级缩放低温分布，实现免训练免验证器自回归锐化。
- 实验或效果：在数学、问答和代码任务上匹配或超越GRPO，推理延迟比MCMC降低超10倍。

## 摘要（原文）

> Reinforcement learning (RL) post-training is a dominant approach for improving the reasoning performance of large language models (LLMs), yet growing evidence suggests that its gains arise primarily from distribution sharpening rather than the acquisition of new capabilities. Recent work has shown that sampling from the power distribution of LLMs using Markov chain Monte Carlo (MCMC) can recover performance comparable to RL post-training without relying on external rewards; however, the high computational cost of MCMC makes such approaches impractical for widespread adoption. In this work, we propose a theoretically grounded alternative that eliminates the need for iterative MCMC. We derive a novel formulation showing that the global power distribution can be approximated by a token-level scaled low-temperature one, where the scaling factor captures future trajectory quality. Leveraging this insight, we introduce a training-free and verifier-free algorithm that sharpens the base model's generative distribution autoregressively. Empirically, we evaluate our method on math, QA, and code tasks across four LLMs, and show that our method matches or surpasses one-shot GRPO without relying on any external rewards, while reducing inference latency by over 10x compared to MCMC-based sampling.

