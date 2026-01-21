---
layout: default
title: ELSA: Efficient LLM-Centric Split Aggregation for Privacy-Aware Hierarchical Federated Learning over Resource-Constrained Edge Networks
---

# ELSA: Efficient LLM-Centric Split Aggregation for Privacy-Aware Hierarchical Federated Learning over Resource-Constrained Edge Networks
**arXiv**：[2601.13824v1](https://arxiv.org/abs/2601.13824) · [PDF](https://arxiv.org/pdf/2601.13824.pdf)  
**作者**：Xiaohong Yang, Tong Xie, Minghui Liwang, Chikai Shang, Yang Lu, Zhenzhen Jiao, Liqun Fu, Seyyedali Hosseinalipour  

**一句话要点**：提出ELSA框架，通过集成分割学习与分层联邦学习，解决资源受限边缘网络中LLM微调的数据异构、隐私与通信挑战。

**关键词**：分层联邦学习, 分割学习, 边缘计算, 隐私保护, 大语言模型微调, 资源受限网络

## 3 点简述
- 核心问题：边缘设备资源有限、数据异构严重、隐私风险高，阻碍LLM在边缘网络的分布式微调。
- 方法要点：采用任务无关的行为感知客户端聚类、LLM三部分分割部署、轻量通信方案结合语义子空间正交扰动。
- 实验或效果：在多种NLP任务中，ELSA在适应性、收敛行为和鲁棒性方面优于现有方法，实现可扩展的隐私感知解决方案。

## 摘要（原文）

> Training large language models (LLMs) at the network edge faces fundamental challenges arising from device resource constraints, severe data heterogeneity, and heightened privacy risks. To address these, we propose ELSA (Efficient LLM-centric Split Aggregation), a novel framework that systematically integrates split learning (SL) and hierarchical federated learning (HFL) for distributed LLM fine-tuning over resource-constrained edge networks. ELSA introduces three key innovations. First, it employs a task-agnostic, behavior-aware client clustering mechanism that constructs semantic fingerprints using public probe inputs and symmetric KL divergence, further enhanced by prediction-consistency-based trust scoring and latency-aware edge assignment to jointly address data heterogeneity, client unreliability, and communication constraints. Second, it splits the LLM into three parts across clients and edge servers, with the cloud used only for adapter aggregation, enabling an effective balance between on-device computation cost and global convergence stability. Third, it incorporates a lightweight communication scheme based on computational sketches combined with semantic subspace orthogonal perturbation (SS-OP) to reduce communication overhead while mitigating privacy leakage during model exchanges. Experiments across diverse NLP tasks demonstrate that ELSA consistently outperforms state-of-the-art methods in terms of adaptability, convergence behavior, and robustness, establishing a scalable and privacy-aware solution for edge-side LLM fine-tuning under resource constraints.

