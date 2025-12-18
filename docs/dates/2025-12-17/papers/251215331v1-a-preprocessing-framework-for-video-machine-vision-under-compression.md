---
layout: default
title: A Preprocessing Framework for Video Machine Vision under Compression
---

# A Preprocessing Framework for Video Machine Vision under Compression
**arXiv**：[2512.15331v1](https://arxiv.org/abs/2512.15331) · [PDF](https://arxiv.org/pdf/2512.15331.pdf)  
**作者**：Fei Zhao, Mengxi Guo, Shijie Zhao, Junlin Li, Li Zhang, Xiaodong Xie  

**一句话要点**：提出面向机器视觉任务的视频预处理框架，以提升压缩视频的率-精度性能。

**关键词**：视频压缩, 机器视觉, 预处理框架, 率-精度优化, 可微分编解码器

## 3 点简述
- 核心问题：视频压缩优化多基于人类感知指标，忽略机器视觉系统的更高需求。
- 方法要点：引入神经预处理器保留关键信息，并采用可微分虚拟编解码器进行训练约束。
- 实验或效果：在多种骨干网络和下游任务上测试，相比标准编解码器可节省超过15%比特率。

## 摘要（原文）

> There has been a growing trend in compressing and transmitting videos from terminals for machine vision tasks. Nevertheless, most video coding optimization method focus on minimizing distortion according to human perceptual metrics, overlooking the heightened demands posed by machine vision systems. In this paper, we propose a video preprocessing framework tailored for machine vision tasks to address this challenge. The proposed method incorporates a neural preprocessor which retaining crucial information for subsequent tasks, resulting in the boosting of rate-accuracy performance. We further introduce a differentiable virtual codec to provide constraints on rate and distortion during the training stage. We directly apply widely used standard codecs for testing. Therefore, our solution can be easily applied to real-world scenarios. We conducted extensive experiments evaluating our compression method on two typical downstream tasks with various backbone networks. The experimental results indicate that our approach can save over 15% of bitrate compared to using only the standard codec anchor version.

