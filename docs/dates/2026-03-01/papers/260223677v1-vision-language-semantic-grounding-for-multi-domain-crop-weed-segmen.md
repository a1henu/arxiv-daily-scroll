---
layout: default
title: Vision-Language Semantic Grounding for Multi-Domain Crop-Weed Segmentation
---

# Vision-Language Semantic Grounding for Multi-Domain Crop-Weed Segmentation
**arXiv**：[2602.23677v1](https://arxiv.org/abs/2602.23677) · [PDF](https://arxiv.org/pdf/2602.23677.pdf)  
**作者**：Nazia Hossain, Xintong Jiang, Yu Tian, Philippe Seguin, O. Grant Clark, Shangpeng Sun  

**一句话要点**：提出VL-WS框架，通过视觉-语言语义对齐解决多域作物-杂草分割的泛化问题。

**关键词**：视觉-语言语义对齐, 多域作物-杂草分割, 特征调制, 泛化性能, 精准农业

## 3 点简述
- 现有深度学习模型依赖数据集特定视觉特征，难以在异构农业环境中泛化。
- VL-WS采用双编码器设计，融合CLIP嵌入和空间特征，通过FiLM层以文本描述调制特征。
- 在四个基准数据集上，VL-WS平均Dice分数达91.64%，对最具挑战的杂草类提升15.42%。

## 摘要（原文）

> Fine-grained crop-weed segmentation is essential for enabling targeted herbicide application in precision agriculture. However, existing deep learning models struggle to generalize across heterogeneous agricultural environments due to reliance on dataset-specific visual features. We propose Vision-Language Weed Segmentation (VL-WS), a novel framework that addresses this limitation by grounding pixel-level segmentation in semantically aligned, domain-invariant representations. Our architecture employs a dual-encoder design, where frozen Contrastive Language-Image Pretraining (CLIP) embeddings and task-specific spatial features are fused and modulated via Feature-wise Linear Modulation (FiLM) layers conditioned on natural language captions. This design enables image level textual descriptions to guide channel-wise feature refinement while preserving fine-grained spatial localization. Unlike prior works restricted to training and evaluation on single-source datasets, VL-WS is trained on a unified corpus that includes close-range ground imagery (robotic platforms) and high-altitude UAV imagery, covering diverse crop types, weed species, growth stages, and sensing conditions. Experimental results across four benchmark datasets demonstrate the effectiveness of our framework, with VL-WS achieving a mean Dice score of 91.64% and outperforming the CNN baseline by 4.98%. The largest gains occur on the most challenging weed class, where VL-WS attains 80.45% Dice score compared to 65.03% for the best baseline, representing a 15.42% improvement. VL-WS further maintains stable weed segmentation performance under limited target-domain supervision, indicating improved generalization and data efficiency. These findings highlight the potential of vision-language alignment to enable scalable, label-efficient segmentation models deployable across diverse real-world agricultural domains.

