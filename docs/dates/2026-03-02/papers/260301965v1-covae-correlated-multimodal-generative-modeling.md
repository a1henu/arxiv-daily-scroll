---
layout: default
title: CoVAE: correlated multimodal generative modeling
---

# CoVAE: correlated multimodal generative modeling
**arXiv**：[2603.01965v1](https://arxiv.org/abs/2603.01965) · [PDF](https://arxiv.org/pdf/2603.01965.pdf)  
**作者**：Federico Caretti, Guido Sanguinetti  

**一句话要点**：提出CoVAE以解决多模态变分自编码器中潜在空间融合破坏联合统计结构的问题

**关键词**：多模态生成建模, 变分自编码器, 相关性捕获, 跨模态重建, 不确定性量化

## 3 点简述
- 核心问题：多模态变分自编码器在潜在空间融合时破坏数据的联合统计结构，影响生成和不确定性量化
- 方法要点：引入CoVAE架构，通过捕获模态间相关性来改进生成建模
- 实验或效果：在真实和合成数据集上测试，展示准确的跨模态重建和有效的不确定性量化

## 摘要（原文）

> Multimodal Variational Autoencoders have emerged as a popular tool to extract effective representations from rich multimodal data. However, such models rely on fusion strategies in latent space that destroy the joint statistical structure of the multimodal data, with profound implications for generation and uncertainty quantification. In this work, we introduce Correlated Variational Autoencoders (CoVAE), a new generative architecture that captures the correlations between modalities. We test CoVAE on a number of real and synthetic data sets demonstrating both accurate cross-modal reconstruction and effective quantification of the associated uncertainties.

