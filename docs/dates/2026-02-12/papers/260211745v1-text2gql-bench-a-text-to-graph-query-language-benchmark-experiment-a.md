---
layout: default
title: Text2GQL-Bench: A Text to Graph Query Language Benchmark [Experiment, Analysis & Benchmark]
---

# Text2GQL-Bench: A Text to Graph Query Language Benchmark [Experiment, Analysis & Benchmark]
**arXiv**：[2602.11745v1](https://arxiv.org/abs/2602.11745) · [PDF](https://arxiv.org/pdf/2602.11745.pdf)  
**作者**：Songlin Lyu, Lujie Ban, Zihang Wu, Tianqi Luo, Jirong Liu, Chenhao Ma, Yuyu Luo, Nan Tang, Shipeng Qi, Heng Lin, Yongchao Liu, Chuntao Hong  

**一句话要点**：提出Text2GQL-Bench基准以解决文本到图查询语言转换的评估不足问题

**关键词**：文本到图查询语言, 图数据库基准, 多领域数据集, ISO-GQL生成, 执行准确率评估, 大语言模型评估

## 3 点简述
- 现有文本到图查询语言数据集在领域覆盖、查询语言支持和评估范围上存在局限
- 构建包含178,184个问答对的多领域多语言数据集，并开发可扩展的生成框架
- 评估发现ISO-GQL生成存在显著方言差距，零射设置下执行准确率最高仅4%

## 摘要（原文）

> Graph models are fundamental to data analysis in domains rich with complex relationships. Text-to-Graph-Query-Language (Text-to-GQL) systems act as a translator, converting natural language into executable graph queries. This capability allows Large Language Models (LLMs) to directly analyze and manipulate graph data, posi-tioning them as powerful agent infrastructures for Graph Database Management System (GDBMS). Despite recent progress, existing datasets are often limited in domain coverage, supported graph query languages, or evaluation scope. The advancement of Text-to-GQL systems is hindered by the lack of high-quality benchmark datasets and evaluation methods to systematically compare model capabilities across different graph query languages and domains. In this work, we present Text2GQL-Bench, a unified Text-to-GQL benchmark designed to address these limitations. Text2GQL-Bench couples a multi-GQL dataset that has 178,184 (Question, Query) pairs spanning 13 domains, with a scalable construction framework that generates datasets in different domains, question abstraction levels, and GQLs with heterogeneous resources. To support compre-hensive assessment, we introduce an evaluation method that goes beyond a single end-to-end metric by jointly reporting grammatical validity, similarity, semantic alignment, and execution accuracy. Our evaluation uncovers a stark dialect gap in ISO-GQL generation: even strong LLMs achieve only at most 4% execution accuracy (EX) in zero-shot settings, though a fixed 3-shot prompt raises accuracy to around 50%, the grammatical validity remains lower than 70%. Moreover, a fine-tuned 8B open-weight model reaches 45.1% EX, and 90.8% grammatical validity, demonstrating that most of the performance jump is unlocked by exposure to sufficient ISO-GQL examples.

