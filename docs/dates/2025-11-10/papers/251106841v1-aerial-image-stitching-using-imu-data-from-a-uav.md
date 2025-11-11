---
layout: default
title: Aerial Image Stitching Using IMU Data from a UAV
---

# Aerial Image Stitching Using IMU Data from a UAV
**arXiv**：[2511.06841v1](https://arxiv.org/abs/2511.06841) · [PDF](https://arxiv.org/pdf/2511.06841.pdf)  
**作者**：Selim Ahmet Iz, Mustafa Unel  

**一句话要点**：提出结合IMU数据与计算机视觉的无人机航拍图像拼接方法，以提升大位移和旋转场景下的精度。

**关键词**：无人机图像拼接, IMU数据融合, 单应性矩阵, 透视畸变校正, 特征匹配优化

## 3 点简述
- 核心问题：特征检测与匹配在无人机图像拼接中易出错，尤其在位移和旋转大时。
- 方法要点：利用IMU数据估计位移和旋转，校正透视畸变，计算单应性矩阵进行图像对齐。
- 实验或效果：实验显示方法在挑战性场景下优于特征基算法，准确性和鲁棒性更高。

## 摘要（原文）

> Unmanned Aerial Vehicles (UAVs) are widely used for aerial photography and
> remote sensing applications. One of the main challenges is to stitch together
> multiple images into a single high-resolution image that covers a large area.
> Featurebased image stitching algorithms are commonly used but can suffer from
> errors and ambiguities in feature detection and matching. To address this,
> several approaches have been proposed, including using bundle adjustment
> techniques or direct image alignment. In this paper, we present a novel method
> that uses a combination of IMU data and computer vision techniques for
> stitching images captured by a UAV. Our method involves several steps such as
> estimating the displacement and rotation of the UAV between consecutive images,
> correcting for perspective distortion, and computing a homography matrix. We
> then use a standard image stitching algorithm to align and blend the images
> together. Our proposed method leverages the additional information provided by
> the IMU data, corrects for various sources of distortion, and can be easily
> integrated into existing UAV workflows. Our experiments demonstrate the
> effectiveness and robustness of our method, outperforming some of the existing
> feature-based image stitching algorithms in terms of accuracy and reliability,
> particularly in challenging scenarios such as large displacements, rotations,
> and variations in camera pose.

