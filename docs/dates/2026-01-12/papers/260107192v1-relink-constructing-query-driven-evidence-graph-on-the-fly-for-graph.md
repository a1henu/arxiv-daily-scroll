---
layout: default
title: Relink: Constructing Query-Driven Evidence Graph On-the-Fly for GraphRAG
---

# Relink: Constructing Query-Driven Evidence Graph On-the-Fly for GraphRAG
**arXiv**：[2601.07192v1](https://arxiv.org/abs/2601.07192) · [PDF](https://arxiv.org/pdf/2601.07192.pdf)  
**作者**：Manzong Huang, Chenyang Bu, Yi He, Xingrui Zhuo, Xindong Wu  

**一句话要点**：提出Relink框架，通过动态构建查询驱动证据图解决GraphRAG中的知识不完整和噪声干扰问题

**关键词**：图检索增强生成, 动态知识图谱构建, 查询驱动推理, 开放域问答, 证据路径修复

## 3 点简述
- 核心问题：现有GraphRAG依赖静态知识图谱，存在知识不完整和噪声事实干扰推理的问题
- 方法要点：采用“推理即构建”范式，从文本语料中动态实例化所需事实并统一评估候选事实
- 实验效果：在五个开放域问答基准上，EM和F1指标平均提升超过5%，优于主流基线方法

## 摘要（原文）

> Graph-based Retrieval-Augmented Generation (GraphRAG) mitigates hallucinations in Large Language Models (LLMs) by grounding them in structured knowledge. However, current GraphRAG methods are constrained by a prevailing \textit{build-then-reason} paradigm, which relies on a static, pre-constructed Knowledge Graph (KG). This paradigm faces two critical challenges. First, the KG's inherent incompleteness often breaks reasoning paths. Second, the graph's low signal-to-noise ratio introduces distractor facts, presenting query-relevant but misleading knowledge that disrupts the reasoning process.
>   To address these challenges, we argue for a \textit{reason-and-construct} paradigm and propose Relink, a framework that dynamically builds a query-specific evidence graph. To tackle incompleteness, \textbf{Relink} instantiates required facts from a latent relation pool derived from the original text corpus, repairing broken paths on the fly. To handle misleading or distractor facts, Relink employs a unified, query-aware evaluation strategy that jointly considers candidates from both the KG and latent relations, selecting those most useful for answering the query rather than relying on their pre-existence. This empowers Relink to actively discard distractor facts and construct the most faithful and precise evidence path for each query.
>   Extensive experiments on five Open-Domain Question Answering benchmarks show that Relink achieves significant average improvements of 5.4\% in EM and 5.2\% in F1 over leading GraphRAG baselines, demonstrating the superiority of our proposed framework.

