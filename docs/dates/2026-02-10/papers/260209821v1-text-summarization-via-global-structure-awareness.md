---
layout: default
title: Text summarization via global structure awareness
---

# Text summarization via global structure awareness
**arXiv**：[2602.09821v1](https://arxiv.org/abs/2602.09821) · [PDF](https://arxiv.org/pdf/2602.09821.pdf)  
**作者**：Jiaquan Zhang, Chaoning Zhang, Shuxu Chen, Yibei Liu, Chenghao Li, Qigan Sun, Shuai Yuan, Fachrina Dewi Puspitasari, Dongshen Han, Guoqing Wang, Sung-Ho Bae, Yang Yang  

**一句话要点**：提出GloSA-sum，通过拓扑数据分析实现全局结构感知，以高效总结长文本并保持语义逻辑完整性。

**关键词**：文本摘要, 全局结构感知, 拓扑数据分析, 长文本处理, 语义完整性, 效率优化

## 3 点简述
- 核心问题：现有文本摘要方法常忽视全局结构，导致连贯性差和下游性能下降，而大语言模型虽准确但资源成本高。
- 方法要点：构建语义加权图，利用持久同调识别核心语义和逻辑结构，设计拓扑引导的迭代策略和分层策略以提高效率。
- 实验或效果：在多个数据集上验证，GloSA-sum减少冗余，平衡准确性与效率，并有助于大语言模型下游任务。

## 摘要（原文）

> Text summarization is a fundamental task in natural language processing (NLP), and the information explosion has made long-document processing increasingly demanding, making summarization essential. Existing research mainly focuses on model improvements and sentence-level pruning, but often overlooks global structure, leading to disrupted coherence and weakened downstream performance. Some studies employ large language models (LLMs), which achieve higher accuracy but incur substantial resource and time costs. To address these issues, we introduce GloSA-sum, the first summarization approach that achieves global structure awareness via topological data analysis (TDA). GloSA-sum summarizes text efficiently while preserving semantic cores and logical dependencies. Specifically, we construct a semantic-weighted graph from sentence embeddings, where persistent homology identifies core semantics and logical structures, preserved in a ``protection pool'' as the backbone for summarization. We design a topology-guided iterative strategy, where lightweight proxy metrics approximate sentence importance to avoid repeated high-cost computations, thus preserving structural integrity while improving efficiency. To further enhance long-text processing, we propose a hierarchical strategy that integrates segment-level and global summarization. Experiments on multiple datasets demonstrate that GloSA-sum reduces redundancy while preserving semantic and logical integrity, striking a balance between accuracy and efficiency, and further benefits LLM downstream tasks by shortening contexts while retaining essential reasoning chains.

