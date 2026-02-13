---
layout: default
title: ThinkRouter: Efficient Reasoning via Routing Thinking between Latent and Discrete Spaces
---

# ThinkRouter: Efficient Reasoning via Routing Thinking between Latent and Discrete Spaces
**arXiv**：[2602.11683v1](https://arxiv.org/abs/2602.11683) · [PDF](https://arxiv.org/pdf/2602.11683.pdf)  
**作者**：Xin Xu, Tong Yu, Xiang Chen, Haoliang Wang, Julian McAuley, Saayan Mitra  

**一句话要点**：提出ThinkRouter推理时置信度感知路由机制，以提升大模型在STEM和编码任务中的推理效率与准确性。

**关键词**：推理效率, 置信度路由, 潜在空间推理, STEM推理, 编码基准, 模型校准

## 3 点简述
- 核心问题：潜在推理中，错误答案轨迹因低置信度步骤少而高置信，软嵌入聚合可能引入噪声，影响推理可靠性。
- 方法要点：ThinkRouter根据模型置信度动态路由思考，低置信时转向离散令牌空间，高置信时转向潜在空间，避免噪声传播。
- 实验或效果：在多个大推理模型上，ThinkRouter在准确率上优于显式CoT、随机路由和潜在推理基线，平均提升Pass@1 19.70点，生成长度减少达15.55%。

## 摘要（原文）

> Recent work explores latent reasoning to improve reasoning efficiency by replacing explicit reasoning trajectories with continuous representations in a latent space, yet its effectiveness varies across settings. Analysis of model confidence dynamics under latent reasoning reveals that thinking trajectories ending in incorrect answers contain fewer low-confidence steps than those ending in correct answers. Meanwhile, we suggest that soft embeddings aggregated by multiple low-confidence thinking alternatives may introduce and propagate noise, leading to high confidence in unreliable reasoning trajectories. Motivated by these observations, ThinkRouter, an inference-time confidence-aware routing mechanism is proposed to avoid high confidence and noise for efficient reasoning. ThinkRouter routes thinking to the discrete token space when model confidence is low, and to the latent space otherwise. Extensive experiments on STEM reasoning and coding benchmarks across diverse large reasoning models demonstrate that ThinkRouter outperforms explicit CoT, random routing, and latent reasoning baselines in terms of accuracy, achieving an average improvement of 19.70 points in Pass@1, while reducing generation length by up to 15.55%. Further comprehensive analysis reveals that ThinkRouter can calibrate errors arising from explicit CoT and latent reasoning, and accelerates end-of-thinking token generation by globally lowering model confidence.

