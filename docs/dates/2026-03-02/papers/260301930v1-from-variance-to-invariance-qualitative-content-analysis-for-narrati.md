---
layout: default
title: From Variance to Invariance: Qualitative Content Analysis for Narrative Graph Annotation
---

# From Variance to Invariance: Qualitative Content Analysis for Narrative Graph Annotation
**arXiv**：[2603.01930v1](https://arxiv.org/abs/2603.01930) · [PDF](https://arxiv.org/pdf/2603.01930.pdf)  
**作者**：Junbo Huang, Max Weinig, Ulrich Fritsche, Ricardo Usbeck  

**一句话要点**：提出基于定性内容分析的叙事图标注框架，以降低标注误差并评估人类标签变异影响。

**关键词**：叙事图标注, 定性内容分析, 人类标签变异, 有向无环图, 标注质量评估, 自然语言处理

## 3 点简述
- 核心问题：新闻叙事中经济事件（如通胀）的结构化标注与评估存在挑战，需处理人类标签变异。
- 方法要点：整合定性内容分析原则，构建有向无环图表示叙事，节点为事件，边为因果关系。
- 实验或效果：通过6×3因子实验设计评估标注质量，发现宽松度量高估可靠性，局部约束表示减少变异。

## 摘要（原文）

> Narratives in news discourse play a critical role in shaping public understanding of economic events, such as inflation. Annotating and evaluating these narratives in a structured manner remains a key challenge for Natural Language Processing (NLP). In this work, we introduce a narrative graph annotation framework that integrates principles from qualitative content analysis (QCA) to prioritize annotation quality by reducing annotation errors. We present a dataset of inflation narratives annotated as directed acyclic graphs (DAGs), where nodes represent events and edges encode causal relations. To evaluate annotation quality, we employed a $6\times3$ factorial experimental design to examine the effects of narrative representation (six levels) and distance metric type (three levels) on inter-annotator agreement (Krippendorrf's $α$), capturing the presence of human label variation (HLV) in narrative interpretations. Our analysis shows that (1) lenient metrics (overlap-based distance) overestimate reliability, and (2) locally-constrained representations (e.g., one-hop neighbors) reduce annotation variability. Our annotation and implementation of graph-based Krippendorrf's $α$ are open-sourced. The annotation framework and evaluation results provide practical guidance for NLP research on graph-based narrative annotation under HLV.

