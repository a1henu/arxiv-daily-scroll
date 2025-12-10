---
layout: default
title: Can TabPFN Compete with GNNs for Node Classification via Graph Tabularization?
---

# Can TabPFN Compete with GNNs for Node Classification via Graph Tabularization?
**arXiv**：[2512.08798v1](https://arxiv.org/abs/2512.08798) · [PDF](https://arxiv.org/pdf/2512.08798.pdf)  
**作者**：Jeongwhan Choi, Woosung Kang, Minseo Kim, Jongwoo Kim, Noseong Park  

**一句话要点**：提出TabPFN-GN将图数据表格化，用于节点分类，无需图特定训练或语言模型依赖。

**关键词**：图节点分类, 表格化学习, 基础模型, 异配图, 特征工程, 零样本泛化

## 3 点简述
- 研究图节点分类能否通过表格学习有效解决，利用TabPFN基础模型。
- 方法提取节点属性、结构特征等，将图数据转换为表格形式进行直接分类。
- 实验显示在异配图上性能优于GNN，同配图上竞争，提供图学习新替代方案。

## 摘要（原文）

> Foundation models pretrained on large data have demonstrated remarkable zero-shot generalization capabilities across domains. Building on the success of TabPFN for tabular data and its recent extension to time series, we investigate whether graph node classification can be effectively reformulated as a tabular learning problem. We introduce TabPFN-GN, which transforms graph data into tabular features by extracting node attributes, structural properties, positional encodings, and optionally smoothed neighborhood features. This enables TabPFN to perform direct node classification without any graph-specific training or language model dependencies. Our experiments on 12 benchmark datasets reveal that TabPFN-GN achieves competitive performance with GNNs on homophilous graphs and consistently outperforms them on heterophilous graphs. These results demonstrate that principled feature engineering can bridge the gap between tabular and graph domains, providing a practical alternative to task-specific GNN training and LLM-dependent graph foundation models.

