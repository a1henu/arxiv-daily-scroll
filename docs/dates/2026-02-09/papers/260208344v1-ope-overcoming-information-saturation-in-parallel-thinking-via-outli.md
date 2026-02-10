---
layout: default
title: OPE: Overcoming Information Saturation in Parallel Thinking via Outline-Guided Path Exploration
---

# OPE: Overcoming Information Saturation in Parallel Thinking via Outline-Guided Path Exploration
**arXiv**：[2602.08344v1](https://arxiv.org/abs/2602.08344) · [PDF](https://arxiv.org/pdf/2602.08344.pdf)  
**作者**：Qi Guo, Jianing Wang, Deyang Kong, Xiangyu Xi, Jianfei Zhang, Yi Lu, Jingang Wang, Wei Wang, Shikun Zhang, Wei Ye  

**一句话要点**：提出OPE以解决并行思维中探索路径信息饱和问题，通过大纲引导提升推理性能

**关键词**：并行思维, 强化学习, 路径探索, 信息饱和, 推理模型, 大纲引导

## 3 点简述
- 核心问题：并行思维中探索路径间互信息瓶颈限制整体性能，导致信息冗余
- 方法要点：OPE通过生成多样化推理大纲划分解空间，减少冗余并提升信息多样性
- 实验或效果：在多个数学基准测试中，OPE有效提升不同聚合策略下的推理性能

## 摘要（原文）

> Parallel thinking has emerged as a new paradigm for large reasoning models (LRMs) in tackling complex problems. Recent methods leverage Reinforcement Learning (RL) to enhance parallel thinking, aiming to address the limitations in computational resources and effectiveness encountered with supervised fine-tuning. However, most existing studies primarily focus on optimizing the aggregation phase, with limited attention to the path exploration stage. In this paper, we theoretically analyze the optimization of parallel thinking under the Reinforcement Learning with Verifiable Rewards (RLVR) setting, and identify that the mutual information bottleneck among exploration paths fundamentally restricts overall performance. To address this, we propose Outline-Guided Path Exploration (OPE), which explicitly partitions the solution space by generating diverse reasoning outlines prior to parallel path reasoning, thereby reducing information redundancy and improving the diversity of information captured across exploration paths. We implement OPE with an iterative RL strategy that optimizes outline planning and outline-guided reasoning independently. Extensive experiments across multiple challenging mathematical benchmarks demonstrate that OPE effectively improves reasoning performance in different aggregation strategies, enabling LRMs to more reliably discover correct solutions.

