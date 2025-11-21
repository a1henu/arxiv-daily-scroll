---
layout: default
title: VTinker: Guided Flow Upsampling and Texture Mapping for High-Resolution Video Frame Interpolation
---

# VTinker: Guided Flow Upsampling and Texture Mapping for High-Resolution Video Frame Interpolation
**arXiv**：[2511.16124v1](https://arxiv.org/abs/2511.16124) · [PDF](https://arxiv.org/pdf/2511.16124.pdf)  
**作者**：Chenyang Wu, Jiayi Fu, Chun-Le Guo, Shuhao Han, Chongyi Li  

**一句话要点**：提出VTinker通过引导流上采样和纹理映射解决高分辨率视频帧插值中的模糊和伪影问题

**关键词**：视频帧插值, 引导流上采样, 纹理映射, 高分辨率处理, 运动估计优化

## 3 点简述
- 核心问题：低分辨率运动估计导致高分辨率帧插值出现模糊、马赛克和伪影
- 方法要点：使用引导流上采样和纹理映射生成中间代理帧以提升细节清晰度
- 实验或效果：在视频帧插值任务中达到最先进性能，代码已开源

## 摘要（原文）

> Due to large pixel movement and high computational cost, estimating the motion of high-resolution frames is challenging. Thus, most flow-based Video Frame Interpolation (VFI) methods first predict bidirectional flows at low resolution and then use high-magnification upsampling (e.g., bilinear) to obtain the high-resolution ones. However, this kind of upsampling strategy may cause blur or mosaic at the flows' edges. Additionally, the motion of fine pixels at high resolution cannot be adequately captured in motion estimation at low resolution, which leads to the misalignment of task-oriented flows. With such inaccurate flows, input frames are warped and combined pixel-by-pixel, resulting in ghosting and discontinuities in the interpolated frame. In this study, we propose a novel VFI pipeline, VTinker, which consists of two core components: guided flow upsampling (GFU) and Texture Mapping. After motion estimation at low resolution, GFU introduces input frames as guidance to alleviate the blurring details in bilinear upsampling flows, which makes flows' edges clearer. Subsequently, to avoid pixel-level ghosting and discontinuities, Texture Mapping generates an initial interpolated frame, referred to as the intermediate proxy. The proxy serves as a cue for selecting clear texture blocks from the input frames, which are then mapped onto the proxy to facilitate producing the final interpolated frame via a reconstruction module. Extensive experiments demonstrate that VTinker achieves state-of-the-art performance in VFI. Codes are available at: https://github.com/Wucy0519/VTinker.

