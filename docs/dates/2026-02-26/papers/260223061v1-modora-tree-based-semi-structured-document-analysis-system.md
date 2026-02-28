---
layout: default
title: MoDora: Tree-Based Semi-Structured Document Analysis System
---

# MoDora: Tree-Based Semi-Structured Document Analysis System
**arXiv**：[2602.23061v1](https://arxiv.org/abs/2602.23061) · [PDF](https://arxiv.org/pdf/2602.23061.pdf)  
**作者**：Bangrui Xu, Qihang Yao, Zirui Tang, Xuanhe Zhou, Yeye He, Shihan Yu, Qianqian Xu, Bin Wang, Guoliang Li, Conghui He, Fan Wu  

**一句话要点**：提出MoDora系统，基于LLM解决半结构化文档自然语言问答中的元素碎片化、结构缺失和跨区域检索难题。

**关键词**：半结构化文档分析, 自然语言问答, 组件关联树, 布局感知检索, LLM引导系统

## 3 点简述
- 核心问题：半结构化文档元素碎片化、结构层次缺失和跨区域信息检索困难，阻碍自然语言问答。
- 方法要点：采用局部对齐聚合和类型提取，设计组件关联树建模层次关系，结合布局网格和LLM引导的检索策略。
- 实验或效果：在准确性上超越基线5.97%-61.07%，代码已开源。

## 摘要（原文）

> Semi-structured documents integrate diverse interleaved data elements (e.g., tables, charts, hierarchical paragraphs) arranged in various and often irregular layouts. These documents are widely observed across domains and account for a large portion of real-world data. However, existing methods struggle to support natural language question answering over these documents due to three main technical challenges: (1) The elements extracted by techniques like OCR are often fragmented and stripped of their original semantic context, making them inadequate for analysis. (2) Existing approaches lack effective representations to capture hierarchical structures within documents (e.g., associating tables with nested chapter titles) and to preserve layout-specific distinctions (e.g., differentiating sidebars from main content). (3) Answering questions often requires retrieving and aligning relevant information scattered across multiple regions or pages, such as linking a descriptive paragraph to table cells located elsewhere in the document.
>   To address these issues, we propose MoDora, an LLM-powered system for semi-structured document analysis. First, we adopt a local-alignment aggregation strategy to convert OCR-parsed elements into layout-aware components, and conduct type-specific information extraction for components with hierarchical titles or non-text elements. Second, we design the Component-Correlation Tree (CCTree) to hierarchically organize components, explicitly modeling inter-component relations and layout distinctions through a bottom-up cascade summarization process. Finally, we propose a question-type-aware retrieval strategy that supports (1) layout-based grid partitioning for location-based retrieval and (2) LLM-guided pruning for semantic-based retrieval. Experiments show MoDora outperforms baselines by 5.97%-61.07% in accuracy. The code is at https://github.com/weAIDB/MoDora.

