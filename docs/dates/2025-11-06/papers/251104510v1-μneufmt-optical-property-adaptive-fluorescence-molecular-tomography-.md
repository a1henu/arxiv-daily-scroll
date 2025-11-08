---
layout: default
title: $μ$NeuFMT: Optical-Property-Adaptive Fluorescence Molecular Tomography via Implicit Neural Representation
---

# $μ$NeuFMT: Optical-Property-Adaptive Fluorescence Molecular Tomography via Implicit Neural Representation
**arXiv**：[2511.04510v1](https://arxiv.org/abs/2511.04510) · [PDF](https://arxiv.org/pdf/2511.04510.pdf)  
**作者**：Shihan Zhao, Jianru Zhang, Yanan Wu, Linlin Li, Siyuan Shen, Xingjun Zhu, Guoyan Zheng, Jiahua Jiang, Wuwei Ren  

**一句话要点**：提出μNeuFMT以解决荧光分子断层扫描中光学属性未知的重建挑战

**关键词**：荧光分子断层扫描, 隐式神经表示, 自监督学习, 光学属性优化, 分子成像

## 3 点简述
- 核心问题：FMT重建因逆问题性质和光学属性不准确而困难，监督方法泛化性差
- 方法要点：结合隐式神经表示与光子传播物理模型，联合优化荧光分布和光学属性
- 实验或效果：在数值、仿体和活体实验中，即使初始值误差大，仍优于传统和监督方法

## 摘要（原文）

> Fluorescence Molecular Tomography (FMT) is a promising technique for
> non-invasive 3D visualization of fluorescent probes, but its reconstruction
> remains challenging due to the inherent ill-posedness and reliance on
> inaccurate or often-unknown tissue optical properties. While deep learning
> methods have shown promise, their supervised nature limits generalization
> beyond training data. To address these problems, we propose $\mu$NeuFMT, a
> self-supervised FMT reconstruction framework that integrates implicit
> neural-based scene representation with explicit physical modeling of photon
> propagation. Its key innovation lies in jointly optimize both the fluorescence
> distribution and the optical properties ($\mu$) during reconstruction,
> eliminating the need for precise prior knowledge of tissue optics or
> pre-conditioned training data. We demonstrate that $\mu$NeuFMT robustly
> recovers accurate fluorophore distributions and optical coefficients even with
> severely erroneous initial values (0.5$\times$ to 2$\times$ of ground truth).
> Extensive numerical, phantom, and in vivo validations show that $\mu$NeuFMT
> outperforms conventional and supervised deep learning approaches across diverse
> heterogeneous scenarios. Our work establishes a new paradigm for robust and
> accurate FMT reconstruction, paving the way for more reliable molecular imaging
> in complex clinically related scenarios, such as fluorescence guided surgery.

