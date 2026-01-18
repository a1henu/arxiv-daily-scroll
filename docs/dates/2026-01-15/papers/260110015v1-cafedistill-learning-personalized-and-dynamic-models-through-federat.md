---
layout: default
title: CAFEDistill: Learning Personalized and Dynamic Models through Federated Early-Exit Network Distillation
---

# CAFEDistill: Learning Personalized and Dynamic Models through Federated Early-Exit Network Distillation
**arXiv**：[2601.10015v1](https://arxiv.org/abs/2601.10015) · [PDF](https://arxiv.org/pdf/2601.10015.pdf)  
**作者**：Boyi Liu, Zimu Zhou, Yongxin Tong  

**一句话要点**：提出CAFEDistill框架，通过联邦早期退出网络蒸馏解决个性化联邦学习中静态模型与动态推理需求的冲突。

**关键词**：个性化联邦学习, 早期退出网络, 知识蒸馏, 动态推理, 客户端异构性, 通信效率

## 3 点简述
- 核心问题：个性化联邦学习现有方法产生静态模型，无法适应动态推理需求，早期退出网络集成面临客户端异构性和深度干扰挑战。
- 方法要点：采用冲突感知的联邦退出蒸馏框架，通过深度优先的学生协调机制缓解干扰，实现跨客户端的个性化知识转移。
- 实验或效果：在评估中优于现有方法，提高准确性并减少30.79%-46.86%的推理成本。

## 摘要（原文）

> Personalized Federated Learning (PFL) enables collaboratively model training on decentralized, heterogeneous data while tailoring them to each client's unique distribution. However, existing PFL methods produce static models with a fixed tradeoff between accuracy and efficiency, limiting their applicability in environments where inference requirements vary with contexts and resource availability. Early-exit networks (EENs) offer adaptive inference by attaching intermediate classifiers. Yet integrating them into PFL is challenging due to client-wise heterogeneity and depth-wise interference arising from conflicting exit objectives. Prior studies fail to resolve both conflicts simultaneously, leading to suboptimal performance. In this paper, we propose CAFEDistill, a Conflict-Aware Federated Exit Distillation framework that jointly addresses these conflicts and extends PFL to early-exit networks. Through a progressive, depth-prioritized student coordination mechanism, CAFEDistill mitigates interference among shallow and deep exits while allowing effective personalized knowledge transfer across clients. Furthermore, it reduces communication overhead via a client-decoupled formulation. Extensive evaluations show that CAFEDistill outperforms the state-of-the-arts, achieving higher accuracy and reducing inference costs by 30.79%-46.86%.

