---
layout: default
title: Deontic Knowledge Graphs for Privacy Compliance in Multimodal Disaster Data Sharing
---

# Deontic Knowledge Graphs for Privacy Compliance in Multimodal Disaster Data Sharing
**arXiv**：[2601.03587v1](https://arxiv.org/abs/2601.03587) · [PDF](https://arxiv.org/pdf/2601.03587.pdf)  
**作者**：Kelvin Uzoma Echenim, Karuna Pande Joshi  

**一句话要点**：提出基于道义知识图谱的框架，以解决多模态灾害数据共享中的隐私合规问题。

**关键词**：知识图谱, 隐私合规, 多模态数据, 灾害管理, 访问控制, 语义推理

## 3 点简述
- 核心问题：灾害响应中多模态数据共享面临重叠隐私法规，现有访问控制脆弱且不灵活。
- 方法要点：集成灾害管理知识图谱与政策知识图谱，支持允许、阻止和允许-转换三种决策。
- 实验或效果：在5.1M三元组数据集上验证决策正确性、亚秒级延迟和交互查询性能。

## 摘要（原文）

> Disaster response requires sharing heterogeneous artifacts, from tabular assistance records to UAS imagery, under overlapping privacy mandates. Operational systems often reduce compliance to binary access control, which is brittle in time-critical workflows. We present a novel deontic knowledge graph-based framework that integrates a Disaster Management Knowledge Graph (DKG) with a Policy Knowledge Graph (PKG) derived from IoT-Reg and FEMA/DHS privacy drivers. Our release decision function supports three outcomes: Allow, Block, and Allow-with-Transform. The latter binds obligations to transforms and verifies post-transform compliance via provenance-linked derived artifacts; blocked requests are logged as semantic privacy incidents. Evaluation on a 5.1M-triple DKG with 316K images shows exact-match decision correctness, sub-second per-decision latency, and interactive query performance across both single-graph and federated workloads.

