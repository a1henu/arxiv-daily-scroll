---
layout: default
title: Beyond Linearization: Attributed Table Graphs for Table Reasoning
---

# Beyond Linearization: Attributed Table Graphs for Table Reasoning
**arXiv**：[2601.08444v1](https://arxiv.org/abs/2601.08444) · [PDF](https://arxiv.org/pdf/2601.08444.pdf)  
**作者**：Yuxiang Wang, Junhao Gan, Shengxiang Gao, Shenghao Ye, Zhengyi Yang, Jianzhong Qi  

**一句话要点**：提出基于属性表图的训练免费模型TABGR，以解决表格推理中线性化方法的结构丢失和可解释性问题。

**关键词**：表格推理, 属性表图, 可解释性推理, 训练免费模型, 个性化PageRank, LLM应用

## 3 点简述
- 核心问题：现有LLM表格推理方法通过线性化表格输入，导致结构丢失、推理路径不明确和中间信息丢失问题。
- 方法要点：引入属性表图（ATG）显式保留表格结构，结合问题引导的个性化PageRank机制进行数据重排，支持基于图的推理以提高可解释性。
- 实验或效果：在两个常用基准测试中，TABGR在准确率上比最先进模型提升高达9.7%，验证了其有效性。

## 摘要（原文）

> Table reasoning, a task to answer questions by reasoning over data presented in tables, is an important topic due to the prevalence of knowledge stored in tabular formats. Recent solutions use Large Language Models (LLMs), exploiting the semantic understanding and reasoning capabilities of LLMs. A common paradigm of such solutions linearizes tables to form plain texts that are served as input to LLMs. This paradigm has critical issues. It loses table structures, lacks explicit reasoning paths for result explainability, and is subject to the "lost-in-the-middle" issue. To address these issues, we propose Table Graph Reasoner (TABGR), a training-free model that represents tables as an Attributed Table Graph (ATG). The ATG explicitly preserves row-column-cell structures while enabling graph-based reasoning for explainability. We further propose a Question-Guided Personalized PageRank (QG-PPR) mechanism to rerank tabular data and mitigate the lost-in-the-middle issue. Extensive experiments on two commonly used benchmarks show that TABGR consistently outperforms state-of-the-art models by up to 9.7% in accuracy. Our code will be made publicly available upon publication.

