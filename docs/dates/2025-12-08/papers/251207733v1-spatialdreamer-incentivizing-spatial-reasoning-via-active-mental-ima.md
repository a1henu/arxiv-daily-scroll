---
layout: default
title: SpatialDreamer: Incentivizing Spatial Reasoning via Active Mental Imagery
---

# SpatialDreamer: Incentivizing Spatial Reasoning via Active Mental Imagery
**arXiv**：[2512.07733v1](https://arxiv.org/abs/2512.07733) · [PDF](https://arxiv.org/pdf/2512.07733.pdf)  
**作者**：Meng Cao, Xingyu Li, Xue Liu, Ian Reid, Xiaodan Liang  

**一句话要点**：提出SpatialDreamer强化学习框架，通过主动探索和世界模型解决MLLMs空间推理任务中的心理模拟不足问题。

**关键词**：空间推理, 强化学习, 世界模型, 心理模拟, 多模态大语言模型, 几何一致性

## 3 点简述
- 核心问题：多模态大语言模型在需要心理模拟的复杂空间推理任务中表现受限，缺乏主动心理意象过程。
- 方法要点：采用强化学习框架，结合主动探索、世界模型视觉想象和基于证据的推理，并引入几何策略优化以处理长序列任务的奖励监督。
- 实验或效果：在多个挑战性基准测试中取得竞争性结果，提升了MLLMs类人主动空间心理模拟能力。

## 摘要（原文）

> Despite advancements in Multi-modal Large Language Models (MLLMs) for scene understanding, their performance on complex spatial reasoning tasks requiring mental simulation remains significantly limited. Current methods often rely on passive observation of spatial data, failing to internalize an active mental imagery process. To bridge this gap, we propose SpatialDreamer, a reinforcement learning framework that enables spatial reasoning through a closedloop process of active exploration, visual imagination via a world model, and evidence-grounded reasoning. To address the lack of fine-grained reward supervision in longhorizontal reasoning tasks, we propose Geometric Policy Optimization (GeoPO), which introduces tree-structured sampling and step-level reward estimation with geometric consistency constraints. Extensive experiments demonstrate that SpatialDreamer delivers highly competitive results across multiple challenging benchmarks, signifying a critical advancement in human-like active spatial mental simulation for MLLMs.

