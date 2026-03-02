---
layout: default
title: End-to-end Differentiable Calibration and Reconstruction for Optical Particle Detectors
---

# End-to-end Differentiable Calibration and Reconstruction for Optical Particle Detectors
**arXiv**：[2602.24129v1](https://arxiv.org/abs/2602.24129) · [PDF](https://arxiv.org/pdf/2602.24129.pdf)  
**作者**：Omar Alterkait, César Jesús-Valls, Ryo Matsumoto, Patrick de Perio, Kazuhiro Terao  

**一句话要点**：提出端到端可微分光学粒子探测器模拟器，实现基于梯度的校准与重建统一框架。

**关键词**：可微分模拟, 光学粒子探测器, 梯度优化, 校准与重建, 端到端学习, 粒子物理实验

## 3 点简述
- 核心问题：传统光学粒子探测器分析依赖分离的模拟、校准和跟踪，导致流程复杂且效率受限。
- 方法要点：构建首个端到端可微分模拟器，通过梯度优化统一光生成、传播和检测的关键阶段。
- 实验或效果：在精度和速度上匹配或超越传统方法，模块化设计支持多种探测器几何结构和材料。

## 摘要（原文）

> Large-scale homogeneous detectors with optical readouts are widely used in particle detection, with Cherenkov and scintillator neutrino detectors as prominent examples. Analyses in experimental physics rely on high-fidelity simulators to translate sensor-level information into physical quantities of interest. This task critically depends on accurate calibration, which aligns simulation behavior with real detector data, and on tracking, which infers particle properties from optical signals. We present the first end-to-end differentiable optical particle detector simulator, enabling simultaneous calibration and reconstruction through gradient-based optimization. Our approach unifies simulation, calibration, and tracking, which are traditionally treated as separate problems, within a single differentiable framework. We demonstrate that it achieves smooth and physically meaningful gradients across all key stages of light generation, propagation, and detection while maintaining computational efficiency. We show that gradient-based calibration and reconstruction greatly simplify existing analysis pipelines while matching or surpassing the performance of conventional non-differentiable methods in both accuracy and speed. Moreover, the framework's modularity allows straightforward adaptation to diverse detector geometries and target materials, providing a flexible foundation for experiment design and optimization. The results demonstrate the readiness of this technique for adoption in current and future optical detector experiments, establishing a new paradigm for simulation and reconstruction in particle physics.

