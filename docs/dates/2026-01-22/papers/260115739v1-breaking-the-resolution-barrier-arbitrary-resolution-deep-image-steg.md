---
layout: default
title: Breaking the Resolution Barrier: Arbitrary-resolution Deep Image Steganography Framework
---

# Breaking the Resolution Barrier: Arbitrary-resolution Deep Image Steganography Framework
**arXiv**：[2601.15739v1](https://arxiv.org/abs/2601.15739) · [PDF](https://arxiv.org/pdf/2601.15739.pdf)  
**作者**：Xinjue Hu, Chi Wang, Boyu Wang, Xiang Zhang, Zhenshan Tan, Zhangjie Fu  

**一句话要点**：提出ARDIS框架以解决深度图像隐写中分辨率不匹配导致的细节损失与盲恢复问题

**关键词**：深度图像隐写, 任意分辨率恢复, 频率解耦, 隐式重建, 盲恢复, 信号重建

## 3 点简述
- 核心问题：现有深度图像隐写方法要求秘密图像与载体图像分辨率一致，导致跨分辨率恢复时细节损失且无法盲恢复原始分辨率
- 方法要点：设计频率解耦架构分离秘密图像为全局基与高频潜码，并引入隐式重建器与分辨率编码策略实现连续信号重建
- 实验或效果：在不可见性和跨分辨率恢复保真度上显著优于现有方法，支持任意分辨率秘密图像的准确恢复

## 摘要（原文）

> Deep image steganography (DIS) has achieved significant results in capacity and invisibility. However, current paradigms enforce the secret image to maintain the same resolution as the cover image during hiding and revealing. This leads to two challenges: secret images with inconsistent resolutions must undergo resampling beforehand which results in detail loss during recovery, and the secret image cannot be recovered to its original resolution when the resolution value is unknown. To address these, we propose ARDIS, the first Arbitrary Resolution DIS framework, which shifts the paradigm from discrete mapping to reference-guided continuous signal reconstruction. Specifically, to minimize the detail loss caused by resolution mismatch, we first design a Frequency Decoupling Architecture in hiding stage. It disentangles the secret into a resolution-aligned global basis and a resolution-agnostic high-frequency latent to hide in a fixed-resolution cover. Second, for recovery, we propose a Latent-Guided Implicit Reconstructor to perform deterministic restoration. The recovered detail latent code modulates a continuous implicit function to accurately query and render high-frequency residuals onto the recovered global basis, ensuring faithful restoration of original details. Furthermore, to achieve blind recovery, we introduce an Implicit Resolution Coding strategy. By transforming discrete resolution values into dense feature maps and hiding them in the redundant space of the feature domain, the reconstructor can correctly decode the secret's resolution directly from the steganographic representation. Experimental results demonstrate that ARDIS significantly outperforms state-of-the-art methods in both invisibility and cross-resolution recovery fidelity.

