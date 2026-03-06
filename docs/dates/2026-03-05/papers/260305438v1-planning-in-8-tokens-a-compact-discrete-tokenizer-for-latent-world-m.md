---
layout: default
title: Planning in 8 Tokens: A Compact Discrete Tokenizer for Latent World Model
---

# Planning in 8 Tokens: A Compact Discrete Tokenizer for Latent World Model
**arXiv**：[2603.05438v1](https://arxiv.org/abs/2603.05438) · [PDF](https://arxiv.org/pdf/2603.05438.pdf)  
**作者**：Dongwon Kim, Gawon Seo, Jinsung Lee, Minsu Cho, Suha Kwak  

**一句话要点**：提出CompACT离散分词器，将观测压缩至8个令牌以加速世界模型决策规划

**关键词**：世界模型, 离散分词器, 决策规划, 计算效率, 观测压缩

## 3 点简述
- 核心问题：传统分词器编码观测为数百令牌，导致世界模型决策规划计算成本高、速度慢
- 方法要点：设计CompACT离散分词器，压缩观测至8个令牌，保留规划所需关键信息
- 实验或效果：基于CompACT的世界模型实现竞争性规划性能，规划速度提升数个数量级

## 摘要（原文）

> World models provide a powerful framework for simulating environment dynamics conditioned on actions or instructions, enabling downstream tasks such as action planning or policy learning. Recent approaches leverage world models as learned simulators, but its application to decision-time planning remains computationally prohibitive for real-time control. A key bottleneck lies in latent representations: conventional tokenizers encode each observation into hundreds of tokens, making planning both slow and resource-intensive. To address this, we propose CompACT, a discrete tokenizer that compresses each observation into as few as 8 tokens, drastically reducing computational cost while preserving essential information for planning. An action-conditioned world model that occupies CompACT tokenizer achieves competitive planning performance with orders-of-magnitude faster planning, offering a practical step toward real-world deployment of world models.

