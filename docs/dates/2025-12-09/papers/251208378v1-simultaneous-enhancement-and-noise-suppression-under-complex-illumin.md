---
layout: default
title: Simultaneous Enhancement and Noise Suppression under Complex Illumination Conditions
---

# Simultaneous Enhancement and Noise Suppression under Complex Illumination Conditions
**arXiv**：[2512.08378v1](https://arxiv.org/abs/2512.08378) · [PDF](https://arxiv.org/pdf/2512.08378.pdf)  
**作者**：Jing Tao, You Li, Banglei Guan, Yang Shang, Qifeng Yu  

**一句话要点**：提出梯度域加权引导滤波与Retinex分解框架，以在复杂光照下同时增强图像并抑制噪声。

**关键词**：图像增强, 噪声抑制, Retinex模型, 梯度域滤波, 多曝光融合

## 3 点简述
- 核心问题：复杂光照导致图像退化，现有方法易放大噪声或仅适用于特定条件。
- 方法要点：使用GDWGIF估计光照，Retinex分解并行处理光照与反射层，结合多曝光融合优化动态范围。
- 实验或效果：在真实数据集上验证，对比度增强和噪声抑制性能优于现有方法。

## 摘要（原文）

> Under challenging light conditions, captured images often suffer from various degradations, leading to a decline in the performance of vision-based applications. Although numerous methods have been proposed to enhance image quality, they either significantly amplify inherent noise or are only effective under specific illumination conditions. To address these issues, we propose a novel framework for simultaneous enhancement and noise suppression under complex illumination conditions. Firstly, a gradient-domain weighted guided filter (GDWGIF) is employed to accurately estimate illumination and improve image quality. Next, the Retinex model is applied to decompose the captured image into separate illumination and reflection layers. These layers undergo parallel processing, with the illumination layer being corrected to optimize lighting conditions and the reflection layer enhanced to improve image quality. Finally, the dynamic range of the image is optimized through multi-exposure fusion and a linear stretching strategy. The proposed method is evaluated on real-world datasets obtained from practical applications. Experimental results demonstrate that our proposed method achieves better performance compared to state-of-the-art methods in both contrast enhancement and noise suppression.

