---
layout: default
title: UniRec-0.1B: Unified Text and Formula Recognition with 0.1B Parameters
---

# UniRec-0.1B: Unified Text and Formula Recognition with 0.1B Parameters
**arXiv**：[2512.21095v1](https://arxiv.org/abs/2512.21095) · [PDF](https://arxiv.org/pdf/2512.21095.pdf)  
**作者**：Yongkun Du, Zhineng Chen, Yazhen Xie, Weikang Baiand Hao Feng, Wei Shi, Yuchen Su, Can Huang, Yu-Gang Jiang  

**一句话要点**：提出UniRec-0.1B以轻量化统一识别文档中的文本和公式

**关键词**：文档解析, 轻量化模型, 统一识别, 分层监督, 语义解耦, 数据集构建

## 3 点简述
- 核心问题：现有视觉语言模型参数量大、计算成本高，限制文档解析应用。
- 方法要点：构建UniRec40M数据集，采用分层监督训练和语义解耦分词器。
- 实验或效果：在多个基准测试中优于通用VLMs和专家模型，速度提升2-9倍。

## 摘要（原文）

> Text and formulas constitute the core informational components of many documents. Accurately and efficiently recognizing both is crucial for developing robust and generalizable document parsing systems. Recently, vision-language models (VLMs) have achieved impressive unified recognition of text and formulas. However, they are large-sized and computationally demanding, restricting their usage in many applications. In this paper, we propose UniRec-0.1B, a unified recognition model with only 0.1B parameters. It is capable of performing text and formula recognition at multiple levels, including characters, words, lines, paragraphs, and documents. To implement this task, we first establish UniRec40M, a large-scale dataset comprises 40 million text, formula and their mix samples, enabling the training of a powerful yet lightweight model. Secondly, we identify two challenges when building such a lightweight but unified expert model. They are: structural variability across hierarchies and semantic entanglement between textual and formulaic content. To tackle these, we introduce a hierarchical supervision training that explicitly guides structural comprehension, and a semantic-decoupled tokenizer that separates text and formula representations. Finally, we develop a comprehensive evaluation benchmark covering Chinese and English documents from multiple domains and with multiple levels. Experimental results on this and public benchmarks demonstrate that UniRec-0.1B outperforms both general-purpose VLMs and leading document parsing expert models, while achieving a 2-9$\times$ speedup, validating its effectiveness and efficiency. Codebase and Dataset: https://github.com/Topdu/OpenOCR.

