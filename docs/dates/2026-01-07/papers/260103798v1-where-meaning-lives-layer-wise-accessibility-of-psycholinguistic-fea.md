---
layout: default
title: Where meaning lives: Layer-wise accessibility of psycholinguistic features in encoder and decoder language models
---

# Where meaning lives: Layer-wise accessibility of psycholinguistic features in encoder and decoder language models
**arXiv**：[2601.03798v1](https://arxiv.org/abs/2601.03798) · [PDF](https://arxiv.org/pdf/2601.03798.pdf)  
**作者**：Taisiia Tikhomirova, Dirk U. Wulff  

**一句话要点**：通过分层探测揭示Transformer模型中语言意义的编码位置，强调方法依赖性与架构约束的交互作用。

**关键词**：Transformer模型, 心理语言学特征, 分层探测, 嵌入提取方法, 意义编码, 模型架构

## 3 点简述
- 核心问题：Transformer语言模型在何处编码心理学上有意义的语言特征，对理论和应用至关重要。
- 方法要点：系统分层探测10个Transformer模型的58个心理语言学特征，比较三种嵌入提取方法。
- 实验或效果：发现意义定位强烈依赖方法，模型共享意义维度的深度排序，最终层表示通常非最优。

## 摘要（原文）

> Understanding where transformer language models encode psychologically meaningful aspects of meaning is essential for both theory and practice. We conduct a systematic layer-wise probing study of 58 psycholinguistic features across 10 transformer models, spanning encoder-only and decoder-only architectures, and compare three embedding extraction methods. We find that apparent localization of meaning is strongly method-dependent: contextualized embeddings yield higher feature-specific selectivity and different layer-wise profiles than isolated embeddings. Across models and methods, final-layer representations are rarely optimal for recovering psycholinguistic information with linear probes. Despite these differences, models exhibit a shared depth ordering of meaning dimensions, with lexical properties peaking earlier and experiential and affective dimensions peaking later. Together, these results show that where meaning "lives" in transformer models reflects an interaction between methodological choices and architectural constraints.

