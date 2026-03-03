---
layout: default
title: Revealing Combinatorial Reasoning of GNNs via Graph Concept Bottleneck Layer
---

# Revealing Combinatorial Reasoning of GNNs via Graph Concept Bottleneck Layer
**arXiv**：[2603.02025v1](https://arxiv.org/abs/2603.02025) · [PDF](https://arxiv.org/pdf/2603.02025.pdf)  
**作者**：Yue Niu, Zhaokai Sun, Jiayi Yang, Xiaofeng Cao, Rui Fan, Xin Sun, Hanli Wang, Wei Ye  

**一句话要点**：提出图概念瓶颈层以增强图神经网络的可解释性，量化概念贡献并提升分类性能。

**关键词**：图神经网络, 可解释性, 概念瓶颈, 组合推理, 语言模型嵌入

## 3 点简述
- 核心问题：图神经网络的黑盒特性隐藏了组合推理逻辑，现有方法仅揭示硬逻辑规则且为事后解释。
- 方法要点：集成图概念瓶颈层预测全局图概念，通过稀疏线性层映射到类别，并利用语言模型学习概念嵌入。
- 实验或效果：在多个数据集上实现分类和可解释性的最先进性能，验证方法的有效性。

## 摘要（原文）

> Despite their success in various domains, the growing dependence on GNNs raises a critical concern about the nature of the combinatorial reasoning underlying their predictions, which is often hidden within their black-box architectures. Addressing this challenge requires understanding how GNNs translate topological patterns into logical rules. However, current works only uncover the hard logical rules over graph concepts, which cannot quantify the contribution of each concept to prediction. Moreover, they are post-hoc interpretable methods that generate explanations after model training and may not accurately reflect the true combinatorial reasoning of GNNs, since they approximate it with a surrogate. In this work, we develop a graph concept bottleneck layer that can be integrated into any GNN architectures to guide them to predict the selected discriminative global graph concepts. The predicted concept scores are further projected to class labels by a sparse linear layer. It enforces the combinatorial reasoning of GNNs' predictions to fit the soft logical rule over graph concepts and thus can quantify the contribution of each concept. To further improve the quality of the concept bottleneck, we treat concepts as "graph words" and graphs as "graph sentences", and leverage language models to learn graph concept embeddings. Extensive experiments on multiple datasets show that our method GCBMs achieve state-of-the-art performance both in classification and interpretability.

