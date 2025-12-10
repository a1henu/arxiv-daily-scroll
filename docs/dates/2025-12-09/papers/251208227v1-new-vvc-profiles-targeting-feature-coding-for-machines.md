---
layout: default
title: New VVC profiles targeting Feature Coding for Machines
---

# New VVC profiles targeting Feature Coding for Machines
**arXiv**：[2512.08227v1](https://arxiv.org/abs/2512.08227) · [PDF](https://arxiv.org/pdf/2512.08227.pdf)  
**作者**：Md Eimran Hossain Eimon, Ashan Perera, Juan Merlos, Velibor Adzic, Hari Kalva  

**一句话要点**：提出三种轻量级VVC配置以优化面向机器的特征编码，提升压缩效率与编码速度。

**关键词**：特征编码, VVC配置, 压缩效率, 编码速度, MPEG-AI FCM, 下游任务准确性

## 3 点简述
- 核心问题：传统视频编码基于人类视觉优化，不适用于神经网络中间特征的抽象、稀疏和任务特定性。
- 方法要点：在MPEG-AI FCM标准下，分析VVC工具对特征压缩效率和下游任务准确性的影响，设计Fast、Faster、Fastest配置。
- 实验或效果：Fast配置提升2.96% BD-Rate并减少21.8%编码时间，Fastest配置减少95.6%编码时间仅损失1.71% BD-Rate。

## 摘要（原文）

> Modern video codecs have been extensively optimized to preserve perceptual quality, leveraging models of the human visual system. However, in split inference systems-where intermediate features from neural network are transmitted instead of pixel data-these assumptions no longer apply. Intermediate features are abstract, sparse, and task-specific, making perceptual fidelity irrelevant. In this paper, we investigate the use of Versatile Video Coding (VVC) for compressing such features under the MPEG-AI Feature Coding for Machines (FCM) standard. We perform a tool-level analysis to understand the impact of individual coding components on compression efficiency and downstream vision task accuracy. Based on these insights, we propose three lightweight essential VVC profiles-Fast, Faster, and Fastest. The Fast profile provides 2.96% BD-Rate gain while reducing encoding time by 21.8%. Faster achieves a 1.85% BD-Rate gain with a 51.5% speedup. Fastest reduces encoding time by 95.6% with only a 1.71% loss in BD-Rate.

