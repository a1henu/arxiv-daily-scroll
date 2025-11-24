---
layout: default
title: Sparse Reasoning is Enough: Biological-Inspired Framework for Video Anomaly Detection with Large Pre-trained Models
---

# Sparse Reasoning is Enough: Biological-Inspired Framework for Video Anomaly Detection with Large Pre-trained Models
**arXiv**：[2511.17094v1](https://arxiv.org/abs/2511.17094) · [PDF](https://arxiv.org/pdf/2511.17094.pdf)  
**作者**：He Huang, Zixuan Hu, Dongxiao Li, Yao Xiao, Ling-Yu Duan  

**一句话要点**：提出ReCoVAD框架以稀疏推理实现高效视频异常检测

**关键词**：视频异常检测, 稀疏推理, 预训练模型, 仿生框架, 训练免费方法

## 3 点简述
- 核心问题：密集帧推理在视频异常检测中计算成本高，是否必要未知
- 方法要点：仿生双通路设计，反射通路快速响应，意识通路精炼更新
- 实验效果：在UCF-Crime和XD-Violence数据集上处理帧数减少，性能领先

## 摘要（原文）

> Video anomaly detection (VAD) plays a vital role in real-world applications such as security surveillance, autonomous driving, and industrial monitoring. Recent advances in large pre-trained models have opened new opportunities for training-free VAD by leveraging rich prior knowledge and general reasoning capabilities. However, existing studies typically rely on dense frame-level inference, incurring high computational costs and latency. This raises a fundamental question: Is dense reasoning truly necessary when using powerful pre-trained models in VAD systems? To answer this, we propose ReCoVAD, a novel framework inspired by the dual reflex and conscious pathways of the human nervous system, enabling selective frame processing to reduce redundant computation. ReCoVAD consists of two core pathways: (i) a Reflex pathway that uses a lightweight CLIP-based module to fuse visual features with prototype prompts and produce decision vectors, which query a dynamic memory of past frames and anomaly scores for fast response; and (ii) a Conscious pathway that employs a medium-scale vision-language model to generate textual event descriptions and refined anomaly scores for novel frames. It continuously updates the memory and prototype prompts, while an integrated large language model periodically reviews accumulated descriptions to identify unseen anomalies, correct errors, and refine prototypes. Extensive experiments show that ReCoVAD achieves state-of-the-art training-free performance while processing only 28.55\% and 16.04\% of the frames used by previous methods on the UCF-Crime and XD-Violence datasets, demonstrating that sparse reasoning is sufficient for effective large-model-based VAD.

