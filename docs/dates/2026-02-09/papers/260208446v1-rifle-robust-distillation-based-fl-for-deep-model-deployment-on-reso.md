---
layout: default
title: RIFLE: Robust Distillation-based FL for Deep Model Deployment on Resource-Constrained IoT Networks
---

# RIFLE: Robust Distillation-based FL for Deep Model Deployment on Resource-Constrained IoT Networks
**arXiv**：[2602.08446v1](https://arxiv.org/abs/2602.08446) · [PDF](https://arxiv.org/pdf/2602.08446.pdf)  
**作者**：Pouria Arefijamal, Mahdi Ahmadlou, Bardia Safaei, Jörg Henkel  

**一句话要点**：提出RIFLE框架，通过基于蒸馏的联邦学习在资源受限物联网中部署深度模型。

**关键词**：联邦学习, 知识蒸馏, 物联网部署, 非IID数据, 鲁棒性验证

## 3 点简述
- 核心问题：资源受限物联网中TinyML模型在非IID数据下性能不足，且面临恶意攻击挑战。
- 方法要点：采用基于logit的知识蒸馏替代梯度共享，结合KL散度验证客户端更新可靠性。
- 实验或效果：在MNIST等数据集上，RIFLE减少误检达87.5%，提升攻击缓解62.5%，准确率提高28.3%。

## 摘要（原文）

> Federated learning (FL) is a decentralized learning paradigm widely adopted in resource-constrained Internet of Things (IoT) environments. These devices, typically relying on TinyML models, collaboratively train global models by sharing gradients with a central server while preserving data privacy. However, as data heterogeneity and task complexity increase, TinyML models often become insufficient to capture intricate patterns, especially under extreme non-IID (non-independent and identically distributed) conditions. Moreover, ensuring robustness against malicious clients and poisoned updates remains a major challenge. Accordingly, this paper introduces RIFLE - a Robust, distillation-based Federated Learning framework that replaces gradient sharing with logit-based knowledge transfer. By leveraging a knowledge distillation aggregation scheme, RIFLE enables the training of deep models such as VGG-19 and Resnet18 within constrained IoT systems. Furthermore, a Kullback-Leibler (KL) divergence-based validation mechanism quantifies the reliability of client updates without exposing raw data, achieving high trust and privacy preservation simultaneously. Experiments on three benchmark datasets (MNIST, CIFAR-10, and CIFAR-100) under heterogeneous non-IID conditions demonstrate that RIFLE reduces false-positive detections by up to 87.5%, enhances poisoning attack mitigation by 62.5%, and achieves up to 28.3% higher accuracy compared to conventional federated learning baselines within only 10 rounds. Notably, RIFLE reduces VGG19 training time from over 600 days to just 1.39 hours on typical IoT devices (0.3 GFLOPS), making deep learning practical in resource-constrained networks.

