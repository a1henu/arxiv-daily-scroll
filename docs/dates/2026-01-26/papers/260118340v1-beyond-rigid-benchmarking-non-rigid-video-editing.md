---
layout: default
title: Beyond Rigid: Benchmarking Non-Rigid Video Editing
---

# Beyond Rigid: Benchmarking Non-Rigid Video Editing
**arXiv**：[2601.18340v1](https://arxiv.org/abs/2601.18340) · [PDF](https://arxiv.org/pdf/2601.18340.pdf)  
**作者**：Bingzheng Qu, Kehai Chen, Xuefeng Bai, Jun Yu, Min Zhang  

**一句话要点**：提出NRVBench基准和VM-Edit方法以解决非刚性视频编辑中的物理失真和时序闪烁问题

**关键词**：非刚性视频编辑, 基准测试, 物理合规性评估, 时序一致性, 文本驱动编辑, 训练免费方法

## 3 点简述
- 核心问题：现有文本驱动视频编辑方法在处理非刚性变形时存在物理失真和时序不一致的挑战
- 方法要点：引入NRVBench基准，包括数据集、NRVE-Acc评估指标和VM-Edit训练免费基线方法
- 实验或效果：实验表明当前方法在物理合理性方面不足，而VM-Edit在标准和新指标上表现优异

## 摘要（原文）

> Despite the remarkable progress in text-driven video editing, generating coherent non-rigid deformations remains a critical challenge, often plagued by physical distortion and temporal flicker. To bridge this gap, we propose NRVBench, the first dedicated and comprehensive benchmark designed to evaluate non-rigid video editing. First, we curate a high-quality dataset consisting of 180 non-rigid motion videos from six physics-based categories, equipped with 2,340 fine-grained task instructions and 360 multiple-choice questions. Second, we propose NRVE-Acc, a novel evaluation metric based on Vision-Language Models that can rigorously assess physical compliance, temporal consistency, and instruction alignment, overcoming the limitations of general metrics in capturing complex dynamics. Third, we introduce a training-free baseline, VM-Edit, which utilizes a dual-region denoising mechanism to achieve structure-aware control, balancing structural preservation and dynamic deformation. Extensive experiments demonstrate that while current methods have shortcomings in maintaining physical plausibility, our method achieves excellent performance across both standard and proposed metrics. We believe the benchmark could serve as a standard testing platform for advancing physics-aware video editing.

