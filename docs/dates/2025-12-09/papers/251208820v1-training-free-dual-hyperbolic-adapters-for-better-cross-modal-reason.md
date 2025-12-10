---
layout: default
title: Training-Free Dual Hyperbolic Adapters for Better Cross-Modal Reasoning
---

# Training-Free Dual Hyperbolic Adapters for Better Cross-Modal Reasoning
**arXiv**：[2512.08820v1](https://arxiv.org/abs/2512.08820) · [PDF](https://arxiv.org/pdf/2512.08820.pdf)  
**作者**：Yi Zhang, Chun-Wun Cheng, Junyi He, Ke Yu, Yushun Tang, Carola-Bibiane Schönlieb, Zhihai He, Angelica I. Aviles-Rivero  

**一句话要点**：提出训练自由双曲适配器以提升跨模态推理的鲁棒性和效率

**关键词**：视觉语言模型, 跨模态推理, 双曲空间, 训练自由适配, 领域泛化, 少样本学习

## 3 点简述
- 现有视觉语言模型在领域变化时性能下降或需大量计算资源微调
- 在双曲空间建模层次化语义关系，利用指数体积增长提升表示能力
- 实验显示在少样本图像识别和领域泛化任务中优于现有方法

## 摘要（原文）

> Recent research in Vision-Language Models (VLMs) has significantly advanced our capabilities in cross-modal reasoning. However, existing methods suffer from performance degradation with domain changes or require substantial computational resources for fine-tuning in new domains. To address this issue, we develop a new adaptation method for large vision-language models, called \textit{Training-free Dual Hyperbolic Adapters} (T-DHA). We characterize the vision-language relationship between semantic concepts, which typically has a hierarchical tree structure, in the hyperbolic space instead of the traditional Euclidean space. Hyperbolic spaces exhibit exponential volume growth with radius, unlike the polynomial growth in Euclidean space. We find that this unique property is particularly effective for embedding hierarchical data structures using the Poincaré ball model, achieving significantly improved representation and discrimination power. Coupled with negative learning, it provides more accurate and robust classifications with fewer feature dimensions. Our extensive experimental results on various datasets demonstrate that the T-DHA method significantly outperforms existing state-of-the-art methods in few-shot image recognition and domain generalization tasks.

