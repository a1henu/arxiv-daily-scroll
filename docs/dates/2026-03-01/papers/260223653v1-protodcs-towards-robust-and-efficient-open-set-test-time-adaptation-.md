---
layout: default
title: ProtoDCS: Towards Robust and Efficient Open-Set Test-Time Adaptation for Vision-Language Models
---

# ProtoDCS: Towards Robust and Efficient Open-Set Test-Time Adaptation for Vision-Language Models
**arXiv**：[2602.23653v1](https://arxiv.org/abs/2602.23653) · [PDF](https://arxiv.org/pdf/2602.23653.pdf)  
**作者**：Wei Luo, Yangfan Ou, Jin Deng, Zeshuai Deng, Xiquan Yan, Zhiquan Wen, Mingkui Tan  

**一句话要点**：提出ProtoDCS以解决视觉语言模型在开放集测试时适应中的鲁棒性与效率问题

**关键词**：开放集测试时适应, 视觉语言模型, 原型学习, 高斯混合模型, 不确定性估计, 计算效率

## 3 点简述
- 核心问题：开放集测试时适应中，现有方法依赖硬阈值分离和熵最小化，导致脆弱性和计算开销大
- 方法要点：采用概率高斯混合模型验证的双重检查分离机制和基于证据的原型级适应策略
- 实验或效果：在CIFAR-10/100-C和Tiny-ImageNet-C上实现最先进性能，提升已知类准确率和OOD检测指标

## 摘要（原文）

> Large-scale Vision-Language Models (VLMs) exhibit strong zero-shot recognition, yet their real-world deployment is challenged by distribution shifts. While Test-Time Adaptation (TTA) can mitigate this, existing VLM-based TTA methods operate under a closed-set assumption, failing in open-set scenarios where test streams contain both covariate-shifted in-distribution (csID) and out-of-distribution (csOOD) data. This leads to a critical difficulty: the model must discriminate unknown csOOD samples to avoid interference while simultaneously adapting to known csID classes for accuracy. Current open-set TTA (OSTTA) methods rely on hard thresholds for separation and entropy minimization for adaptation. These strategies are brittle, often misclassifying ambiguous csOOD samples and inducing overconfident predictions, and their parameter-update mechanism is computationally prohibitive for VLMs. To address these limitations, we propose Prototype-based Double-Check Separation (ProtoDCS), a robust framework for OSTTA that effectively separates csID and csOOD samples, enabling safe and efficient adaptation of VLMs to csID data. Our main contributions are: (1) a novel double-check separation mechanism employing probabilistic Gaussian Mixture Model (GMM) verification to replace brittle thresholding; and (2) an evidence-driven adaptation strategy utilizing uncertainty-aware loss and efficient prototype-level updates, mitigating overconfidence and reducing computational overhead. Extensive experiments on CIFAR-10/100-C and Tiny-ImageNet-C demonstrate that ProtoDCS achieves state-of-the-art performance, significantly boosting both known-class accuracy and OOD detection metrics. Code will be available at https://github.com/O-YangF/ProtoDCS.

