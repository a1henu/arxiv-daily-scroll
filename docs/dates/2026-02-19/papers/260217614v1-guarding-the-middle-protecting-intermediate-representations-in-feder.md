---
layout: default
title: Guarding the Middle: Protecting Intermediate Representations in Federated Split Learning
---

# Guarding the Middle: Protecting Intermediate Representations in Federated Split Learning
**arXiv**：[2602.17614v1](https://arxiv.org/abs/2602.17614) · [PDF](https://arxiv.org/pdf/2602.17614.pdf)  
**作者**：Obaidullah Zaland, Sajib Mistry, Monowar Bhuyan  

**一句话要点**：提出KD-UFSL以保护联邦分割学习中的中间表示，平衡隐私与模型效用。

**关键词**：联邦学习, 分割学习, 差分隐私, 数据隐私保护, 中间表示安全, 大数据应用

## 3 点简述
- 核心问题：UFSL中客户端共享的中间表示易暴露私有数据，面临重构攻击风险。
- 方法要点：结合微聚合和差分隐私，设计k-匿名差分私有UFSL以最小化数据泄露。
- 实验或效果：在基准数据集上，显著增加重构误差和降低结构相似性，同时保持全局模型效用。

## 摘要（原文）

> Big data scenarios, where massive, heterogeneous datasets are distributed across clients, demand scalable, privacy-preserving learning methods. Federated learning (FL) enables decentralized training of machine learning (ML) models across clients without data centralization. Decentralized training, however, introduces a computational burden on client devices. U-shaped federated split learning (UFSL) offloads a fraction of the client computation to the server while keeping both data and labels on the clients' side. However, the intermediate representations (i.e., smashed data) shared by clients with the server are prone to exposing clients' private data. To reduce exposure of client data through intermediate data representations, this work proposes k-anonymous differentially private UFSL (KD-UFSL), which leverages privacy-enhancing techniques such as microaggregation and differential privacy to minimize data leakage from the smashed data transferred to the server. We first demonstrate that an adversary can access private client data from intermediate representations via a data-reconstruction attack, and then present a privacy-enhancing solution, KD-UFSL, to mitigate this risk. Our experiments indicate that, alongside increasing the mean squared error between the actual and reconstructed images by up to 50% in some cases, KD-UFSL also decreases the structural similarity between them by up to 40% on four benchmarking datasets. More importantly, KD-UFSL improves privacy while preserving the utility of the global model. This highlights its suitability for large-scale big data applications where privacy and utility must be balanced.

