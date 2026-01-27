---
layout: default
title: Differentiable Architecture Search for Adversarially Robust Quantum Computer Vision
---

# Differentiable Architecture Search for Adversarially Robust Quantum Computer Vision
**arXiv**：[2601.18058v1](https://arxiv.org/abs/2601.18058) · [PDF](https://arxiv.org/pdf/2601.18058.pdf)  
**作者**：Mohamed Afane, Quanjiang Long, Haoting Shen, Ying Mao, Junaid Farooq, Ying Wang, Juntao Chen  

**一句话要点**：提出混合量子-经典可微分架构搜索框架，以增强量子神经网络的对抗鲁棒性和硬件噪声容忍度。

**关键词**：量子神经网络, 对抗鲁棒性, 可微分架构搜索, 量子噪声, 混合量子-经典系统

## 3 点简述
- 量子神经网络对对抗扰动和硬件噪声高度敏感，阻碍实际部署。
- 引入轻量级经典噪声层，联合优化电路结构和鲁棒性参数。
- 在MNIST等数据集上，对抗攻击和量子噪声下性能优于现有方法。

## 摘要（原文）

> Current quantum neural networks suffer from extreme sensitivity to both adversarial perturbations and hardware noise, creating a significant barrier to real-world deployment. Existing robustness techniques typically sacrifice clean accuracy or require prohibitive computational resources. We propose a hybrid quantum-classical Differentiable Quantum Architecture Search (DQAS) framework that addresses these limitations by jointly optimizing circuit structure and robustness through gradient-based methods. Our approach enhances traditional DQAS with a lightweight Classical Noise Layer applied before quantum processing, enabling simultaneous optimization of gate selection and noise parameters. This design preserves the quantum circuit's integrity while introducing trainable perturbations that enhance robustness without compromising standard performance. Experimental validation on MNIST, FashionMNIST, and CIFAR datasets shows consistent improvements in both clean and adversarial accuracy compared to existing quantum architecture search methods. Under various attack scenarios, including Fast Gradient Sign Method (FGSM), Projected Gradient Descent (PGD), Basic Iterative Method (BIM), and Momentum Iterative Method (MIM), and under realistic quantum noise conditions, our hybrid framework maintains superior performance. Testing on actual quantum hardware confirms the practical viability of discovered architectures. These results demonstrate that strategic classical preprocessing combined with differentiable quantum architecture optimization can significantly enhance quantum neural network robustness while maintaining computational efficiency.

