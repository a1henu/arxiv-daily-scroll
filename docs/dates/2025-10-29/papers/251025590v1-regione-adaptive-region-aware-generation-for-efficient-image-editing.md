---
layout: default
title: RegionE: Adaptive Region-Aware Generation for Efficient Image Editing
---

# RegionE: Adaptive Region-Aware Generation for Efficient Image Editing
**arXiv**：[2510.25590v1](https://arxiv.org/abs/2510.25590) · [PDF](https://arxiv.org/pdf/2510.25590.pdf)  
**作者**：Pengtao Chen, Xianfang Zeng, Maosen Zhao, Mingzhu Shen, Peng Ye, Bangyin Xiang, Zhibo Wang, Wei Cheng, Gang Yu, Tao Chen  

**一句话要点**：提出RegionE自适应区域感知生成框架，以加速指令图像编辑任务。

**关键词**：指令图像编辑, 区域感知生成, 自适应分区, 去噪加速, KV缓存

## 3 点简述
- 核心问题：现有指令图像编辑模型未区分编辑与未编辑区域，导致计算冗余。
- 方法要点：自适应区域分区、区域感知生成和自适应速度衰减缓存。
- 实验效果：在多个基准模型上实现2倍以上加速，保持语义和感知保真度。

## 摘要（原文）

> Recently, instruction-based image editing (IIE) has received widespread
> attention. In practice, IIE often modifies only specific regions of an image,
> while the remaining areas largely remain unchanged. Although these two types of
> regions differ significantly in generation difficulty and computational
> redundancy, existing IIE models do not account for this distinction, instead
> applying a uniform generation process across the entire image. This motivates
> us to propose RegionE, an adaptive, region-aware generation framework that
> accelerates IIE tasks without additional training. Specifically, the RegionE
> framework consists of three main components: 1) Adaptive Region Partition. We
> observed that the trajectory of unedited regions is straight, allowing for
> multi-step denoised predictions to be inferred in a single step. Therefore, in
> the early denoising stages, we partition the image into edited and unedited
> regions based on the difference between the final estimated result and the
> reference image. 2) Region-Aware Generation. After distinguishing the regions,
> we replace multi-step denoising with one-step prediction for unedited areas.
> For edited regions, the trajectory is curved, requiring local iterative
> denoising. To improve the efficiency and quality of local iterative generation,
> we propose the Region-Instruction KV Cache, which reduces computational cost
> while incorporating global information. 3) Adaptive Velocity Decay Cache.
> Observing that adjacent timesteps in edited regions exhibit strong velocity
> similarity, we further propose an adaptive velocity decay cache to accelerate
> the local denoising process. We applied RegionE to state-of-the-art IIE base
> models, including Step1X-Edit, FLUX.1 Kontext, and Qwen-Image-Edit. RegionE
> achieved acceleration factors of 2.57, 2.41, and 2.06. Evaluations by GPT-4o
> confirmed that semantic and perceptual fidelity were well preserved.

