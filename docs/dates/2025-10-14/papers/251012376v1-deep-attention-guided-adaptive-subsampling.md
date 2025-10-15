---
layout: default
title: Deep Attention-guided Adaptive Subsampling
---

# Deep Attention-guided Adaptive Subsampling
**arXiv**：[2510.12376v1](https://arxiv.org/abs/2510.12376) · [PDF](https://arxiv.org/pdf/2510.12376.pdf)  
**作者**：Sharath M Shankaranarayana, Soumava Kumar Roy, Prasad Sudhakar, Chandan Aladahalli  

**一句话要点**：提出注意力引导自适应子采样框架，以降低3D医学影像和视频分类的计算复杂度。

**关键词**：自适应子采样, 注意力机制, 3D医学影像分类, 视频分类, 计算复杂度优化

## 3 点简述
- 核心问题：深度神经网络计算复杂度高，且现有子采样方法无法根据输入动态调整。
- 方法要点：使用注意力机制实现输入自适应子采样，克服不可微操作挑战。
- 实验或效果：在MedMNIST3D和超声视频数据集上验证，提升性能并减少计算量。

## 摘要（原文）

> Although deep neural networks have provided impressive gains in performance,
> these improvements often come at the cost of increased computational complexity
> and expense. In many cases, such as 3D volume or video classification tasks,
> not all slices or frames are necessary due to inherent redundancies. To address
> this issue, we propose a novel learnable subsampling framework that can be
> integrated into any neural network architecture. Subsampling, being a
> nondifferentiable operation, poses significant challenges for direct adaptation
> into deep learning models. While some works, have proposed solutions using the
> Gumbel-max trick to overcome the problem of non-differentiability, they fall
> short in a crucial aspect: they are only task-adaptive and not inputadaptive.
> Once the sampling mechanism is learned, it remains static and does not adjust
> to different inputs, making it unsuitable for real-world applications. To this
> end, we propose an attention-guided sampling module that adapts to inputs even
> during inference. This dynamic adaptation results in performance gains and
> reduces complexity in deep neural network models. We demonstrate the
> effectiveness of our method on 3D medical imaging datasets from MedMNIST3D as
> well as two ultrasound video datasets for classification tasks, one of them
> being a challenging in-house dataset collected under real-world clinical
> conditions.

