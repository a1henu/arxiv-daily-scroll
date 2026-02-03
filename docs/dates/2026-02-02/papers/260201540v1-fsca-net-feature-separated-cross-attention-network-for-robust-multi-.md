---
layout: default
title: FSCA-Net: Feature-Separated Cross-Attention Network for Robust Multi-Dataset Training
---

# FSCA-Net: Feature-Separated Cross-Attention Network for Robust Multi-Dataset Training
**arXiv**：[2602.01540v1](https://arxiv.org/abs/2602.01540) · [PDF](https://arxiv.org/pdf/2602.01540.pdf)  
**作者**：Yuehai Chen  

**一句话要点**：提出FSCA-Net以解决人群计数中多数据集训练时的负迁移问题

**关键词**：人群计数, 多数据集训练, 特征解耦, 交叉注意力, 域泛化, 负迁移缓解

## 3 点简述
- 核心问题：多数据集联合训练导致特征纠缠和负迁移，影响跨域泛化能力
- 方法要点：通过特征分离和交叉注意力模块，解耦域不变与域特定特征，并优化互信息
- 实验或效果：在多个基准测试中有效缓解负迁移，实现先进的跨数据集泛化性能

## 摘要（原文）

> Crowd counting plays a vital role in public safety, traffic regulation, and smart city management. However, despite the impressive progress achieved by CNN- and Transformer-based models, their performance often deteriorates when applied across diverse environments due to severe domain discrepancies. Direct joint training on multiple datasets, which intuitively should enhance generalization, instead results in negative transfer, as shared and domain-specific representations become entangled. To address this challenge, we propose the Feature Separation and Cross-Attention Network FSCA-Net, a unified framework that explicitly disentangles feature representations into domain-invariant and domain-specific components. A novel cross-attention fusion module adaptively models interactions between these components, ensuring effective knowledge transfer while preserving dataset-specific discriminability. Furthermore, a mutual information optimization objective is introduced to maximize consistency among domain-invariant features and minimize redundancy among domain-specific ones, promoting complementary shared-private representations. Extensive experiments on multiple crowd counting benchmarks demonstrate that FSCA-Net effectively mitigates negative transfer and achieves state-of-the-art cross-dataset generalization, providing a robust and scalable solution for real-world crowd analysis.

