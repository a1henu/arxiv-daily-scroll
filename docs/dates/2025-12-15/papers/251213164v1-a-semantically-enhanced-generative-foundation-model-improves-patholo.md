---
layout: default
title: A Semantically Enhanced Generative Foundation Model Improves Pathological Image Synthesis
---

# A Semantically Enhanced Generative Foundation Model Improves Pathological Image Synthesis
**arXiv**：[2512.13164v1](https://arxiv.org/abs/2512.13164) · [PDF](https://arxiv.org/pdf/2512.13164.pdf)  
**作者**：Xianchao Guan, Zhiyuan Fan, Yifeng Wang, Fuqiang Chen, Yanjiang Zhou, Zengyang Che, Hongxue Meng, Xin Li, Yaowei Wang, Hongpeng Wang, Min Zhang, Heng Tao Shen, Zheng Zhang, Yongbing Zhang  

**一句话要点**：提出CRAFTS生成基础模型以解决病理图像合成中的语义不稳定问题

**关键词**：病理图像合成, 生成基础模型, 语义对齐, 数据增强, 临床AI

## 3 点简述
- 核心问题：病理AI发展受限于高质量标注数据稀缺，现有生成模型存在语义漂移和形态幻觉。
- 方法要点：采用双阶段训练和相关性对齐机制，基于280万图像-文本对，确保生物准确性。
- 实验或效果：生成30种癌症类型图像，通过客观指标和病理学家评估验证，增强多种临床任务性能。

## 摘要（原文）

> The development of clinical-grade artificial intelligence in pathology is limited by the scarcity of diverse, high-quality annotated datasets. Generative models offer a potential solution but suffer from semantic instability and morphological hallucinations that compromise diagnostic reliability. To address this challenge, we introduce a Correlation-Regulated Alignment Framework for Tissue Synthesis (CRAFTS), the first generative foundation model for pathology-specific text-to-image synthesis. By leveraging a dual-stage training strategy on approximately 2.8 million image-caption pairs, CRAFTS incorporates a novel alignment mechanism that suppresses semantic drift to ensure biological accuracy. This model generates diverse pathological images spanning 30 cancer types, with quality rigorously validated by objective metrics and pathologist evaluations. Furthermore, CRAFTS-augmented datasets enhance the performance across various clinical tasks, including classification, cross-modal retrieval, self-supervised learning, and visual question answering. In addition, coupling CRAFTS with ControlNet enables precise control over tissue architecture from inputs such as nuclear segmentation masks and fluorescence images. By overcoming the critical barriers of data scarcity and privacy concerns, CRAFTS provides a limitless source of diverse, annotated histology data, effectively unlocking the creation of robust diagnostic tools for rare and complex cancer phenotypes.

