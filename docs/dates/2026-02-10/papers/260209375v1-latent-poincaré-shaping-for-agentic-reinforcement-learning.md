---
layout: default
title: Latent Poincaré Shaping for Agentic Reinforcement Learning
---

# Latent Poincaré Shaping for Agentic Reinforcement Learning
**arXiv**：[2602.09375v1](https://arxiv.org/abs/2602.09375) · [PDF](https://arxiv.org/pdf/2602.09375.pdf)  
**作者**：Hanchen Xia, Baoyou Chen, Zelin Zang, Yutang Ge, Guojiang Zhao, Siyu Zhu  

**一句话要点**：提出LaPha方法，在双曲潜在空间中训练AlphaZero类LLM代理以提升数学推理性能。

**关键词**：强化学习, 双曲几何, 潜在空间, 数学推理, AlphaZero代理, 值头引导搜索

## 3 点简述
- 核心问题：如何高效训练AlphaZero类LLM代理以增强数学推理能力。
- 方法要点：在双曲潜在空间中构建搜索树，利用负曲率增加容量，定义节点势能分配密集奖励。
- 实验或效果：在MATH-500上提升Qwen2.5-Math-1.5B至88.2%，在AIME'24上LaPha-7B达到60.0%准确率。

## 摘要（原文）

> We propose LaPha, a method for training AlphaZero-like LLM agents in a Poincaré latent space. Under LaPha, the search process can be visualized as a tree rooted at the prompt and growing outward from the origin toward the boundary of the Poincaré ball, where negative curvature provides exponentially increasing capacity with radius. Using hyperbolic geodesic distance to rule-verified correctness, we define a node potential and assign dense process rewards by potential differences. We further attach a lightweight value head on the same shared latent space, enabling self-guided test-time scaling with almost no additional overhead. On MATH-500, LaPha improves Qwen2.5-Math-1.5B from 66.0% to 88.2%. With value-head-guided search, LaPha-1.5B reaches 56.7% accuracy on AIME'24, and LaPha-7B further achieves 60.0% on AIME'24 and 53.3% on AIME'25.

