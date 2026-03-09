---
layout: default
title: Evaluating Austrian A-Level German Essays with Large Language Models for Automated Essay Scoring
---

# Evaluating Austrian A-Level German Essays with Large Language Models for Automated Essay Scoring
**arXiv**：[2603.06066v1](https://arxiv.org/abs/2603.06066) · [PDF](https://arxiv.org/pdf/2603.06066.pdf)  
**作者**：Jonas Kubesch, Lena Huber, Clemens Havas  

**一句话要点**：评估大型语言模型在奥地利A级德语作文自动评分中的应用，发现其准确性不足

**关键词**：自动作文评分, 大型语言模型, 德语文本评估, 评分标准, 教育技术

## 3 点简述
- 核心问题：研究大型语言模型在奥地利A级德语作文自动评分中的表现，以减轻教师负担和减少主观偏见。
- 方法要点：使用四种开源大型语言模型，基于标准化评分标准，处理101篇匿名学生考试文本。
- 实验或效果：模型在子维度上与人类评分者最高达成40.6%一致，最终评分匹配率仅32.8%，表明准确性不足以实际应用。

## 摘要（原文）

> Automated Essay Scoring (AES) has been explored for decades with the goal to support teachers by reducing grading workload and mitigating subjective biases. While early systems relied on handcrafted features and statistical models, recent advances in Large Language Models (LLMs) have made it possible to evaluate student writing with unprecedented flexibility. This paper investigates the application of state-of-the-art open-weight LLMs for the grading of Austrian A-level German texts, with a particular focus on rubric-based evaluation. A dataset of 101 anonymised student exams across three text types was processed and evaluated. Four LLMs, DeepSeek-R1 32b, Qwen3 30b, Mixtral 8x7b and LLama3.3 70b, were evaluated with different contexts and prompting strategies. The LLMs were able to reach a maximum of 40.6% agreement with the human rater in the rubric-provided sub-dimensions, and only 32.8% of final grades matched the ones given by a human expert. The results indicate that even though smaller models are able to use standardised rubrics for German essay grading, they are not accurate enough to be used in a real-world grading environment.

