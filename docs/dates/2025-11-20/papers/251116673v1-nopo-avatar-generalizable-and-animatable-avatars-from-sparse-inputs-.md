---
layout: default
title: NoPo-Avatar: Generalizable and Animatable Avatars from Sparse Inputs without Human Poses
---

# NoPo-Avatar: Generalizable and Animatable Avatars from Sparse Inputs without Human Poses
**arXiv**：[2511.16673v1](https://arxiv.org/abs/2511.16673) · [PDF](https://arxiv.org/pdf/2511.16673.pdf)  
**作者**：Jing Wen, Alexander G. Schwing, Shenlong Wang  

**一句话要点**：提出NoPo-Avatar从稀疏图像重建可动画3D人体化身，无需人体姿态输入

**关键词**：3D人体重建, 可动画化身, 稀疏图像输入, 无姿态依赖, 鲁棒性提升

## 3 点简述
- 核心问题：从单张或稀疏图像重建可动画3D人体化身，现有方法依赖准确姿态输入易受噪声影响
- 方法要点：仅使用图像输入，消除测试时对人体姿态的依赖，提升鲁棒性和适用性
- 实验或效果：在THuman2.0等数据集上，无姿态输入时优于基线，有姿态输入时结果相当

## 摘要（原文）

> We tackle the task of recovering an animatable 3D human avatar from a single or a sparse set of images. For this task, beyond a set of images, many prior state-of-the-art methods use accurate "ground-truth" camera poses and human poses as input to guide reconstruction at test-time. We show that pose-dependent reconstruction degrades results significantly if pose estimates are noisy. To overcome this, we introduce NoPo-Avatar, which reconstructs avatars solely from images, without any pose input. By removing the dependence of test-time reconstruction on human poses, NoPo-Avatar is not affected by noisy human pose estimates, making it more widely applicable. Experiments on challenging THuman2.0, XHuman, and HuGe100K data show that NoPo-Avatar outperforms existing baselines in practical settings (without ground-truth poses) and delivers comparable results in lab settings (with ground-truth poses).

