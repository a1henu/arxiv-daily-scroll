---
layout: default
title: SRAS: A Lightweight Reinforcement Learning-based Document Selector for Edge-Native RAG Pipelines
---

# SRAS: A Lightweight Reinforcement Learning-based Document Selector for Edge-Native RAG Pipelines
**arXiv**：[2601.01785v1](https://arxiv.org/abs/2601.01785) · [PDF](https://arxiv.org/pdf/2601.01785.pdf)  
**作者**：Rajiv Chaitanya Muttur  

**一句话要点**：提出SRAS，一种基于强化学习的轻量级文档选择器，用于边缘原生RAG管道。

**关键词**：检索增强生成, 强化学习, 文档选择, 边缘计算, 轻量级模型, 延迟优化

## 3 点简述
- 核心问题：传统RAG系统使用固定top-k文档选择，忽略生成质量且计算开销大。
- 方法要点：SRAS通过PPO训练紧凑策略，结合Relaxed F1和BERTScore奖励，适应边缘设备约束。
- 实验或效果：在合成QA基准上优于监督和随机选择器，SQuAD v2上BERTScore F1达0.8546，无需领域调优。

## 摘要（原文）

> Retrieval-Augmented Generation (RAG) systems often rely on fixed top-k document selection mechanisms that ignore downstream generation quality and impose computational overheads. We propose SRAS (Sparse Reward-Aware Selector), a lightweight document selector trained via reinforcement learning (RL) for edge-native RAG deployment. Unlike prior RL-based retrievers that assume large memory and latency budgets, SRAS learns a compact (~0.76MB) policy using Proximal Policy Optimization (PPO), guided by a hybrid reward signal combining Relaxed F1 and BERTScore. Our method operates under tight token and compute constraints, maintaining <1s latency on CPU. SRAS outperforms supervised and random selectors on a synthetic QA benchmark, and generalizes to real-world data, achieving BERTScore F1 of 0.8546 on SQuAD v2 without domain-specific tuning. This work is the first to demonstrate that RL-based document selection can be made ultra-lightweight, latency-aware, and effective for on-device RAG pipelines.

