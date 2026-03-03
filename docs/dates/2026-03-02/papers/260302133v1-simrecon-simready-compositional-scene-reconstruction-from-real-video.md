---
layout: default
title: SimRecon: SimReady Compositional Scene Reconstruction from Real Videos
---

# SimRecon: SimReady Compositional Scene Reconstruction from Real Videos
**arXiv**：[2603.02133v1](https://arxiv.org/abs/2603.02133) · [PDF](https://arxiv.org/pdf/2603.02133.pdf)  
**作者**：Chong Xia, Kai Zhu, Zizhuo Wang, Fangfu Liu, Zhizheng Zhang, Yueqi Duan  

**一句话要点**：提出SimRecon框架，通过感知-生成-仿真流程解决复杂场景重建中的视觉保真与物理合理性问题。

**关键词**：组合场景重建, 感知-生成-仿真, 主动视角优化, 场景图合成, 真实视频处理, 三维模拟

## 3 点简述
- 核心问题：传统组合重建方法在真实场景中视觉保真度低且物理合理性差，难以泛化。
- 方法要点：引入主动视角优化和场景图合成器，优化单对象生成与仿真组装，提升重建质量。
- 实验或效果：在ScanNet数据集上验证，性能优于现有方法，适用于模拟与交互应用。

## 摘要（原文）

> Compositional scene reconstruction seeks to create object-centric representations rather than holistic scenes from real-world videos, which is natively applicable for simulation and interaction. Conventional compositional reconstruction approaches primarily emphasize on visual appearance and show limited generalization ability to real-world scenarios. In this paper, we propose SimRecon, a framework that realizes a "Perception-Generation-Simulation" pipeline towards cluttered scene reconstruction, which first conducts scene-level semantic reconstruction from video input, then performs single-object generation, and finally assembles these assets in the simulator. However, naively combining these three stages leads to visual infidelity of generated assets and physical implausibility of the final scene, a problem particularly severe for complex scenes. Thus, we further propose two bridging modules between the three stages to address this problem. To be specific, for the transition from Perception to Generation, critical for visual fidelity, we introduce Active Viewpoint Optimization, which actively searches in 3D space to acquire optimal projected images as conditions for single-object completion. Moreover, for the transition from Generation to Simulation, essential for physical plausibility, we propose a Scene Graph Synthesizer, which guides the construction from scratch in 3D simulators, mirroring the native, constructive principle of the real world. Extensive experiments on the ScanNet dataset validate our method's superior performance over previous state-of-the-art approaches.

