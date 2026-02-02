---
layout: default
title: Non-Intrusive Graph-Based Bot Detection for E-Commerce Using Inductive Graph Neural Networks
---

# Non-Intrusive Graph-Based Bot Detection for E-Commerce Using Inductive Graph Neural Networks
**arXiv**：[2601.22579v1](https://arxiv.org/abs/2601.22579) · [PDF](https://arxiv.org/pdf/2601.22579.pdf)  
**作者**：Sichen Zhao, Zhiming Xue, Yalun Qi, Xianling Zeng, Zihan Yu  

**一句话要点**：提出基于归纳图神经网络的非侵入式图模型，用于电商平台恶意机器人检测。

**关键词**：机器人检测, 图神经网络, 电商安全, 归纳学习, 非侵入式检测

## 3 点简述
- 核心问题：传统机器人检测方法如IP黑名单和验证码，因代理和AI规避策略而效果不佳或侵入性强。
- 方法要点：通过图表示建模用户会话行为，应用归纳图神经网络捕获关系结构和行为语义，实现非侵入式检测。
- 实验或效果：在真实电商流量上，模型在AUC和F1分数上优于会话级多层感知器基线，并展示对抗扰动和冷启动下的鲁棒性。

## 摘要（原文）

> Malicious bots pose a growing threat to e-commerce platforms by scraping data, hoarding inventory, and perpetrating fraud. Traditional bot mitigation techniques, including IP blacklists and CAPTCHA-based challenges, are increasingly ineffective or intrusive, as modern bots leverage proxies, botnets, and AI-assisted evasion strategies. This work proposes a non-intrusive graph-based bot detection framework for e-commerce that models user session behavior through a graph representation and applies an inductive graph neural network for classification. The approach captures both relational structure and behavioral semantics, enabling accurate identification of subtle automated activity that evades feature-based methods. Experiments on real-world e-commerce traffic demonstrate that the proposed inductive graph model outperforms a strong session-level multilayer perceptron baseline in terms of AUC and F1 score. Additional adversarial perturbation and cold-start simulations show that the model remains robust under moderate graph modifications and generalizes effectively to previously unseen sessions and URLs. The proposed framework is deployment-friendly, integrates with existing systems without client-side instrumentation, and supports real-time inference and incremental updates, making it suitable for practical e-commerce security deployments.

