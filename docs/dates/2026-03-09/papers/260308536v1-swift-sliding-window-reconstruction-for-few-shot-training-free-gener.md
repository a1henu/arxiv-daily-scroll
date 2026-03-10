---
layout: default
title: SWIFT: Sliding Window Reconstruction for Few-Shot Training-Free Generated Video Attribution
---

# SWIFT: Sliding Window Reconstruction for Few-Shot Training-Free Generated Video Attribution
**arXiv**：[2603.08536v1](https://arxiv.org/abs/2603.08536) · [PDF](https://arxiv.org/pdf/2603.08536.pdf)  
**作者**：Chao Wang, Zijin Yang, Yaofei Wang, Yuang Qi, Weiming Zhang, Nenghai Yu, Kejiang Chen  

**一句话要点**：提出SWIFT方法，通过滑动窗口重建实现少样本免训练生成视频溯源

**关键词**：生成视频溯源, 少样本学习, 免训练方法, 滑动窗口重建, 时间特性分析

## 3 点简述
- 核心问题：生成视频溯源需额外操作或训练模型，可能降低质量或需大量样本。
- 方法要点：利用视频时间特性，通过滑动窗口进行正常与损坏重建，以损失差异作为溯源信号。
- 实验或效果：在五个SOTA模型上，仅用20样本实现超90%平均溯源准确率，部分模型支持零样本溯源。

## 摘要（原文）

> Recent advancements in video generation technologies have been significant, resulting in their widespread application across multiple domains. However, concerns have been mounting over the potential misuse of generated content. Tracing the origin of generated videos has become crucial to mitigate potential misuse and identify responsible parties. Existing video attribution methods require additional operations or the training of source attribution models, which may degrade video quality or necessitate large amounts of training samples. To address these challenges, we define for the first time the "few-shot training-free generated video attribution" task and propose SWIFT, which is tightly integrated with the temporal characteristics of the video. By leveraging the "Pixel Frames(many) to Latent Frame(one)" temporal mapping within each video chunk, SWIFT applies a fixed-length sliding window to perform two distinct reconstructions: normal and corrupted. The variation in the losses between two reconstructions is then used as an attribution signal. We conducted an extensive evaluation of five state-of-the-art (SOTA) video generation models. Experimental results show that SWIFT achieves over 90% average attribution accuracy with merely 20 video samples across all models and even enables zero-shot attribution for HunyuanVideo, EasyAnimate, and Wan2.2. Our source code is available at https://github.com/wangchao0708/SWIFT.

