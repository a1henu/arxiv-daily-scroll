---
layout: default
title: DSAEval: Evaluating Data Science Agents on a Wide Range of Real-World Data Science Problems
---

# DSAEval: Evaluating Data Science Agents on a Wide Range of Real-World Data Science Problems
**arXiv**：[2601.13591v1](https://arxiv.org/abs/2601.13591) · [PDF](https://arxiv.org/pdf/2601.13591.pdf)  
**作者**：Maojun Sun, Yifei Xie, Yue Wu, Ruijian Han, Binyan Jiang, Defeng Sun, Yancheng Yuan, Jian Huang  

**一句话要点**：提出DSAEval基准以评估数据科学代理在真实世界多模态问题上的性能

**关键词**：数据科学代理评估, 多模态基准, 真实世界数据集, 结构化与非结构化数据, 迭代交互, 多维性能分析

## 3 点简述
- 核心问题：真实世界数据科学问题开放性强、跨分类且缺乏标准答案，评估困难
- 方法要点：基准包含641个问题基于285个数据集，支持多模态感知、多查询交互和多维评估
- 实验或效果：评估11个代理模型，Claude-Sonnet-4.5整体最强，多模态感知提升视觉任务性能2.04%-11.30%

## 摘要（原文）

> Recent LLM-based data agents aim to automate data science tasks ranging from data analysis to deep learning. However, the open-ended nature of real-world data science problems, which often span multiple taxonomies and lack standard answers, poses a significant challenge for evaluation. To address this, we introduce DSAEval, a benchmark comprising 641 real-world data science problems grounded in 285 diverse datasets, covering both structured and unstructured data (e.g., vision and text). DSAEval incorporates three distinctive features: (1) Multimodal Environment Perception, which enables agents to interpret observations from multiple modalities including text and vision; (2) Multi-Query Interactions, which mirror the iterative and cumulative nature of real-world data science projects; and (3) Multi-Dimensional Evaluation, which provides a holistic assessment across reasoning, code, and results. We systematically evaluate 11 advanced agentic LLMs using DSAEval. Our results show that Claude-Sonnet-4.5 achieves the strongest overall performance, GPT-5.2 is the most efficient, and MiMo-V2-Flash is the most cost-effective. We further demonstrate that multimodal perception consistently improves performance on vision-related tasks, with gains ranging from 2.04% to 11.30%. Overall, while current data science agents perform well on structured data and routine data anlysis workflows, substantial challenges remain in unstructured domains. Finally, we offer critical insights and outline future research directions to advance the development of data science agents.

