---
layout: default
title: MobileI2V: Fast and High-Resolution Image-to-Video on Mobile Devices
---

# MobileI2V: Fast and High-Resolution Image-to-Video on Mobile Devices
**arXiv**：[2511.21475v1](https://arxiv.org/abs/2511.21475) · [PDF](https://arxiv.org/pdf/2511.21475.pdf)  
**作者**：Shuai Zhang, Bao Tang, Siyuan Yu, Yueting Zhu, Jingfeng Yao, Ya Zou, Shanglin Yuan, Li Yu, Wenyu Liu, Xinggang Wang  

**一句话要点**：提出MobileI2V轻量扩散模型，实现移动设备实时高分辨率图像到视频生成

**关键词**：图像到视频生成, 轻量扩散模型, 移动设备优化, 时间步蒸馏, 注意力机制优化

## 3 点简述
- 移动设备图像到视频生成面临计算复杂和速度慢的挑战
- 采用线性混合架构、时间步蒸馏和移动优化注意力模块
- 在720p分辨率下，每帧生成时间小于100毫秒，质量可比现有模型

## 摘要（原文）

> Recently, video generation has witnessed rapid advancements, drawing increasing attention to image-to-video (I2V) synthesis on mobile devices. However, the substantial computational complexity and slow generation speed of diffusion models pose significant challenges for real-time, high-resolution video generation on resource-constrained mobile devices. In this work, we propose MobileI2V, a 270M lightweight diffusion model for real-time image-to-video generation on mobile devices. The core lies in: (1) We analyzed the performance of linear attention modules and softmax attention modules on mobile devices, and proposed a linear hybrid architecture denoiser that balances generation efficiency and quality. (2) We design a time-step distillation strategy that compresses the I2V sampling steps from more than 20 to only two without significant quality loss, resulting in a 10-fold increase in generation speed. (3) We apply mobile-specific attention optimizations that yield a 2-fold speed-up for attention operations during on-device inference. MobileI2V enables, for the first time, fast 720p image-to-video generation on mobile devices, with quality comparable to existing models. Under one-step conditions, the generation speed of each frame of 720p video is less than 100 ms. Our code is available at: https://github.com/hustvl/MobileI2V.

