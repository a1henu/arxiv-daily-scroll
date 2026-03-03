---
layout: default
title: PleaSQLarify: Visual Pragmatic Repair for Natural Language Database Querying
---

# PleaSQLarify: Visual Pragmatic Repair for Natural Language Database Querying
**arXiv**：[2603.01795v1](https://arxiv.org/abs/2603.01795) · [PDF](https://arxiv.org/pdf/2603.01795.pdf)  
**作者**：Robin Shing Moon Chan, Rita Sevastjanova, Mennatallah El-Assady  

**一句话要点**：提出PleaSQLarify，通过语用修复解决自然语言数据库查询中的歧义问题。

**关键词**：自然语言数据库接口, 语用修复, 歧义解析, 可视化交互, 用户控制

## 3 点简述
- 核心问题：自然语言数据库接口在输入歧义下脆弱，用户意图与系统解释易错配。
- 方法要点：基于语用推理，通过结构化交互和可视化界面实现增量澄清与信念更新。
- 实验或效果：12名参与者研究显示，系统帮助用户识别替代解释并高效解决歧义。

## 摘要（原文）

> Natural language database interfaces broaden data access, yet they remain brittle under input ambiguity. Standard approaches often collapse uncertainty into a single query, offering little support for mismatches between user intent and system interpretation. We reframe this challenge through pragmatic inference: while users economize expressions, systems operate on priors over the action space that may not align with the users'. In this view, pragmatic repair -- incremental clarification through minimal interaction -- is a natural strategy for resolving underspecification. We present \textsc{PleaSQLarify}, which operationalizes pragmatic repair by structuring interaction around interpretable decision variables that enable efficient clarification. A visual interface complements this by surfacing the action space for exploration, requesting user disambiguation, and making belief updates traceable across turns. In a study with twelve participants, \textsc{PleaSQLarify} helped users recognize alternative interpretations and efficiently resolve ambiguity. Our findings highlight pragmatic repair as a design principle that fosters effective user control in natural language interfaces.

