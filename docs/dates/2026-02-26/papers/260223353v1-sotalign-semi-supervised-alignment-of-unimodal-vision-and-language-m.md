---
layout: default
title: SOTAlign: Semi-Supervised Alignment of Unimodal Vision and Language Models via Optimal Transport
---

# SOTAlign: Semi-Supervised Alignment of Unimodal Vision and Language Models via Optimal Transport
**arXiv**：[2602.23353v1](https://arxiv.org/abs/2602.23353) · [PDF](https://arxiv.org/pdf/2602.23353.pdf)  
**作者**：Simon Roschmann, Paul Krzakala, Sonia Mazelet, Quentin Bouniot, Zeynep Akata  

**一句话要点**：提出SOTAlign框架，通过最优传输在半监督场景下对齐单模态视觉与语言模型。

**关键词**：视觉语言对齐, 半监督学习, 最优传输, 单模态编码器, 联合嵌入

## 3 点简述
- 核心问题：如何用少量配对数据和大量未配对数据对齐预训练单模态编码器。
- 方法要点：两阶段框架，先用线性教师恢复粗略共享几何，再基于最优传输在未配对数据上精炼对齐。
- 实验或效果：显著优于监督和半监督基线，学习跨数据集和编码器对的鲁棒联合嵌入。

## 摘要（原文）

> The Platonic Representation Hypothesis posits that neural networks trained on different modalities converge toward a shared statistical model of the world. Recent work exploits this convergence by aligning frozen pretrained vision and language models with lightweight alignment layers, but typically relies on contrastive losses and millions of paired samples. In this work, we ask whether meaningful alignment can be achieved with substantially less supervision. We introduce a semi-supervised setting in which pretrained unimodal encoders are aligned using a small number of image-text pairs together with large amounts of unpaired data. To address this challenge, we propose SOTAlign, a two-stage framework that first recovers a coarse shared geometry from limited paired data using a linear teacher, then refines the alignment on unpaired samples via an optimal-transport-based divergence that transfers relational structure without overconstraining the target space. Unlike existing semi-supervised methods, SOTAlign effectively leverages unpaired images and text, learning robust joint embeddings across datasets and encoder pairs, and significantly outperforming supervised and semi-supervised baselines.

