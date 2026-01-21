---
layout: default
title: Rig-Aware 3D Reconstruction of Vehicle Undercarriages using Gaussian Splatting
---

# Rig-Aware 3D Reconstruction of Vehicle Undercarriages using Gaussian Splatting
**arXiv**：[2601.14208v1](https://arxiv.org/abs/2601.14208) · [PDF](https://arxiv.org/pdf/2601.14208.pdf)  
**作者**：Nitin Kulkarni, Akhil Devarashetti, Charlie Cluss, Livio Forte, Dan Buckmaster, Philip Schneider, Chunming Qiao, Alina Vereshchaka  

**一句话要点**：提出基于相机阵列感知的SfM与高斯溅射方法，实现车辆底盘实时交互式3D重建以提升检测效率。

**关键词**：车辆底盘3D重建, 相机阵列感知SfM, 高斯溅射渲染, 低视差场景处理, 实时交互模型

## 3 点简述
- 核心问题：车辆底盘检测依赖人工爬行检查，效率低且在线买家难以查看底盘照片。
- 方法要点：集成相机阵列几何先验、约束匹配策略与高斯溅射，克服广角畸变和低视差场景挑战。
- 实验或效果：生成高质量稀疏点云和实时渲染的逼真3D模型，提升检测速度和买家信心。

## 摘要（原文）

> Inspecting the undercarriage of used vehicles is a labor-intensive task that requires inspectors to crouch or crawl underneath each vehicle to thoroughly examine it. Additionally, online buyers rarely see undercarriage photos. We present an end-to-end pipeline that utilizes a three-camera rig to capture videos of the undercarriage as the vehicle drives over it, and produces an interactive 3D model of the undercarriage. The 3D model enables inspectors and customers to rotate, zoom, and slice through the undercarriage, allowing them to detect rust, leaks, or impact damage in seconds, thereby improving both workplace safety and buyer confidence. Our primary contribution is a rig-aware Structure-from-Motion (SfM) pipeline specifically designed to overcome the challenges of wide-angle lens distortion and low-parallax scenes. Our method overcomes the challenges of wide-angle lens distortion and low-parallax scenes by integrating precise camera calibration, synchronized video streams, and strong geometric priors from the camera rig. We use a constrained matching strategy with learned components, the DISK feature extractor, and the attention-based LightGlue matcher to generate high-quality sparse point clouds that are often unattainable with standard SfM pipelines. These point clouds seed the Gaussian splatting process to generate photorealistic undercarriage models that render in real-time. Our experiments and ablation studies demonstrate that our design choices are essential to achieve state-of-the-art quality.

