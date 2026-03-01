---
layout: default
title: HARU-Net: Hybrid Attention Residual U-Net for Edge-Preserving Denoising in Cone-Beam Computed Tomography
---

# HARU-Net: Hybrid Attention Residual U-Net for Edge-Preserving Denoising in Cone-Beam Computed Tomography
**arXiv**：[2602.22544v1](https://arxiv.org/abs/2602.22544) · [PDF](https://arxiv.org/pdf/2602.22544.pdf)  
**作者**：Khuram Naveed, Ruben Pauwels  

**一句话要点**：提出HARU-Net以解决CBCT低剂量去噪中噪声抑制与边缘保留的难题。

**关键词**：锥束CT去噪, 混合注意力网络, 残差学习, 边缘保留, 深度学习, 医学图像处理

## 3 点简述
- CBCT低剂量成像引入强噪声，降低软组织可见度，传统方法难以兼顾去噪与边缘保留。
- HARU-Net集成混合注意力Transformer块和残差学习，增强特征选择与全局建模，提升去噪性能。
- 在尸体数据集上训练，HARU-Net在PSNR、SSIM和GMSD指标上优于SOTA方法，计算成本更低。

## 摘要（原文）

> Cone-beam computed tomography (CBCT) is widely used in dental and maxillofacial imaging, but low-dose acquisition introduces strong, spatially varying noise that degrades soft-tissue visibility and obscures fine anatomical structures. Classical denoising methods struggle to suppress noise in CBCT while preserving edges. Although deep learning-based approaches offer high-fidelity restoration, their use in CBCT denoising is limited by the scarcity of high-resolution CBCT data for supervised training. To address this research gap, we propose a novel Hybrid Attention Residual U-Net (HARU-Net) for high-quality denoising of CBCT data, trained on a cadaver dataset of human hemimandibles acquired using a high-resolution protocol of the 3D Accuitomo 170 (J. Morita, Kyoto, Japan) CBCT system. The novel contribution of this approach is the integration of three complementary architectural components: (i) a hybrid attention transformer block (HAB) embedded within each skip connection to selectively emphasize salient anatomical features, (ii) a residual hybrid attention transformer group (RHAG) at the bottleneck to strengthen global contextual modeling and long-range feature interactions, and (iii) residual learning convolutional blocks to facilitate deeper, more stable feature extraction throughout the network. HARU-Net consistently outperforms state-of-the-art (SOTA) methods including SwinIR and Uformer, achieving the highest PSNR (37.52 dB), highest SSIM (0.9557), and lowest GMSD (0.1084). This effective and clinically reliable CBCT denoising is achieved at a computational cost significantly lower than that of the SOTA methods, offering a practical advancement toward improving diagnostic quality in low-dose CBCT imaging.

