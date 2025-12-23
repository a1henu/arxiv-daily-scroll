---
layout: default
title: MixFlow Training: Alleviating Exposure Bias with Slowed Interpolation Mixture
---

# MixFlow Training: Alleviating Exposure Bias with Slowed Interpolation Mixture
**arXiv**：[2512.19311v1](https://arxiv.org/abs/2512.19311) · [PDF](https://arxiv.org/pdf/2512.19311.pdf)  
**作者**：Hui Li, Jiayue Lyu, Fu-Yun Wang, Kaihui Cheng, Siyu Zhu, Jingdong Wang  

**一句话要点**：提出MixFlow训练方法，通过减缓插值混合缓解扩散模型中的曝光偏差问题

**关键词**：扩散模型, 曝光偏差, 训练策略, 图像生成, 慢流现象

## 3 点简述
- 核心问题：扩散模型训练与测试阶段输入不一致导致曝光偏差，影响生成质量
- 方法要点：利用慢流现象，在训练时引入减缓时间步的插值混合进行后训练
- 实验或效果：在类条件图像生成和文本到图像生成任务中验证有效性，RAE模型在ImageNet上取得低FID分数

## 摘要（原文）

> This paper studies the training-testing discrepancy (a.k.a. exposure bias) problem for improving the diffusion models. During training, the input of a prediction network at one training timestep is the corresponding ground-truth noisy data that is an interpolation of the noise and the data, and during testing, the input is the generated noisy data. We present a novel training approach, named MixFlow, for improving the performance. Our approach is motivated by the Slow Flow phenomenon: the ground-truth interpolation that is the nearest to the generated noisy data at a given sampling timestep is observed to correspond to a higher-noise timestep (termed slowed timestep), i.e., the corresponding ground-truth timestep is slower than the sampling timestep. MixFlow leverages the interpolations at the slowed timesteps, named slowed interpolation mixture, for post-training the prediction network for each training timestep. Experiments over class-conditional image generation (including SiT, REPA, and RAE) and text-to-image generation validate the effectiveness of our approach. Our approach MixFlow over the RAE models achieve strong generation results on ImageNet: 1.43 FID (without guidance) and 1.10 (with guidance) at 256 x 256, and 1.55 FID (without guidance) and 1.10 (with guidance) at 512 x 512.

