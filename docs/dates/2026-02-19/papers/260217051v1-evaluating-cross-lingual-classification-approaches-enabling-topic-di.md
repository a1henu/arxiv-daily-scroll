---
layout: default
title: Evaluating Cross-Lingual Classification Approaches Enabling Topic Discovery for Multilingual Social Media Data
---

# Evaluating Cross-Lingual Classification Approaches Enabling Topic Discovery for Multilingual Social Media Data
**arXiv**：[2602.17051v1](https://arxiv.org/abs/2602.17051) · [PDF](https://arxiv.org/pdf/2602.17051.pdf)  
**作者**：Deepak Uniyal, Md Abul Bashar, Richi Nayak  

**一句话要点**：评估跨语言分类方法以支持多语言社交媒体数据的主题发现

**关键词**：跨语言文本分类, 多语言社交媒体分析, 主题建模, 翻译方法, 多语言变换器, 噪声过滤

## 3 点简述
- 核心问题：多语言社交媒体分析面临噪声数据和跨语言分类挑战，需过滤无关内容以提取主题。
- 方法要点：比较四种跨语言分类方法，包括翻译、多语言模型和混合策略，用于过滤氢能相关推文。
- 实验或效果：基于十年多语言推文数据集评估方法性能，揭示翻译与多语言方法间的权衡，优化分析流程。

## 摘要（原文）

> Analysing multilingual social media discourse remains a major challenge in natural language processing, particularly when large-scale public debates span across diverse languages. This study investigates how different approaches for cross-lingual text classification can support reliable analysis of global conversations. Using hydrogen energy as a case study, we analyse a decade-long dataset of over nine million tweets in English, Japanese, Hindi, and Korean (2013--2022) for topic discovery. The online keyword-driven data collection results in a significant amount of irrelevant content. We explore four approaches to filter relevant content: (1) translating English annotated data into target languages for building language-specific models for each target language, (2) translating unlabelled data appearing from all languages into English for creating a single model based on English annotations, (3) applying English fine-tuned multilingual transformers directly to each target language data, and (4) a hybrid strategy that combines translated annotations with multilingual training. Each approach is evaluated for its ability to filter hydrogen-related tweets from noisy keyword-based collections. Subsequently, topic modeling is performed to extract dominant themes within the relevant subsets. The results highlight key trade-offs between translation and multilingual approaches, offering actionable insights into optimising cross-lingual pipelines for large-scale social media analysis.

