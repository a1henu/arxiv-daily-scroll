---
layout: default
title: ModalImmune: Immunity Driven Unlearning via Self Destructive Training
---

# ModalImmune: Immunity Driven Unlearning via Self Destructive Training
**arXiv**：[2602.16197v1](https://arxiv.org/abs/2602.16197) · [PDF](https://arxiv.org/pdf/2602.16197.pdf)  
**作者**：Rong Fu, Jia Yee Tan, Wenxin Zhang, Zijian Zhang, Ziming Wang, Zhaolu Kang, Muge Qi, Shuning Zhang, Simon Fong  

**一句话要点**：提出ModalImmune训练框架，通过可控模态崩溃增强多模态系统对输入通道丢失的鲁棒性。

**关键词**：多模态鲁棒性, 模态免疫训练, 可控崩溃正则化, 信息增益控制, 梯度掩码, 超梯度优化

## 3 点简述
- 核心问题：多模态系统在部署时易受部分或全部输入通道丢失影响，降低可靠性。
- 方法要点：结合崩溃正则化、信息增益控制器、梯度掩码和超梯度过程，实现可控模态信息崩溃训练。
- 实验或效果：在标准多模态基准上验证，提升对模态移除和损坏的韧性，保持收敛稳定性和重建能力。

## 摘要（原文）

> Multimodal systems are vulnerable to partial or complete loss of input channels at deployment, which undermines reliability in real-world settings. This paper presents ModalImmune, a training framework that enforces modality immunity by intentionally and controllably collapsing selected modality information during training so the model learns joint representations that are robust to destructive modality influence. The framework combines a spectrum-adaptive collapse regularizer, an information-gain guided controller for targeted interventions, curvature-aware gradient masking to stabilize destructive updates, and a certified Neumann-truncated hyper-gradient procedure for automatic meta-parameter adaptation. Empirical evaluation on standard multimodal benchmarks demonstrates that ModalImmune improves resilience to modality removal and corruption while retaining convergence stability and reconstruction capacity.

