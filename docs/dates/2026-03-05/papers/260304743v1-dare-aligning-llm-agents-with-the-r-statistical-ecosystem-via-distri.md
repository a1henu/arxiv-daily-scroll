---
layout: default
title: DARE: Aligning LLM Agents with the R Statistical Ecosystem via Distribution-Aware Retrieval
---

# DARE: Aligning LLM Agents with the R Statistical Ecosystem via Distribution-Aware Retrieval
**arXiv**：[2603.04743v1](https://arxiv.org/abs/2603.04743) · [PDF](https://arxiv.org/pdf/2603.04743.pdf)  
**作者**：Maojun Sun, Yue Wu, Yifei Xie, Ruijian Han, Binyan Jiang, Defeng Sun, Yancheng Yuan, Jian Huang  

**一句话要点**：提出DARE模型，通过分布感知检索对齐LLM代理与R统计生态系统，以解决统计工具检索不足问题。

**关键词**：LLM代理, R统计生态系统, 分布感知检索, R包知识库, 代码生成, 数据分析任务

## 3 点简述
- 核心问题：LLM代理在自动化数据科学工作流时，因缺乏统计知识和忽略数据分布，难以有效检索R包中的严谨统计方法。
- 方法要点：开发DARE，一个轻量级即插即用检索模型，融合数据分布特征与函数元数据，提升R包检索相关性。
- 实验或效果：DARE在包检索任务上NDCG@10达93.47%，优于开源模型达17%，集成到RCodingAgent后显著提升下游分析任务性能。

## 摘要（原文）

> Large Language Model (LLM) agents can automate data-science workflows, but many rigorous statistical methods implemented in R remain underused because LLMs struggle with statistical knowledge and tool retrieval. Existing retrieval-augmented approaches focus on function-level semantics and ignore data distribution, producing suboptimal matches. We propose DARE (Distribution-Aware Retrieval Embedding), a lightweight, plug-and-play retrieval model that incorporates data distribution information into function representations for R package retrieval. Our main contributions are: (i) RPKB, a curated R Package Knowledge Base derived from 8,191 high-quality CRAN packages; (ii) DARE, an embedding model that fuses distributional features with function metadata to improve retrieval relevance; and (iii) RCodingAgent, an R-oriented LLM agent for reliable R code generation and a suite of statistical analysis tasks for systematically evaluating LLM agents in realistic analytical scenarios. Empirically, DARE achieves an NDCG at 10 of 93.47%, outperforming state-of-the-art open-source embedding models by up to 17% on package retrieval while using substantially fewer parameters. Integrating DARE into RCodingAgent yields significant gains on downstream analysis tasks. This work helps narrow the gap between LLM automation and the mature R statistical ecosystem.

