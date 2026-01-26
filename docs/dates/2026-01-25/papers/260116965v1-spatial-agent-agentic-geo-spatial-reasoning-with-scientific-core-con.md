---
layout: default
title: Spatial-Agent: Agentic Geo-spatial Reasoning with Scientific Core Concepts
---

# Spatial-Agent: Agentic Geo-spatial Reasoning with Scientific Core Concepts
**arXiv**：[2601.16965v1](https://arxiv.org/abs/2601.16965) · [PDF](https://arxiv.org/pdf/2601.16965.pdf)  
**作者**：Riyang Bao, Cheng Yang, Dazhou Yu, Zhexiang Tang, Gengchen Mai, Liang Zhao  

**一句话要点**：提出Spatial-Agent，基于空间信息科学理论解决地理空间推理中的计算幻觉问题。

**关键词**：地理空间推理, 空间信息科学, GeoFlow图, 概念转换, AI代理, 可解释工作流

## 3 点简述
- 现有LLM代理在地理空间计算中依赖搜索或模式匹配，常产生空间关系幻觉。
- 方法将地理分析问题形式化为概念转换，通过GeoFlow图表示可执行工作流。
- 在MapEval-API和MapQA基准上显著优于ReAct和Reflexion等基线，生成可解释工作流。

## 摘要（原文）

> Geospatial reasoning is essential for real-world applications such as urban analytics, transportation planning, and disaster response. However, existing LLM-based agents often fail at genuine geospatial computation, relying instead on web search or pattern matching while hallucinating spatial relationships. We present Spatial-Agent, an AI agent grounded in foundational theories of spatial information science. Our approach formalizes geo-analytical question answering as a concept transformation problem, where natural-language questions are parsed into executable workflows represented as GeoFlow Graphs -- directed acyclic graphs with nodes corresponding to spatial concepts and edges representing transformations. Drawing on spatial information theory, Spatial-Agent extracts spatial concepts, assigns functional roles with principled ordering constraints, and composes transformation sequences through template-based generation. Extensive experiments on MapEval-API and MapQA benchmarks demonstrate that Spatial-Agent significantly outperforms existing baselines including ReAct and Reflexion, while producing interpretable and executable geospatial workflows.

