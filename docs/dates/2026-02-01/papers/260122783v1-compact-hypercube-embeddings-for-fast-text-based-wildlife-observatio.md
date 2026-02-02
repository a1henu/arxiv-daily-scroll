---
layout: default
title: Compact Hypercube Embeddings for Fast Text-based Wildlife Observation Retrieval
---

# Compact Hypercube Embeddings for Fast Text-based Wildlife Observation Retrieval
**arXiv**：[2601.22783v1](https://arxiv.org/abs/2601.22783) · [PDF](https://arxiv.org/pdf/2601.22783.pdf)  
**作者**：Ilyass Moummad, Marius Miron, David Robinson, Kawtar Zaher, Hervé Goëau, Olivier Pietquin, Pierre Bonnet, Emmanuel Chemla, Matthieu Geist, Alexis Joly  

**一句话要点**：提出紧凑超立方体嵌入以解决大规模野生动物观测中基于文本的高效检索问题

**关键词**：紧凑嵌入, 文本检索, 多模态对齐, 哈希学习, 生物多样性监测, 参数高效微调

## 3 点简述
- 核心问题：大规模生物多样性监测平台中，多模态野生动物观测的高维相似性搜索计算成本高，检索效率低。
- 方法要点：基于跨视图代码对齐哈希框架，扩展轻量级哈希至多模态，在共享汉明空间中对齐自然语言描述与视觉或声学观测。
- 实验或效果：在iNaturalist2024和iNatSounds2024等基准测试中，二进制嵌入实现竞争性或更优性能，大幅降低内存和搜索成本。

## 摘要（原文）

> Large-scale biodiversity monitoring platforms increasingly rely on multimodal wildlife observations. While recent foundation models enable rich semantic representations across vision, audio, and language, retrieving relevant observations from massive archives remains challenging due to the computational cost of high-dimensional similarity search. In this work, we introduce compact hypercube embeddings for fast text-based wildlife observation retrieval, a framework that enables efficient text-based search over large-scale wildlife image and audio databases using compact binary representations. Building on the cross-view code alignment hashing framework, we extend lightweight hashing beyond a single-modality setup to align natural language descriptions with visual or acoustic observations in a shared Hamming space. Our approach leverages pretrained wildlife foundation models, including BioCLIP and BioLingual, and adapts them efficiently for hashing using parameter-efficient fine-tuning. We evaluate our method on large-scale benchmarks, including iNaturalist2024 for text-to-image retrieval and iNatSounds2024 for text-to-audio retrieval, as well as multiple soundscape datasets to assess robustness under domain shift. Results show that retrieval using discrete hypercube embeddings achieves competitive, and in several cases superior, performance compared to continuous embeddings, while drastically reducing memory and search cost. Moreover, we observe that the hashing objective consistently improves the underlying encoder representations, leading to stronger retrieval and zero-shot generalization. These results demonstrate that binary, language-based retrieval enables scalable and efficient search over large wildlife archives for biodiversity monitoring systems.

