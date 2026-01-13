---
layout: default
title: DiSCo: Making Absence Visible in Intelligent Summarization Interfaces
---

# DiSCo: Making Absence Visible in Intelligent Summarization Interfaces
**arXiv**：[2601.07229v1](https://arxiv.org/abs/2601.07229) · [PDF](https://arxiv.org/pdf/2601.07229.pdf)  
**作者**：Eran Fainman, Hagit Ben Shoshan, Adir Solomon, Osnat Mokryn  

**一句话要点**：提出DiSCo方法，通过对比领域期望减少智能摘要中的存在偏见，提升决策支持。

**关键词**：智能摘要, 存在偏见, 领域期望建模, 对比分析, 决策支持, 用户研究

## 3 点简述
- 智能摘要因存在偏见而忽略缺失内容，可能误导用户决策。
- DiSCo基于领域主题期望分布，对比实体内容以识别异常强调或缺失方面。
- 用户研究显示DiSCo摘要更详细有用，但可读性略低，验证了其减少偏见的效果。

## 摘要（原文）

> Intelligent interfaces increasingly use large language models to summarize user-generated content, yet these summaries emphasize what is mentioned while overlooking what is missing. This presence bias can mislead users who rely on summaries to make decisions. We present Domain Informed Summarization through Contrast (DiSCo), an expectation-based computational approach that makes absences visible by comparing each entity's content with domain topical expectations captured in reference distributions of aspects typically discussed in comparable accommodations. This comparison identifies aspects that are either unusually emphasized or missing relative to domain norms and integrates them into the generated text. In a user study across three accommodation domains, namely ski, beach, and city center, DiSCo summaries were rated as more detailed and useful for decision making than baseline large language model summaries, although slightly harder to read. The findings show that modeling expectations reduces presence bias and improves both transparency and decision support in intelligent summarization interfaces.

