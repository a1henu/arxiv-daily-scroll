---
layout: default
title: Evaluating Disentangled Representations for Controllable Music Generation
---

# Evaluating Disentangled Representations for Controllable Music Generation
**arXiv**：[2602.10058v1](https://arxiv.org/abs/2602.10058) · [PDF](https://arxiv.org/pdf/2602.10058.pdf)  
**作者**：Laura Ibáñez-Martínez, Chukwuemeka Nkama, Andrea Poltronieri, Xavier Serra, Martín Rocamora  

**一句话要点**：评估解耦表示在可控音乐生成中的实际语义一致性

**关键词**：可控音乐生成, 解耦表示评估, 无监督学习, 音频模型, 语义一致性, 探测框架

## 3 点简述
- 核心问题：现有音乐生成模型依赖解耦表示（如结构与音色）实现可控合成，但其嵌入的实际语义与预期不符，缺乏深入评估。
- 方法要点：采用基于探测的框架，超越标准下游任务，评估多种无监督解耦策略（如归纳偏置、数据增强）在信息性、等变性、不变性和解耦性四个轴上的表现。
- 实验或效果：分析揭示嵌入语义不一致，表明当前策略未能产生真正解耦的表示，提示需重新审视可控音乐生成方法。

## 摘要（原文）

> Recent approaches in music generation rely on disentangled representations, often labeled as structure and timbre or local and global, to enable controllable synthesis. Yet the underlying properties of these embeddings remain underexplored. In this work, we evaluate such disentangled representations in a set of music audio models for controllable generation using a probing-based framework that goes beyond standard downstream tasks. The selected models reflect diverse unsupervised disentanglement strategies, including inductive biases, data augmentations, adversarial objectives, and staged training procedures. We further isolate specific strategies to analyze their effect. Our analysis spans four key axes: informativeness, equivariance, invariance, and disentanglement, which are assessed across datasets, tasks, and controlled transformations. Our findings reveal inconsistencies between intended and actual semantics of the embeddings, suggesting that current strategies fall short of producing truly disentangled representations, and prompting a re-examination of how controllability is approached in music generation.

