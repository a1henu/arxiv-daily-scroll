---
layout: default
title: CricBench: A Multilingual Benchmark for Evaluating LLMs in Cricket Analytics
---

# CricBench: A Multilingual Benchmark for Evaluating LLMs in Cricket Analytics
**arXiv**：[2512.21877v1](https://arxiv.org/abs/2512.21877) · [PDF](https://arxiv.org/pdf/2512.21877.pdf)  
**作者**：Vaibhav Devraj, Dhruv Kumar, Jagat Sesh Challa  

**一句话要点**：提出CricBench多语言基准以评估LLMs在板球分析中的SQL能力

**关键词**：板球分析, 多语言基准, SQL查询评估, 大型语言模型, 领域特定任务

## 3 点简述
- 核心问题：LLMs在体育分析领域处理复杂SQL查询和多语言需求的能力尚不明确
- 方法要点：与专家合作构建包含英语和印地语的黄金标准数据集，涵盖复杂查询
- 实验或效果：评估显示DeepSeek R1表现最佳但准确性下降，印地语查询有时优于英语

## 摘要（原文）

> Cricket is the second most popular sport globally, commanding a massive following of over 2.5 billion fans globally. Enthusiasts and analysts frequently seek advanced statistical insights, such as long-term historical performance trends or complex player comparisons, that are often unavailable through standard web searches. While Large Language Models (LLMs) have advanced significantly in Text-to-SQL tasks, their capability to handle the domain-specific nuances, complex schema variations, and multilingual requirements inherent to sports analytics remains under-explored. To investigate this potential capability gap, we present CricBench, a comprehensive benchmark suite for evaluating LLMs on specialized cricket data. To curate a "Gold Standard" dataset, we collaborate with domain experts in cricket and SQL to manually author complex queries, ensuring logical correctness. Recognizing linguistic diversity, we construct the benchmark in both English and Hindi, establishing a framework that is open for further extension to other regional languages. We evaluate six state-of-the-art models, including GPT-4o, Claude 3.7 Sonnet, and open-source models, using a strict evaluation protocol. Our results reveal that high performance on general benchmarks does not guarantee success in specialized domains. While the open-weights reasoning model DeepSeek R1 achieves state-of-the-art performance (50.6%), surpassing proprietary giants like Claude 3.7 Sonnet (47.7%) and GPT-4o (33.7%), it still exhibits a significant accuracy drop when moving from general benchmarks (BIRD) to CricBench. Furthermore, we observe that code-mixed Hindi queries frequently yield parity or higher accuracy compared to English, challenging the assumption that English is the optimal prompt language for specialized SQL tasks.

