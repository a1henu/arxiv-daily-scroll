---
layout: default
title: Cross-modal Retrieval Models for Stripped Binary Analysis
---

# Cross-modal Retrieval Models for Stripped Binary Analysis
**arXiv**：[2512.10393v1](https://arxiv.org/abs/2512.10393) · [PDF](https://arxiv.org/pdf/2512.10393.pdf)  
**作者**：Guoqiang Chen, Lingyun Ying, Ziyang Song, Daguang Liu, Qiang Wang, Zhiqi Wang, Li Hu, Shaoyin Cheng, Weiming Zhang, Nenghai Yu  

**一句话要点**：提出BinSeek两阶段跨模态检索框架以解决剥离二进制代码分析中的查询检索挑战

**关键词**：跨模态检索, 二进制代码分析, LLM数据合成, 两阶段框架, 语义嵌入, 重排序模型

## 3 点简述
- 核心问题：剥离二进制函数缺乏符号信息，难以基于自然语言查询进行高效检索
- 方法要点：结合BinSeekEmbedding学习语义相关性和BinSeek-Reranker上下文增强重排序
- 实验或效果：在Rec@3和MRR@3指标上超越同规模模型31.42%和27.17%，优于参数大16倍的通用模型

## 摘要（原文）

> LLM-agent based binary code analysis has demonstrated significant potential across a wide range of software security scenarios, including vulnerability detection, malware analysis, etc. In agent workflow, however, retrieving the positive from thousands of stripped binary functions based on user query remains under-studied and challenging, as the absence of symbolic information distinguishes it from source code retrieval. In this paper, we introduce, BinSeek, the first two-stage cross-modal retrieval framework for stripped binary code analysis. It consists of two models: BinSeekEmbedding is trained on large-scale dataset to learn the semantic relevance of the binary code and the natural language description, furthermore, BinSeek-Reranker learns to carefully judge the relevance of the candidate code to the description with context augmentation. To this end, we built an LLM-based data synthesis pipeline to automate training construction, also deriving a domain benchmark for future research. Our evaluation results show that BinSeek achieved the state-of-the-art performance, surpassing the the same scale models by 31.42% in Rec@3 and 27.17% in MRR@3, as well as leading the advanced general-purpose models that have 16 times larger parameters.

