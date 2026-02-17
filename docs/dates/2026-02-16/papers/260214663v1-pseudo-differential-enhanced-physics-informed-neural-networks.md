---
layout: default
title: Pseudo-differential-enhanced physics-informed neural networks
---

# Pseudo-differential-enhanced physics-informed neural networks
**arXiv**：[2602.14663v1](https://arxiv.org/abs/2602.14663) · [PDF](https://arxiv.org/pdf/2602.14663.pdf)  
**作者**：Andrew Gracyk  

**一句话要点**：提出伪微分增强物理信息神经网络，在傅里叶空间扩展梯度增强以提升训练效果。

**关键词**：物理信息神经网络, 傅里叶变换, 伪微分增强, 神经正切核, 分数导数, 蒙特卡洛方法

## 3 点简述
- 核心问题：PINNs训练中梯度增强在物理空间可能受限，影响高频学习与收敛。
- 方法要点：在傅里叶空间应用伪微分增强，通过乘傅里叶波数实现高效微分，兼容分数导数和傅里叶特征嵌入。
- 实验或效果：提升NTK谱特征值衰减，加速训练，减少样本需求，在低配置点设置中突破平台期。

## 摘要（原文）

> We present pseudo-differential enhanced physics-informed neural networks (PINNs), an extension of gradient enhancement but in Fourier space. Gradient enhancement of PINNs dictates that the PDE residual is taken to a higher differential order than prescribed by the PDE, added to the objective as an augmented term in order to improve training and overall learning fidelity. We propose the same procedure after application via Fourier transforms, since differentiating in Fourier space is multiplication with the Fourier wavenumber under suitable decay. Our methods are fast and efficient. Our methods oftentimes achieve superior PINN versus numerical error in fewer training iterations, potentially pair well with few samples in collocation, and can on occasion break plateaus in low collocation settings. Moreover, our methods are suitable for fractional derivatives. We establish that our methods improve spectral eigenvalue decay of the neural tangent kernel (NTK), and so our methods contribute towards the learning of high frequencies in early training, mitigating the effects of frequency bias up to the polynomial order and possibly greater with smooth activations. Our methods accommodate advanced techniques in PINNs, such as Fourier feature embeddings. A pitfall of discrete Fourier transforms via the Fast Fourier Transform (FFT) is mesh subjugation, and so we demonstrate compatibility of our methods for greater mesh flexibility and invariance on alternative Euclidean and non-Euclidean domains via Monte Carlo methods and otherwise.

