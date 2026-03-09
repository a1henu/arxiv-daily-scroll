---
layout: default
title: SLER-IR: Spherical Layer-wise Expert Routing for All-in-One Image Restoration
---

# SLER-IR: Spherical Layer-wise Expert Routing for All-in-One Image Restoration
**arXiv**：[2603.05940v1](https://arxiv.org/abs/2603.05940) · [PDF](https://arxiv.org/pdf/2603.05940.pdf)  
**作者**：Peng Shurui, Xin Lin, Shi Luo, Jincen Ou, Dizhe Zhang, Lu Qi, Truong Nguyen, Chao Ren  

**一句话要点**：提出SLER-IR框架，通过球形专家路由解决多退化图像恢复中的特征干扰问题

**关键词**：图像恢复, 专家路由, 球形嵌入, 退化表示, 多任务学习, 对比学习

## 3 点简述
- 核心问题：统一框架在多退化图像恢复中面临特征干扰和专家专业化不足的挑战
- 方法要点：引入球形均匀退化嵌入和全局-局部粒度融合模块，动态激活层间专家
- 实验或效果：在三任务和五任务基准测试中，PSNR和SSIM指标均优于现有方法

## 摘要（原文）

> Image restoration under diverse degradations remains challenging for unified all-in-one frameworks due to feature interference and insufficient expert specialization. We propose SLER-IR, a spherical layer-wise expert routing framework that dynamically activates specialized experts across network layers. To ensure reliable routing, we introduce a Spherical Uniform Degradation Embedding with contrastive learning, which maps degradation representations onto a hypersphere to eliminate geometry bias in linear embedding spaces. In addition, a Global-Local Granularity Fusion (GLGF) module integrates global semantics and local degradation cues to address spatially non-uniform degradations and the train-test granularity gap. Experiments on three-task and five-task benchmarks demonstrate that SLER-IR achieves consistent improvements over state-of-the-art methods in both PSNR and SSIM. Code and models will be publicly released.

