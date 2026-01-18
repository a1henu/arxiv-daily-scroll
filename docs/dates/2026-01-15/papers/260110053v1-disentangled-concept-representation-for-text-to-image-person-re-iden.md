---
layout: default
title: Disentangled Concept Representation for Text-to-image Person Re-identification
---

# Disentangled Concept Representation for Text-to-image Person Re-identification
**arXiv**：[2601.10053v1](https://arxiv.org/abs/2601.10053) · [PDF](https://arxiv.org/pdf/2601.10053.pdf)  
**作者**：Giyeol Kim, Chanho Eom  

**一句话要点**：提出DiCo框架，通过解耦概念表示解决文本到图像行人重识别中的模态鸿沟与细粒度对齐问题。

**关键词**：文本到图像行人重识别, 解耦表示学习, 跨模态对齐, 细粒度检索, 槽位表示

## 3 点简述
- 核心问题：文本与图像间存在模态鸿沟，需建模细粒度对应以区分相似属性（如颜色、纹理）。
- 方法要点：引入共享槽位表示，每个槽作为跨模态部分级锚点，分解为多个概念块以实现属性解耦。
- 实验或效果：在CUHK-PEDES等数据集上达到竞争性性能，增强可解释性，支持更细粒度检索。

## 摘要（原文）

> Text-to-image person re-identification (TIReID) aims to retrieve person images from a large gallery given free-form textual descriptions. TIReID is challenging due to the substantial modality gap between visual appearances and textual expressions, as well as the need to model fine-grained correspondences that distinguish individuals with similar attributes such as clothing color, texture, or outfit style. To address these issues, we propose DiCo (Disentangled Concept Representation), a novel framework that achieves hierarchical and disentangled cross-modal alignment. DiCo introduces a shared slot-based representation, where each slot acts as a part-level anchor across modalities and is further decomposed into multiple concept blocks. This design enables the disentanglement of complementary attributes (\textit{e.g.}, color, texture, shape) while maintaining consistent part-level correspondence between image and text. Extensive experiments on CUHK-PEDES, ICFG-PEDES, and RSTPReid demonstrate that our framework achieves competitive performance with state-of-the-art methods, while also enhancing interpretability through explicit slot- and block-level representations for more fine-grained retrieval results.

