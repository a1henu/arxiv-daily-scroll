---
layout: default
title: Bridging Cognitive Gap: Hierarchical Description Learning for Artistic Image Aesthetics Assessment
---

# Bridging Cognitive Gap: Hierarchical Description Learning for Artistic Image Aesthetics Assessment
**arXiv**：[2512.23413v1](https://arxiv.org/abs/2512.23413) · [PDF](https://arxiv.org/pdf/2512.23413.pdf)  
**作者**：Henglin Liu, Nisha Huang, Chang Liu, Jiangpeng Yan, Huijuan Huang, Jixuan Ying, Tong-Yee Lee, Pengfei Wan, Xiangyang Ji  

**一句话要点**：提出ArtQuant框架与RAD数据集，以解决艺术图像美学评估中的认知鸿沟问题。

**关键词**：艺术图像美学评估, 美学描述数据集, 多模态学习, 长文本语义建模, 认知鸿沟

## 3 点简述
- 核心问题：美学评估数据稀缺且模型碎片化，难以处理深层认知维度。
- 方法要点：构建大规模RAD数据集，并设计ArtQuant框架结合LLM解码器生成联合描述。
- 实验或效果：在多个数据集上达到SOTA性能，训练周期减少至33%。

## 摘要（原文）

> The aesthetic quality assessment task is crucial for developing a human-aligned quantitative evaluation system for AIGC. However, its inherently complex nature, spanning visual perception, cognition, and emotion, poses fundamental challenges. Although aesthetic descriptions offer a viable representation of this complexity, two critical challenges persist: (1) data scarcity and imbalance: existing dataset overly focuses on visual perception and neglects deeper dimensions due to the expensive manual annotation; and (2) model fragmentation: current visual networks isolate aesthetic attributes with multi-branch encoder, while multimodal methods represented by contrastive learning struggle to effectively process long-form textual descriptions. To resolve challenge (1), we first present the Refined Aesthetic Description (RAD) dataset, a large-scale (70k), multi-dimensional structured dataset, generated via an iterative pipeline without heavy annotation costs and easy to scale. To address challenge (2), we propose ArtQuant, an aesthetics assessment framework for artistic images which not only couples isolated aesthetic dimensions through joint description generation, but also better models long-text semantics with the help of LLM decoders. Besides, theoretical analysis confirms this symbiosis: RAD's semantic adequacy (data) and generation paradigm (model) collectively minimize prediction entropy, providing mathematical grounding for the framework. Our approach achieves state-of-the-art performance on several datasets while requiring only 33% of conventional training epochs, narrowing the cognitive gap between artistic images and aesthetic judgment. We will release both code and dataset to support future research.

