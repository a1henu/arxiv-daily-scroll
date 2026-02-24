---
layout: default
title: Unlearning Noise in PINNs: A Selective Pruning Framework for PDE Inverse Problems
---

# Unlearning Noise in PINNs: A Selective Pruning Framework for PDE Inverse Problems
**arXiv**：[2602.19967v1](https://arxiv.org/abs/2602.19967) · [PDF](https://arxiv.org/pdf/2602.19967.pdf)  
**作者**：Yongsheng Chen, Yong Chen, Wei Guo, Xinghui Zhong  

**一句话要点**：提出P-PINN选择性剪枝框架，以解决偏微分方程逆问题中噪声数据对物理信息神经网络的影响。

**关键词**：物理信息神经网络, 偏微分方程逆问题, 噪声鲁棒性, 选择性剪枝, 机器遗忘, 激活分析

## 3 点简述
- 核心问题：偏微分方程逆问题因不适定性对噪声敏感，少量损坏数据会扭曲神经网络表示，降低精度和训练稳定性。
- 方法要点：基于联合残差-数据保真度指标划分数据集，引入偏置神经元重要性度量识别噪声敏感神经元，通过迭代剪枝移除并微调。
- 实验或效果：在噪声条件下显著提升鲁棒性、精度和训练稳定性，相对误差减少高达96.6%。

## 摘要（原文）

> Physics-informed neural networks (PINNs) provide a promising framework for solving inverse problems governed by partial differential equations (PDEs) by integrating observational data and physical constraints in a unified optimization objective. However, the ill-posed nature of PDE inverse problems makes them highly sensitive to noise. Even a small fraction of corrupted observations can distort internal neural representations, severely impairing accuracy and destabilizing training. Motivated by recent advances in machine unlearning and structured network pruning, we propose P-PINN, a selective pruning framework designed to unlearn the influence of corrupted data in a pretrained PINN. Specifically, starting from a PINN trained on the full dataset, P-PINN evaluates a joint residual--data fidelity indicator, a weighted combination of data misfit and PDE residuals, to partition the training set into reliable and corrupted subsets. Next, we introduce a bias-based neuron importance measure that quantifies directional activation discrepancies between the two subsets, identifying neurons whose representations are predominantly driven by corrupted samples. Building on this, an iterative pruning strategy then removes noise-sensitive neurons layer by layer. The resulting pruned network is fine-tuned on the reliable data subject to the original PDE constraints, acting as a lightweight post-processing stage rather than a complete retraining. Numerical experiments on extensive PDE inverse-problem benchmarks demonstrate that P-PINN substantially improves robustness, accuracy, and training stability under noisy conditions, achieving up to a 96.6\% reduction in relative error compared with baseline PINNs. These results indicate that activation-level post hoc pruning is a promising mechanism for enhancing the reliability of physics-informed learning in noise-contaminated settings.

