---
layout: default
title: Latent Chain-of-Thought as Planning: Decoupling Reasoning from Verbalization
---

# Latent Chain-of-Thought as Planning: Decoupling Reasoning from Verbalization
**arXiv**：[2601.21358v1](https://arxiv.org/abs/2601.21358) · [PDF](https://arxiv.org/pdf/2601.21358.pdf)  
**作者**：Jiecong Wang, Hao Peng, Chunyang Liu  

**一句话要点**：提出PLaT框架，通过解耦推理与语言化，将潜在推理建模为规划过程。

**关键词**：潜在推理, 推理规划, 语言模型推理, 推理多样性, 动态终止

## 3 点简述
- 核心问题：CoT推理受限于计算成本和离散标记空间中的推理路径崩溃。
- 方法要点：将推理建模为确定性潜在规划轨迹，分离解码器进行语言化，支持动态终止。
- 实验或效果：在数学基准上，PLaT展现推理多样性优势，学习更鲁棒的解决方案空间。

## 摘要（原文）

> Chain-of-Thought (CoT) empowers Large Language Models (LLMs) to tackle complex problems, but remains constrained by the computational cost and reasoning path collapse when grounded in discrete token spaces. Recent latent reasoning approaches attempt to optimize efficiency by performing reasoning within continuous hidden states. However, these methods typically operate as opaque end-to-end mappings from explicit reasoning steps to latent states, and often require a pre-defined number of latent steps during inference. In this work, we introduce PLaT (Planning with Latent Thoughts), a framework that reformulates latent reasoning as planning by fundamentally decouple reasoning from verbalization. We model reasoning as a deterministic trajectory of latent planning states, while a separate Decoder grounds these thoughts into text when necessary. This decoupling allows the model to dynamically determine when to terminate reasoning rather than relying on fixed hyperparameters. Empirical results on mathematical benchmarks reveal a distinct trade-off: while PLaT achieves lower greedy accuracy than baselines, it demonstrates superior scalability in terms of reasoning diversity. This indicates that PLaT learns a robust, broader solution space, offering a transparent and scalable foundation for inference-time search.

