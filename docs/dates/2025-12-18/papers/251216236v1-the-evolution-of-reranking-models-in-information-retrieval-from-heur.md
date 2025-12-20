---
layout: default
title: The Evolution of Reranking Models in Information Retrieval: From Heuristic Methods to Large Language Models
---

# The Evolution of Reranking Models in Information Retrieval: From Heuristic Methods to Large Language Models
**arXiv**：[2512.16236v1](https://arxiv.org/abs/2512.16236) · [PDF](https://arxiv.org/pdf/2512.16236.pdf)  
**作者**：Tejul Pandit, Sakshi Mahendru, Meet Raval, Dhvani Upadhyay  

**一句话要点**：综述信息检索中重排序模型的演进，从启发式方法到大型语言模型，聚焦现代RAG管道应用。

**关键词**：信息检索重排序, 检索增强生成, 神经网络架构, 大型语言模型, 知识蒸馏, 效率优化

## 3 点简述
- 核心问题：重排序在信息检索中提升结果相关性，尤其在RAG管道中影响输出质量。
- 方法要点：涵盖启发式方法、神经网络架构如交叉编码器和T5，以及LLM集成与效率优化技术。
- 实验或效果：分析不同策略的原理、效果、计算特征和实际权衡，提供结构化综合。

## 摘要（原文）

> Reranking is a critical stage in contemporary information retrieval (IR) systems, improving the relevance of the user-presented final results by honing initial candidate sets. This paper is a thorough guide to examine the changing reranker landscape and offer a clear view of the advancements made in reranking methods. We present a comprehensive survey of reranking models employed in IR, particularly within modern Retrieval Augmented Generation (RAG) pipelines, where retrieved documents notably influence output quality.
>   We embark on a chronological journey through the historical trajectory of reranking techniques, starting with foundational approaches, before exploring the wide range of sophisticated neural network architectures such as cross-encoders, sequence-generation models like T5, and Graph Neural Networks (GNNs) utilized for structural information. Recognizing the computational cost of advancing neural rerankers, we analyze techniques for enhancing efficiency, notably knowledge distillation for creating competitive, lighter alternatives. Furthermore, we map the emerging territory of integrating Large Language Models (LLMs) in reranking, examining novel prompting strategies and fine-tuning tactics. This survey seeks to elucidate the fundamental ideas, relative effectiveness, computational features, and real-world trade-offs of various reranking strategies. The survey provides a structured synthesis of the diverse reranking paradigms, highlighting their underlying principles and comparative strengths and weaknesses.

