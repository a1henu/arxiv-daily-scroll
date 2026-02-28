---
layout: default
title: Mitigating Membership Inference in Intermediate Representations via Layer-wise MIA-risk-aware DP-SGD
---

# Mitigating Membership Inference in Intermediate Representations via Layer-wise MIA-risk-aware DP-SGD
**arXiv**：[2602.22611v1](https://arxiv.org/abs/2602.22611) · [PDF](https://arxiv.org/pdf/2602.22611.pdf)  
**作者**：Jiayang Meng, Tao Huang, Chen Hou, Guolong Zheng, Hong Chen  

**一句话要点**：提出层间MIA风险感知的DP-SGD以缓解嵌入即接口场景中的中间表示成员推理攻击

**关键词**：成员推理攻击, 差分隐私SGD, 中间表示, 层间风险感知, 隐私-效用权衡, 嵌入即接口

## 3 点简述
- 核心问题：中间表示分布特性泄露训练集成员信号，现有DP-SGD忽略层间MIA风险异质性。
- 方法要点：基于影子模型估计层间MIA风险，自适应分配隐私保护，重加权梯度贡献。
- 实验或效果：相同隐私预算下降低峰值MIA风险，保持效用，提升隐私-效用权衡。

## 摘要（原文）

> In Embedding-as-an-Interface (EaaI) settings, pre-trained models are queried for Intermediate Representations (IRs). The distributional properties of IRs can leak training-set membership signals, enabling Membership Inference Attacks (MIAs) whose strength varies across layers. Although Differentially Private Stochastic Gradient Descent (DP-SGD) mitigates such leakage, existing implementations employ per-example gradient clipping and a uniform, layer-agnostic noise multiplier, ignoring heterogeneous layer-wise MIA vulnerability. This paper introduces Layer-wise MIA-risk-aware DP-SGD (LM-DP-SGD), which adaptively allocates privacy protection across layers in proportion to their MIA risk. Specifically, LM-DP-SGD trains a shadow model on a public shadow dataset, extracts per-layer IRs from its train/test splits, and fits layer-specific MIA adversaries, using their attack error rates as MIA-risk estimates. Leveraging the cross-dataset transferability of MIAs, these estimates are then used to reweight each layer's contribution to the globally clipped gradient during private training, providing layer-appropriate protection under a fixed noise magnitude. We further establish theoretical guarantees on both privacy and convergence of LM-DP-SGD. Extensive experiments show that, under the same privacy budget, LM-DP-SGD reduces the peak IR-level MIA risk while preserving utility, yielding a superior privacy-utility trade-off.

