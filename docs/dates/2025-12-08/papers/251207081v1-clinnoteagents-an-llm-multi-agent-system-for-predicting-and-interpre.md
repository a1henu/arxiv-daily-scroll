---
layout: default
title: ClinNoteAgents: An LLM Multi-Agent System for Predicting and Interpreting Heart Failure 30-Day Readmission from Clinical Notes
---

# ClinNoteAgents: An LLM Multi-Agent System for Predicting and Interpreting Heart Failure 30-Day Readmission from Clinical Notes
**arXiv**：[2512.07081v1](https://arxiv.org/abs/2512.07081) · [PDF](https://arxiv.org/pdf/2512.07081.pdf)  
**作者**：Rongjia Zhou, Chengzhuo Li, Carl Yang, Jiaying Lu  

**一句话要点**：提出ClinNoteAgents，基于LLM多智能体系统从临床笔记预测和解释心衰30天再入院风险。

**关键词**：心衰再入院预测, 临床笔记分析, LLM多智能体系统, 医疗风险建模, 可解释人工智能

## 3 点简述
- 核心问题：心衰再入院风险高，临床笔记信息丰富但利用不足，传统方法依赖专家规则且处理自由文本困难。
- 方法要点：使用LLM多智能体框架，将自由文本临床笔记转化为结构化风险因素表示和临床风格抽象，用于关联分析和预测。
- 实验或效果：在3,544份笔记上评估，展示强性能，减少对结构化字段依赖，提供可扩展和可解释的建模方法。

## 摘要（原文）

> Heart failure (HF) is one of the leading causes of rehospitalization among older adults in the United States. Although clinical notes contain rich, detailed patient information and make up a large portion of electronic health records (EHRs), they remain underutilized for HF readmission risk analysis. Traditional computational models for HF readmission often rely on expert-crafted rules, medical thesauri, and ontologies to interpret clinical notes, which are typically written under time pressure and may contain misspellings, abbreviations, and domain-specific jargon. We present ClinNoteAgents, an LLM-based multi-agent framework that transforms free-text clinical notes into (1) structured representations of clinical and social risk factors for association analysis and (2) clinician-style abstractions for HF 30-day readmission prediction. We evaluate ClinNoteAgents on 3,544 notes from 2,065 patients (readmission rate=35.16%), demonstrating strong performance in extracting risk factors from free-text, identifying key contributing factors, and predicting readmission risk. By reducing reliance on structured fields and minimizing manual annotation and model training, ClinNoteAgents provides a scalable and interpretable approach to note-based HF readmission risk modeling in data-limited healthcare systems.

