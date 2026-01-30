---
layout: default
title: Transferable Graph Condensation from the Causal Perspective
---

# Transferable Graph Condensation from the Causal Perspective
**arXiv**：[2601.21309v1](https://arxiv.org/abs/2601.21309) · [PDF](https://arxiv.org/pdf/2601.21309.pdf)  
**作者**：Huaming Du, Yijie Huang, Su Yao, Yiying Wang, Yueyang Zhou, Jingwen Yang, Jinshi Zhang, Han Ji, Yu Zhao, Guisong Liu, Hegui Zhang, Carl Yang, Gang Kou  

**一句话要点**：提出因果不变性图数据集压缩方法TGCC，以提升跨任务和跨域场景下的可迁移性。

**关键词**：图数据集压缩, 因果不变性, 可迁移学习, 图表示学习, 跨域场景

## 3 点简述
- 核心问题：现有图数据集压缩方法在跨任务和跨域场景中可迁移性不足。
- 方法要点：通过因果干预提取空间域不变特征，结合增强压缩和谱域对比学习注入因果信息。
- 实验或效果：在6个数据集上验证，跨场景性能提升达13.41%，单场景5个数据集达到最优。

## 摘要（原文）

> The increasing scale of graph datasets has significantly improved the performance of graph representation learning methods, but it has also introduced substantial training challenges. Graph dataset condensation techniques have emerged to compress large datasets into smaller yet information-rich datasets, while maintaining similar test performance. However, these methods strictly require downstream applications to match the original dataset and task, which often fails in cross-task and cross-domain scenarios. To address these challenges, we propose a novel causal-invariance-based and transferable graph dataset condensation method, named \textbf{TGCC}, providing effective and transferable condensed datasets. Specifically, to preserve domain-invariant knowledge, we first extract domain causal-invariant features from the spatial domain of the graph using causal interventions. Then, to fully capture the structural and feature information of the original graph, we perform enhanced condensation operations. Finally, through spectral-domain enhanced contrastive learning, we inject the causal-invariant features into the condensed graph, ensuring that the compressed graph retains the causal information of the original graph. Experimental results on five public datasets and our novel \textbf{FinReport} dataset demonstrate that TGCC achieves up to a 13.41\% improvement in cross-task and cross-domain complex scenarios compared to existing methods, and achieves state-of-the-art performance on 5 out of 6 datasets in the single dataset and task scenario.

