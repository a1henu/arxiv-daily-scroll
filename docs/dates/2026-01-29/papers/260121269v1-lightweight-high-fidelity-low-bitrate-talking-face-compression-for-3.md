---
layout: default
title: Lightweight High-Fidelity Low-Bitrate Talking Face Compression for 3D Video Conference
---

# Lightweight High-Fidelity Low-Bitrate Talking Face Compression for 3D Video Conference
**arXiv**：[2601.21269v1](https://arxiv.org/abs/2601.21269) · [PDF](https://arxiv.org/pdf/2601.21269.pdf)  
**作者**：Jianglong Li, Jun Xu, Bingcong Lu, Zhengxue Cheng, Hongwei Hu, Ronghua Wu, Li Song  

**一句话要点**：提出轻量级高保真低码率3D说话人脸压缩框架，集成参数化建模与神经渲染，适用于实时3D视频会议。

**关键词**：3D视频会议, 说话人脸压缩, 参数化建模, 神经渲染, 低码率传输, 高斯泼溅

## 3 点简述
- 核心问题：传统2D压缩难以保留3D人脸细节，NeRF等方法计算成本高，低码率下实现高保真3D说话人脸表示是挑战。
- 方法要点：基于FLAME参数化建模与3D高斯泼溅神经渲染，传输少量面部元数据，采用高斯属性压缩和MLP优化提升效率。
- 实验或效果：在极低码率下实现优越的率失真性能，提供高质量面部渲染，适合实时3D视频会议应用。

## 摘要（原文）

> The demand for immersive and interactive communication has driven advancements in 3D video conferencing, yet achieving high-fidelity 3D talking face representation at low bitrates remains a challenge. Traditional 2D video compression techniques fail to preserve fine-grained geometric and appearance details, while implicit neural rendering methods like NeRF suffer from prohibitive computational costs. To address these challenges, we propose a lightweight, high-fidelity, low-bitrate 3D talking face compression framework that integrates FLAME-based parametric modeling with 3DGS neural rendering. Our approach transmits only essential facial metadata in real time, enabling efficient reconstruction with a Gaussian-based head model. Additionally, we introduce a compact representation and compression scheme, including Gaussian attribute compression and MLP optimization, to enhance transmission efficiency. Experimental results demonstrate that our method achieves superior rate-distortion performance, delivering high-quality facial rendering at extremely low bitrates, making it well-suited for real-time 3D video conferencing applications.

