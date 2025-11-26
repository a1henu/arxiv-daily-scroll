---
layout: default
title: New York Smells: A Large Multimodal Dataset for Olfaction
---

# New York Smells: A Large Multimodal Dataset for Olfaction
**arXiv**：[2511.20544v1](https://arxiv.org/abs/2511.20544) · [PDF](https://arxiv.org/pdf/2511.20544.pdf)  
**作者**：Ege Ozguroglu, Junbang Liang, Ruoshi Liu, Mia Chiquier, Michael DeTienne, Wesley Wei Qian, Alexandra Horowitz, Andrew Owens, Carl Vondrick  

**一句话要点**：提出大型多模态嗅觉数据集以解决自然场景嗅觉数据缺乏问题

**关键词**：多模态数据集, 嗅觉表示学习, 跨模态检索, 场景识别, 细粒度分类

## 3 点简述
- 核心问题：嗅觉作为动物感知世界的重要方式，在机器中难以访问，缺乏自然场景多模态数据。
- 方法要点：收集7000对图像-嗅觉信号，覆盖3500个对象，室内外环境，数据规模远超现有。
- 实验或效果：视觉数据支持跨模态嗅觉学习，学习表示优于手工特征，应用于检索和识别任务。

## 摘要（原文）

> While olfaction is central to how animals perceive the world, this rich chemical sensory modality remains largely inaccessible to machines. One key bottleneck is the lack of diverse, multimodal olfactory training data collected in natural settings. We present New York Smells, a large dataset of paired image and olfactory signals captured ``in the wild.'' Our dataset contains 7,000 smell-image pairs from 3,500 distinct objects across indoor and outdoor environments, with approximately 70$\times$ more objects than existing olfactory datasets. Our benchmark has three tasks: cross-modal smell-to-image retrieval, recognizing scenes, objects, and materials from smell alone, and fine-grained discrimination between grass species. Through experiments on our dataset, we find that visual data enables cross-modal olfactory representation learning, and that our learned olfactory representations outperform widely-used hand-crafted features.

