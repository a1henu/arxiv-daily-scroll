---
layout: default
title: With Argus Eyes: Assessing Retrieval Gaps via Uncertainty Scoring to Detect and Remedy Retrieval Blind Spots
---

# With Argus Eyes: Assessing Retrieval Gaps via Uncertainty Scoring to Detect and Remedy Retrieval Blind Spots
**arXiv**：[2602.09616v1](https://arxiv.org/abs/2602.09616) · [PDF](https://arxiv.org/pdf/2602.09616.pdf)  
**作者**：Zeinab Sadat Taghavi, Ali Modarressi, Hinrich Schutze, Andreas Marfurt  

**一句话要点**：提出ARGUS管道以通过不确定性评分检测和补救检索增强生成系统中的检索盲点

**关键词**：检索增强生成, 不确定性评分, 检索盲点, 文档增强, 嵌入几何

## 3 点简述
- 核心问题：神经检索器在RAG系统中存在盲点，即无法检索与查询相关但嵌入相似度低的实体
- 方法要点：引入检索概率评分（RPS）预测盲点风险，并利用知识库进行针对性文档增强
- 实验或效果：在多个数据集上，ARGUS显著提升检索性能，平均增加nDCG@5和nDCG@10分数

## 摘要（原文）

> Reliable retrieval-augmented generation (RAG) systems depend fundamentally on the retriever's ability to find relevant information. We show that neural retrievers used in RAG systems have blind spots, which we define as the failure to retrieve entities that are relevant to the query, but have low similarity to the query embedding. We investigate the training-induced biases that cause such blind spot entities to be mapped to inaccessible parts of the embedding space, resulting in low retrievability. Using a large-scale dataset constructed from Wikidata relations and first paragraphs of Wikipedia, and our proposed Retrieval Probability Score (RPS), we show that blind spot risk in standard retrievers (e.g., CONTRIEVER, REASONIR) can be predicted pre-index from entity embedding geometry, avoiding expensive retrieval evaluations. To address these blind spots, we introduce ARGUS, a pipeline that enables the retrievability of high-risk (low-RPS) entities through targeted document augmentation from a knowledge base (KB), first paragraphs of Wikipedia, in our case. Extensive experiments on BRIGHT, IMPLIRET, and RAR-B show that ARGUS achieves consistent improvements across all evaluated retrievers (averaging +3.4 nDCG@5 and +4.5 nDCG@10 absolute points), with substantially larger gains in challenging subsets. These results establish that preemptively remedying blind spots is critical for building robust and trustworthy RAG systems (Code and Data).

