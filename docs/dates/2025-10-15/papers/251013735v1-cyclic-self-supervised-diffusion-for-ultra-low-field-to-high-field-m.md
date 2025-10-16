---
layout: default
title: Cyclic Self-Supervised Diffusion for Ultra Low-field to High-field MRI Synthesis
---

# Cyclic Self-Supervised Diffusion for Ultra Low-field to High-field MRI Synthesis
**arXiv**：[2510.13735v1](https://arxiv.org/abs/2510.13735) · [PDF](https://arxiv.org/pdf/2510.13735.pdf)  
**作者**：Zhenxuan Zhang, Peiyuan Jing, Zi Wang, Ula Briski, Coraline Beitone, Yue Yang, Yinzhe Wu, Fanwen Wang, Liutao Yang, Jiahao Huang, Zhifan Gao, Zhaolin Chen, Kh Tohidul Islam, Guang Yang, Peter J. Lally  

**一句话要点**：提出循环自监督扩散框架以解决低场到高场MRI合成中的解剖保真度问题

**关键词**：医学图像合成, 扩散模型, 自监督学习, MRI增强, 解剖保真度

## 3 点简述
- 核心问题：低场MRI图像分辨率低、信噪比差，合成高场MRI时存在解剖保真度不足。
- 方法要点：采用循环一致性约束扩散模型，结合切片感知和局部结构校正网络。
- 实验效果：在PSNR、SSIM和LPIPS指标上达到最优，显著降低解剖结构误差。

## 摘要（原文）

> Synthesizing high-quality images from low-field MRI holds significant
> potential. Low-field MRI is cheaper, more accessible, and safer, but suffers
> from low resolution and poor signal-to-noise ratio. This synthesis process can
> reduce reliance on costly acquisitions and expand data availability. However,
> synthesizing high-field MRI still suffers from a clinical fidelity gap. There
> is a need to preserve anatomical fidelity, enhance fine-grained structural
> details, and bridge domain gaps in image contrast. To address these issues, we
> propose a \emph{cyclic self-supervised diffusion (CSS-Diff)} framework for
> high-field MRI synthesis from real low-field MRI data. Our core idea is to
> reformulate diffusion-based synthesis under a cycle-consistent constraint. It
> enforces anatomical preservation throughout the generative process rather than
> just relying on paired pixel-level supervision. The CSS-Diff framework further
> incorporates two novel processes. The slice-wise gap perception network aligns
> inter-slice inconsistencies via contrastive learning. The local structure
> correction network enhances local feature restoration through
> self-reconstruction of masked and perturbed patches. Extensive experiments on
> cross-field synthesis tasks demonstrate the effectiveness of our method,
> achieving state-of-the-art performance (e.g., 31.80 $\pm$ 2.70 dB in PSNR,
> 0.943 $\pm$ 0.102 in SSIM, and 0.0864 $\pm$ 0.0689 in LPIPS). Beyond pixel-wise
> fidelity, our method also preserves fine-grained anatomical structures compared
> with the original low-field MRI (e.g., left cerebral white matter error drops
> from 12.1$\%$ to 2.1$\%$, cortex from 4.2$\%$ to 3.7$\%$). To conclude, our
> CSS-Diff can synthesize images that are both quantitatively reliable and
> anatomically consistent.

