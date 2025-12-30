---
layout: default
title: Not too long do read: Evaluating LLM-generated extreme scientific summaries
---

# Not too long do read: Evaluating LLM-generated extreme scientific summaries
**arXiv**：[2512.23206v1](https://arxiv.org/abs/2512.23206) · [PDF](https://arxiv.org/pdf/2512.23206.pdf)  
**作者**：Zhuoqi Lyu, Qing Ke  

**一句话要点**：提出BiomedTLDR数据集以评估LLM生成科学极简摘要的能力

**关键词**：科学摘要生成, 大型语言模型评估, 数据集构建, 文本摘要, 生物医学文本

## 3 点简述
- 核心问题：缺乏高质量科学极简摘要数据集，阻碍LLM摘要能力的开发与评估
- 方法要点：利用论文作者评论构建BiomedTLDR数据集，测试LLM基于摘要生成TLDR
- 实验或效果：LLM生成摘要更偏向提取式，与人类相比抽象性较弱

## 摘要（原文）

> High-quality scientific extreme summary (TLDR) facilitates effective science communication. How do large language models (LLMs) perform in generating them? How are LLM-generated summaries different from those written by human experts? However, the lack of a comprehensive, high-quality scientific TLDR dataset hinders both the development and evaluation of LLMs' summarization ability. To address these, we propose a novel dataset, BiomedTLDR, containing a large sample of researcher-authored summaries from scientific papers, which leverages the common practice of including authors' comments alongside bibliography items. We then test popular open-weight LLMs for generating TLDRs based on abstracts. Our analysis reveals that, although some of them successfully produce humanoid summaries, LLMs generally exhibit a greater affinity for the original text's lexical choices and rhetorical structures, hence tend to be more extractive rather than abstractive in general, compared to humans. Our code and datasets are available at https://github.com/netknowledge/LLM_summarization (Lyu and Ke, 2025).

