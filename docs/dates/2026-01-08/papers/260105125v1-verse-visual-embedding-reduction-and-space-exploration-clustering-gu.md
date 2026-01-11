---
layout: default
title: VERSE: Visual Embedding Reduction and Space Exploration. Clustering-Guided Insights for Training Data Enhancement in Visually-Rich Document Understanding
---

# VERSE: Visual Embedding Reduction and Space Exploration. Clustering-Guided Insights for Training Data Enhancement in Visually-Rich Document Understanding
**arXiv**：[2601.05125v1](https://arxiv.org/abs/2601.05125) · [PDF](https://arxiv.org/pdf/2601.05125.pdf)  
**作者**：Ignacio de Rodrigo, Alvaro J. Lopez-Lopez, Jaime Boal  

**一句话要点**：提出VERSE方法，通过聚类引导的视觉嵌入空间探索，增强视觉丰富文档理解模型的训练数据。

**关键词**：视觉丰富文档理解, 视觉嵌入空间分析, 聚类引导数据增强, 合成数据生成, 模型性能优化

## 3 点简述
- 核心问题：视觉语言模型在视觉丰富文档理解中，视觉嵌入空间难以可视化，导致模型评估和性能提升受限。
- 方法要点：VERSE通过降维和聚类分析，可视化潜在表示，识别问题区域，并指导合成数据生成以优化训练。
- 实验或效果：在MERIT数据集上验证，VERSE帮助发现错误特征，重训练后F1性能显著提升，且不损害泛化能力。

## 摘要（原文）

> This work introduces VERSE, a methodology for analyzing and improving Vision-Language Models applied to Visually-rich Document Understanding by exploring their visual embedding space. VERSE enables the visualization of latent representations, supporting the assessment of model feasibility. It also facilitates the identification of problematic regions and guides the generation of synthetic data to enhance performance in those clusters. We validate the methodology by training on the synthetic MERIT Dataset and evaluating on its real-world counterpart, MERIT Secret. Results show that VERSE helps uncover the visual features associated with error-prone clusters, and that retraining with samples containing these features substantially boosts F1 performance without degrading generalization. Furthermore, we demonstrate that on-premise models such as Donut and Idefics2, when optimized with VERSE, match or even surpass the performance of SaaS solutions like GPT-4 and Pixtral.

