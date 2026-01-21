---
layout: default
title: Variational Dual-path Attention Network for CSI-Based Gesture Recognition
---

# Variational Dual-path Attention Network for CSI-Based Gesture Recognition
**arXiv**：[2601.13745v1](https://arxiv.org/abs/2601.13745) · [PDF](https://arxiv.org/pdf/2601.13745.pdf)  
**作者**：N. Zhang  

**一句话要点**：提出变分双路径注意力网络，用于基于CSI的手势识别，以解决噪声和资源约束问题。

**关键词**：Wi-Fi手势识别, 信道状态信息, 变分推理, 注意力机制, 轻量级网络, 可解释性

## 3 点简述
- 核心问题：基于CSI的手势识别面临高维噪声和边缘设备资源限制，现有端到端模型忽略时间-频率稀疏性，导致冗余和泛化差。
- 方法要点：设计轻量级特征预处理模块VDAN，通过频域滤波和时域检测进行结构化特征精炼，引入变分推理建模注意力权重不确定性以增强鲁棒性。
- 实验或效果：在公共数据集上验证，学习到的注意力权重与CSI物理稀疏特性对齐，证明其可解释性和高效性。

## 摘要（原文）

> Wi-Fi gesture recognition based on Channel State Information (CSI) is challenged by high-dimensional noise and resource constraints on edge devices. Prevailing end-to-end models tightly couple feature extraction with classification, overlooking the inherent time-frequency sparsity of CSI and leading to redundancy and poor generalization. To address this, this paper proposes a lightweight feature preprocessing module--the Variational Dual-path Attention Network (VDAN). It performs structured feature refinement through frequency-domain filtering and temporal detection. Variational inference is introduced to model the uncertainty in attention weights, thereby enhancing robustness to noise. The design principles of the module are explained from the perspectives of the information bottleneck and regularization. Experiments on a public dataset demonstrate that the learned attention weights align with the physical sparse characteristics of CSI, verifying its interpretability. This work provides an efficient and explainable front-end processing solution for resource-constrained wireless sensing systems.

