---
layout: default
title: AdaCultureSafe: Adaptive Cultural Safety Grounded by Cultural Knowledge in Large Language Models
---

# AdaCultureSafe: Adaptive Cultural Safety Grounded by Cultural Knowledge in Large Language Models
**arXiv**：[2603.08275v1](https://arxiv.org/abs/2603.08275) · [PDF](https://arxiv.org/pdf/2603.08275.pdf)  
**作者**：Hankun Kang, Di Lin, Zhirong Liao, Pengfei Bai, Xinyi Zeng, Jiawei Jiang, Yuanyuan Zhu, Tieyun Qian  

**一句话要点**：提出AdaCultureSafe框架，通过联合建模文化安全与知识以增强大语言模型的文化适应性。

**关键词**：文化安全, 文化知识, 大语言模型, 自适应学习, 数据集构建, 响应生成

## 3 点简述
- 核心问题：现有研究忽视文化安全需基于文化知识，导致大语言模型难以生成尊重特定文化的响应。
- 方法要点：构建包含文化描述与查询的数据集，并开发知识驱动方法以整合知识到响应生成过程。
- 实验或效果：评估流行大语言模型，发现文化安全与知识熟练度无显著相关性，新方法显著提升文化安全。

## 摘要（原文）

> With the widespread adoption of Large Language Models (LLMs), respecting indigenous cultures becomes essential for models' culturally safety and responsible global applications. Existing studies separately consider cultural safety and cultural knowledge and neglect that the former should be grounded by the latter. This severely prevents LLMs from yielding culture-specific respectful responses. Consequently, adaptive cultural safety remains a formidable task. In this work, we propose to jointly model cultural safety and knowledge. First and foremost, cultural-safety and knowledge-paired data serve as the key prerequisite to conduct this research. However, the cultural diversity across regions and the subtlety of cultural differences pose significant challenges to the creation of such paired evaluation data. To address this issue, we propose a novel framework that integrates authoritative cultural knowledge descriptions curation, LLM-automated query generation, and heavy manual verification. Accordingly, we obtain a dataset named AdaCultureSafe containing 4.8K manually decomposed fine-grained cultural descriptions and the corresponding 48K manually verified safety- and knowledge-oriented queries. Upon the constructed dataset, we evaluate three families of popular LLMs on their cultural safety and knowledge proficiency, via which we make a critical discovery: no significant correlation exists between their cultural safety and knowledge proficiency. We then delve into the utility-related neuron activations within LLMs to investigate the potential cause of the absence of correlation, which can be attributed to the difference of the objectives of pre-training and post-alignment. We finally present a knowledge-grounded method, which significantly enhances cultural safety by enforcing the integration of knowledge into the LLM response generation process.

