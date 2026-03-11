---
layout: default
title: GIAT: A Geologically-Informed Attention Transformer for Lithology Identification
---

# GIAT: A Geologically-Informed Attention Transformer for Lithology Identification
**arXiv**：[2603.09165v1](https://arxiv.org/abs/2603.09165) · [PDF](https://arxiv.org/pdf/2603.09165.pdf)  
**作者**：Jie Li, Qishun Yang, Nuo Li  

**一句话要点**：提出GIAT框架，融合地质先验与注意力机制以提升岩性识别准确性与可解释性。

**关键词**：岩性识别, 注意力机制, 地质先验, Transformer模型, 可解释性AI

## 3 点简述
- 核心问题：Transformer模型在岩性识别中缺乏地质指导，导致性能受限且可解释性差。
- 方法要点：引入地质信息注意力机制，通过CSC滤波器生成关系矩阵，引导模型学习地质一致性模式。
- 实验或效果：在两个数据集上达到最高95.4%准确率，显著优于现有模型，并展示出强鲁棒性和可解释性。

## 摘要（原文）

> Accurate lithology identification from well logs is crucial for subsurface resource evaluation. Although Transformer-based models excel at sequence modeling, their "black-box" nature and lack of geological guidance limit their performance and trustworthiness. To overcome these limitations, this letter proposes the Geologically-Informed Attention Transformer (GIAT), a novel framework that deeply fuses data-driven geological priors with the Transformer's attention mechanism. The core of GIAT is a new attention-biasing mechanism. We repurpose Category-Wise Sequence Correlation (CSC) filters to generate a geologically-informed relational matrix, which is injected into the self-attention calculation to explicitly guide the model toward geologically coherent patterns. On two challenging datasets, GIAT achieves state-of-the-art performance with an accuracy of up to 95.4%, significantly outperforming existing models. More importantly, GIAT demonstrates exceptional interpretation faithfulness under input perturbations and generates geologically coherent predictions. Our work presents a new paradigm for building more accurate, reliable, and interpretable deep learning models for geoscience applications.

