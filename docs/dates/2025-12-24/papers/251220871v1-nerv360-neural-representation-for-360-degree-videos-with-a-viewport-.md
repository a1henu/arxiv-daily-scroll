---
layout: default
title: NeRV360: Neural Representation for 360-Degree Videos with a Viewport Decoder
---

# NeRV360: Neural Representation for 360-Degree Videos with a Viewport Decoder
**arXiv**：[2512.20871v1](https://arxiv.org/abs/2512.20871) · [PDF](https://arxiv.org/pdf/2512.20871.pdf)  
**作者**：Daichi Arai, Kyohei Unno, Yasuko Sugito, Yuichi Kusakabe  

**一句话要点**：提出NeRV360框架，通过视口解码解决360度视频中隐式神经表示的内存和速度问题。

**关键词**：360度视频压缩, 隐式神经表示, 视口解码, 时空仿射变换, 条件解码

## 3 点简述
- 核心问题：隐式神经表示应用于高分辨率360度视频时内存占用高、解码慢，难以实时应用。
- 方法要点：集成视口提取到解码过程，引入时空仿射变换模块，基于视点和时间进行条件解码。
- 实验或效果：在6K分辨率视频上，相比HNeRV，内存消耗降低7倍，解码速度提升2.5倍，图像质量更优。

## 摘要（原文）

> Implicit neural representations for videos (NeRV) have shown strong potential for video compression. However, applying NeRV to high-resolution 360-degree videos causes high memory usage and slow decoding, making real-time applications impractical. We propose NeRV360, an end-to-end framework that decodes only the user-selected viewport instead of reconstructing the entire panoramic frame. Unlike conventional pipelines, NeRV360 integrates viewport extraction into decoding and introduces a spatial-temporal affine transform module for conditional decoding based on viewpoint and time. Experiments on 6K-resolution videos show that NeRV360 achieves a 7-fold reduction in memory consumption and a 2.5-fold increase in decoding speed compared to HNeRV, a representative prior work, while delivering better image quality in terms of objective metrics.

