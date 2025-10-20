---
layout: default
title: DriveGen3D: Boosting Feed-Forward Driving Scene Generation with Efficient Video Diffusion
---

# DriveGen3D: Boosting Feed-Forward Driving Scene Generation with Efficient Video Diffusion
**arXiv**：[2510.15264v1](https://arxiv.org/abs/2510.15264) · [PDF](https://arxiv.org/pdf/2510.15264.pdf)  
**作者**：Weijie Wang, Jiagang Zhu, Zeyu Zhang, Xiaofeng Wang, Zheng Zhu, Guosheng Zhao, Chaojun Ni, Haoxiao Wang, Guan Huang, Xinze Chen, Yukun Zhou, Wenkang Qin, Duochao Shi, Haoyun Li, Guanghong Jia, Jiwen Lu  

**一句话要点**：提出DriveGen3D框架，通过高效视频扩散和3D重建生成可控动态驾驶场景。

**关键词**：驾驶场景生成, 视频扩散模型, 3D高斯重建, 多模态控制, 实时生成

## 3 点简述
- 现有方法计算成本高、缺乏3D表示或仅限静态场景，难以生成长期动态驾驶场景。
- 集成FastDrive-DiT和FastRecon3D，实现文本和BEV引导的视频合成与3D高斯重建。
- 实验显示可实时生成高分辨率视频和动态3D场景，SSIM达0.811，PSNR为22.84。

## 摘要（原文）

> We present DriveGen3D, a novel framework for generating high-quality and
> highly controllable dynamic 3D driving scenes that addresses critical
> limitations in existing methodologies. Current approaches to driving scene
> synthesis either suffer from prohibitive computational demands for extended
> temporal generation, focus exclusively on prolonged video synthesis without 3D
> representation, or restrict themselves to static single-scene reconstruction.
> Our work bridges this methodological gap by integrating accelerated long-term
> video generation with large-scale dynamic scene reconstruction through
> multimodal conditional control. DriveGen3D introduces a unified pipeline
> consisting of two specialized components: FastDrive-DiT, an efficient video
> diffusion transformer for high-resolution, temporally coherent video synthesis
> under text and Bird's-Eye-View (BEV) layout guidance; and FastRecon3D, a
> feed-forward reconstruction module that rapidly builds 3D Gaussian
> representations across time, ensuring spatial-temporal consistency. Together,
> these components enable real-time generation of extended driving videos (up to
> $424\times800$ at 12 FPS) and corresponding dynamic 3D scenes, achieving SSIM
> of 0.811 and PSNR of 22.84 on novel view synthesis, all while maintaining
> parameter efficiency.

