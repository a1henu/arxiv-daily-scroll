---
layout: default
title: FairGE: Fairness-Aware Graph Encoding in Incomplete Social Networks
---

# FairGE: Fairness-Aware Graph Encoding in Incomplete Social Networks
**arXiv**：[2601.09394v1](https://arxiv.org/abs/2601.09394) · [PDF](https://arxiv.org/pdf/2601.09394.pdf)  
**作者**：Renqiang Luo, Huafei Huang, Tao Tang, Jing Ren, Ziqi Xu, Mingliang Hou, Enyan Dai, Feng Xia  

**一句话要点**：提出FairGE框架，通过谱图理论在不完整社交网络中实现公平感知的图编码。

**关键词**：图Transformer, 公平性学习, 社交网络分析, 谱图理论, 不完整数据

## 3 点简述
- 核心问题：图Transformer在不完整社交网络中部署时，因敏感属性缺失而面临公平性挑战。
- 方法要点：利用主特征向量编码结构信息，零填充缺失属性，避免数据重构以增强公平性。
- 实验或效果：在七个真实数据集上，统计均等和机会均等指标相比基线提升至少16%。

## 摘要（原文）

> Graph Transformers (GTs) are increasingly applied to social network analysis, yet their deployment is often constrained by fairness concerns. This issue is particularly critical in incomplete social networks, where sensitive attributes are frequently missing due to privacy and ethical restrictions. Existing solutions commonly generate these incomplete attributes, which may introduce additional biases and further compromise user privacy. To address this challenge, FairGE (Fair Graph Encoding) is introduced as a fairness-aware framework for GTs in incomplete social networks. Instead of generating sensitive attributes, FairGE encodes fairness directly through spectral graph theory. By leveraging the principal eigenvector to represent structural information and padding incomplete sensitive attributes with zeros to maintain independence, FairGE ensures fairness without data reconstruction. Theoretical analysis demonstrates that the method suppresses the influence of non-principal spectral components, thereby enhancing fairness. Extensive experiments on seven real-world social network datasets confirm that FairGE achieves at least a 16% improvement in both statistical parity and equality of opportunity compared with state-of-the-art baselines. The source code is shown in https://github.com/LuoRenqiang/FairGE.

