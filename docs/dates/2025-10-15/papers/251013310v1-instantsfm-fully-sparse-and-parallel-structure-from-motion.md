---
layout: default
title: InstantSfM: Fully Sparse and Parallel Structure-from-Motion
---

# InstantSfM: Fully Sparse and Parallel Structure-from-Motion
**arXiv**：[2510.13310v1](https://arxiv.org/abs/2510.13310) · [PDF](https://arxiv.org/pdf/2510.13310.pdf)  
**作者**：Jiankun Zhong, Zitong Zhan, Quankai Gao, Ziyu Chen, Haozhe Lou, Jiageng Mao, Ulrich Neumann, Yue Wang  

**一句话要点**：提出全稀疏并行SfM方法以加速大规模场景重建

**关键词**：结构从运动, GPU并行计算, 稀疏束调整, 大规模重建, 全局定位优化

## 3 点简述
- 传统SfM方法在大型场景中计算开销大，精度与速度难以兼顾
- 利用GPU并行计算优化BA和GP，实现全稀疏统一框架
- 实验显示在5000图像数据集上速度提升40倍，精度相当或更高

## 摘要（原文）

> Structure-from-Motion (SfM), a method that recovers camera poses and scene
> geometry from uncalibrated images, is a central component in robotic
> reconstruction and simulation. Despite the state-of-the-art performance of
> traditional SfM methods such as COLMAP and its follow-up work, GLOMAP, naive
> CPU-specialized implementations of bundle adjustment (BA) or global positioning
> (GP) introduce significant computational overhead when handling large-scale
> scenarios, leading to a trade-off between accuracy and speed in SfM. Moreover,
> the blessing of efficient C++-based implementations in COLMAP and GLOMAP comes
> with the curse of limited flexibility, as they lack support for various
> external optimization options. On the other hand, while deep learning based SfM
> pipelines like VGGSfM and VGGT enable feed-forward 3D reconstruction, they are
> unable to scale to thousands of input views at once as GPU memory consumption
> increases sharply as the number of input views grows. In this paper, we unleash
> the full potential of GPU parallel computation to accelerate each critical
> stage of the standard SfM pipeline. Building upon recent advances in
> sparse-aware bundle adjustment optimization, our design extends these
> techniques to accelerate both BA and GP within a unified global SfM framework.
> Through extensive experiments on datasets of varying scales (e.g. 5000 images
> where VGGSfM and VGGT run out of memory), our method demonstrates up to about
> 40 times speedup over COLMAP while achieving consistently comparable or even
> improved reconstruction accuracy. Our project page can be found at
> https://cre185.github.io/InstantSfM/.

