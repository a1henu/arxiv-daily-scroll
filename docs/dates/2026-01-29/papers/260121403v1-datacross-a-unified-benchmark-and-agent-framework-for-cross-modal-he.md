---
layout: default
title: DataCross: A Unified Benchmark and Agent Framework for Cross-Modal Heterogeneous Data Analysis
---

# DataCross: A Unified Benchmark and Agent Framework for Cross-Modal Heterogeneous Data Analysis
**arXiv**：[2601.21403v1](https://arxiv.org/abs/2601.21403) · [PDF](https://arxiv.org/pdf/2601.21403.pdf)  
**作者**：Ruyi Qi, Zhou Liu, Wentao Zhang  

**一句话要点**：提出DataCross基准与代理框架，以解决跨模态异构数据分析中视觉信息激活不足的问题。

**关键词**：跨模态分析, 异构数据, 代理框架, 视觉表格提取, 基准构建, 事实性验证

## 3 点简述
- 核心问题：现有数据分析代理主要处理结构化数据，无法有效利用视觉文档中的高价值信息，导致与工业需求脱节。
- 方法要点：引入DataCrossBench基准，包含200个跨领域任务，并设计DataCrossAgent框架，采用分治策略协调专家子代理进行跨模态分析。
- 实验或效果：DataCrossAgent在事实性上比GPT-4o提升29.7%，在高难度任务中表现出更强的鲁棒性，有效激活碎片化数据。

## 摘要（原文）

> In real-world data science and enterprise decision-making, critical information is often fragmented across directly queryable structured sources (e.g., SQL, CSV) and "zombie data" locked in unstructured visual documents (e.g., scanned reports, invoice images). Existing data analytics agents are predominantly limited to processing structured data, failing to activate and correlate this high-value visual information, thus creating a significant gap with industrial needs. To bridge this gap, we introduce DataCross, a novel benchmark and collaborative agent framework for unified, insight-driven analysis across heterogeneous data modalities. DataCrossBench comprises 200 end-to-end analysis tasks across finance, healthcare, and other domains. It is constructed via a human-in-the-loop reverse-synthesis pipeline, ensuring realistic complexity, cross-source dependency, and verifiable ground truth. The benchmark categorizes tasks into three difficulty tiers to evaluate agents' capabilities in visual table extraction, cross-modal alignment, and multi-step joint reasoning. We also propose the DataCrossAgent framework, inspired by the "divide-and-conquer" workflow of human analysts. It employs specialized sub-agents, each an expert on a specific data source, which are coordinated via a structured workflow of Intra-source Deep Exploration, Key Source Identification, and Contextual Cross-pollination. A novel reReAct mechanism enables robust code generation and debugging for factual verification. Experimental results show that DataCrossAgent achieves a 29.7% improvement in factuality over GPT-4o and exhibits superior robustness on high-difficulty tasks, effectively activating fragmented "zombie data" for insightful, cross-modal analysis.

