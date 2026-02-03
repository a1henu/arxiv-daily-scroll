---
layout: default
title: Decoupling Generalizability and Membership Privacy Risks in Neural Networks
---

# Decoupling Generalizability and Membership Privacy Risks in Neural Networks
**arXiv**：[2602.02296v1](https://arxiv.org/abs/2602.02296) · [PDF](https://arxiv.org/pdf/2602.02296.pdf)  
**作者**：Xingli Fang, Jung-Eun Kim  

**一句话要点**：提出隐私保护训练原则以解耦神经网络泛化性与成员隐私风险

**关键词**：隐私保护, 神经网络泛化性, 成员隐私风险, 解耦训练, 深度学习安全

## 3 点简述
- 核心问题：深度学习模型在隐私保护与泛化性之间存在权衡关系，损失差异暗示解耦潜力
- 方法要点：基于泛化与隐私风险在神经网络架构中分布不同的观察，设计PPTP保护模型组件
- 实验或效果：评估显示PPTP在增强隐私保护的同时显著保持模型泛化性

## 摘要（原文）

> A deep learning model usually has to sacrifice some utilities when it acquires some other abilities or characteristics. Privacy preservation has such trade-off relationships with utilities. The loss disparity between various defense approaches implies the potential to decouple generalizability and privacy risks to maximize privacy gain. In this paper, we identify that the model's generalization and privacy risks exist in different regions in deep neural network architectures. Based on the observations that we investigate, we propose Privacy-Preserving Training Principle (PPTP) to protect model components from privacy risks while minimizing the loss in generalizability. Through extensive evaluations, our approach shows significantly better maintenance in model generalizability while enhancing privacy preservation.

