---
layout: default
title: 6G-Bench: An Open Benchmark for Semantic Communication and Network-Level Reasoning with Foundation Models in AI-Native 6G Networks
---

# 6G-Bench: An Open Benchmark for Semantic Communication and Network-Level Reasoning with Foundation Models in AI-Native 6G Networks
**arXiv**：[2602.08675v1](https://arxiv.org/abs/2602.08675) · [PDF](https://arxiv.org/pdf/2602.08675.pdf)  
**作者**：Mohamed Amine Ferrag, Abderrahmane Lakas, Merouane Debbah  

**一句话要点**：提出6G-Bench开放基准，用于评估AI原生6G网络中的语义通信与网络级推理能力。

**关键词**：语义通信, 网络级推理, 6G网络, 基础模型评估, 开放基准

## 3 点简述
- 核心问题：缺乏标准化基准来评估6G网络中语义通信和网络级推理的AI模型性能。
- 方法要点：基于5个标准化组织活动，定义30个决策任务，生成10,000个多选问题作为评估集。
- 实验或效果：评估22个基础模型，准确率范围0.22-0.82，领先模型在意图和政策推理上达0.87-0.89。

## 摘要（原文）

> This paper introduces 6G-Bench, an open benchmark for evaluating semantic communication and network-level reasoning in AI-native 6G networks. 6G-Bench defines a taxonomy of 30 decision-making tasks (T1--T30) extracted from ongoing 6G and AI-agent standardization activities in 3GPP, IETF, ETSI, ITU-T, and the O-RAN Alliance, and organizes them into five standardization-aligned capability categories. Starting from 113,475 scenarios, we generate a balanced pool of 10,000 very-hard multiple-choice questions using task-conditioned prompts that enforce multi-step quantitative reasoning under uncertainty and worst-case regret minimization over multi-turn horizons. After automated filtering and expert human validation, 3,722 questions are retained as a high-confidence evaluation set, while the full pool is released to support training and fine-tuning of 6G-specialized models. Using 6G-Bench, we evaluate 22 foundation models spanning dense and mixture-of-experts architectures, short- and long-context designs (up to 1M tokens), and both open-weight and proprietary systems. Across models, deterministic single-shot accuracy (pass@1) spans a wide range from 0.22 to 0.82, highlighting substantial variation in semantic reasoning capability. Leading models achieve intent and policy reasoning accuracy in the range 0.87--0.89, while selective robustness analysis on reasoning-intensive tasks shows pass@5 values ranging from 0.20 to 0.91. To support open science and reproducibility, we release the 6G-Bench dataset on GitHub: https://github.com/maferrag/6G-Bench

