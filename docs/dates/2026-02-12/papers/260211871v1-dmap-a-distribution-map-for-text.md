---
layout: default
title: DMAP: A Distribution Map for Text
---

# DMAP: A Distribution Map for Text
**arXiv**：[2602.11871v1](https://arxiv.org/abs/2602.11871) · [PDF](https://arxiv.org/pdf/2602.11871.pdf)  
**作者**：Tom Kempton, Julia Rozanova, Parameswaran Kamalaruban, Maeve Madigan, Karolina Wresilo, Yoann L. Launay, David Sutton, Stuart Burrell  

**一句话要点**：提出DMAP方法，将文本映射到单位区间样本以支持统计文本分析

**关键词**：文本分析, 语言模型, 概率分布, 统计方法, 模型无关分析

## 3 点简述
- 核心问题：传统指标如困惑度无法充分捕捉上下文，需改进语言模型概率分布的解释方法
- 方法要点：基于数学基础，通过语言模型将文本转换为编码排名和概率信息的单位区间样本集
- 实验或效果：应用于生成参数验证、机器生成文本检测和下游模型指纹分析，展示统一统计视图

## 摘要（原文）

> Large Language Models (LLMs) are a powerful tool for statistical text analysis, with derived sequences of next-token probability distributions offering a wealth of information. Extracting this signal typically relies on metrics such as perplexity, which do not adequately account for context; how one should interpret a given next-token probability is dependent on the number of reasonable choices encoded by the shape of the conditional distribution. In this work, we present DMAP, a mathematically grounded method that maps a text, via a language model, to a set of samples in the unit interval that jointly encode rank and probability information. This representation enables efficient, model-agnostic analysis and supports a range of applications. We illustrate its utility through three case studies: (i) validation of generation parameters to ensure data integrity, (ii) examining the role of probability curvature in machine-generated text detection, and (iii) a forensic analysis revealing statistical fingerprints left in downstream models that have been subject to post-training on synthetic data. Our results demonstrate that DMAP offers a unified statistical view of text that is simple to compute on consumer hardware, widely applicable, and provides a foundation for further research into text analysis with LLMs.

