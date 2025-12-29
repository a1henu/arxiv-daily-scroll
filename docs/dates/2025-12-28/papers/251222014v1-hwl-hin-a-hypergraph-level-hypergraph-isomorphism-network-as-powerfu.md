---
layout: default
title: HWL-HIN: A Hypergraph-Level Hypergraph Isomorphism Network as Powerful as the Hypergraph Weisfeiler-Lehman Test with Application to Higher-Order Network Robustness
---

# HWL-HIN: A Hypergraph-Level Hypergraph Isomorphism Network as Powerful as the Hypergraph Weisfeiler-Lehman Test with Application to Higher-Order Network Robustness
**arXiv**：[2512.22014v1](https://arxiv.org/abs/2512.22014) · [PDF](https://arxiv.org/pdf/2512.22014.pdf)  
**作者**：Chengyu Tian, Wenbin Pei  

**一句话要点**：提出超图级超图同构网络，以提升超图拓扑表达能力并应用于高阶网络鲁棒性预测。

**关键词**：超图神经网络, 拓扑表达能力, 高阶网络鲁棒性, 超图同构网络, Weisfeiler-Lehman测试

## 3 点简述
- 核心问题：现有超图神经网络拓扑表达能力未达理论上限，无法有效处理高阶相关性。
- 方法要点：受图同构网络启发，设计超图级超图同构网络，理论证明其表达能力等价于超图Weisfeiler-Lehman测试。
- 实验或效果：在训练和预测效率优越的同时，在拓扑结构表示任务中显著超越现有图模型和传统超图神经网络。

## 摘要（原文）

> Robustness in complex systems is of significant engineering and economic importance. However, conventional attack-based a posteriori robustness assessments incur prohibitive computational overhead. Recently, deep learning methods, such as Convolutional Neural Networks (CNNs) and Graph Neural Networks (GNNs), have been widely employed as surrogates for rapid robustness prediction. Nevertheless, these methods neglect the complex higher-order correlations prevalent in real-world systems, which are naturally modeled as hypergraphs. Although Hypergraph Neural Networks (HGNNs) have been widely adopted for hypergraph learning, their topological expressive power has not yet reached the theoretical upper bound. To address this limitation, inspired by Graph Isomorphism Networks, this paper proposes a hypergraph-level Hypergraph Isomorphism Network framework. Theoretically, this approach is proven to possess an expressive power strictly equivalent to the Hypergraph Weisfeiler-Lehman test and is applied to predict hypergraph robustness. Experimental results demonstrate that while maintaining superior efficiency in training and prediction, the proposed method not only outperforms existing graph-based models but also significantly surpasses conventional HGNNs in tasks that prioritize topological structure representation.

