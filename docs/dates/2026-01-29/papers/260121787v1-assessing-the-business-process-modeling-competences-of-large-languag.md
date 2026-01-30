---
layout: default
title: Assessing the Business Process Modeling Competences of Large Language Models
---

# Assessing the Business Process Modeling Competences of Large Language Models
**arXiv**：[2601.21787v1](https://arxiv.org/abs/2601.21787) · [PDF](https://arxiv.org/pdf/2601.21787.pdf)  
**作者**：Chantale Lauer, Peter Pfeiffer, Alexander Rombach, Nijat Mehdiyev  

**一句话要点**：提出BEF4LLM框架以评估大语言模型在业务流程建模中的能力

**关键词**：业务流程建模, 大语言模型评估, BPMN模型生成, 模型质量维度, 文本到过程转换

## 3 点简述
- 核心问题：缺乏对大语言模型生成BPMN模型的系统性评估，现有方法忽略模型质量维度。
- 方法要点：引入BEF4LLM框架，从语法、语用、语义和有效性四个维度评估模型。
- 实验或效果：分析开源大语言模型，结果显示其在语法和语用质量上表现优异，但在语义方面人类更优。

## 摘要（原文）

> The creation of Business Process Model and Notation (BPMN) models is a complex and time-consuming task requiring both domain knowledge and proficiency in modeling conventions. Recent advances in large language models (LLMs) have significantly expanded the possibilities for generating BPMN models directly from natural language, building upon earlier text-to-process methods with enhanced capabilities in handling complex descriptions. However, there is a lack of systematic evaluations of LLM-generated process models. Current efforts either use LLM-as-a-judge approaches or do not consider established dimensions of model quality. To this end, we introduce BEF4LLM, a novel LLM evaluation framework comprising four perspectives: syntactic quality, pragmatic quality, semantic quality, and validity. Using BEF4LLM, we conduct a comprehensive analysis of open-source LLMs and benchmark their performance against human modeling experts. Results indicate that LLMs excel in syntactic and pragmatic quality, while humans outperform in semantic aspects; however, the differences in scores are relatively modest, highlighting LLMs' competitive potential despite challenges in validity and semantic quality. The insights highlight current strengths and limitations of using LLMs for BPMN modeling and guide future model development and fine-tuning. Addressing these areas is essential for advancing the practical deployment of LLMs in business process modeling.

