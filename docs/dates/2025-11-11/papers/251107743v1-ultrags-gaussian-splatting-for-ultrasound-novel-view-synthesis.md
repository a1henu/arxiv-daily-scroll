---
layout: default
title: UltraGS: Gaussian Splatting for Ultrasound Novel View Synthesis
---

# UltraGS: Gaussian Splatting for Ultrasound Novel View Synthesis
**arXiv**：[2511.07743v1](https://arxiv.org/abs/2511.07743) · [PDF](https://arxiv.org/pdf/2511.07743.pdf)  
**作者**：Yuezhe Yang, Wenjie Cai, Dexin Yang, Yufang Dong, Xingbo Dong, Zhe Jin  

**一句话要点**：提出UltraGS框架以解决超声成像新视角合成问题

**关键词**：高斯溅射, 超声成像, 新视角合成, 深度预测, 实时渲染, 临床数据集

## 3 点简述
- 超声成像视野有限，新视角合成困难
- 采用深度感知高斯溅射和SH-DARS渲染函数，结合超声物理建模
- 在多个数据集上实现SOTA性能，PSNR达29.55，实时合成64.69 fps

## 摘要（原文）

> Ultrasound imaging is a cornerstone of non-invasive clinical diagnostics, yet its limited field of view complicates novel view synthesis. We propose \textbf{UltraGS}, a Gaussian Splatting framework optimized for ultrasound imaging. First, we introduce a depth-aware Gaussian splatting strategy, where each Gaussian is assigned a learnable field of view, enabling accurate depth prediction and precise structural representation. Second, we design SH-DARS, a lightweight rendering function combining low-order spherical harmonics with ultrasound-specific wave physics, including depth attenuation, reflection, and scattering, to model tissue intensity accurately. Third, we contribute the Clinical Ultrasound Examination Dataset, a benchmark capturing diverse anatomical scans under real-world clinical protocols. Extensive experiments on three datasets demonstrate UltraGS's superiority, achieving state-of-the-art results in PSNR (up to 29.55), SSIM (up to 0.89), and MSE (as low as 0.002) while enabling real-time synthesis at 64.69 fps. The code and dataset are open-sourced at: https://github.com/Bean-Young/UltraGS.

