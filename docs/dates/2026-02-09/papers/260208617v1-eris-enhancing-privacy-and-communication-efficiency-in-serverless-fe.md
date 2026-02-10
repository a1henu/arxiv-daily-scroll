---
layout: default
title: ERIS: Enhancing Privacy and Communication Efficiency in Serverless Federated Learning
---

# ERIS: Enhancing Privacy and Communication Efficiency in Serverless Federated Learning
**arXiv**：[2602.08617v1](https://arxiv.org/abs/2602.08617) · [PDF](https://arxiv.org/pdf/2602.08617.pdf)  
**作者**：Dario Fenoglio, Pasquale Polverino, Jacopo Quizi, Martin Gjoreski, Marc Langheinrich  

**一句话要点**：提出ERIS框架以在无服务器联邦学习中平衡隐私与通信效率

**关键词**：联邦学习, 隐私保护, 通信效率, 无服务器架构, 梯度压缩, 模型分区

## 3 点简述
- 核心问题：大规模联邦学习面临通信效率、模型精度和隐私保护的权衡挑战
- 方法要点：结合模型分区策略和分布式梯度压缩机制，实现无服务器聚合
- 实验或效果：在图像和文本任务中达到FedAvg精度，降低通信成本并增强隐私

## 摘要（原文）

> Scaling federated learning (FL) to billion-parameter models introduces critical trade-offs between communication efficiency, model accuracy, and privacy guarantees. Existing solutions often tackle these challenges in isolation, sacrificing accuracy or relying on costly cryptographic tools. We propose ERIS, a serverless FL framework that balances privacy and accuracy while eliminating the server bottleneck and distributing the communication load. ERIS combines a model partitioning strategy, distributing aggregation across multiple client-side aggregators, with a distributed shifted gradient compression mechanism. We theoretically prove that ERIS (i) converges at the same rate as FedAvg under standard assumptions, and (ii) bounds mutual information leakage inversely with the number of aggregators, enabling strong privacy guarantees with no accuracy degradation. Experiments across image and text tasks, including large language models, confirm that ERIS achieves FedAvg-level accuracy while substantially reducing communication cost and improving robustness to membership inference and reconstruction attacks, without relying on heavy cryptography or noise injection.

