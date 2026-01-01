---
layout: default
title: RAIR: A Rule-Aware Benchmark Uniting Challenging Long-Tail and Visual Salience Subset for E-commerce Relevance Assessment
---

# RAIR: A Rule-Aware Benchmark Uniting Challenging Long-Tail and Visual Salience Subset for E-commerce Relevance Assessment
**arXiv**：[2512.24943v1](https://arxiv.org/abs/2512.24943) · [PDF](https://arxiv.org/pdf/2512.24943.pdf)  
**作者**：Chenji Lu, Zhuo Chen, Hui Zhao, Zhenyi Wang, Pengjie Wang, Jian Xu, Bo Zheng  

**一句话要点**：提出RAIR基准以解决电商搜索相关性评估中缺乏复杂标准化数据集的问题。

**关键词**：电商搜索相关性, 长尾子集, 视觉显著性, 标准化评估, 多模态理解, 基准数据集

## 3 点简述
- 核心问题：现有基准缺乏复杂性，导致行业缺乏标准化相关性评估指标。
- 方法要点：构建包含通用、长尾困难和视觉显著性子集的中文数据集，提供标准化规则框架。
- 实验或效果：在14个模型上测试，RAIR对GPT-5等模型构成挑战，促进LLM和VLM评估。

## 摘要（原文）

> Search relevance plays a central role in web e-commerce. While large language models (LLMs) have shown significant results on relevance task, existing benchmarks lack sufficient complexity for comprehensive model assessment, resulting in an absence of standardized relevance evaluation metrics across the industry. To address this limitation, we propose Rule-Aware benchmark with Image for Relevance assessment(RAIR), a Chinese dataset derived from real-world scenarios. RAIR established a standardized framework for relevance assessment and provides a set of universal rules, which forms the foundation for standardized evaluation. Additionally, RAIR analyzes essential capabilities required for current relevance models and introduces a comprehensive dataset consists of three subset: (1) a general subset with industry-balanced sampling to evaluate fundamental model competencies; (2) a long-tail hard subset focus on challenging cases to assess performance limits; (3) a visual salience subset for evaluating multimodal understanding capabilities. We conducted experiments on RAIR using 14 open and closed-source models. The results demonstrate that RAIR presents sufficient challenges even for GPT-5, which achieved the best performance. RAIR data are now available, serving as an industry benchmark for relevance assessment while providing new insights into general LLM and Visual Language Model(VLM) evaluation.

