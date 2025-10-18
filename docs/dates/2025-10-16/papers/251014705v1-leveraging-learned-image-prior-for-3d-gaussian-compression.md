---
layout: default
title: Leveraging Learned Image Prior for 3D Gaussian Compression
---

# Leveraging Learned Image Prior for 3D Gaussian Compression
**arXiv**：[2510.14705v1](https://arxiv.org/abs/2510.14705) · [PDF](https://arxiv.org/pdf/2510.14705.pdf)  
**作者**：Seungjoo Shin, Jaesik Park, Sunghyun Cho  

**一句话要点**：提出基于学习图像先验的3D高斯压缩框架，以提升率失真性能。

**关键词**：3D高斯压缩, 学习图像先验, 率失真优化, 压缩伪影恢复, 渲染质量提升

## 3 点简述
- 核心问题：现有3D高斯压缩方法缺乏学习先验，限制率失真权衡的进一步优化。
- 方法要点：利用学习图像先验和渲染残差，通过恢复网络减少压缩伪影并精炼高斯表示。
- 实验或效果：在广泛实验中，框架实现优越率失真性能，超越现有方法且存储需求更低。

## 摘要（原文）

> Compression techniques for 3D Gaussian Splatting (3DGS) have recently
> achieved considerable success in minimizing storage overhead for 3D Gaussians
> while preserving high rendering quality. Despite the impressive storage
> reduction, the lack of learned priors restricts further advances in the
> rate-distortion trade-off for 3DGS compression tasks. To address this, we
> introduce a novel 3DGS compression framework that leverages the powerful
> representational capacity of learned image priors to recover
> compression-induced quality degradation. Built upon initially compressed
> Gaussians, our restoration network effectively models the compression artifacts
> in the image space between degraded and original Gaussians. To enhance the
> rate-distortion performance, we provide coarse rendering residuals into the
> restoration network as side information. By leveraging the supervision of
> restored images, the compressed Gaussians are refined, resulting in a highly
> compact representation with enhanced rendering performance. Our framework is
> designed to be compatible with existing Gaussian compression methods, making it
> broadly applicable across different baselines. Extensive experiments validate
> the effectiveness of our framework, demonstrating superior rate-distortion
> performance and outperforming the rendering quality of state-of-the-art 3DGS
> compression methods while requiring substantially less storage.

