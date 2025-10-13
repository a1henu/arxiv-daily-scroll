---
layout: default
title: Tag-Enriched Multi-Attention with Large Language Models for Cross-Domain Sequential Recommendation
---

# Tag-Enriched Multi-Attention with Large Language Models for Cross-Domain Sequential Recommendation
**arXiv**：[2510.09224v1](https://arxiv.org/abs/2510.09224) · [PDF](https://arxiv.org/pdf/2510.09224.pdf)  
**作者**：Wangyu Wu, Xuhang Chen, Zhenhong Chen, Jing-En Jiang, Kim-Fung Tsang, Xiaowei Huang, Fei Ma, Jimin Xiao  

**一句话要点**：提出TEMA-LLM框架，利用大语言模型生成语义标签以提升跨域序列推荐性能

**关键词**：跨域序列推荐, 大语言模型, 语义标签生成, 多注意力机制, 物品表示增强

## 3 点简述
- 跨域序列推荐需捕捉域内和跨域用户行为模式，以提供个性化体验
- 集成大语言模型生成描述性标签，结合多特征构建增强物品表示
- 在四个电商数据集上实验，TEMA-LLM优于现有基线方法

## 摘要（原文）

> Cross-Domain Sequential Recommendation (CDSR) plays a crucial role in modern
> consumer electronics and e-commerce platforms, where users interact with
> diverse services such as books, movies, and online retail products. These
> systems must accurately capture both domain-specific and cross-domain
> behavioral patterns to provide personalized and seamless consumer experiences.
> To address this challenge, we propose \textbf{TEMA-LLM} (\textit{Tag-Enriched
> Multi-Attention with Large Language Models}), a practical and effective
> framework that integrates \textit{Large Language Models (LLMs)} for semantic
> tag generation and enrichment. Specifically, TEMA-LLM employs LLMs to assign
> domain-aware prompts and generate descriptive tags from item titles and
> descriptions. The resulting tag embeddings are fused with item identifiers as
> well as textual and visual features to construct enhanced item representations.
> A \textit{Tag-Enriched Multi-Attention} mechanism is then introduced to jointly
> model user preferences within and across domains, enabling the system to
> capture complex and evolving consumer interests. Extensive experiments on four
> large-scale e-commerce datasets demonstrate that TEMA-LLM consistently
> outperforms state-of-the-art baselines, underscoring the benefits of LLM-based
> semantic tagging and multi-attention integration for consumer-facing
> recommendation systems. The proposed approach highlights the potential of LLMs
> to advance intelligent, user-centric services in the field of consumer
> electronics.

