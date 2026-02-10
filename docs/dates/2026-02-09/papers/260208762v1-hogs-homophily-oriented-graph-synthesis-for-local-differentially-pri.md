---
layout: default
title: HoGS: Homophily-Oriented Graph Synthesis for Local Differentially Private GNN Training
---

# HoGS: Homophily-Oriented Graph Synthesis for Local Differentially Private GNN Training
**arXiv**：[2602.08762v1](https://arxiv.org/abs/2602.08762) · [PDF](https://arxiv.org/pdf/2602.08762.pdf)  
**作者**：Wen Xu, Zhetao Li, Yong Xiao, Pengpeng Qiao, Mianxiong Dong, Kaoru Ota  

**一句话要点**：提出HoGS框架，通过同质性导向的图合成实现本地差分隐私下的GNN训练

**关键词**：图神经网络, 本地差分隐私, 图合成, 同质性, 隐私保护, 图数据

## 3 点简述
- 问题：现有本地差分隐私GNN方法在保护链接和节点特征隐私时，存在效用损失大或仅保护链接的问题。
- 方法：HoGS在LDP下收集图信息，利用同质性现象分别重构图结构和节点特征，生成合成图用于GNN训练。
- 效果：在三个真实数据集上，HoGS显著优于基线方法，提升了GNN训练准确性。

## 摘要（原文）

> Graph neural networks (GNNs) have demonstrated remarkable performance in various graph-based machine learning tasks by effectively modeling high-order interactions between nodes. However, training GNNs without protection may leak sensitive personal information in graph data, including links and node features. Local differential privacy (LDP) is an advanced technique for protecting data privacy in decentralized networks. Unfortunately, existing local differentially private GNNs either only preserve link privacy or suffer significant utility loss in the process of preserving link and node feature privacy. In this paper, we propose an effective LDP framework, called HoGS, which trains GNNs with link and feature protection by generating a synthetic graph. Concretely, HoGS first collects the link and feature information of the graph under LDP, and then utilizes the phenomenon of homophily in graph data to reconstruct the graph structure and node features separately, thereby effectively mitigating the negative impact of LDP on the downstream GNN training. We theoretically analyze the privacy guarantee of HoGS and conduct experiments using the generated synthetic graph as input to various state-of-the-art GNN architectures. Experimental results on three real-world datasets show that HoGS significantly outperforms baseline methods in the accuracy of training GNNs.

