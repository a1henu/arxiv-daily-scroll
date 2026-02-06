---
layout: default
title: Thinking with Geometry: Active Geometry Integration for Spatial Reasoning
---

# Thinking with Geometry: Active Geometry Integration for Spatial Reasoning
**arXiv**：[2602.06037v1](https://arxiv.org/abs/2602.06037) · [PDF](https://arxiv.org/pdf/2602.06037.pdf)  
**作者**：Haoyuan Li, Qihang Cao, Tao Tang, Kun Xiang, Zihan Guo, Jianhua Han, Hang Xu, Xiaodan Liang  

**一句话要点**：提出GeoThinker框架，通过主动几何感知解决MLLMs空间推理中的语义-几何错位问题

**关键词**：空间推理, 多模态大语言模型, 几何感知, 主动检索, 跨模态融合, 视觉语言模型

## 3 点简述
- 现有MLLMs空间推理方法被动融合全局几何特征，导致语义-几何错位和冗余信号
- GeoThinker采用空间锚定融合和重要性门控，使模型能按推理需求主动检索几何证据
- 在VSI-Bench达到72.6分SOTA，并在具身指代和自动驾驶等场景展现强泛化能力

## 摘要（原文）

> Recent progress in spatial reasoning with Multimodal Large Language Models (MLLMs) increasingly leverages geometric priors from 3D encoders. However, most existing integration strategies remain passive: geometry is exposed as a global stream and fused in an indiscriminate manner, which often induces semantic-geometry misalignment and redundant signals. We propose GeoThinker, a framework that shifts the paradigm from passive fusion to active perception. Instead of feature mixing, GeoThinker enables the model to selectively retrieve geometric evidence conditioned on its internal reasoning demands. GeoThinker achieves this through Spatial-Grounded Fusion applied at carefully selected VLM layers, where semantic visual priors selectively query and integrate task-relevant geometry via frame-strict cross-attention, further calibrated by Importance Gating that biases per-frame attention toward task-relevant structures. Comprehensive evaluation results show that GeoThinker sets a new state-of-the-art in spatial intelligence, achieving a peak score of 72.6 on the VSI-Bench. Furthermore, GeoThinker demonstrates robust generalization and significantly improved spatial perception across complex downstream scenarios, including embodied referring and autonomous driving. Our results indicate that the ability to actively integrate spatial structures is essential for next-generation spatial intelligence. Code can be found at https://github.com/Li-Hao-yuan/GeoThinker.

