---
layout: default
title: Succeeding at Scale: Automated Multi-Retriever Fusion and Query-Side Adaptation for Multi-Tenant Search
---

# Succeeding at Scale: Automated Multi-Retriever Fusion and Query-Side Adaptation for Multi-Tenant Search
**arXiv**：[2601.04646v1](https://arxiv.org/abs/2601.04646) · [PDF](https://arxiv.org/pdf/2601.04646.pdf)  
**作者**：Prateek Jain, Shabari S Nair, Ritesh Goru, Prakhar Agarwal, Ajay Yadav, Yoga Sri Varshan Varadharajan, Constantine Caramanis  

**一句话要点**：提出融合检索与查询端适应方法，以解决多租户搜索中数据标注缺失和模型更新成本高的问题。

**关键词**：多租户搜索, 检索融合, 查询端适应, 低秩适应, 自动标注, 企业搜索

## 3 点简述
- 核心问题：多租户检索系统缺乏标注数据，且联合微调编码器需重新索引，成本高昂。
- 方法要点：采用融合检索策略和LLM评估，并仅微调查询编码器以保持文档索引不变。
- 实验或效果：在DevRev Search和SciFact基准上验证，实现性能提升与效率平衡。

## 摘要（原文）

> Large-scale multi-tenant retrieval systems amass vast user query logs yet critically lack the curated relevance labels required for effective domain adaptation. This "dark data" problem is exacerbated by the operational cost of model updates: jointly fine-tuning query and document encoders requires re-indexing the entire corpus, which is prohibitive in multi-tenant environments with thousands of isolated indices. To address these dual challenges, we introduce \textbf{DevRev Search}, a passage retrieval benchmark for technical customer support constructed through a fully automatic pipeline. We employ a \textbf{fusion-based candidate generation} strategy, pooling results from diverse sparse and dense retrievers, and utilize an LLM-as-a-Judge to perform rigorous \textbf{consistency filtering} and relevance assignment. We further propose a practical \textbf{Index-Preserving Adaptation} strategy: by fine-tuning only the query encoder via Low-Rank Adaptation (LoRA), we achieve competitive performance improvements while keeping the document index frozen. Our experiments on DevRev Search and SciFact demonstrate that targeting specific transformer layers in the query encoder yields optimal quality-efficiency trade-offs, offering a scalable path for personalized enterprise search.

