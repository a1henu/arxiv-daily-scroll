---
layout: default
title: Knowledge-based Visual Question Answer with Multimodal Processing, Retrieval and Filtering
---

# Knowledge-based Visual Question Answer with Multimodal Processing, Retrieval and Filtering
**arXiv**：[2510.14605v1](https://arxiv.org/abs/2510.14605) · [PDF](https://arxiv.org/pdf/2510.14605.pdf)  
**作者**：Yuyang Hong, Jiaqi Gu, Qi Yang, Lubin Fan, Yue Wu, Ying Wang, Kun Ding, Shiming Xiang, Jieping Ye  

**一句话要点**：提出Wiki-PRF三阶段方法以解决知识视觉问答中查询质量和检索结果相关性问题

**关键词**：知识视觉问答, 多模态检索, 强化学习训练, 检索增强生成, 视觉语言模型

## 3 点简述
- 核心问题：知识视觉问答中多模态查询质量差和检索结果相关性低
- 方法要点：通过处理、检索和过滤三阶段，结合视觉工具和强化学习训练
- 实验或效果：在E-VQA和InfoSeek数据集上答案质量显著提升，达到SOTA

## 摘要（原文）

> Knowledge-based visual question answering (KB-VQA) requires visual language
> models (VLMs) to integrate visual understanding with external knowledge
> retrieval. Although retrieval-augmented generation (RAG) achieves significant
> advances in this task by combining knowledge-base querying, it still struggles
> with the quality of multimodal queries and the relevance of retrieved results.
> To overcome these challenges, we propose a novel three-stage method, termed
> Wiki-PRF, including Processing, Retrieval and Filtering stages. The processing
> stage dynamically invokes visual tools to extract precise multimodal
> information for retrieval. The retrieval stage integrates visual and text
> features to achieve multimodal knowledge retrieval. The filtering stage
> performs relevance filtering and concentration on retrieval results. To this
> end, we introduce a visual language model trained with answer accuracy and
> format consistency as reward signals via a reinforcement learning manner. This
> enhances the model's reasoning, tool invocation for accurate queries, and
> filtering of irrelevant content. Experiments on benchmark datasets (E-VQA and
> InfoSeek) show significant improvements~(36.0 and 42.8) in answer quality,
> achieving state-of-the-art performance. Code is available at
> https://github.com/cqu-student/Wiki-PRF

