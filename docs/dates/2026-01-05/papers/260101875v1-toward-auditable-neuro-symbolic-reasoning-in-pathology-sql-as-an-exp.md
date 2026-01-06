---
layout: default
title: Toward Auditable Neuro-Symbolic Reasoning in Pathology: SQL as an Explicit Trace of Evidence
---

# Toward Auditable Neuro-Symbolic Reasoning in Pathology: SQL as an Explicit Trace of Evidence
**arXiv**：[2601.01875v1](https://arxiv.org/abs/2601.01875) · [PDF](https://arxiv.org/pdf/2601.01875.pdf)  
**作者**：Kewen Cao, Jianxu Chen, Yongbing Zhang, Ye Zhang, Hongxiao Wang  

**一句话要点**：提出基于SQL的代理框架，以提升病理图像分析的可审计性和可解释性。

**关键词**：病理图像分析, 可解释人工智能, SQL查询, 视觉问答, 代理框架

## 3 点简述
- 核心问题：病理图像分析中模型决策缺乏可验证证据，现有解释方法多为相关性描述。
- 方法要点：通过特征推理代理执行SQL查询，将视觉证据量化为可审计的推理过程。
- 实验或效果：在两个病理视觉问答数据集上验证，方法提高了可解释性和决策可追溯性。

## 摘要（原文）

> Automated pathology image analysis is central to clinical diagnosis, but clinicians still ask which slide features drive a model's decision and why. Vision-language models can produce natural language explanations, but these are often correlational and lack verifiable evidence. In this paper, we introduce an SQL-centered agentic framework that enables both feature measurement and reasoning to be auditable. Specifically, after extracting human-interpretable cellular features, Feature Reasoning Agents compose and execute SQL queries over feature tables to aggregate visual evidence into quantitative findings. A Knowledge Comparison Agent then evaluates these findings against established pathological knowledge, mirroring how pathologists justify diagnoses from measurable observations. Extensive experiments evaluated on two pathology visual question answering datasets demonstrate our method improves interpretability and decision traceability while producing executable SQL traces that link cellular measurements to diagnostic conclusions.

