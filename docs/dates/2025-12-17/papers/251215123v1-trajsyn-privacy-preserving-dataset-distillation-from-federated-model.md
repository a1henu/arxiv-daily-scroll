---
layout: default
title: TrajSyn: Privacy-Preserving Dataset Distillation from Federated Model Trajectories for Server-Side Adversarial Training
---

# TrajSyn: Privacy-Preserving Dataset Distillation from Federated Model Trajectories for Server-Side Adversarial Training
**arXiv**：[2512.15123v1](https://arxiv.org/abs/2512.15123) · [PDF](https://arxiv.org/pdf/2512.15123.pdf)  
**作者**：Mukur Gupta, Niharika Gupta, Saifur Rahman, Shantanu Pal, Chandan Karmakar  

**一句话要点**：提出TrajSyn框架，通过联邦模型更新轨迹合成代理数据集，以在服务器端实现隐私保护的对抗训练。

**关键词**：联邦学习, 隐私保护, 对抗训练, 数据集蒸馏, 模型轨迹, 服务器端训练

## 3 点简述
- 核心问题：联邦学习中客户端数据隐私限制和边缘设备计算资源有限，难以进行对抗训练。
- 方法要点：从客户端模型更新轨迹中合成代理数据集，无需访问原始数据，支持服务器端对抗训练。
- 实验或效果：在图像分类基准上一致提升对抗鲁棒性，且不增加客户端计算负担。

## 摘要（原文）

> Deep learning models deployed on edge devices are increasingly used in safety-critical applications. However, their vulnerability to adversarial perturbations poses significant risks, especially in Federated Learning (FL) settings where identical models are distributed across thousands of clients. While adversarial training is a strong defense, it is difficult to apply in FL due to strict client-data privacy constraints and the limited compute available on edge devices. In this work, we introduce TrajSyn, a privacy-preserving framework that enables effective server-side adversarial training by synthesizing a proxy dataset from the trajectories of client model updates, without accessing raw client data. We show that TrajSyn consistently improves adversarial robustness on image classification benchmarks with no extra compute burden on the client device.

