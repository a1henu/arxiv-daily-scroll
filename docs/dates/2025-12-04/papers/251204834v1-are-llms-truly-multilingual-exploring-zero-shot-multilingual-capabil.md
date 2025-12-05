---
layout: default
title: Are LLMs Truly Multilingual? Exploring Zero-Shot Multilingual Capability of LLMs for Information Retrieval: An Italian Healthcare Use Case
---

# Are LLMs Truly Multilingual? Exploring Zero-Shot Multilingual Capability of LLMs for Information Retrieval: An Italian Healthcare Use Case
**arXiv**：[2512.04834v1](https://arxiv.org/abs/2512.04834) · [PDF](https://arxiv.org/pdf/2512.04834.pdf)  
**作者**：Vignesh Kumar Kembu, Pierandrea Morandini, Marta Bianca Maria Ranzini, Antonino Nocera  

**一句话要点**：评估开源多语言大模型在意大利电子健康记录中零样本提取共病信息的能力

**关键词**：多语言大模型, 零样本学习, 电子健康记录, 信息提取, 意大利语临床文本, 共病分析

## 3 点简述
- 核心问题：多语言大模型在零样本、本地设置下处理意大利语临床文本的共病信息提取效果未知
- 方法要点：比较开源多语言大模型与传统模式匹配及人工标注在实时信息提取中的表现
- 实验或效果：实验显示部分模型性能波动大，难以泛化到不同疾病，与传统方法相比存在挑战

## 摘要（原文）

> Large Language Models (LLMs) have become a key topic in AI and NLP, transforming sectors like healthcare, finance, education, and marketing by improving customer service, automating tasks, providing insights, improving diagnostics, and personalizing learning experiences. Information extraction from clinical records is a crucial task in digital healthcare. Although traditional NLP techniques have been used for this in the past, they often fall short due to the complexity, variability of clinical language, and high inner semantics in the free clinical text. Recently, Large Language Models (LLMs) have become a powerful tool for better understanding and generating human-like text, making them highly effective in this area. In this paper, we explore the ability of open-source multilingual LLMs to understand EHRs (Electronic Health Records) in Italian and help extract information from them in real-time. Our detailed experimental campaign on comorbidity extraction from EHR reveals that some LLMs struggle in zero-shot, on-premises settings, and others show significant variation in performance, struggling to generalize across various diseases when compared to native pattern matching and manual annotations.

