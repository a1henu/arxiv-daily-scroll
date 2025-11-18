---
layout: default
title: HDW-SR: High-Frequency Guided Diffusion Model based on Wavelet Decomposition for Image Super-Resolution
---

# HDW-SR: High-Frequency Guided Diffusion Model based on Wavelet Decomposition for Image Super-Resolution
**arXiv**：[2511.13175v1](https://arxiv.org/abs/2511.13175) · [PDF](https://arxiv.org/pdf/2511.13175.pdf)  
**作者**：Chao Yang, Boqian Zhang, Jinghao Xu, Guang Jiang  

**一句话要点**：提出基于小波分解的高频引导扩散模型HDW-SR，以解决图像超分辨率中细节模糊问题。

**关键词**：图像超分辨率, 扩散模型, 小波分解, 高频引导, 稀疏注意力

## 3 点简述
- 核心问题：现有扩散方法在图像超分辨率中高频信息引导不足，导致细节模糊。
- 方法要点：使用小波分解替换U-Net，在残差图上扩散，并引入稀疏交叉注意力进行高频引导。
- 实验效果：在合成和真实数据集上表现优异，尤其在恢复精细图像细节方面。

## 摘要（原文）

> Diffusion-based methods have shown great promise in single image super-resolution (SISR); however, existing approaches often produce blurred fine details due to insufficient guidance in the high-frequency domain. To address this issue, we propose a High-Frequency Guided Diffusion Network based on Wavelet Decomposition (HDW-SR), which replaces the conventional U-Net backbone in diffusion frameworks. Specifically, we perform diffusion only on the residual map, allowing the network to focus more effectively on high-frequency information restoration. We then introduce wavelet-based downsampling in place of standard CNN downsampling to achieve multi-scale frequency decomposition, enabling sparse cross-attention between the high-frequency subbands of the pre-super-resolved image and the low-frequency subbands of the diffused image for explicit high-frequency guidance. Moreover, a Dynamic Thresholding Block (DTB) is designed to refine high-frequency selection during the sparse attention process. During upsampling, the invertibility of the wavelet transform ensures low-loss feature reconstruction. Experiments on both synthetic and real-world datasets demonstrate that HDW-SR achieves competitive super-resolution performance, excelling particularly in recovering fine-grained image details. The code will be available after acceptance.

