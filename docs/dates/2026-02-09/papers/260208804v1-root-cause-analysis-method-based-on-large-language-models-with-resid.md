---
layout: default
title: Root Cause Analysis Method Based on Large Language Models with Residual Connection Structures
---

# Root Cause Analysis Method Based on Large Language Models with Residual Connection Structures
**arXiv**：[2602.08804v1](https://arxiv.org/abs/2602.08804) · [PDF](https://arxiv.org/pdf/2602.08804.pdf)  
**作者**：Liming Zhou, Ailing Liu, Hongwei Liu, Min He, Heng Zhang  

**一句话要点**：提出基于残差连接结构的大语言模型根因分析方法RC-LLM，以解决微服务架构中故障定位的挑战。

**关键词**：根因分析, 大语言模型, 残差连接, 微服务架构, 多源数据融合, 故障定位

## 3 点简述
- 核心问题：微服务架构中故障传播复杂和遥测数据高维性限制现有根因分析方法的有效性。
- 方法要点：设计残差式层次融合结构整合多源遥测数据，利用大语言模型建模时空和跨服务因果依赖。
- 实验或效果：在CCF-AIOps数据集上验证RC-LLM在根因分析中具有高准确性和效率。

## 摘要（原文）

> Root cause localization remain challenging in complex and large-scale microservice architectures. The complex fault propagation among microservices and the high dimensionality of telemetry data, including metrics, logs, and traces, limit the effectiveness of existing root cause analysis (RCA) methods. In this paper, a residual-connection-based RCA method using large language model (LLM), named RC-LLM, is proposed. A residual-like hierarchical fusion structure is designed to integrate multi-source telemetry data, while the contextual reasoning capability of large language models is leveraged to model temporal and cross-microservice causal dependencies. Experimental results on CCF-AIOps microservice datasets demonstrate that RC-LLM achieves strong accuracy and efficiency in root cause analysis.

