---
layout: default
title: Cross-platform Product Matching Based on Entity Alignment of Knowledge Graph with RAEA model
---

# Cross-platform Product Matching Based on Entity Alignment of Knowledge Graph with RAEA model
**arXiv**：[2512.07232v1](https://arxiv.org/abs/2512.07232) · [PDF](https://arxiv.org/pdf/2512.07232.pdf)  
**作者**：Wenlong Liu, Jiahua Pan, Xingyu Zhang, Xinxin Gong, Yang Ye, Xujin Zhao, Xin Wang, Kent Wu, Hua Xiang, Houmin Yan, Qingpeng Zhang  

**一句话要点**：提出RAEA模型以解决跨平台产品匹配中的实体对齐问题，通过结合属性和关系三元组交互提升性能。

**关键词**：实体对齐, 知识图谱, 产品匹配, 图注意力网络, 跨平台应用

## 3 点简述
- 核心问题：现有实体对齐方法未能充分利用属性和关系三元组及其交互，影响跨平台产品匹配准确性。
- 方法要点：采用两阶段流程（粗筛和精筛），在精筛阶段引入RAEA框架，通过属性感知实体编码器和关系感知图注意力网络聚合对齐信号。
- 实验或效果：在跨语言数据集DBP15K上相比12个基线平均Hits@1提升6.59%，在单语言数据集DWY100K上取得竞争性结果。

## 摘要（原文）

> Product matching aims to identify identical or similar products sold on different platforms. By building knowledge graphs (KGs), the product matching problem can be converted to the Entity Alignment (EA) task, which aims to discover the equivalent entities from diverse KGs. The existing EA methods inadequately utilize both attribute triples and relation triples simultaneously, especially the interactions between them. This paper introduces a two-stage pipeline consisting of rough filter and fine filter to match products from eBay and Amazon. For fine filtering, a new framework for Entity Alignment, Relation-aware and Attribute-aware Graph Attention Networks for Entity Alignment (RAEA), is employed. RAEA focuses on the interactions between attribute triples and relation triples, where the entity representation aggregates the alignment signals from attributes and relations with Attribute-aware Entity Encoder and Relation-aware Graph Attention Networks. The experimental results indicate that the RAEA model achieves significant improvements over 12 baselines on EA task in the cross-lingual dataset DBP15K (6.59% on average Hits@1) and delivers competitive results in the monolingual dataset DWY100K. The source code for experiments on DBP15K and DWY100K is available at github (https://github.com/Mockingjay-liu/RAEA-model-for-Entity-Alignment).

