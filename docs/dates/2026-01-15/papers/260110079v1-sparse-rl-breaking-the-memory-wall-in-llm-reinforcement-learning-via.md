---
layout: default
title: Sparse-RL: Breaking the Memory Wall in LLM Reinforcement Learning via Stable Sparse Rollouts
---

# Sparse-RL: Breaking the Memory Wall in LLM Reinforcement Learning via Stable Sparse Rollouts
**arXiv**：[2601.10079v1](https://arxiv.org/abs/2601.10079) · [PDF](https://arxiv.org/pdf/2601.10079.pdf)  
**作者**：Sijia Luo, Xiaokang Zhang, Yuxuan Hu, Bohan Zhang, Ke Wang, Jinbo Su, Mengshu Sun, Lei Liang, Jing Zhang  

**一句话要点**：提出Sparse-RL以解决大语言模型强化学习中长序列rollout的内存瓶颈问题

**关键词**：大语言模型强化学习, KV缓存压缩, 稀疏rollout训练, 策略失配纠正, 内存优化

## 3 点简述
- 核心问题：长序列rollout中KV缓存内存开销大，现有压缩技术直接用于RL训练导致策略失配和性能崩溃
- 方法要点：通过稀疏感知拒绝采样和重要性重加权，纠正压缩引入的离策略偏差，实现稳定稀疏rollout训练
- 实验或效果：相比密集基线减少rollout开销，保持性能，并增强稀疏推理部署的模型鲁棒性

## 摘要（原文）

> Reinforcement Learning (RL) has become essential for eliciting complex reasoning capabilities in Large Language Models (LLMs). However, the substantial memory overhead of storing Key-Value (KV) caches during long-horizon rollouts acts as a critical bottleneck, often prohibiting efficient training on limited hardware. While existing KV compression techniques offer a remedy for inference, directly applying them to RL training induces a severe policy mismatch, leading to catastrophic performance collapse. To address this, we introduce Sparse-RL empowers stable RL training under sparse rollouts. We show that instability arises from a fundamental policy mismatch among the dense old policy, the sparse sampler policy, and the learner policy. To mitigate this issue, Sparse-RL incorporates Sparsity-Aware Rejection Sampling and Importance-based Reweighting to correct the off-policy bias introduced by compression-induced information loss. Experimental results show that Sparse-RL reduces rollout overhead compared to dense baselines while preserving the performance. Furthermore, Sparse-RL inherently implements sparsity-aware training, significantly enhancing model robustness during sparse inference deployment.

