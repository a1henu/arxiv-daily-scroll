---
layout: default
title: Enhancing Physics-Informed Neural Networks with Domain-aware Fourier Features: Towards Improved Performance and Interpretable Results
---

# Enhancing Physics-Informed Neural Networks with Domain-aware Fourier Features: Towards Improved Performance and Interpretable Results
**arXiv**：[2603.02948v1](https://arxiv.org/abs/2603.02948) · [PDF](https://arxiv.org/pdf/2603.02948.pdf)  
**作者**：Alberto Miño Calero, Luis Salamanca, Konstantinos E. Tatsis  

**一句话要点**：提出域感知傅里叶特征以增强物理信息神经网络的性能与可解释性

**关键词**：物理信息神经网络, 傅里叶特征, 可解释性分析, 偏微分方程求解, 域感知编码, LRP框架

## 3 点简述
- PINNs训练困难且难以解释，核心问题在于输入编码和边界条件处理。
- 方法引入域感知傅里叶特征，编码几何和边界条件，简化优化并降低计算成本。
- 实验显示PINN-DaFFs误差显著降低、收敛更快，LRP分析揭示更物理一致的特征归因。

## 摘要（原文）

> Physics-Informed Neural Networks (PINNs) incorporate physics into neural networks by embedding partial differential equations (PDEs) into their loss function. Despite their success in learning the underlying physics, PINN models remain difficult to train and interpret. In this work, a novel modeling approach is proposed, which relies on the use of Domain-aware Fourier Features (DaFFs) for the positional encoding of the input space. These features encapsulate all the domain-specific characteristics, such as the geometry and boundary conditions, and unlike Random Fourier Features (RFFs), eliminate the need for explicit boundary condition loss terms and loss balancing schemes, while simplifying the optimization process and reducing the computational cost associated with training. We further develop an LRP-based explainability framework tailored to PINNs, enabling the extraction of relevance attribution scores for the input space. It is demonstrated that PINN-DaFFs achieve orders-of-magnitude lower errors and allow faster convergence compared to vanilla PINNs and RFFs-based PINNs. Furthermore, LRP analysis reveals that the proposed leads to more physically consistent feature attributions, while PINN-RFFs and vanilla PINNs display more scattered and less physics-relevant patterns. These results demonstrate that DaFFs not only enhance PINNs' accuracy and efficiency but also improve interpretability, laying the ground for more robust and informative physics-informed learning.

