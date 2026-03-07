---
layout: default
title: DARE: Aligning LLM Agents with the R Statistical Ecosystem via Distribution-Aware Retrieval
---

# DARE: Aligning LLM Agents with the R Statistical Ecosystem via Distribution-Aware Retrieval
**arXiv**：[2603.04743v1](https://arxiv.org/abs/2603.04743) · [PDF](https://arxiv.org/pdf/2603.04743.pdf)  
**作者**：Maojun Sun, Yue Wu, Yifei Xie, Ruijian Han, Binyan Jiang, Defeng Sun, Yancheng Yuan, Jian Huang  

**一句话要点**：提出DARE嵌入模型，通过分布感知检索提升LLM代理在R统计生态系统中的代码生成能力。

**关键词**：大语言模型代理, R统计生态系统, 分布感知检索, 代码生成, 检索增强, 数据科学自动化

## 3 点简述
- 问题：LLM代理在自动化数据科学工作流时，因统计知识不足和工具检索困难，难以有效利用R中的统计方法。
- 方法：开发DARE模型，融合数据分布特征与函数元数据，构建RPKB知识库，以轻量级方式改进R包检索。
- 效果：DARE在包检索上NDCG@10达93.47%，优于开源模型，集成到RCodingAgent后提升下游分析任务性能。

## 摘要（原文）

> Large Language Model (LLM) agents can automate data-science workflows, but many rigorous statistical methods implemented in R remain underused because LLMs struggle with statistical knowledge and tool retrieval. Existing retrieval-augmented approaches focus on function-level semantics and ignore data distribution, producing suboptimal matches. We propose DARE (Distribution-Aware Retrieval Embedding), a lightweight, plug-and-play retrieval model that incorporates data distribution information into function representations for R package retrieval. Our main contributions are: (i) RPKB, a curated R Package Knowledge Base derived from 8,191 high-quality CRAN packages; (ii) DARE, an embedding model that fuses distributional features with function metadata to improve retrieval relevance; and (iii) RCodingAgent, an R-oriented LLM agent for reliable R code generation and a suite of statistical analysis tasks for systematically evaluating LLM agents in realistic analytical scenarios. Empirically, DARE achieves an NDCG at 10 of 93.47%, outperforming state-of-the-art open-source embedding models by up to 17% on package retrieval while using substantially fewer parameters. Integrating DARE into RCodingAgent yields significant gains on downstream analysis tasks. This work helps narrow the gap between LLM automation and the mature R statistical ecosystem.

