---
layout: default
title: Fusion Matters: Length-Aware Analysis of Positional-Encoding Fusion in Transformers
---

# Fusion Matters: Length-Aware Analysis of Positional-Encoding Fusion in Transformers
**arXiv**：[2601.05807v1](https://arxiv.org/abs/2601.05807) · [PDF](https://arxiv.org/pdf/2601.05807.pdf)  
**作者**：Mohamed Amine Hallam, Kuo-Kun Tseng  

**一句话要点**：研究位置编码融合机制对长序列Transformer性能的影响，提出卷积门控融合方法。

**关键词**：位置编码融合, 长序列Transformer, 融合机制比较, 卷积门控, 文本分类, 序列长度分析

## 3 点简述
- 核心问题：位置编码与词嵌入的融合机制是否影响Transformer性能，尤其在长序列场景。
- 方法要点：比较三种经典融合策略（加法、拼接投影、标量门控），并探索卷积门控融合引入局部归纳偏置。
- 实验或效果：在短文本上融合选择影响小，在长文档上带来一致增益，且增益具有结构性和泛化性。

## 摘要（原文）

> Transformers require positional encodings to represent sequence order, yet most prior work focuses on designing new positional encodings rather than examining how positional information is fused with token embeddings. In this paper, we study whether the fusion mechanism itself affects performance, particularly in long-sequence settings. We conduct a controlled empirical study comparing three canonical fusion strategies--element-wise addition, concatenation with projection, and scalar gated fusion--under identical Transformer architectures, data splits, and random seeds. Experiments on three text classification datasets spanning short (AG News), medium (IMDB), and long (ArXiv) sequences show that fusion choice has negligible impact on short texts but produces consistent gains on long documents. To verify that these gains are structural rather than stochastic, we perform paired-seed analysis and cross-dataset comparison across sequence-length regimes. Additional experiments on the ArXiv dataset indicate that the benefit of learnable fusion generalizes across multiple positional encoding families. Finally, we explore a lightweight convolutional gating mechanism that introduces local inductive bias at the fusion level, evaluated on long documents only. Our results indicate that positional-encoding fusion is a non-trivial design choice for long-sequence Transformers and should be treated as an explicit modeling decision rather than a fixed default.

