---
layout: default
title: Robust Federated Learning via Byzantine Filtering over Encrypted Updates
---

# Robust Federated Learning via Byzantine Filtering over Encrypted Updates
**arXiv**：[2602.05410v1](https://arxiv.org/abs/2602.05410) · [PDF](https://arxiv.org/pdf/2602.05410.pdf)  
**作者**：Adda Akram Bendoukha, Aymen Boudguiga, Nesrine Kaaniche, Renaud Sirdey, Didem Demirag, Sébastien Gambs  

**一句话要点**：提出基于同态加密与元分类器的拜占庭过滤方法，以解决联邦学习中隐私保护与拜占庭攻击的联合挑战。

**关键词**：联邦学习, 同态加密, 拜占庭鲁棒性, 元分类器, 隐私保护, 安全聚合

## 3 点简述
- 核心问题：联邦学习中隐私保护与拜占庭攻击并存，现有方案常独立处理，难以兼顾安全聚合与拜占庭鲁棒性。
- 方法要点：结合同态加密实现隐私保护聚合，利用属性推断攻击启发训练元分类器过滤拜占庭更新，并自动优化CKKS密码系统参数。
- 实验或效果：在多个基准测试中，SVM过滤识别拜占庭更新准确率达90%-94%，模型效用损失小，加密推理时间可控。

## 摘要（原文）

> Federated Learning (FL) aims to train a collaborative model while preserving data privacy. However, the distributed nature of this approach still raises privacy and security issues, such as the exposure of sensitive data due to inference attacks and the influence of Byzantine behaviors on the trained model. In particular, achieving both secure aggregation and Byzantine resilience remains challenging, as existing solutions often address these aspects independently. In this work, we propose to address these challenges through a novel approach that combines homomorphic encryption for privacy-preserving aggregation with property-inference-inspired meta-classifiers for Byzantine filtering. First, following the property-inference attacks blueprint, we train a set of filtering meta-classifiers on labeled shadow updates, reproducing a diverse ensemble of Byzantine misbehaviors in FL, including backdoor, gradient-inversion, label-flipping and shuffling attacks. The outputs of these meta-classifiers are then used to cancel the Byzantine encrypted updates by reweighting. Second, we propose an automated method for selecting the optimal kernel and the dimensionality hyperparameters with respect to homomorphic inference, aggregation constraints and efficiency over the CKKS cryptosystem. Finally, we demonstrate through extensive experiments the effectiveness of our approach against Byzantine participants on the FEMNIST, CIFAR10, GTSRB, and acsincome benchmarks. More precisely, our SVM filtering achieves accuracies between $90$% and $94$% for identifying Byzantine updates at the cost of marginal losses in model utility and encrypted inference runtimes ranging from $6$ to $24$ seconds and from $9$ to $26$ seconds for an overall aggregation.

