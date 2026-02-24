---
layout: default
title: Beyond a Single Extractor: Re-thinking HTML-to-Text Extraction for LLM Pretraining
---

# Beyond a Single Extractor: Re-thinking HTML-to-Text Extraction for LLM Pretraining
**arXiv**：[2602.19548v1](https://arxiv.org/abs/2602.19548) · [PDF](https://arxiv.org/pdf/2602.19548.pdf)  
**作者**：Jeffrey Li, Josh Gardner, Doug Kang, Fangping Shi, Karanjeet Singh, Chun-Liang Li, Herumb Shandilya, David Hall, Oncel Tuzel, Percy Liang, Ludwig Schmidt, Hadi Pour Ansari, Fartash Faghri  

**一句话要点**：提出多提取器联合方法以提升LLM预训练中HTML到文本提取的覆盖率和下游任务性能

**关键词**：HTML到文本提取, LLM预训练, 数据预处理, 提取器多样性, 结构化内容提取, 下游任务性能

## 3 点简述
- 核心问题：现有LLM预训练数据集对多样网页内容使用单一固定提取器，可能导致数据覆盖不足和利用不充分
- 方法要点：通过联合不同提取器，增加token产量，并分析提取器选择对结构化内容（如表格和代码块）的影响
- 实验或效果：联合提取器使DCLM-Baseline的token产量提升高达71%，并在WikiTQ和HumanEval任务中带来显著性能差异

## 摘要（原文）

> One of the first pre-processing steps for constructing web-scale LLM pretraining datasets involves extracting text from HTML. Despite the immense diversity of web content, existing open-source datasets predominantly apply a single fixed extractor to all webpages. In this work, we investigate whether this practice leads to suboptimal coverage and utilization of Internet data. We first show that while different extractors may lead to similar model performance on standard language understanding tasks, the pages surviving a fixed filtering pipeline can differ substantially. This suggests a simple intervention: by taking a Union over different extractors, we can increase the token yield of DCLM-Baseline by up to 71% while maintaining benchmark performance. We further show that for structured content such as tables and code blocks, extractor choice can significantly impact downstream task performance, with differences of up to 10 percentage points (p.p.) on WikiTQ and 3 p.p. on HumanEval.

