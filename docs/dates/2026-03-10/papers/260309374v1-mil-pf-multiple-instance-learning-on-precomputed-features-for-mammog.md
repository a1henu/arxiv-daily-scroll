---
layout: default
title: MIL-PF: Multiple Instance Learning on Precomputed Features for Mammography Classification
---

# MIL-PF: Multiple Instance Learning on Precomputed Features for Mammography Classification
**arXiv**：[2603.09374v1](https://arxiv.org/abs/2603.09374) · [PDF](https://arxiv.org/pdf/2603.09374.pdf)  
**作者**：Nikola Jovišić, Milica Škipina, Nicola Dall'Asen, Dubravko Ćulibrk  

**一句话要点**：提出MIL-PF框架，结合冻结基础编码器与轻量MIL头，用于乳腺X线摄影分类。

**关键词**：多实例学习, 医学影像分类, 预计算特征, 注意力聚合, 乳腺X线摄影, 轻量模型

## 3 点简述
- 问题：乳腺X线摄影图像大、标注少，端到端微调计算成本高。
- 方法：预计算特征后，仅训练小型注意力聚合模块，降低训练复杂度。
- 效果：在临床规模上实现先进分类性能，代码开源确保可复现性。

## 摘要（原文）

> Modern foundation models provide highly expressive visual representations, yet adapting them to high-resolution medical imaging remains challenging due to limited annotations and weak supervision. Mammography, in particular, is characterized by large images, variable multi-view studies and predominantly breast-level labels, making end-to-end fine-tuning computationally expensive and often impractical. We propose Multiple Instance Learning on Precomputed Features (MIL-PF), a scalable framework that combines frozen foundation encoders with a lightweight MIL head for mammography classification. By precomputing the semantic representations and training only a small task-specific aggregation module (40k parameters), the method enables efficient experimentation and adaptation without retraining large backbones. The architecture explicitly models the global tissue context and the sparse local lesion signals through attention-based aggregation. MIL-PF achieves state-of-the-art classification performance at clinical scale while substantially reducing training complexity. We release the code for full reproducibility.

