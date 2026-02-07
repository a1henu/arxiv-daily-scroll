---
layout: default
title: THOR: Inductive Link Prediction over Hyper-Relational Knowledge Graphs
---

# THOR: Inductive Link Prediction over Hyper-Relational Knowledge Graphs
**arXiv**：[2602.05424v1](https://arxiv.org/abs/2602.05424) · [PDF](https://arxiv.org/pdf/2602.05424.pdf)  
**作者**：Weijian Yu, Yuhuan Lu, Dingqi Yang  

**一句话要点**：提出THOR以解决超关系知识图谱的归纳链接预测问题

**关键词**：超关系知识图谱, 归纳链接预测, 图神经网络, Transformer, 结构不变性

## 3 点简述
- 核心问题：现有超关系知识图谱链接预测方法多为转导式，无法泛化到未见词汇。
- 方法要点：引入关系和实体基础图，通过图编码器和Transformer解码器学习结构不变性。
- 实验或效果：在12个数据集上评估，THOR优于基线，提升达66.1%、55.9%和20.4%。

## 摘要（原文）

> Knowledge graphs (KGs) have become a key ingredient supporting a variety of applications. Beyond the traditional triplet representation of facts where a relation connects two entities, modern KGs observe an increasing number of hyper-relational facts, where an arbitrary number of qualifiers associated with a triplet provide auxiliary information to further describe the rich semantics of the triplet, which can effectively boost the reasoning performance in link prediction tasks. However, existing link prediction techniques over such hyper-relational KGs (HKGs) mostly focus on a transductive setting, where KG embedding models are learned from the specific vocabulary of a given KG and subsequently can only make predictions within the same vocabulary, limiting their generalizability to previously unseen vocabularies. Against this background, we propose THOR, an inducTive link prediction technique for Hyper-relational knOwledge gRaphs. Specifically, we first introduce both relation and entity foundation graphs, modeling their fundamental inter- and intra-fact interactions in HKGs, which are agnostic to any specific relations and entities. Afterward, THOR is designed to learn from the two foundation graphs with two parallel graph encoders followed by a transformer decoder, which supports efficient masked training and fully-inductive inference. We conduct a thorough evaluation of THOR in hyper-relational link prediction tasks on 12 datasets with different settings. Results show that THOR outperforms a sizable collection of baselines, yielding 66.1%, 55.9%, and 20.4% improvement over the best-performing rule-based, semi-inductive, and fully-inductive techniques, respectively. A series of ablation studies also reveals our key design factors capturing the structural invariance transferable across HKGs for inductive tasks.

