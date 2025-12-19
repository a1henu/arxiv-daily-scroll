---
layout: default
title: ModelTables: A Corpus of Tables about Models
---

# ModelTables: A Corpus of Tables about Models
**arXiv**：[2512.16106v1](https://arxiv.org/abs/2512.16106) · [PDF](https://arxiv.org/pdf/2512.16106.pdf)  
**作者**：Zhengyuan Dong, Victor Zhong, Renée J. Miller  

**一句话要点**：提出ModelTables基准以解决模型湖中表格语义检索问题

**关键词**：模型湖, 表格检索, 结构化数据, 语义搜索, 基准构建

## 3 点简述
- 核心问题：模型性能与配置表格的语义检索常被文本检索忽视，缺乏大规模结构化基准。
- 方法要点：从Hugging Face模型卡等构建包含60K模型和90K表格的语料库，链接模型与出版上下文。
- 实验或效果：评估表格搜索方法，基于联合的语义检索达54.8% P@1，基于表格的密集检索达66.5% P@1。

## 摘要（原文）

> We present ModelTables, a benchmark of tables in Model Lakes that captures the structured semantics of performance and configuration tables often overlooked by text only retrieval. The corpus is built from Hugging Face model cards, GitHub READMEs, and referenced papers, linking each table to its surrounding model and publication context. Compared with open data lake tables, model tables are smaller yet exhibit denser inter table relationships, reflecting tightly coupled model and benchmark evolution. The current release covers over 60K models and 90K tables. To evaluate model and table relatedness, we construct a multi source ground truth using three complementary signals: (1) paper citation links, (2) explicit model card links and inheritance, and (3) shared training datasets. We present one extensive empirical use case for the benchmark which is table search. We compare canonical Data Lake search operators (unionable, joinable, keyword) and Information Retrieval baselines (dense, sparse, hybrid retrieval) on this benchmark. Union based semantic table retrieval attains 54.8 % P@1 overall (54.6 % on citation, 31.3 % on inheritance, 30.6 % on shared dataset signals); table based dense retrieval reaches 66.5 % P@1, and metadata hybrid retrieval achieves 54.1 %. This evaluation indicates clear room for developing better table search methods. By releasing ModelTables and its creation protocol, we provide the first large scale benchmark of structured data describing AI model. Our use case of table discovery in Model Lakes, provides intuition and evidence for developing more accurate semantic retrieval, structured comparison, and principled organization of structured model knowledge. Source code, data, and other artifacts have been made available at https://github.com/RJMillerLab/ModelTables.

