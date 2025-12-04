---
layout: default
title: BlurDM: A Blur Diffusion Model for Image Deblurring
---

# BlurDM: A Blur Diffusion Model for Image Deblurring
**arXiv**：[2512.03979v1](https://arxiv.org/abs/2512.03979) · [PDF](https://arxiv.org/pdf/2512.03979.pdf)  
**作者**：Jin-Ting He, Fu-Jen Tsai, Yan-Tsung Peng, Min-Hung Chen, Chia-Wen Lin, Yen-Yu Lin  

**一句话要点**：提出BlurDM模型，通过双扩散方案集成模糊形成过程以增强图像去模糊效果。

**关键词**：图像去模糊, 扩散模型, 双扩散方案, 模糊形成建模, 潜在空间处理

## 3 点简述
- 现有扩散模型未充分利用模糊形成的内在特性，限制了去模糊潜力。
- BlurDM采用双扩散前向方案隐式建模模糊形成，并在反向过程中同时去噪和去模糊。
- 在四个基准数据集上，BlurDM显著提升了现有去模糊方法的性能。

## 摘要（原文）

> Diffusion models show promise for dynamic scene deblurring; however, existing studies often fail to leverage the intrinsic nature of the blurring process within diffusion models, limiting their full potential. To address it, we present a Blur Diffusion Model (BlurDM), which seamlessly integrates the blur formation process into diffusion for image deblurring. Observing that motion blur stems from continuous exposure, BlurDM implicitly models the blur formation process through a dual-diffusion forward scheme, diffusing both noise and blur onto a sharp image. During the reverse generation process, we derive a dual denoising and deblurring formulation, enabling BlurDM to recover the sharp image by simultaneously denoising and deblurring, given pure Gaussian noise conditioned on the blurred image as input. Additionally, to efficiently integrate BlurDM into deblurring networks, we perform BlurDM in the latent space, forming a flexible prior generation network for deblurring. Extensive experiments demonstrate that BlurDM significantly and consistently enhances existing deblurring methods on four benchmark datasets. The source code is available at https://github.com/Jin-Ting-He/BlurDM.

