---
layout: default
title: TexAvatars : Hybrid Texel-3D Representations for Stable Rigging of Photorealistic Gaussian Head Avatars
---

# TexAvatars : Hybrid Texel-3D Representations for Stable Rigging of Photorealistic Gaussian Head Avatars
**arXiv**：[2512.21099v1](https://arxiv.org/abs/2512.21099) · [PDF](https://arxiv.org/pdf/2512.21099.pdf)  
**作者**：Jaeseong Lee, Junyeong Ahn, Taewoong Kang, Jaegul Choo  

**一句话要点**：提出TexAvatars混合表示，结合分析绑定与纹理空间，以稳定驱动逼真高斯头化身

**关键词**：3D高斯化身, 混合表示, 分析绑定, 纹理空间, 头重演, 泛化性

## 3 点简述
- 现有方法在极端重演中泛化不足，TexAvatars通过UV空间CNN预测几何属性，结合网格感知雅可比驱动变形
- 混合设计分离语义建模与几何控制，提升泛化性、可解释性和稳定性，捕捉肌肉皱纹等细节
- 在极端姿态和表情变化下实现最先进性能，在挑战性头重演场景中展示强泛化能力

## 摘要（原文）

> Constructing drivable and photorealistic 3D head avatars has become a central task in AR/XR, enabling immersive and expressive user experiences. With the emergence of high-fidelity and efficient representations such as 3D Gaussians, recent works have pushed toward ultra-detailed head avatars. Existing approaches typically fall into two categories: rule-based analytic rigging or neural network-based deformation fields. While effective in constrained settings, both approaches often fail to generalize to unseen expressions and poses, particularly in extreme reenactment scenarios. Other methods constrain Gaussians to the global texel space of 3DMMs to reduce rendering complexity. However, these texel-based avatars tend to underutilize the underlying mesh structure. They apply minimal analytic deformation and rely heavily on neural regressors and heuristic regularization in UV space, which weakens geometric consistency and limits extrapolation to complex, out-of-distribution deformations. To address these limitations, we introduce TexAvatars, a hybrid avatar representation that combines the explicit geometric grounding of analytic rigging with the spatial continuity of texel space. Our approach predicts local geometric attributes in UV space via CNNs, but drives 3D deformation through mesh-aware Jacobians, enabling smooth and semantically meaningful transitions across triangle boundaries. This hybrid design separates semantic modeling from geometric control, resulting in improved generalization, interpretability, and stability. Furthermore, TexAvatars captures fine-grained expression effects, including muscle-induced wrinkles, glabellar lines, and realistic mouth cavity geometry, with high fidelity. Our method achieves state-of-the-art performance under extreme pose and expression variations, demonstrating strong generalization in challenging head reenactment settings.

