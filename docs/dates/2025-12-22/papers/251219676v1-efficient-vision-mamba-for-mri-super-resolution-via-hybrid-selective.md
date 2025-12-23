---
layout: default
title: Efficient Vision Mamba for MRI Super-Resolution via Hybrid Selective Scanning
---

# Efficient Vision Mamba for MRI Super-Resolution via Hybrid Selective Scanning
**arXiv**：[2512.19676v1](https://arxiv.org/abs/2512.19676) · [PDF](https://arxiv.org/pdf/2512.19676.pdf)  
**作者**：Mojtaba Safari, Shansong Wang, Vanessa L Wildman, Mingzhe Hu, Zach Eidex, Chih-Wei Chang, Erik H Middlebrooks, Richard L. J Qiu, Pretesh Patel, Ashesh B. Jania, Hui Mao, Zhen Tian, Xiaofeng Yang  

**一句话要点**：提出高效视觉Mamba框架，通过混合选择性扫描实现MRI超分辨率，以解决临床应用中分辨率与效率的权衡问题。

**关键词**：MRI超分辨率, 选择性状态空间模型, 混合扫描, 轻量级网络, 临床影像增强, 计算效率优化

## 3 点简述
- 核心问题：高分辨率MRI采集时间长，现有超分辨率方法在保真度与计算效率间存在权衡。
- 方法要点：结合多头选择性状态空间模型与轻量级通道MLP，采用混合扫描捕获长程依赖，集成MambaFormer块提升效率。
- 实验或效果：在7T脑和1.5T前列腺数据上，性能优于基线模型，参数仅0.9M，计算量减少97.5%，显示临床转化潜力。

## 摘要（原文）

> Background: High-resolution MRI is critical for diagnosis, but long acquisition times limit clinical use. Super-resolution (SR) can enhance resolution post-scan, yet existing deep learning methods face fidelity-efficiency trade-offs. Purpose: To develop a computationally efficient and accurate deep learning framework for MRI SR that preserves anatomical detail for clinical integration. Materials and Methods: We propose a novel SR framework combining multi-head selective state-space models (MHSSM) with a lightweight channel MLP. The model uses 2D patch extraction with hybrid scanning to capture long-range dependencies. Each MambaFormer block integrates MHSSM, depthwise convolutions, and gated channel mixing. Evaluation used 7T brain T1 MP2RAGE maps (n=142) and 1.5T prostate T2w MRI (n=334). Comparisons included Bicubic interpolation, GANs (CycleGAN, Pix2pix, SPSR), transformers (SwinIR), Mamba (MambaIR), and diffusion models (I2SB, Res-SRDiff). Results: Our model achieved superior performance with exceptional efficiency. For 7T brain data: SSIM=0.951+-0.021, PSNR=26.90+-1.41 dB, LPIPS=0.076+-0.022, GMSD=0.083+-0.017, significantly outperforming all baselines (p<0.001). For prostate data: SSIM=0.770+-0.049, PSNR=27.15+-2.19 dB, LPIPS=0.190+-0.095, GMSD=0.087+-0.013. The framework used only 0.9M parameters and 57 GFLOPs, reducing parameters by 99.8% and computation by 97.5% versus Res-SRDiff, while outperforming SwinIR and MambaIR in accuracy and efficiency. Conclusion: The proposed framework provides an efficient, accurate MRI SR solution, delivering enhanced anatomical detail across datasets. Its low computational demand and state-of-the-art performance show strong potential for clinical translation.

