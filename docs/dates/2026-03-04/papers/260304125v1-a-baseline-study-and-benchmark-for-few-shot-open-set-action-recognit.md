---
layout: default
title: A Baseline Study and Benchmark for Few-Shot Open-Set Action Recognition with Feature Residual Discrimination
---

# A Baseline Study and Benchmark for Few-Shot Open-Set Action Recognition with Feature Residual Discrimination
**arXiv**：[2603.04125v1](https://arxiv.org/abs/2603.04125) · [PDF](https://arxiv.org/pdf/2603.04125.pdf)  
**作者**：Stefano Berti, Giulia Pasquale, Lorenzo Natale  

**一句话要点**：提出基于特征残差判别器的架构扩展，以解决少样本开放集动作识别问题。

**关键词**：少样本学习, 开放集识别, 动作识别, 视频分析, 特征残差判别

## 3 点简述
- 核心问题：少样本动作识别在开放集场景中受限，视频数据应用未充分探索。
- 方法要点：引入特征残差判别器，将骨骼数据方法适配到复杂视频域。
- 实验或效果：在五个数据集上验证，显著提升未知动作拒绝能力，保持闭集精度。

## 摘要（原文）

> Few-Shot Action Recognition (FS-AR) has shown promising results but is often limited by a closed-set assumption that fails in real-world open-set scenarios. While Few-Shot Open-Set (FSOS) recognition is well-established for images, its extension to spatio-temporal video data remains underexplored. To address this, we propose an architectural extension based on a Feature-Residual Discriminator (FR-Disc), adapting previous work on skeletal data to the more complex video domain. Extensive experiments on five datasets demonstrate that while common open-set techniques provide only marginal gains, our FR-Disc significantly enhances unknown rejection capabilities without compromising closed-set accuracy, setting a new state-of-the-art for FSOS-AR. The project website, code, and benchmark are available at: https://hsp-iit.github.io/fsosar/.

