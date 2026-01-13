---
layout: default
title: Beyond Dialogue Time: Temporal Semantic Memory for Personalized LLM Agents
---

# Beyond Dialogue Time: Temporal Semantic Memory for Personalized LLM Agents
**arXiv**：[2601.07468v1](https://arxiv.org/abs/2601.07468) · [PDF](https://arxiv.org/pdf/2601.07468.pdf)  
**作者**：Miao Su, Yucan Guo, Zhongni Hou, Long Bai, Zixuan Li, Yufei Zhang, Guojun Yin, Wei Lin, Xiaolong Jin, Jiafeng Guo, Xueqi Cheng  

**一句话要点**：提出时序语义记忆框架以解决LLM代理中记忆的时间不准确和碎片化问题

**关键词**：时序语义记忆, LLM代理, 个性化对话, 记忆建模, 持续性记忆

## 3 点简述
- 现有方法基于对话时间组织记忆，导致时间不准确和点状记忆碎片化
- TSM构建语义时间线，整合连续信息为持续性记忆，并基于查询时间意图检索
- 在LongMemEval和LoCoMo实验中，TSM准确率最高提升12.2%，优于现有方法

## 摘要（原文）

> Memory enables Large Language Model (LLM) agents to perceive, store, and use information from past dialogues, which is essential for personalization. However, existing methods fail to properly model the temporal dimension of memory in two aspects: 1) Temporal inaccuracy: memories are organized by dialogue time rather than their actual occurrence time; 2) Temporal fragmentation: existing methods focus on point-wise memory, losing durative information that captures persistent states and evolving patterns. To address these limitations, we propose Temporal Semantic Memory (TSM), a memory framework that models semantic time for point-wise memory and supports the construction and utilization of durative memory. During memory construction, it first builds a semantic timeline rather than a dialogue one. Then, it consolidates temporally continuous and semantically related information into a durative memory. During memory utilization, it incorporates the query's temporal intent on the semantic timeline, enabling the retrieval of temporally appropriate durative memories and providing time-valid, duration-consistent context to support response generation. Experiments on LongMemEval and LoCoMo show that TSM consistently outperforms existing methods and achieves up to 12.2% absolute improvement in accuracy, demonstrating the effectiveness of the proposed method.

