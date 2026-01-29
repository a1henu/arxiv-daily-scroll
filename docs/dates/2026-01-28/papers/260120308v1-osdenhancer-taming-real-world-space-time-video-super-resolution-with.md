---
layout: default
title: OSDEnhancer: Taming Real-World Space-Time Video Super-Resolution with One-Step Diffusion
---

# OSDEnhancer: Taming Real-World Space-Time Video Super-Resolution with One-Step Diffusion
**arXiv**：[2601.20308v1](https://arxiv.org/abs/2601.20308) · [PDF](https://arxiv.org/pdf/2601.20308.pdf)  
**作者**：Shuoyan Wei, Feng Li, Chen Zhou, Runmin Cong, Yao Zhao, Huihui Bai  

**一句话要点**：提出OSDEnhancer框架，通过一步扩散过程实现真实世界时空视频超分辨率。

**关键词**：时空视频超分辨率, 扩散模型, 混合专家网络, 变形变分自编码器, 真实世界视频增强

## 3 点简述
- 核心问题：现有时空视频超分辨率方法在复杂未知退化下性能受限，需兼顾重建保真度和时间一致性。
- 方法要点：采用线性预插值初始化结构，训练TR-SE MoE专家网络，并引入双向变形VAE解码器进行时空聚合。
- 实验或效果：在真实世界场景中达到最先进性能，并保持优越的泛化能力。

## 摘要（原文）

> Diffusion models (DMs) have demonstrated exceptional success in video super-resolution (VSR), showcasing a powerful capacity for generating fine-grained details. However, their potential for space-time video super-resolution (STVSR), which necessitates not only recovering realistic visual content from low-resolution to high-resolution but also improving the frame rate with coherent temporal dynamics, remains largely underexplored. Moreover, existing STVSR methods predominantly address spatiotemporal upsampling under simplified degradation assumptions, which often struggle in real-world scenarios with complex unknown degradations. Such a high demand for reconstruction fidelity and temporal consistency makes the development of a robust STVSR framework particularly non-trivial. To address these challenges, we propose OSDEnhancer, a novel framework that, to the best of our knowledge, represents the first method to achieve real-world STVSR through an efficient one-step diffusion process. OSDEnhancer initializes essential spatiotemporal structures through a linear pre-interpolation strategy and pivots on training temporal refinement and spatial enhancement mixture of experts (TR-SE MoE), which allows distinct expert pathways to progressively learn robust, specialized representations for temporal coherence and spatial detail, further collaboratively reinforcing each other during inference. A bidirectional deformable variational autoencoder (VAE) decoder is further introduced to perform recurrent spatiotemporal aggregation and propagation, enhancing cross-frame reconstruction fidelity. Experiments demonstrate that the proposed method achieves state-of-the-art performance while maintaining superior generalization capability in real-world scenarios.

