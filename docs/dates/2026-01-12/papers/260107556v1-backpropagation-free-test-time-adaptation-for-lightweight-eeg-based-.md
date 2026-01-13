---
layout: default
title: Backpropagation-Free Test-Time Adaptation for Lightweight EEG-Based Brain-Computer Interfaces
---

# Backpropagation-Free Test-Time Adaptation for Lightweight EEG-Based Brain-Computer Interfaces
**arXiv**：[2601.07556v1](https://arxiv.org/abs/2601.07556) · [PDF](https://arxiv.org/pdf/2601.07556.pdf)  
**作者**：Siyang Li, Jiayi Ouyang, Zhenyao Cui, Ziwei Wang, Tianwang Jia, Feng Wan, Dongrui Wu  

**一句话要点**：提出无反向传播变换以解决脑机接口测试时适应中的计算与隐私问题

**关键词**：脑机接口, 测试时适应, 无反向传播学习, 脑电解码, 不确定性抑制, 轻量级系统

## 3 点简述
- 核心问题：脑机接口面临个体差异和计算限制，现有测试时适应方法依赖反向传播，导致计算开销和隐私风险
- 方法要点：通过知识引导增强或近似贝叶斯推理进行样本变换，结合学习排序模块加权聚合预测，实现无反向传播的适应
- 实验或效果：在五个脑电数据集上验证了方法在运动想象分类和驾驶员困倦回归任务中的有效性、鲁棒性和效率

## 摘要（原文）

> Electroencephalogram (EEG)-based brain-computer interfaces (BCIs) face significant deployment challenges due to inter-subject variability, signal non-stationarity, and computational constraints. While test-time adaptation (TTA) mitigates distribution shifts under online data streams without per-use calibration sessions, existing TTA approaches heavily rely on explicitly defined loss objectives that require backpropagation for updating model parameters, which incurs computational overhead, privacy risks, and sensitivity to noisy data streams. This paper proposes Backpropagation-Free Transformations (BFT), a TTA approach for EEG decoding that eliminates such issues. BFT applies multiple sample-wise transformations of knowledge-guided augmentations or approximate Bayesian inference to each test trial, generating multiple prediction scores for a single test sample. A learning-to-rank module enhances the weighting of these predictions, enabling robust aggregation for uncertainty suppression during inference under theoretical justifications. Extensive experiments on five EEG datasets of motor imagery classification and driver drowsiness regression tasks demonstrate the effectiveness, versatility, robustness, and efficiency of BFT. This research enables lightweight plug-and-play BCIs on resource-constrained devices, broadening the real-world deployment of decoding algorithms for EEG-based BCI.

