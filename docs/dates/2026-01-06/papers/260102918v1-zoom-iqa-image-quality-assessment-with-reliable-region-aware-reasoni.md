---
layout: default
title: Zoom-IQA: Image Quality Assessment with Reliable Region-Aware Reasoning
---

# Zoom-IQA: Image Quality Assessment with Reliable Region-Aware Reasoning
**arXiv**：[2601.02918v1](https://arxiv.org/abs/2601.02918) · [PDF](https://arxiv.org/pdf/2601.02918.pdf)  
**作者**：Guoqiang Liang, Jianyi Wang, Zhonghua Wu, Shangchen Zhou  

**一句话要点**：提出Zoom-IQA模型，通过模拟关键认知行为提升图像质量评估的可靠性与可解释性。

**关键词**：图像质量评估, 视觉语言模型, 强化学习, 可解释性, 区域推理, 迭代优化

## 3 点简述
- 核心问题：现有基于视觉语言模型的IQA方法因视觉与文本线索整合能力有限，导致推理不可靠。
- 方法要点：采用两阶段训练，包括监督微调以基于关键区域评估，以及强化学习结合KL-Coverage正则化防止多样性崩溃。
- 实验或效果：实验显示Zoom-IQA在鲁棒性、可解释性和泛化性方面有改进，并在图像修复等下游任务中验证有效性。

## 摘要（原文）

> Image Quality Assessment (IQA) is a long-standing problem in computer vision. Previous methods typically focus on predicting numerical scores without explanation or provide low-level descriptions lacking precise scores. Recent reasoning-based vision language models (VLMs) have shown strong potential for IQA, enabling joint generation of quality descriptions and scores. However, we notice that existing VLM-based IQA methods tend to exhibit unreliable reasoning due to their limited capability of integrating visual and textual cues. In this work, we introduce Zoom-IQA, a VLM-based IQA model to explicitly emulate key cognitive behaviors: uncertainty awareness, region reasoning, and iterative refinement. Specifically, we present a two-stage training pipeline: 1) supervised fine-tuning (SFT) on our Grounded-Rationale-IQA (GR-IQA) dataset to teach the model to ground its assessments in key regions; and 2) reinforcement learning (RL) for dynamic policy exploration, primarily stabilized by our KL-Coverage regularizer to prevent reasoning and scoring diversity collapse, and supported by a Progressive Re-sampling Strategy to mitigate annotation bias. Extensive experiments show that Zoom-IQA achieves improved robustness, explainability, and generalization. The application to downstream tasks, such as image restoration, further demonstrates the effectiveness of Zoom-IQA.

