---
layout: default
title: Hetero-SplitEE: Split Learning of Neural Networks with Early Exits for Heterogeneous IoT Devices
---

# Hetero-SplitEE: Split Learning of Neural Networks with Early Exits for Heterogeneous IoT Devices
**arXiv**：[2512.09313v1](https://arxiv.org/abs/2512.09313) · [PDF](https://arxiv.org/pdf/2512.09313.pdf)  
**作者**：Yuki Oda, Yuta Ono, Hiroshi Nakamura, Hideki Takase  

**一句话要点**：提出Hetero-SplitEE方法，通过异构早期退出支持异构物联网设备的分割学习

**关键词**：分割学习, 异构物联网, 早期退出, 协作训练, 神经网络训练

## 3 点简述
- 核心问题：现有分割学习假设设备同质，不适用于计算资源异构的物联网系统
- 方法要点：集成异构早期退出，允许客户端根据计算能力选择不同分割点，并提出顺序和平均两种协作训练策略
- 实验或效果：在CIFAR-10等数据集上验证，保持竞争性精度，高效支持多样计算约束

## 摘要（原文）

> The continuous scaling of deep neural networks has fundamentally transformed machine learning, with larger models demonstrating improved performance across diverse tasks. This growth in model size has dramatically increased the computational resources required for the training process. Consequently, distributed approaches, such as Federated Learning and Split Learning, have become essential paradigms for scalable deployment. However, existing Split Learning approaches assume client homogeneity and uniform split points across all participants. This critically limits their applicability to real-world IoT systems where devices exhibit heterogeneity in computational resources. To address this limitation, this paper proposes Hetero-SplitEE, a novel method that enables heterogeneous IoT devices to train a shared deep neural network in parallel collaboratively. By integrating heterogeneous early exits into hierarchical training, our approach allows each client to select distinct split points (cut layers) tailored to its computational capacity. In addition, we propose two cooperative training strategies, the Sequential strategy and the Averaging strategy, to facilitate this collaboration among clients with different split points. The Sequential strategy trains clients sequentially with a shared server model to reduce computational overhead. The Averaging strategy enables parallel client training with periodic cross-layer aggregation. Extensive experiments on CIFAR-10, CIFAR-100, and STL-10 datasets using ResNet-18 demonstrate that our method maintains competitive accuracy while efficiently supporting diverse computational constraints, enabling practical deployment of collaborative deep learning in heterogeneous IoT ecosystems.

