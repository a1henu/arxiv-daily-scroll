---
layout: default
title: GorillaWatch: An Automated System for In-the-Wild Gorilla Re-Identification and Population Monitoring
---

# GorillaWatch: An Automated System for In-the-Wild Gorilla Re-Identification and Population Monitoring
**arXiv**：[2512.07776v1](https://arxiv.org/abs/2512.07776) · [PDF](https://arxiv.org/pdf/2512.07776.pdf)  
**作者**：Maximilian Schall, Felix Leonard Knöfel, Noah Elias König, Jan Jonas Kubeler, Maximilian von Klinski, Joan Wilhelm Linnemann, Xiaoshi Liu, Iven Jelle Schlegelmilch, Ole Woyciniuk, Alexandra Schild, Dante Wasmuht, Magdalena Bermejo Espinet, German Illera Basas, Gerard de Melo  

**一句话要点**：提出GorillaWatch系统以解决野外大猩猩重识别与种群监测的自动化难题

**关键词**：野生动物重识别, 多目标跟踪, 自监督学习, 种群监测, 相机陷阱视频, 跨域泛化

## 3 点简述
- 核心问题：缺乏大规模野外视频数据集，阻碍自动化重识别模型训练。
- 方法要点：引入多数据集基准，集成检测、跟踪与重识别，采用多帧自监督预训练策略。
- 实验或效果：通过AttnLRP验证模型依赖生物特征，大规模图像骨干优于视频架构，实现无监督种群计数。

## 摘要（原文）

> Monitoring critically endangered western lowland gorillas is currently hampered by the immense manual effort required to re-identify individuals from vast archives of camera trap footage. The primary obstacle to automating this process has been the lack of large-scale, "in-the-wild" video datasets suitable for training robust deep learning models. To address this gap, we introduce a comprehensive benchmark with three novel datasets: Gorilla-SPAC-Wild, the largest video dataset for wild primate re-identification to date; Gorilla-Berlin-Zoo, for assessing cross-domain re-identification generalization; and Gorilla-SPAC-MoT, for evaluating multi-object tracking in camera trap footage. Building on these datasets, we present GorillaWatch, an end-to-end pipeline integrating detection, tracking, and re-identification. To exploit temporal information, we introduce a multi-frame self-supervised pretraining strategy that leverages consistency in tracklets to learn domain-specific features without manual labels. To ensure scientific validity, a differentiable adaptation of AttnLRP verifies that our model relies on discriminative biometric traits rather than background correlations. Extensive benchmarking subsequently demonstrates that aggregating features from large-scale image backbones outperforms specialized video architectures. Finally, we address unsupervised population counting by integrating spatiotemporal constraints into standard clustering to mitigate over-segmentation. We publicly release all code and datasets to facilitate scalable, non-invasive monitoring of endangered species

