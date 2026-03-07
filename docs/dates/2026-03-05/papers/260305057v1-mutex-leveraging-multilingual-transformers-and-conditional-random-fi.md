---
layout: default
title: MUTEX: Leveraging Multilingual Transformers and Conditional Random Fields for Enhanced Urdu Toxic Span Detection
---

# MUTEX: Leveraging Multilingual Transformers and Conditional Random Fields for Enhanced Urdu Toxic Span Detection
**arXiv**：[2603.05057v1](https://arxiv.org/abs/2603.05057) · [PDF](https://arxiv.org/pdf/2603.05057.pdf)  
**作者**：Inayat Arshad, Fajar Saleem, Ijaz Hussain  

**一句话要点**：提出MUTEX框架，结合多语言Transformer与CRF，以提升乌尔都语毒性片段检测性能。

**关键词**：毒性片段检测, 多语言Transformer, 条件随机场, 乌尔都语处理, 序列标注, 社交媒体分析

## 3 点简述
- 乌尔都语毒性检测面临句子级分类局限，缺乏词级标注资源及语言复杂性挑战。
- MUTEX采用XLM RoBERTa与CRF层进行序列标注，利用手动标注词级数据集提升检测精度。
- 实验显示MUTEX在社交媒体等多领域数据上达到60%词级F1分数，优于其他模型处理代码切换问题。

## 摘要（原文）

> Urdu toxic span detection remains limited because most existing systems rely on sentence-level classification and fail to identify the specific toxic spans within those text. It is further exacerbated by the multiple factors i.e. lack of token-level annotated resources, linguistic complexity of Urdu, frequent code-switching, informal expressions, and rich morphological variations. In this research, we propose MUTEX: a multilingual transformer combined with conditional random fields (CRF) for Urdu toxic span detection framework that uses manually annotated token-level toxic span dataset to improve performance and interpretability. MUTEX uses XLM RoBERTa with CRF layer to perform sequence labeling and is tested on multi-domain data extracted from social media, online news, and YouTube reviews using token-level F1 to evaluate fine-grained span detection. The results indicate that MUTEX achieves 60% token-level F1 score that is the first supervised baseline for Urdu toxic span detection. Further examination reveals that transformer-based models are more effective at implicitly capturing the contextual toxicity and are able to address the issues of code-switching and morphological variation than other models.

