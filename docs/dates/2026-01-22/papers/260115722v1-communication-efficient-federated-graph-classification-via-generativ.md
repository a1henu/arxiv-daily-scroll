---
layout: default
title: Communication-efficient Federated Graph Classification via Generative Diffusion Modeling
---

# Communication-efficient Federated Graph Classification via Generative Diffusion Modeling
**arXiv**：[2601.15722v1](https://arxiv.org/abs/2601.15722) · [PDF](https://arxiv.org/pdf/2601.15722.pdf)  
**作者**：Xiuling Wang, Xin Huang, Haibo Hu, Jianliang Xu  

**一句话要点**：提出CeFGC以解决联邦图分类中通信开销高与非IID数据问题

**关键词**：联邦学习, 图神经网络, 生成扩散模型, 非IID数据, 通信效率, 图分类

## 3 点简述
- 核心问题：联邦图神经网络面临多轮参数交换的高通信开销和客户端间非IID数据分布挑战
- 方法要点：利用生成扩散模型捕获本地图分布，仅需三轮通信，通过合成图增强训练集
- 实验或效果：理论分析显示通信轮次降至常数，多数据集实验验证了在非IID图上的高效性和性能优势

## 摘要（原文）

> Graph Neural Networks (GNNs) unlock new ways of learning from graph-structured data, proving highly effective in capturing complex relationships and patterns. Federated GNNs (FGNNs) have emerged as a prominent distributed learning paradigm for training GNNs over decentralized data. However, FGNNs face two significant challenges: high communication overhead from multiple rounds of parameter exchanges and non-IID data characteristics across clients. To address these issues, we introduce CeFGC, a novel FGNN paradigm that facilitates efficient GNN training over non-IID data by limiting communication between the server and clients to three rounds only. The core idea of CeFGC is to leverage generative diffusion models to minimize direct client-server communication. Each client trains a generative diffusion model that captures its local graph distribution and shares this model with the server, which then redistributes it back to all clients. Using these generative models, clients generate synthetic graphs combined with their local graphs to train local GNN models. Finally, clients upload their model weights to the server for aggregation into a global GNN model. We theoretically analyze the I/O complexity of communication volume to show that CeFGC reduces to a constant of three communication rounds only. Extensive experiments on several real graph datasets demonstrate the effectiveness and efficiency of CeFGC against state-of-the-art competitors, reflecting our superior performance on non-IID graphs by aligning local and global model objectives and enriching the training set with diverse graphs.

