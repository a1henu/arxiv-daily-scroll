---
layout: default
title: BiEvLight: Bi-level Learning of Task-Aware Event Refinement for Low-Light Image Enhancement
---

# BiEvLight: Bi-level Learning of Task-Aware Event Refinement for Low-Light Image Enhancement
**arXiv**：[2603.04975v1](https://arxiv.org/abs/2603.04975) · [PDF](https://arxiv.org/pdf/2603.04975.pdf)  
**作者**：Zishu Yao, Xiang-Xiang Su, Shengning Zhou, Guang-Yong Chen, Guodong Fan, Xing Chen  

**一句话要点**：提出BiEvLight框架，通过双层优化协同去噪与增强，解决低光图像增强中事件噪声耦合问题。

**关键词**：低光图像增强, 事件相机, 双层优化, 任务感知去噪, 模态融合, 梯度引导

## 3 点简述
- 核心问题：事件相机固有背景活动噪声与图像低信噪比导致模态融合时噪声耦合，限制低光增强性能。
- 方法要点：利用图像与事件梯度相关性构建梯度引导去噪先验，并采用双层优化将事件去噪约束于增强任务，实现任务感知协同优化。
- 实验或效果：在SDE数据集上显著优于现有方法，PSNR平均提升1.30dB，PSNR*提升2.03dB，SSIM提升0.047。

## 摘要（原文）

> Event cameras, with their high dynamic range, show great promise for Low-light Image Enhancement (LLIE). Existing works primarily focus on designing effective modal fusion strategies. However, a key challenge is the dual degradation from intrinsic background activity (BA) noise in events and low signal-to-noise ratio (SNR) in images, which causes severe noise coupling during modal fusion, creating a critical performance bottleneck. We therefore posit that precise event denoising is the prerequisite to unlocking the full potential of event-based fusion. To this end, we propose BiEvLight, a hierarchical and task-aware framework that collaboratively optimizes enhancement and denoising by exploiting their intrinsic interdependence. Specifically, BiEvLight exploits the strong gradient correlation between images and events to build a gradient-guided event denoising prior that alleviates insufficient denoising in heavily noisy regions. Moreover, instead of treating event denoising as a static pre-processing stage-which inevitably incurs a trade-off between over- and under-denoising and cannot adapt to the requirements of a specific enhancement objective-we recast it as a bilevel optimization problem constrained by the enhancement task. Through cross-task interaction, the upper-level denoising problem learns event representations tailored to the lower-level enhancement objective, thereby substantially improving overall enhancement quality. Extensive experiments on the Real-world noise Dataset SDE demonstrate that our method significantly outperforms state-of-the-art (SOTA) approaches, with average improvements of 1.30dB in PSNR, 2.03dB in PSNR* and 0.047 in SSIM, respectively. The code will be publicly available at https://github.com/iijjlk/BiEvlight.

