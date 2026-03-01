---
layout: default
title: Beyond Detection: Multi-Scale Hidden-Code for Natural Image Deepfake Recovery and Factual Retrieval
---

# Beyond Detection: Multi-Scale Hidden-Code for Natural Image Deepfake Recovery and Factual Retrieval
**arXiv**：[2602.22759v1](https://arxiv.org/abs/2602.22759) · [PDF](https://arxiv.org/pdf/2602.22759.pdf)  
**作者**：Yuan-Chih Chen, Chun-Shien Lu  

**一句话要点**：提出多尺度隐藏码框架以解决自然图像深度伪造恢复与事实检索问题

**关键词**：深度伪造恢复, 事实检索, 多尺度隐藏码, 向量量化, 条件Transformer, 图像水印

## 3 点简述
- 核心问题：深度伪造检测与定位后，篡改内容恢复与事实检索研究不足
- 方法要点：通过多尺度向量量化和条件Transformer模块编码语义感知信息为紧凑隐藏码
- 实验或效果：在ImageNet-S基准上展示良好检索与重建性能，兼容多种水印方案

## 摘要（原文）

> Recent advances in image authenticity have primarily focused on deepfake detection and localization, leaving recovery of tampered contents for factual retrieval relatively underexplored. We propose a unified hidden-code recovery framework that enables both retrieval and restoration from post-hoc and in-generation watermarking paradigms. Our method encodes semantic and perceptual information into a compact hidden-code representation, refined through multi-scale vector quantization, and enhances contextual reasoning via conditional Transformer modules. To enable systematic evaluation for natural images, we construct ImageNet-S, a benchmark that provides paired image-label factual retrieval tasks. Extensive experiments on ImageNet-S demonstrate that our method exhibits promising retrieval and reconstruction performance while remaining fully compatible with diverse watermarking pipelines. This framework establishes a foundation for general-purpose image recovery beyond detection and localization.

