---
layout: default
title: Robust Spiking Neural Networks Against Adversarial Attacks
---

# Robust Spiking Neural Networks Against Adversarial Attacks
**arXiv**：[2602.20548v1](https://arxiv.org/abs/2602.20548) · [PDF](https://arxiv.org/pdf/2602.20548.pdf)  
**作者**：Shuai Wang, Malu Zhang, Yulin Jiang, Dehao Zhang, Ammar Belatreche, Yu Liang, Yimeng Shan, Zijian Zhou, Yang Yang, Haizhou Li  

**一句话要点**：提出阈值守卫优化方法以增强脉冲神经网络在对抗攻击下的鲁棒性

**关键词**：脉冲神经网络, 对抗攻击, 鲁棒性优化, 阈值守卫, 噪声神经元, 神经形态计算

## 3 点简述
- 核心问题：阈值邻近脉冲神经元是直接训练SNN鲁棒性受限的关键因素，易受微小扰动翻转状态
- 方法要点：通过损失函数约束使膜电位远离阈值，并引入噪声神经元将放电机制从确定性转为概率性
- 实验或效果：在标准对抗场景中验证，该方法显著提升直接训练SNN的鲁棒性

## 摘要（原文）

> Spiking Neural Networks (SNNs) represent a promising paradigm for energy-efficient neuromorphic computing due to their bio-plausible and spike-driven characteristics. However, the robustness of SNNs in complex adversarial environments remains significantly constrained. In this study, we theoretically demonstrate that those threshold-neighboring spiking neurons are the key factors limiting the robustness of directly trained SNNs. We find that these neurons set the upper limits for the maximum potential strength of adversarial attacks and are prone to state-flipping under minor disturbances. To address this challenge, we propose a Threshold Guarding Optimization (TGO) method, which comprises two key aspects. First, we incorporate additional constraints into the loss function to move neurons' membrane potentials away from their thresholds. It increases SNNs' gradient sparsity, thereby reducing the theoretical upper bound of adversarial attacks. Second, we introduce noisy spiking neurons to transition the neuronal firing mechanism from deterministic to probabilistic, decreasing their state-flipping probability due to minor disturbances. Extensive experiments conducted in standard adversarial scenarios prove that our method significantly enhances the robustness of directly trained SNNs. These findings pave the way for advancing more reliable and secure neuromorphic computing in real-world applications.

