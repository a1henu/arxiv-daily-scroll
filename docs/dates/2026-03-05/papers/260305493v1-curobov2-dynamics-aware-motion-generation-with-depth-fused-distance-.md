---
layout: default
title: cuRoboV2: Dynamics-Aware Motion Generation with Depth-Fused Distance Fields for High-DoF Robots
---

# cuRoboV2: Dynamics-Aware Motion Generation with Depth-Fused Distance Fields for High-DoF Robots
**arXiv**：[2603.05493v1](https://arxiv.org/abs/2603.05493) · [PDF](https://arxiv.org/pdf/2603.05493.pdf)  
**作者**：Balakumar Sundaralingam, Adithyavairavan Murali, Stan Birchfield  

**一句话要点**：提出cuRoboV2框架，通过B样条优化、GPU感知和全身计算实现高自由度机器人的动态感知运动生成。

**关键词**：运动生成, 高自由度机器人, GPU计算, 距离场, 轨迹优化, 人形机器人

## 3 点简述
- 核心问题：现有方法在高自由度系统中存在轨迹不可执行、感知不精确和计算不可扩展的问题。
- 方法要点：采用B样条轨迹优化、GPU原生TSDF/ESDF感知管道和可扩展GPU全身计算。
- 实验或效果：在负载、碰撞避免和约束满足方面显著优于基线，并支持人形机器人应用。

## 摘要（原文）

> Effective robot autonomy requires motion generation that is safe, feasible, and reactive. Current methods are fragmented: fast planners output physically unexecutable trajectories, reactive controllers struggle with high-fidelity perception, and existing solvers fail on high-DoF systems. We present cuRoboV2, a unified framework with three key innovations: (1) B-spline trajectory optimization that enforces smoothness and torque limits; (2) a GPU-native TSDF/ESDF perception pipeline that generates dense signed distance fields covering the full workspace, unlike existing methods that only provide distances within sparsely allocated blocks, up to 10x faster and in 8x less memory than the state-of-the-art at manipulation scale, with up to 99% collision recall; and (3) scalable GPU-native whole-body computation, namely topology-aware kinematics, differentiable inverse dynamics, and map-reduce self-collision, that achieves up to 61x speedup while also extending to high-DoF humanoids (where previous GPU implementations fail). On benchmarks, cuRoboV2 achieves 99.7% success under 3kg payload (where baselines achieve only 72--77%), 99.6% collision-free IK on a 48-DoF humanoid (where prior methods fail entirely), and 89.5% retargeting constraint satisfaction (vs. 61% for PyRoki); these collision-free motions yield locomotion policies with 21% lower tracking error than PyRoki and 12x lower cross-seed variance than mink. A ground-up codebase redesign for discoverability enabled LLM coding assistants to author up to 73% of new modules, including hand-optimized CUDA kernels, demonstrating that well-structured robotics code can unlock productive human--LLM collaboration. Together, these advances provide a unified, dynamics-aware motion generation stack that scales from single-arm manipulators to full humanoids.

