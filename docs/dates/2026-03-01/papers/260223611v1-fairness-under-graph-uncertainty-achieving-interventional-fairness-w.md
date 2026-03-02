---
layout: default
title: Fairness under Graph Uncertainty: Achieving Interventional Fairness with Partially Known Causal Graphs over Clusters of Variables
---

# Fairness under Graph Uncertainty: Achieving Interventional Fairness with Partially Known Causal Graphs over Clusters of Variables
**arXiv**：[2602.23611v1](https://arxiv.org/abs/2602.23611) · [PDF](https://arxiv.org/pdf/2602.23611.pdf)  
**作者**：Yoichi Chikahara  

**一句话要点**：提出基于变量簇因果图的干预公平学习框架，以解决因果图知识有限下的公平预测问题。

**关键词**：因果公平, 干预公平, 变量簇因果图, 最大均值差异, 公平机器学习, 算法公平性

## 3 点简述
- 核心问题：因果公平方法通常依赖详细因果图，实践中难以获取，导致公平性受限。
- 方法要点：利用变量簇因果图识别调整簇集，通过最小化干预分布差异训练模型，实现干预公平。
- 实验或效果：实验显示，在公平性与准确性平衡上优于现有方法，适用于因果图知识有限场景。

## 摘要（原文）

> Algorithmic decisions about individuals require predictions that are not only accurate but also fair with respect to sensitive attributes such as gender and race. Causal notions of fairness align with legal requirements, yet many methods assume access to detailed knowledge of the underlying causal graph, which is a demanding assumption in practice. We propose a learning framework that achieves interventional fairness by leveraging a causal graph over \textit{clusters of variables}, which is substantially easier to estimate than a variable-level graph. With possible \textit{adjustment cluster sets} identified from such a cluster causal graph, our framework trains a prediction model by reducing the worst-case discrepancy between interventional distributions across these sets. To this end, we develop a computationally efficient barycenter kernel maximum mean discrepancy (MMD) that scales favorably with the number of sensitive attribute values. Extensive experiments show that our framework strikes a better balance between fairness and accuracy than existing approaches, highlighting its effectiveness under limited causal graph knowledge.

