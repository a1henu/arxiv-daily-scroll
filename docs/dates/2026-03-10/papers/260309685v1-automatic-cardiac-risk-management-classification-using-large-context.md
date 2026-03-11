---
layout: default
title: Automatic Cardiac Risk Management Classification using large-context Electronic Patients Health Records
---

# Automatic Cardiac Risk Management Classification using large-context Electronic Patients Health Records
**arXiv**：[2603.09685v1](https://arxiv.org/abs/2603.09685) · [PDF](https://arxiv.org/pdf/2603.09685.pdf)  
**作者**：Jacopo Vitale, David Della Morte, Luca Bacco, Mario Merone, Mark de Groot, Saskia Haitjema, Leandro Pecchia, Bram van Es  

**一句话要点**：提出基于大上下文电子健康记录的自动心血管风险管理分类框架，以替代手动编码。

**关键词**：电子健康记录, 心血管风险管理, Transformer架构, 零样本学习, 数据融合, 临床风险分层

## 3 点简述
- 核心问题：手动管理编码在老年心血管风险管理中存在局限性，需自动化解决方案。
- 方法要点：使用经典机器学习、定制Transformer架构和零样本LLMs，结合结构化数据融合。
- 实验或效果：定制Transformer在F1分数和MCC上表现最佳，优于传统方法和生成式LLMs。

## 摘要（原文）

> To overcome the limitations of manual administrative coding in geriatric Cardiovascular Risk Management, this study introduces an automated classification framework leveraging unstructured Electronic Health Records (EHRs). Using a dataset of 3,482 patients, we benchmarked three distinct modeling paradigms on longitudinal Dutch clinical narratives: classical machine learning baselines, specialized deep learning architectures optimized for large-context sequences, and general-purpose generative Large Language Models (LLMs) in a zero-shot setting. Additionally, we evaluated a late fusion strategy to integrate unstructured text with structured medication embeddings and anthropometric data. Our analysis reveals that the custom Transformer architecture outperforms both traditional methods and generative \acs{llm}s, achieving the highest F1-scores and Matthews Correlation Coefficients. These findings underscore the critical role of specialized hierarchical attention mechanisms in capturing long-range dependencies within medical texts, presenting a robust, automated alternative to manual workflows for clinical risk stratification.

