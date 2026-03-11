---
layout: default
title: GeoSolver: Scaling Test-Time Reasoning in Remote Sensing with Fine-Grained Process Supervision
---

# GeoSolver: Scaling Test-Time Reasoning in Remote Sensing with Fine-Grained Process Supervision
**arXiv**：[2603.09551v1](https://arxiv.org/abs/2603.09551) · [PDF](https://arxiv.org/pdf/2603.09551.pdf)  
**作者**：Lang Sun, Ronghao Fu, Zhuoran Duan, Haoran Liu, Xueyan Liu, Bo Yang  

**一句话要点**：提出GeoSolver框架，通过细粒度过程监督增强遥感视觉语言模型的测试时推理能力

**关键词**：遥感视觉语言模型, 过程监督, 强化学习, 测试时扩展, 令牌级奖励模型, 视觉忠实性

## 3 点简述
- 核心问题：遥感视觉语言模型在复杂逐步推理中视觉忠实性不足，制约性能提升
- 方法要点：构建Geo-PRM-2M数据集训练令牌级过程奖励模型，结合过程感知强化学习优化推理步骤
- 实验或效果：GeoSolver-9B在多个遥感基准上达到最优，并实现跨模型的测试时性能扩展

## 摘要（原文）

> While Vision-Language Models (VLMs) have significantly advanced remote sensing interpretation, enabling them to perform complex, step-by-step reasoning remains highly challenging. Recent efforts to introduce Chain-of-Thought (CoT) reasoning to this domain have shown promise, yet ensuring the visual faithfulness of these intermediate steps remains a critical bottleneck. To address this, we introduce GeoSolver, a novel framework that transitions remote sensing reasoning toward verifiable, process-supervised reinforcement learning. We first construct Geo-PRM-2M, a large-scale, token-level process supervision dataset synthesized via entropy-guided Monte Carlo Tree Search (MCTS) and targeted visual hallucination injection. Building upon this dataset, we train GeoPRM, a token-level process reward model (PRM) that provides granular faithfulness feedback. To effectively leverage these verification signals, we propose Process-Aware Tree-GRPO, a reinforcement learning algorithm that integrates tree-structured exploration with a faithfulness-weighted reward mechanism to precisely assign credit to intermediate steps. Extensive experiments demonstrate that our resulting model, GeoSolver-9B, achieves state-of-the-art performance across diverse remote sensing benchmarks. Crucially, GeoPRM unlocks robust Test-Time Scaling (TTS). Serving as a universal geospatial verifier, it seamlessly scales the performance of GeoSolver-9B and directly enhances general-purpose VLMs, highlighting its remarkable cross-model generalization.

