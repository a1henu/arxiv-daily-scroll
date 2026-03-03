---
layout: default
title: Pharmacology Knowledge Graphs: Do We Need Chemical Structure for Drug Repurposing?
---

# Pharmacology Knowledge Graphs: Do We Need Chemical Structure for Drug Repurposing?
**arXiv**：[2603.01537v1](https://arxiv.org/abs/2603.01537) · [PDF](https://arxiv.org/pdf/2603.01537.pdf)  
**作者**：Youssef Abo-Dahab, Ruby Hernandez, Ismael Caleb Arechiga Duran  

**一句话要点**：提出基于知识图谱的药物重定位方法，无需化学结构即可准确预测药理行为。

**关键词**：药物重定位, 知识图谱嵌入, 图神经网络, 药理学预测, 特征消融研究, 时间验证

## 3 点简述
- 核心问题：模型复杂度、数据量和特征模态对知识图谱药物重定位的影响未量化。
- 方法要点：构建药理学知识图谱，使用严格时间分割和生物验证负样本进行基准测试。
- 实验或效果：移除药物化学结构编码器提升性能，增加数据量持续改善结果，外部验证确认预测有效性。

## 摘要（原文）

> The contributions of model complexity, data volume, and feature modalities to knowledge graph-based drug repurposing remain poorly quantified under rigorous temporal validation. We constructed a pharmacology knowledge graph from ChEMBL 36 comprising 5,348 entities including 3,127 drugs, 1,156 proteins, and 1,065 indications. A strict temporal split was enforced with training data up to 2022 and testing data from 2023 to 2025, together with biologically verified hard negatives mined from failed assays and clinical trials. We benchmarked five knowledge graph embedding models and a standard graph neural network with 3.44 million parameters that incorporates drug chemical structure using a graph attention encoder and ESM-2 protein embeddings. Scaling experiments ranging from 0.78 to 9.75 million parameters and from 25 to 100 percent of the data, together with feature ablation studies, were used to isolate the contributions of model capacity, graph density, and node feature modalities. Removing the graph attention based drug structure encoder and retaining only topological embeddings combined with ESM-2 protein features improved drug protein PR-AUC from 0.5631 to 0.5785 while reducing VRAM usage from 5.30 GB to 353 MB. Replacing the drug encoder with Morgan fingerprints further degraded performance, indicating that explicit chemical structure representations can be detrimental for predicting pharmacological network interactions. Increasing model size beyond 2.44 million parameters yielded diminishing returns, whereas increasing training data consistently improved performance. External validation confirmed 6 of the top 14 novel predictions as established therapeutic indications. These results show that drug pharmacological behavior can be accurately predicted using target-centric information and drug network topology alone, without requiring explicit chemical structure representations.

