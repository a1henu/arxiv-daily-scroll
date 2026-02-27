---
layout: default
title: GSTurb: Gaussian Splatting for Atmospheric Turbulence Mitigation
---

# GSTurb: Gaussian Splatting for Atmospheric Turbulence Mitigation
**arXiv**：[2602.22800v1](https://arxiv.org/abs/2602.22800) · [PDF](https://arxiv.org/pdf/2602.22800.pdf)  
**作者**：Hanliang Du, Zhangji Lu, Zewei Cai, Qijian Tang, Qifeng Yu, Xiaoli Liu  

**一句话要点**：提出GSTurb框架，结合光流引导倾斜校正与高斯泼溅，以缓解大气湍流导致的图像退化。

**关键词**：大气湍流缓解, 高斯泼溅, 光流引导校正, 图像恢复, 长距离成像

## 3 点简述
- 核心问题：大气湍流导致像素位移和模糊，影响长距离成像质量。
- 方法要点：使用高斯参数建模倾斜和非等晕模糊，通过多帧优化进行图像恢复。
- 实验或效果：在ATSyn-static数据集上PSNR达27.67 dB，优于现有方法，并在真实数据集上表现优异。

## 摘要（原文）

> Atmospheric turbulence causes significant image degradation due to pixel displacement (tilt) and blur, particularly in long-range imaging applications. In this paper, we propose a novel framework for atmospheric turbulence mitigation, GSTurb, which integrates optical flow-guided tilt correction and Gaussian splatting for modeling non-isoplanatic blur. The framework employs Gaussian parameters to represent tilt and blur, and optimizes them across multiple frames to enhance restoration. Experimental results on the ATSyn-static dataset demonstrate the effectiveness of our method, achieving a peak PSNR of 27.67 dB and SSIM of 0.8735. Compared to the state-of-the-art method, GSTurb improves PSNR by 1.3 dB (a 4.5% increase) and SSIM by 0.048 (a 5.8% increase). Additionally, on real datasets, including the TSRWGAN Real-World and CLEAR datasets, GSTurb outperforms existing methods, showing significant improvements in both qualitative and quantitative performance. These results highlight that combining optical flow-guided tilt correction with Gaussian splatting effectively enhances image restoration under both synthetic and real-world turbulence conditions. The code for this method will be available at https://github.com/DuhlLiamz/3DGS_turbulence/tree/main.

