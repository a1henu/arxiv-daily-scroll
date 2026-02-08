---
layout: default
title: PMT Waveform Simulation and Reconstruction with Conditional Diffusion Network
---

# PMT Waveform Simulation and Reconstruction with Conditional Diffusion Network
**arXiv**：[2602.05767v1](https://arxiv.org/abs/2602.05767) · [PDF](https://arxiv.org/pdf/2602.05767.pdf)  
**作者**：Kainan Liu, Jingyu Huang, Guihong Huang, Jianyi Luo  

**一句话要点**：提出基于双向条件扩散网络的弱监督波形模拟与重建方法，以解决光电倍增管波形中光子重叠问题。

**关键词**：光电倍增管波形重建, 条件扩散网络, 弱监督学习, 光子重叠问题, 数据驱动方法

## 3 点简述
- 核心问题：光电倍增管波形中多光子重叠导致单个光电子难以分辨，且真实数据缺乏精确标签。
- 方法要点：采用双向条件扩散网络，通过波形模拟和重建的迭代优化，学习重叠波形特征。
- 实验或效果：在1-5光电子范围内，归一化光电子数分辨率达到全监督学习的99%，时间分辨率达到80%。

## 摘要（原文）

> Photomultiplier tubes (PMTs) are widely employed in particle and nuclear physics experiments. The accuracy of PMT waveform reconstruction directly impacts the detector's spatial and energy resolution. A key challenge arises when multiple photons arrive within a few nanoseconds, making it difficult to resolve individual photoelectrons (PEs). Although supervised deep learning methods have surpassed traditional methods in performance, their practical applicability is limited by the lack of ground-truth PE labels in real data. To address this issue, we propose an innovative weakly supervised waveform simulation and reconstruction approach based on a bidirectional conditional diffusion network framework. The method is fully data-driven and requires only raw waveforms and coarse estimates of PE information as input. It first employs a PE-conditioned diffusion model to simulate realistic waveforms from PE sequences, thereby learning the features of overlapping waveforms. Subsequently, these simulated waveforms are used to train a waveform-conditioned diffusion model to reconstruct the PE sequences from waveforms, reinforcing the learning of features of overlapping waveforms. Through iterative refinement between the two conditional diffusion processes, the model progressively improves reconstruction accuracy. Experimental results demonstrate that the proposed method achieves 99% of the normalized PE-number resolution averaged over 1-5 p.e. and 80% of the timing resolution attained by fully supervised learning.

