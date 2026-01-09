---
layout: default
title: Decentralized Privacy-Preserving Federal Learning of Computer Vision Models on Edge Devices
---

# Decentralized Privacy-Preserving Federal Learning of Computer Vision Models on Edge Devices
**arXiv**：[2601.04912v1](https://arxiv.org/abs/2601.04912) · [PDF](https://arxiv.org/pdf/2601.04912.pdf)  
**作者**：Damian Harenčák, Lukáš Gajdošech, Martin Madaras  

**一句话要点**：分析联邦学习中边缘设备上计算机视觉模型的去中心化隐私保护方法

**关键词**：联邦学习, 隐私保护, 边缘计算, 计算机视觉, 梯度压缩, 同态加密

## 3 点简述
- 核心问题：联邦学习中模型参数可能泄露客户端敏感数据，现有方法多假设服务器安全而忽略其他客户端恶意行为。
- 方法要点：评估同态加密、梯度压缩、梯度噪声等方法，并讨论分割学习等改进系统，以增强对服务器和其他客户端的隐私保护。
- 实验或效果：在NVIDIA Jetson TX2上实现概念验证，分析梯度压缩和噪声对卷积神经网络分类准确性的负面影响，并展示分割网络中数据重建的困难。

## 摘要（原文）

> Collaborative training of a machine learning model comes with a risk of sharing sensitive or private data. Federated learning offers a way of collectively training a single global model without the need to share client data, by sharing only the updated parameters from each client's local model. A central server is then used to aggregate parameters from all clients and redistribute the aggregated model back to the clients. Recent findings have shown that even in this scenario, private data can be reconstructed only using information about model parameters. Current efforts to mitigate this are mainly focused on reducing privacy risks on the server side, assuming that other clients will not act maliciously. In this work, we analyzed various methods for improving the privacy of client data concerning both the server and other clients for neural networks. Some of these methods include homomorphic encryption, gradient compression, gradient noising, and discussion on possible usage of modified federated learning systems such as split learning, swarm learning or fully encrypted models. We have analyzed the negative effects of gradient compression and gradient noising on the accuracy of convolutional neural networks used for classification. We have shown the difficulty of data reconstruction in the case of segmentation networks. We have also implemented a proof of concept on the NVIDIA Jetson TX2 module used in edge devices and simulated a federated learning process.

