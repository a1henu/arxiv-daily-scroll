---
layout: default
title: DeepMMSearch-R1: Empowering Multimodal LLMs in Multimodal Web Search
---

# DeepMMSearch-R1: Empowering Multimodal LLMs in Multimodal Web Search
**arXiv**：[2510.12801v1](https://arxiv.org/abs/2510.12801) · [PDF](https://arxiv.org/pdf/2510.12801.pdf)  
**作者**：Kartik Narayan, Yang Xu, Tian Cao, Kavya Nerella, Vishal M. Patel, Navid Shiee, Peter Grasch, Chao Jia, Yinfei Yang, Zhe Gan  

**一句话要点**：提出DeepMMSearch-R1以解决多模态LLM在动态网络搜索中的效率问题

**关键词**：多模态大语言模型, 检索增强生成, 网络搜索, 强化学习, 多模态VQA数据集, 图像搜索优化

## 3 点简述
- 现有方法存在管道僵化、搜索调用过多和查询构建不佳等问题
- 采用两阶段训练：监督微调与在线强化学习，支持多轮图像和文本搜索
- 在知识密集型基准测试中表现优越，提供多模态网络搜索洞见

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) in real-world applications require
> access to external knowledge sources and must remain responsive to the dynamic
> and ever-changing real-world information in order to address
> information-seeking and knowledge-intensive user queries. Existing approaches,
> such as retrieval augmented generation (RAG) methods, search agents, and search
> equipped MLLMs, often suffer from rigid pipelines, excessive search calls, and
> poorly constructed search queries, which result in inefficiencies and
> suboptimal outcomes. To address these limitations, we present DeepMMSearch-R1,
> the first multimodal LLM capable of performing on-demand, multi-turn web
> searches and dynamically crafting queries for both image and text search tools.
> Specifically, DeepMMSearch-R1 can initiate web searches based on relevant crops
> of the input image making the image search more effective, and can iteratively
> adapt text search queries based on retrieved information, thereby enabling
> self-reflection and self-correction. Our approach relies on a two-stage
> training pipeline: a cold start supervised finetuning phase followed by an
> online reinforcement learning optimization. For training, we introduce
> DeepMMSearchVQA, a novel multimodal VQA dataset created through an automated
> pipeline intermixed with real-world information from web search tools. This
> dataset contains diverse, multi-hop queries that integrate textual and visual
> information, teaching the model when to search, what to search for, which
> search tool to use and how to reason over the retrieved information. We conduct
> extensive experiments across a range of knowledge-intensive benchmarks to
> demonstrate the superiority of our approach. Finally, we analyze the results
> and provide insights that are valuable for advancing multimodal web-search.

