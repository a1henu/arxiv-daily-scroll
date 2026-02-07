---
layout: default
title: BhashaSetu: Cross-Lingual Knowledge Transfer from High-Resource to Extreme Low-Resource Languages
---

# BhashaSetu: Cross-Lingual Knowledge Transfer from High-Resource to Extreme Low-Resource Languages
**arXiv**：[2602.05599v1](https://arxiv.org/abs/2602.05599) · [PDF](https://arxiv.org/pdf/2602.05599.pdf)  
**作者**：Subhadip Maji, Arnab Bhattacharya  

**一句话要点**：提出GETR方法，通过图增强令牌表示实现从高资源到极低资源语言的跨语言知识迁移。

**关键词**：跨语言知识迁移, 低资源语言处理, 图神经网络, 令牌表示增强, POS标注, 情感分类

## 3 点简述
- 核心问题：低资源语言因数据稀缺导致NLP性能远落后于高资源语言。
- 方法要点：引入GETR，基于图神经网络增强令牌表示，用于句子级和词级任务。
- 实验或效果：在POS标注等任务上显著超越基线，提升达13-27个百分点。

## 摘要（原文）

> Despite remarkable advances in natural language processing, developing effective systems for low-resource languages remains a formidable challenge, with performances typically lagging far behind high-resource counterparts due to data scarcity and insufficient linguistic resources. Cross-lingual knowledge transfer has emerged as a promising approach to address this challenge by leveraging resources from high-resource languages. In this paper, we investigate methods for transferring linguistic knowledge from high-resource languages to low-resource languages, where the number of labeled training instances is in hundreds. We focus on sentence-level and word-level tasks. We introduce a novel method, GETR (Graph-Enhanced Token Representation) for cross-lingual knowledge transfer along with two adopted baselines (a) augmentation in hidden layers and (b) token embedding transfer through token translation. Experimental results demonstrate that our GNN-based approach significantly outperforms existing multilingual and cross-lingual baseline methods, achieving 13 percentage point improvements on truly low-resource languages (Mizo, Khasi) for POS tagging, and 20 and 27 percentage point improvements in macro-F1 on simulated low-resource languages (Marathi, Bangla, Malayalam) across sentiment classification and NER tasks respectively. We also present a detailed analysis of the transfer mechanisms and identify key factors that contribute to successful knowledge transfer in this linguistic context.

