---
layout: default
title: The Confidence Trap: Gender Bias and Predictive Certainty in LLMs
---

# The Confidence Trap: Gender Bias and Predictive Certainty in LLMs
**arXiv**：[2601.07806v1](https://arxiv.org/abs/2601.07806) · [PDF](https://arxiv.org/pdf/2601.07806.pdf)  
**作者**：Ahmed Sabir, Markus Kängsepp, Rajesh Sharma  

**一句话要点**：提出Gender-ECE校准指标以评估大语言模型在性别偏见任务中的置信度校准公平性

**关键词**：大语言模型, 性别偏见, 置信度校准, 公平性评估, 代词消解

## 3 点简述
- 核心问题：大语言模型在敏感领域应用中，置信度分数与公平性及性别偏见的对应关系未知
- 方法要点：基于预测置信度与人类标注偏见判断的对齐，研究性别代词消解中的概率置信度校准
- 实验或效果：在六个先进模型中，Gemma-2在性别偏见基准上表现出最差的校准效果

## 摘要（原文）

> The increased use of Large Language Models (LLMs) in sensitive domains leads to growing interest in how their confidence scores correspond to fairness and bias. This study examines the alignment between LLM-predicted confidence and human-annotated bias judgments. Focusing on gender bias, the research investigates probability confidence calibration in contexts involving gendered pronoun resolution. The goal is to evaluate if calibration metrics based on predicted confidence scores effectively capture fairness-related disparities in LLMs. The results show that, among the six state-of-the-art models, Gemma-2 demonstrates the worst calibration according to the gender bias benchmark. The primary contribution of this work is a fairness-aware evaluation of LLMs' confidence calibration, offering guidance for ethical deployment. In addition, we introduce a new calibration metric, Gender-ECE, designed to measure gender disparities in resolution tasks.

