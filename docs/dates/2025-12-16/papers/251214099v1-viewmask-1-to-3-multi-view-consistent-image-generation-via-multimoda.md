---
layout: default
title: ViewMask-1-to-3: Multi-View Consistent Image Generation via Multimodal Diffusion Models
---

# ViewMask-1-to-3: Multi-View Consistent Image Generation via Multimodal Diffusion Models
**arXiv**：[2512.14099v1](https://arxiv.org/abs/2512.14099) · [PDF](https://arxiv.org/pdf/2512.14099.pdf)  
**作者**：Ruishu Zhu, Zhihao Huang, Jiacheng Sun, Ping Luo, Hongyuan Zhang, Xuelong Li  

**一句话要点**：提出ViewMask-1-to-3，通过离散扩散模型实现单图文本到多视角一致图像生成。

**关键词**：多视角图像生成, 离散扩散模型, 视觉令牌化, 掩码令牌预测, 几何一致性, 自注意力机制

## 3 点简述
- 核心问题：单图文本生成多视角图像时，几何一致性难以保持，现有方法依赖复杂3D架构或大量数据。
- 方法要点：将多视角合成建模为离散序列问题，使用MAGVIT-v2视觉令牌和掩码令牌预测，结合自注意力实现一致性。
- 实验或效果：在GSO和3D-FUTURE数据集上PSNR、SSIM、LPIPS指标平均排名第一，架构简单。

## 摘要（原文）

> Multi-view image generation from a single image and text description remains challenging due to the difficulty of maintaining geometric consistency across different viewpoints. Existing approaches typically rely on 3D-aware architectures or specialized diffusion models that require extensive multi-view training data and complex geometric priors. In this work, we introduce ViewMask-1-to-3, a pioneering approach to apply discrete diffusion models to multi-view image generation. Unlike continuous diffusion methods that operate in latent spaces, ViewMask-1-to-3 formulates multi-view synthesis as a discrete sequence modeling problem, where each viewpoint is represented as visual tokens obtained through MAGVIT-v2 tokenization. By unifying language and vision through masked token prediction, our approach enables progressive generation of multiple viewpoints through iterative token unmasking with text input. ViewMask-1-to-3 achieves cross-view consistency through simple random masking combined with self-attention, eliminating the requirement for complex 3D geometric constraints or specialized attention architectures. Our approach demonstrates that discrete diffusion provides a viable and simple alternative to existing multi-view generation methods, ranking first on average across GSO and 3D-FUTURE datasets in terms of PSNR, SSIM, and LPIPS, while maintaining architectural simplicity.

