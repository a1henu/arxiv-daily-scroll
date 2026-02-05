---
layout: default
title: Less Finetuning, Better Retrieval: Rethinking LLM Adaptation for Biomedical Retrievers via Synthetic Data and Model Merging
---

# Less Finetuning, Better Retrieval: Rethinking LLM Adaptation for Biomedical Retrievers via Synthetic Data and Model Merging
**arXiv**：[2602.04731v1](https://arxiv.org/abs/2602.04731) · [PDF](https://arxiv.org/pdf/2602.04731.pdf)  
**作者**：Sameh Khattab, Jean-Philippe Corbeil, Osman Alperen Koraş, Amin Dada, Julian Friedrich, François Beaulieu, Paul Vozila, Jens Kleesiek  

**一句话要点**：提出STM框架，通过合成数据和模型合并，高效适配通用LLM为生物医学检索器

**关键词**：检索增强生成, 模型适配, 合成数据, 模型合并, 生物医学检索, LLM检索器

## 3 点简述
- 核心问题：通用LLM在生物医学等专业领域检索任务中适配不足，技术细节未充分探索
- 方法要点：STM框架结合合成困难负样本、检索提示优化和模型合并，提升领域特异性
- 实验或效果：在MTEB基准12个任务上，STM提升专家模型达23.5%，合并模型优于单专家和基线

## 摘要（原文）

> Retrieval-augmented generation (RAG) has become the backbone of grounding Large Language Models (LLMs), improving knowledge updates and reducing hallucinations. Recently, LLM-based retriever models have shown state-of-the-art performance for RAG applications. However, several technical aspects remain underexplored on how to adapt general-purpose LLMs into effective domain-specific retrievers, especially in specialized domains such as biomedicine. We present Synthesize-Train-Merge (STM), a modular framework that enhances decoder-only LLMs with synthetic hard negatives, retrieval prompt optimization, and model merging. Experiments on a subset of 12 medical and general tasks from the MTEB benchmark show STM boosts task-specific experts by up to 23.5\% (average 7.5\%) and produces merged models that outperform both single experts and strong baselines without extensive pretraining. Our results demonstrate a scalable, efficient path for turning general LLMs into high-performing, domain-specialized retrievers, preserving general-domain capabilities while excelling on specialized tasks.

