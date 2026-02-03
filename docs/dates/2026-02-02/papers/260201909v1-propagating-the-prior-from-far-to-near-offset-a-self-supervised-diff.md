---
layout: default
title: Propagating the prior from far to near offset: A self-supervised diffusion framework for progressively recovering near-offsets of towed-streamer data
---

# Propagating the prior from far to near offset: A self-supervised diffusion framework for progressively recovering near-offsets of towed-streamer data
**arXiv**：[2602.01909v1](https://arxiv.org/abs/2602.01909) · [PDF](https://arxiv.org/pdf/2602.01909.pdf)  
**作者**：Shijun Cheng, Tariq Alkhalifah  

**一句话要点**：提出自监督扩散框架，通过从远偏移向近偏移传播先验，逐步恢复拖缆数据近偏移缺失道

**关键词**：地震数据重建, 自监督学习, 扩散模型, 近偏移缺失, 不确定性估计, 拖缆采集

## 3 点简述
- 海洋拖缆地震采集常缺失近偏移道，影响处理流程如多次波消除和速度分析
- 方法基于条件扩散模型，从远偏移数据学习统计模式，递归外推重建近偏移道
- 合成和现场数据验证显示性能优于传统方法，提供不确定性估计，波形保持真实振幅趋势

## 摘要（原文）

> In marine towed-streamer seismic acquisition, the nearest hydrophone is often two hundred meter away from the source resulting in missing near-offset traces, which degrades critical processing workflows such as surface-related multiple elimination, velocity analysis, and full-waveform inversion. Existing reconstruction methods, like transform-domain interpolation, often produce kinematic inconsistencies and amplitude distortions, while supervised deep learning approaches require complete ground-truth near-offset data that are unavailable in realistic acquisition scenarios. To address these limitations, we propose a self-supervised diffusion-based framework that reconstructs missing near-offset traces without requiring near-offset reference data. Our method leverages overlapping patch extraction with single-trace shifts from the available far-offset section to train a conditional diffusion model, which learns offset-dependent statistical patterns governing event curvature, amplitude variation, and wavelet characteristics. At inference, we perform trace-by-trace recursive extrapolation from the nearest recorded offset toward zero offset, progressively propagating learned prior information from far to near offsets. The generative formulation further provides uncertainty estimates via ensemble sampling, quantifying prediction confidence where validation data are absent. Controlled validation experiments on synthetic and field datasets show substantial performance gains over conventional parabolic Radon transform baselines. Operational deployment on actual near-offset gaps demonstrates practical viability where ground-truth validation is impossible. Notably, the reconstructed waveforms preserve realistic amplitude-versus-offset trends despite training exclusively on far-offset observations, and uncertainty maps accurately identify challenging extrapolation regions.

