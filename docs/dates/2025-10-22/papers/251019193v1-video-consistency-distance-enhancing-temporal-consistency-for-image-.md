---
layout: default
title: Video Consistency Distance: Enhancing Temporal Consistency for Image-to-Video Generation via Reward-Based Fine-Tuning
---

# Video Consistency Distance: Enhancing Temporal Consistency for Image-to-Video Generation via Reward-Based Fine-Tuning
**arXiv**：[2510.19193v1](https://arxiv.org/abs/2510.19193) · [PDF](https://arxiv.org/pdf/2510.19193.pdf)  
**作者**：Takehiro Aoshima, Yusuke Shinohara, Park Byeongseon  

**一句话要点**：提出视频一致性距离以增强图像到视频生成中的时序一致性

**关键词**：图像到视频生成, 奖励微调, 时序一致性, 频域分析, 视频扩散模型

## 3 点简述
- 核心问题：基于奖励的微调在图像到视频生成中常导致时序一致性不足
- 方法要点：定义视频一致性距离，在频域分析视频帧特征以提升时序一致性
- 实验或效果：多数据集实验显示，微调后时序一致性显著增强，其他性能未下降

## 摘要（原文）

> Reward-based fine-tuning of video diffusion models is an effective approach
> to improve the quality of generated videos, as it can fine-tune models without
> requiring real-world video datasets. However, it can sometimes be limited to
> specific performances because conventional reward functions are mainly aimed at
> enhancing the quality across the whole generated video sequence, such as
> aesthetic appeal and overall consistency. Notably, the temporal consistency of
> the generated video often suffers when applying previous approaches to
> image-to-video (I2V) generation tasks. To address this limitation, we propose
> Video Consistency Distance (VCD), a novel metric designed to enhance temporal
> consistency, and fine-tune a model with the reward-based fine-tuning framework.
> To achieve coherent temporal consistency relative to a conditioning image, VCD
> is defined in the frequency space of video frame features to capture frame
> information effectively through frequency-domain analysis. Experimental results
> across multiple I2V datasets demonstrate that fine-tuning a video generation
> model with VCD significantly enhances temporal consistency without degrading
> other performance compared to the previous method.

