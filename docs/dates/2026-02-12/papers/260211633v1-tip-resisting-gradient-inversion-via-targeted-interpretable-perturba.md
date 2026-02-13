---
layout: default
title: TIP: Resisting Gradient Inversion via Targeted Interpretable Perturbation in Federated Learning
---

# TIP: Resisting Gradient Inversion via Targeted Interpretable Perturbation in Federated Learning
**arXiv**：[2602.11633v1](https://arxiv.org/abs/2602.11633) · [PDF](https://arxiv.org/pdf/2602.11633.pdf)  
**作者**：Jianhua Wang, Yinlin Su  

**一句话要点**：提出TIP框架，通过针对性可解释扰动防御联邦学习中的梯度反演攻击。

**关键词**：联邦学习, 梯度反演攻击防御, 模型可解释性, 频域分析, 隐私-效用权衡

## 3 点简述
- 核心问题：联邦学习梯度交换易受反演攻击，现有差分隐私方法损害模型性能。
- 方法要点：结合Grad-CAM和频域分析，选择性扰动关键卷积通道的高频成分。
- 实验或效果：在基准数据集上有效破坏图像重建细节，保持模型精度优于差分隐私方法。

## 摘要（原文）

> Federated Learning (FL) facilitates collaborative model training while preserving data locality; however, the exchange of gradients renders the system vulnerable to Gradient Inversion Attacks (GIAs), allowing adversaries to reconstruct private training data with high fidelity. Existing defenses, such as Differential Privacy (DP), typically employ indiscriminate noise injection across all parameters, which severely degrades model utility and convergence stability. To address those limitation, we proposes Targeted Interpretable Perturbation (TIP), a novel defense framework that integrates model interpretability with frequency domain analysis. Unlike conventional methods that treat parameters uniformly, TIP introduces a dual-targeting strategy. First, leveraging Gradient-weighted Class Activation Mapping (Grad-CAM) to quantify channel sensitivity, we dynamically identify critical convolution channels that encode primary semantic features. Second, we transform these selected kernels into the frequency domain via the Discrete Fourier Transform and selectively inject calibrated perturbations into the high-frequency spectrum. By selectively perturbing high-frequency components, TIP effectively destroys the fine-grained details necessary for image reconstruction while preserving the low-frequency information crucial for model accuracy. Extensive experiments on benchmark datasets demonstrate that TIP renders reconstructed images visually unrecognizable against state-of-the-art GIAs, while maintaining global model accuracy comparable to non-private baselines, significantly outperforming existing DP-based defenses in the privacy-utility trade-off and interpretability. Code is available in https://github.com/2766733506/asldkfjssdf_arxiv

