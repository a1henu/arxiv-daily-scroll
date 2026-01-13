---
layout: default
title: Mimic Human Cognition, Master Multi-Image Reasoning: A Meta-Action Framework for Enhanced Visual Understanding
---

# Mimic Human Cognition, Master Multi-Image Reasoning: A Meta-Action Framework for Enhanced Visual Understanding
**arXiv**：[2601.07298v1](https://arxiv.org/abs/2601.07298) · [PDF](https://arxiv.org/pdf/2601.07298.pdf)  
**作者**：Jianghao Yin, Qingbin Li, Kun Sun, Cheng Ding, Jie Wang, Qin Chen, Jie Zhou, Nan Wang, Changqing Li, Pei Wu, Jian Xu, Zheming Yang, Liang He  

**一句话要点**：提出CINEMA框架以解决多图像推理性能下降问题，通过模拟人类认知步骤提升视觉理解

**关键词**：多图像推理, 认知启发框架, 元动作分解, 强化学习训练, 视觉理解增强

## 3 点简述
- 多模态大语言模型在多图像推理中性能显著下降，面临图像间复杂关系和信息分散的挑战
- 受人类认知启发，提出CINEMA框架，将推理分解为五个结构化元动作，并采用检索树采样和两阶段强化学习训练
- 在多个基准测试中取得竞争性最优性能，超越GPT-4o和专用视频推理模型，验证框架有效性和泛化性

## 摘要（原文）

> While Multimodal Large Language Models (MLLMs) excel at single-image understanding, they exhibit significantly degraded performance in multi-image reasoning scenarios. Multi-image reasoning presents fundamental challenges including complex inter-relationships between images and scattered critical information across image sets. Inspired by human cognitive processes, we propose the Cognition-Inspired Meta-Action Framework (CINEMA), a novel approach that decomposes multi-image reasoning into five structured meta-actions: Global, Focus, Hint, Think, and Answer which explicitly modeling the sequential cognitive steps humans naturally employ. For cold-start training, we introduce a Retrieval-Based Tree Sampling strategy that generates high-quality meta-action trajectories to bootstrap the model with reasoning patterns. During reinforcement learning, we adopt a two-stage paradigm: an exploration phase with Diversity-Preserving Strategy to avoid entropy collapse, followed by an annealed exploitation phase with DAPO to gradually strengthen exploitation. To train our model, we construct a dataset of 57k cold-start and 58k reinforcement learning instances spanning multi-image, multi-frame, and single-image tasks. We conduct extensive evaluations on multi-image reasoning benchmarks, video understanding benchmarks, and single-image benchmarks, achieving competitive state-of-the-art performance on several key benchmarks. Our model surpasses GPT-4o on the MUIR and MVMath benchmarks and notably outperforms specialized video reasoning models on video understanding benchmarks, demonstrating the effectiveness and generalizability of our human cognition-inspired reasoning framework.

