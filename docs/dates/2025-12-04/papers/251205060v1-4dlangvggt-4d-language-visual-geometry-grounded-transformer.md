---
layout: default
title: 4DLangVGGT: 4D Language-Visual Geometry Grounded Transformer
---

# 4DLangVGGT: 4D Language-Visual Geometry Grounded Transformer
**arXiv**：[2512.05060v1](https://arxiv.org/abs/2512.05060) · [PDF](https://arxiv.org/pdf/2512.05060.pdf)  
**作者**：Xianfeng Wu, Yajing Bai, Minghan Li, Xianzu Wu, Xueqi Zhao, Zhongyuan Lai, Wenyu Liu, Xinggang Wang  

**一句话要点**：提出4DLangVGGT以解决4D语言场构建中依赖场景特定优化、泛化能力有限的问题。

**关键词**：4D语言场构建, Transformer架构, 几何感知, 语言对齐, 动态场景理解, 开放词汇查询

## 3 点简述
- 核心问题：现有4D语义场构建方法依赖场景特定高斯泼溅，需逐场景优化，泛化能力差，难以规模化应用。
- 方法要点：基于Transformer的前馈统一框架，集成几何感知与语言对齐，包括StreamVGGT捕获时空几何表示和SBD投影到语言对齐语义空间。
- 实验或效果：在HyperNeRF和Neu3D数据集上实现有效泛化，达到最先进性能，单场景训练提升2%，多场景训练提升1%。

## 摘要（原文）

> Constructing 4D language fields is crucial for embodied AI, augmented/virtual reality, and 4D scene understanding, as they provide enriched semantic representations of dynamic environments and enable open-vocabulary querying in complex scenarios. However, existing approaches to 4D semantic field construction primarily rely on scene-specific Gaussian splatting, which requires per-scene optimization, exhibits limited generalization, and is difficult to scale to real-world applications. To address these limitations, we propose 4DLangVGGT, the first Transformer-based feed-forward unified framework for 4D language grounding, that jointly integrates geometric perception and language alignment within a single architecture. 4DLangVGGT has two key components: the 4D Visual Geometry Transformer, StreamVGGT, which captures spatio-temporal geometric representations of dynamic scenes; and the Semantic Bridging Decoder (SBD), which projects geometry-aware features into a language-aligned semantic space, thereby enhancing semantic interpretability while preserving structural fidelity. Unlike prior methods that depend on costly per-scene optimization, 4DLangVGGT can be jointly trained across multiple dynamic scenes and directly applied during inference, achieving both deployment efficiency and strong generalization. This design significantly improves the practicality of large-scale deployment and establishes a new paradigm for open-vocabulary 4D scene understanding. Experiments on HyperNeRF and Neu3D datasets demonstrate that our approach not only generalizes effectively but also achieves state-of-the-art performance, achieving up to 2% gains under per-scene training and 1% improvements under multi-scene training. Our code released in https://github.com/hustvl/4DLangVGGT

