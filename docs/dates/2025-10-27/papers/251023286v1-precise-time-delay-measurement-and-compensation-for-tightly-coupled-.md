---
layout: default
title: Precise Time Delay Measurement and Compensation for Tightly Coupled Underwater SINS/piUSBL Navigation
---

# Precise Time Delay Measurement and Compensation for Tightly Coupled Underwater SINS/piUSBL Navigation
**arXiv**：[2510.23286v1](https://arxiv.org/abs/2510.23286) · [PDF](https://arxiv.org/pdf/2510.23286.pdf)  
**作者**：Jin Huang, Yingqiang Wang, Haoda Li, Zichen Liu, Zhikun Wang, Ying Chen  

**一句话要点**：提出紧密耦合水下SINS/piUSBL导航框架，通过精确时延测量与补偿提升精度

**关键词**：水下导航, 时延补偿, 紧密耦合, 声学定位, 多传感器融合, 惯性导航系统

## 3 点简述
- 核心问题：水下集成导航系统中传感器时间不同步，导致测量融合误差显著。
- 方法要点：结合同步定时与声信号处理，将时延量化为可估计参数。
- 实验或效果：仿真与现场实验显示，时延补偿使RMSE降低40.45%，最大误差减少32.55%。

## 摘要（原文）

> In multi-sensor systems, time synchronization between sensors is a
> significant challenge, and this issue is particularly pronounced in underwater
> integrated navigation systems incorporating acoustic positioning. Such systems
> are highly susceptible to time delay, which can significantly degrade accuracy
> when measurement and fusion moments are misaligned. To address this challenge,
> this paper introduces a tightly coupled navigation framework that integrates a
> passive inverted ultra-short baseline (piUSBL) acoustic positioning system, a
> strapdown inertial navigation system (SINS), and a depth gauge under precise
> time synchronization. The framework fuses azimuth and slant range from the
> piUSBL with depth data, thereby avoiding poor vertical-angle observability in
> planar arrays. A novel delay measurement strategy is introduced, combining
> synchronized timing with acoustic signal processing, which redefines
> delay-traditionally an unobservable error-into a quantifiable parameter,
> enabling explicit estimation of both acoustic propagation and system processing
> delays. Simulations and field experiments confirm the feasibility of the
> proposed method, with delay-compensated navigation reducing RMSE by 40.45% and
> maximum error by 32.55%. These findings show that precise delay measurement and
> compensation not only enhance underwater navigation accuracy but also establish
> a generalizable framework for acoustic positioning integration, offering
> valuable insights into time alignment and data fusion in latency-sensitive
> multi-sensor systems.

