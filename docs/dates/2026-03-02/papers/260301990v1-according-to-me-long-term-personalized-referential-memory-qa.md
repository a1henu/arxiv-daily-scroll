---
layout: default
title: According to Me: Long-Term Personalized Referential Memory QA
---

# According to Me: Long-Term Personalized Referential Memory QA
**arXiv**：[2603.01990v1](https://arxiv.org/abs/2603.01990) · [PDF](https://arxiv.org/pdf/2603.01990.pdf)  
**作者**：Jingbiao Mei, Jinghong Chen, Guangyu Yang, Xinyu Hou, Margaret Li, Bill Byrne  

**一句话要点**：提出ATM-Bench基准和Schema-Guided Memory方法，以解决多模态多源个性化参考记忆问答问题。

**关键词**：个性化AI助手, 多模态记忆, 参考记忆问答, 长期记忆基准, 结构化记忆表示

## 3 点简述
- 核心问题：现有长期记忆基准主要关注对话历史，缺乏基于真实生活经验的个性化多模态多源参考记忆评估。
- 方法要点：引入ATM-Bench基准，包含隐私保护的个人记忆数据和标注问答对；提出Schema-Guided Memory结构化表示不同来源的记忆项。
- 实验或效果：在ATM-Bench-Hard集上现有方法准确率低于20%，Schema-Guided Memory优于先前常用的描述性记忆方法。

## 摘要（原文）

> Personalized AI assistants must recall and reason over long-term user memory, which naturally spans multiple modalities and sources such as images, videos, and emails. However, existing Long-term Memory benchmarks focus primarily on dialogue history, failing to capture realistic personalized references grounded in lived experience. We introduce ATM-Bench, the first benchmark for multimodal, multi-source personalized referential Memory QA. ATM-Bench contains approximately four years of privacy-preserving personal memory data and human-annotated question-answer pairs with ground-truth memory evidence, including queries that require resolving personal references, multi-evidence reasoning from multi-source and handling conflicting evidence. We propose Schema-Guided Memory (SGM) to structurally represent memory items originated from different sources. In experiments, we implement 5 state-of-the-art memory systems along with a standard RAG baseline and evaluate variants with different memory ingestion, retrieval, and answer generation techniques. We find poor performance (under 20\% accuracy) on the ATM-Bench-Hard set, and that SGM improves performance over Descriptive Memory commonly adopted in prior works. Code available at: https://github.com/JingbiaoMei/ATM-Bench

