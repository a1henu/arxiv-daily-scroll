---
layout: default
title: Blur2seq: Blind Deblurring and Camera Trajectory Estimation from a Single Camera Motion-blurred Image
---

# Blur2seq: Blind Deblurring and Camera Trajectory Estimation from a Single Camera Motion-blurred Image
**arXiv**：[2510.20539v1](https://arxiv.org/abs/2510.20539) · [PDF](https://arxiv.org/pdf/2510.20539.pdf)  
**作者**：Guillermo Carbajal, Andrés Almansa, Pablo Musé  

**一句话要点**：提出Blur2seq框架，从单张运动模糊图像联合估计清晰图像和相机轨迹

**关键词**：盲去模糊, 相机轨迹估计, 运动模糊模型, 深度学习, 图像恢复

## 3 点简述
- 核心问题：相机抖动导致运动模糊，尤其在严重或空间变化模糊下图像恢复困难
- 方法要点：使用可微分模糊模块和神经网络预测3D旋转轨迹，端到端训练模型
- 实验或效果：在合成和真实数据集上达到先进性能，优于端到端去模糊网络

## 摘要（原文）

> Motion blur caused by camera shake, particularly under large or rotational
> movements, remains a major challenge in image restoration. We propose a deep
> learning framework that jointly estimates the latent sharp image and the
> underlying camera motion trajectory from a single blurry image. Our method
> leverages the Projective Motion Blur Model (PMBM), implemented efficiently
> using a differentiable blur creation module compatible with modern networks. A
> neural network predicts a full 3D rotation trajectory, which guides a
> model-based restoration network trained end-to-end. This modular architecture
> provides interpretability by revealing the camera motion that produced the
> blur. Moreover, this trajectory enables the reconstruction of the sequence of
> sharp images that generated the observed blurry image. To further refine
> results, we optimize the trajectory post-inference via a reblur loss, improving
> consistency between the blurry input and the restored output. Extensive
> experiments show that our method achieves state-of-the-art performance on both
> synthetic and real datasets, particularly in cases with severe or spatially
> variant blur, where end-to-end deblurring networks struggle.
>   Code and trained models are available at
> https://github.com/GuillermoCarbajal/Blur2Seq/

