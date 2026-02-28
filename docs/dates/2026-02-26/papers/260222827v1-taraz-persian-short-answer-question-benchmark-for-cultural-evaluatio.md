---
layout: default
title: TARAZ: Persian Short-Answer Question Benchmark for Cultural Evaluation of Language Models
---

# TARAZ: Persian Short-Answer Question Benchmark for Cultural Evaluation of Language Models
**arXiv**：[2602.22827v1](https://arxiv.org/abs/2602.22827) · [PDF](https://arxiv.org/pdf/2602.22827.pdf)  
**作者**：Reihaneh Iranmanesh, Saeedeh Davoudi, Pasha Abrishamchian, Ophir Frieder, Nazli Goharian  

**一句话要点**：提出波斯语短答案评估框架以解决大语言模型文化能力评估问题

**关键词**：波斯语文化评估, 短答案基准, 形态归一化, 混合相似度评分, 大语言模型评估, 跨文化研究

## 3 点简述
- 现有波斯语文化基准依赖选择题和英语中心指标，无法捕捉波斯语形态复杂性和语义细微差别
- 框架结合基于规则的形态归一化和混合句法语义相似度模块，实现超越精确字符串匹配的软匹配评分
- 通过评估15个先进模型，混合评估比精确匹配基线提高评分一致性10%，并公开框架作为首个标准化基准

## 摘要（原文）

> This paper presents a comprehensive evaluation framework for assessing the cultural competence of large language models (LLMs) in Persian. Existing Persian cultural benchmarks rely predominantly on multiple-choice formats and English-centric metrics that fail to capture Persian's morphological complexity and semantic nuance. Our framework introduces a Persian-specific short-answer evaluation that combines rule-based morphological normalization with a hybrid syntactic and semantic similarity module, enabling robust soft-match scoring beyond exact string overlap. Through systematic evaluation of 15 state-of-the-art open- and closed-source models, we demonstrate that our hybrid evaluation improves scoring consistency by +10% compared to exact-match baselines by capturing meaning that surface-level methods cannot detect. We publicly release our evaluation framework, providing the first standardized benchmark for measuring cultural understanding in Persian and establishing a reproducible foundation for cross-cultural LLM evaluation research.

