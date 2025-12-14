---
layout: default
title: MotionEdit: Benchmarking and Learning Motion-Centric Image Editing
---

# MotionEdit: Benchmarking and Learning Motion-Centric Image Editing
**arXiv**：[2512.10284v1](https://arxiv.org/abs/2512.10284) · [PDF](https://arxiv.org/pdf/2512.10284.pdf)  
**作者**：Yixin Wan, Lei Ke, Wenhao Yu, Kai-Wei Chang, Dong Yu  

**一句话要点**：提出MotionEdit数据集与MotionNFT框架以解决运动中心图像编辑任务中的挑战

**关键词**：运动中心图像编辑, 数据集构建, 扩散模型微调, 运动对齐奖励, 视频合成, 图像编辑基准

## 3 点简述
- 核心问题：现有图像编辑数据集缺乏高质量运动变换，导致模型在修改主体动作时性能不足
- 方法要点：基于视频提取高保真图像对构建MotionEdit数据集，并设计MotionNFT框架通过运动对齐奖励微调模型
- 实验或效果：在FLUX.1 Kontext和Qwen-Image-Edit上验证，MotionNFT提升编辑质量和运动保真度，不损害通用编辑能力

## 摘要（原文）

> We introduce MotionEdit, a novel dataset for motion-centric image editing-the task of modifying subject actions and interactions while preserving identity, structure, and physical plausibility. Unlike existing image editing datasets that focus on static appearance changes or contain only sparse, low-quality motion edits, MotionEdit provides high-fidelity image pairs depicting realistic motion transformations extracted and verified from continuous videos. This new task is not only scientifically challenging but also practically significant, powering downstream applications such as frame-controlled video synthesis and animation.
>   To evaluate model performance on the novel task, we introduce MotionEdit-Bench, a benchmark that challenges models on motion-centric edits and measures model performance with generative, discriminative, and preference-based metrics. Benchmark results reveal that motion editing remains highly challenging for existing state-of-the-art diffusion-based editing models. To address this gap, we propose MotionNFT (Motion-guided Negative-aware Fine Tuning), a post-training framework that computes motion alignment rewards based on how well the motion flow between input and model-edited images matches the ground-truth motion, guiding models toward accurate motion transformations. Extensive experiments on FLUX.1 Kontext and Qwen-Image-Edit show that MotionNFT consistently improves editing quality and motion fidelity of both base models on the motion editing task without sacrificing general editing ability, demonstrating its effectiveness.

