---
layout: default
title: WWE-UIE: A Wavelet & White Balance Efficient Network for Underwater Image Enhancement
---

# WWE-UIE: A Wavelet & White Balance Efficient Network for Underwater Image Enhancement
**arXiv**：[2511.16321v1](https://arxiv.org/abs/2511.16321) · [PDF](https://arxiv.org/pdf/2511.16321.pdf)  
**作者**：Ching-Heng Cheng, Jen-Wei Lee, Chia-Ming Lee, Chih-Chung Hsu  

**一句话要点**：提出WWE-UIE网络以高效增强水下图像，实现实时处理

**关键词**：水下图像增强, 小波变换, 白平衡校正, 边缘保持, 高效网络, 实时处理

## 3 点简述
- 水下图像因波长吸收和散射导致可见性差和颜色失真
- 集成自适应白平衡、小波增强和梯度感知模块，提升恢复效果
- 实验显示参数和计算量少，在资源受限平台实现实时推理

## 摘要（原文）

> Underwater Image Enhancement (UIE) aims to restore visibility and correct color distortions caused by wavelength-dependent absorption and scattering. Recent hybrid approaches, which couple domain priors with modern deep neural architectures, have achieved strong performance but incur high computational cost, limiting their practicality in real-time scenarios. In this work, we propose WWE-UIE, a compact and efficient enhancement network that integrates three interpretable priors. First, adaptive white balance alleviates the strong wavelength-dependent color attenuation, particularly the dominance of blue-green tones. Second, a wavelet-based enhancement block (WEB) performs multi-band decomposition, enabling the network to capture both global structures and fine textures, which are critical for underwater restoration. Third, a gradient-aware module (SGFB) leverages Sobel operators with learnable gating to explicitly preserve edge structures degraded by scattering. Extensive experiments on benchmark datasets demonstrate that WWE-UIE achieves competitive restoration quality with substantially fewer parameters and FLOPs, enabling real-time inference on resource-limited platforms. Ablation studies and visualizations further validate the contribution of each component. The source code is available at https://github.com/chingheng0808/WWE-UIE.

