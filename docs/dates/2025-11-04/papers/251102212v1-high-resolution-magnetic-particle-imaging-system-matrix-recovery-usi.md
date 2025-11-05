---
layout: default
title: High-Resolution Magnetic Particle Imaging System Matrix Recovery Using a Vision Transformer with Residual Feature Network
---

# High-Resolution Magnetic Particle Imaging System Matrix Recovery Using a Vision Transformer with Residual Feature Network
**arXiv**：[2511.02212v1](https://arxiv.org/abs/2511.02212) · [PDF](https://arxiv.org/pdf/2511.02212.pdf)  
**作者**：Abuobaida M. Khair, Wenjing Jiang, Yousuf Babiker M. Osman, Wenjun Xia, Xiaopeng Ma  

**一句话要点**：提出VRF-Net混合深度学习框架，用于磁粒子成像高分辨率系统矩阵恢复。

**关键词**：磁粒子成像, 系统矩阵恢复, 视觉Transformer, 残差网络, 超分辨率, 深度学习框架

## 3 点简述
- 磁粒子成像分辨率受下采样和线圈灵敏度变化影响，导致系统矩阵退化。
- VRF-Net结合Transformer全局注意力和残差卷积，恢复大尺度结构和精细细节。
- 在Open MPI数据集上，2倍缩放时nRMSE=0.403，pSNR=39.08 dB，优于现有方法。

## 摘要（原文）

> This study presents a hybrid deep learning framework, the Vision Transformer
> with Residual Feature Network (VRF-Net), for recovering high-resolution system
> matrices in Magnetic Particle Imaging (MPI). MPI resolution often suffers from
> downsampling and coil sensitivity variations. VRF-Net addresses these
> challenges by combining transformer-based global attention with residual
> convolutional refinement, enabling recovery of both large-scale structures and
> fine details. To reflect realistic MPI conditions, the system matrix is
> degraded using a dual-stage downsampling strategy. Training employed
> paired-image super-resolution on the public Open MPI dataset and a simulated
> dataset incorporating variable coil sensitivity profiles. For system matrix
> recovery on the Open MPI dataset, VRF-Net achieved nRMSE = 0.403, pSNR = 39.08
> dB, and SSIM = 0.835 at 2x scaling, and maintained strong performance even at
> challenging scale 8x (pSNR = 31.06 dB, SSIM = 0.717). For the simulated
> dataset, VRF-Net achieved nRMSE = 4.44, pSNR = 28.52 dB, and SSIM = 0.771 at 2x
> scaling, with stable performance at higher scales. On average, it reduced nRMSE
> by 88.2%, increased pSNR by 44.7%, and improved SSIM by 34.3% over
> interpolation and CNN-based methods. In image reconstruction of Open MPI
> phantoms, VRF-Net further reduced reconstruction error to nRMSE = 1.79 at 2x
> scaling, while preserving structural fidelity (pSNR = 41.58 dB, SSIM = 0.960),
> outperforming existing methods. These findings demonstrate that VRF-Net enables
> sharper, artifact-free system matrix recovery and robust image reconstruction
> across multiple scales, offering a promising direction for future in vivo
> applications.

