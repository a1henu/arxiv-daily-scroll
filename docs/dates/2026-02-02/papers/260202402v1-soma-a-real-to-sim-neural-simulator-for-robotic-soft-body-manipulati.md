---
layout: default
title: SoMA: A Real-to-Sim Neural Simulator for Robotic Soft-body Manipulation
---

# SoMA: A Real-to-Sim Neural Simulator for Robotic Soft-body Manipulation
**arXiv**：[2602.02402v1](https://arxiv.org/abs/2602.02402) · [PDF](https://arxiv.org/pdf/2602.02402.pdf)  
**作者**：Mu Huang, Hui Wang, Kerui Ren, Linning Xu, Yunsong Zhou, Mulin Yu, Bo Dai, Jiangmiao Pang  

**一句话要点**：提出SoMA，一种基于3D高斯泼溅的神经模拟器，用于机器人软体操纵的真实到模拟仿真。

**关键词**：软体操纵, 神经模拟器, 3D高斯泼溅, 真实到模拟, 机器人控制, 变形动力学

## 3 点简述
- 核心问题：现有模拟器依赖预定义物理或数据驱动动力学，缺乏机器人条件控制，导致精度、稳定性和泛化性受限。
- 方法要点：在统一潜在神经空间中耦合变形动力学、环境力和机器人关节动作，实现端到端真实到模拟仿真。
- 实验或效果：在真实世界机器人操纵任务中，重模拟精度和泛化性提升20%，支持长时程布料折叠等复杂任务稳定模拟。

## 摘要（原文）

> Simulating deformable objects under rich interactions remains a fundamental challenge for real-to-sim robot manipulation, with dynamics jointly driven by environmental effects and robot actions. Existing simulators rely on predefined physics or data-driven dynamics without robot-conditioned control, limiting accuracy, stability, and generalization. This paper presents SoMA, a 3D Gaussian Splat simulator for soft-body manipulation. SoMA couples deformable dynamics, environmental forces, and robot joint actions in a unified latent neural space for end-to-end real-to-sim simulation. Modeling interactions over learned Gaussian splats enables controllable, stable long-horizon manipulation and generalization beyond observed trajectories without predefined physical models. SoMA improves resimulation accuracy and generalization on real-world robot manipulation by 20%, enabling stable simulation of complex tasks such as long-horizon cloth folding.

