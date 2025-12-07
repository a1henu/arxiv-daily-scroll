---
layout: default
title: OsmT: Bridging OpenStreetMap Queries and Natural Language with Open-source Tag-aware Language Models
---

# OsmT: Bridging OpenStreetMap Queries and Natural Language with Open-source Tag-aware Language Models
**arXiv**：[2512.04738v1](https://arxiv.org/abs/2512.04738) · [PDF](https://arxiv.org/pdf/2512.04738.pdf)  
**作者**：Zhuoyue Wan, Wentao Hu, Chen Jason Zhang, Yuanfeng Song, Shuaimin Li, Ruiqiang Xiao, Xiao-Yong Wei, Raymond Chi-Wing Wong  

**一句话要点**：提出OsmT开源标签感知语言模型，以增强自然语言与OpenStreetMap查询语言的转换

**关键词**：开源语言模型, 标签检索增强, 自然语言查询转换, 地理空间查询, OverpassQL, 查询解释

## 3 点简述
- 核心问题：现有方案依赖闭源大模型，导致高推理成本、透明度低，难以轻量部署。
- 方法要点：引入标签检索增强机制，融入上下文相关标签知识，提升查询准确性和结构有效性。
- 实验或效果：在公开基准上评估，模型参数较少但达到竞争性准确度，支持查询生成与解释任务。

## 摘要（原文）

> Bridging natural language and structured query languages is a long-standing challenge in the database community. While recent advances in language models have shown promise in this direction, existing solutions often rely on large-scale closed-source models that suffer from high inference costs, limited transparency, and lack of adaptability for lightweight deployment. In this paper, we present OsmT, an open-source tag-aware language model specifically designed to bridge natural language and Overpass Query Language (OverpassQL), a structured query language for accessing large-scale OpenStreetMap (OSM) data. To enhance the accuracy and structural validity of generated queries, we introduce a Tag Retrieval Augmentation (TRA) mechanism that incorporates contextually relevant tag knowledge into the generation process. This mechanism is designed to capture the hierarchical and relational dependencies present in the OSM database, addressing the topological complexity inherent in geospatial query formulation. In addition, we define a reverse task, OverpassQL-to-Text, which translates structured queries into natural language explanations to support query interpretation and improve user accessibility. We evaluate OsmT on a public benchmark against strong baselines and observe consistent improvements in both query generation and interpretation. Despite using significantly fewer parameters, our model achieves competitive accuracy, demonstrating the effectiveness of open-source pre-trained language models in bridging natural language and structured query languages within schema-rich geospatial environments.

