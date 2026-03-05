---
layout: default
title: End-to-end event reconstruction for precision physics at future colliders
---

# End-to-end event reconstruction for precision physics at future colliders
**arXiv**：[2603.04084v1](https://arxiv.org/abs/2603.04084) · [PDF](https://arxiv.org/pdf/2603.04084.pdf)  
**作者**：Dolores Garcia, Lena Herrmann, Gregor Krzmanc, Michele Selvaggi  

**一句话要点**：提出端到端全局事件重建方法，以提升未来对撞机实验的粒子重建精度和灵活性。

**关键词**：事件重建, 几何代数Transformer, 对象凝聚聚类, 粒子流算法, 对撞机实验, 端到端学习

## 3 点简述
- 核心问题：未来对撞机实验需高精度测量希格斯等粒子，但现有粒子流算法依赖探测器特定聚类，限制设计灵活性。
- 方法要点：结合几何代数Transformer网络和对象凝聚聚类，直接映射轨迹和击中到粒子级对象，并用于粒子识别和能量回归。
- 实验或效果：在FCC-ee模拟中，相对重建效率提升10-20%，假粒子率降低达两个数量级，可见能量和不变质量分辨率提高22%。

## 摘要（原文）

> Future collider experiments require unprecedented precision in measurements of Higgs, electroweak, and flavour observables, placing stringent demands on event reconstruction. The achievable precision on Higgs couplings scales directly with the resolution on visible final state particles and their invariant masses. Current particle flow algorithms rely on detector specific clustering, limiting flexibility during detector design. Here we present an end-to-end global event reconstruction approach that maps charged particle tracks and calorimeter and muon hits directly to particle level objects. The method combines geometric algebra transformer networks with object condensation based clustering, followed by dedicated networks for particle identification and energy regression. Our approach is benchmarked on fully simulated electron positron collisions at FCC-ee using the CLD detector concept. It outperforms the state-of-the-art rule-based algorithm by 10--20\% in relative reconstruction efficiency, achieves up to two orders of magnitude reduction in fake-particle rates for charged hadrons, and improves visible energy and invariant mass resolution by 22\%. By decoupling reconstruction performance from detector-specific tuning, this framework enables rapid iteration during the detector design phase of future collider experiments.

