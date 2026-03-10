---
layout: default
title: RAPID: Redundancy-Aware and Compatibility-Optimal Edge-Cloud Partitioned Inference for Diverse VLA models
---

# RAPID: Redundancy-Aware and Compatibility-Optimal Edge-Cloud Partitioned Inference for Diverse VLA models
**arXiv**：[2603.07949v1](https://arxiv.org/abs/2603.07949) · [PDF](https://arxiv.org/pdf/2603.07949.pdf)  
**作者**：Zihao Zheng, Sicheng Tian, Hangyu Cao, Chenyue Li, Jiayu Chen, Maoliang Li, Xinhao Sun, Hailong Zou, Guojie Luo, Xiang Chen  

**一句话要点**：提出RAPID框架以解决VLA模型在边云协同推理中的视觉噪声干扰和运动连续性破坏问题

**关键词**：边云协同推理, 视觉语言动作模型, 冗余感知, 兼容性优化, 分区推理

## 3 点简述
- 核心问题：现有边云协同推理框架对VLA模型不优，易受视觉噪声干扰且忽视任务冗余性
- 方法要点：开发冗余感知和兼容性优化的边云分区方法，提升推理效率和运动连续性
- 实验或效果：实验显示实现最高1.73倍加速，仅5%~7%开销

## 摘要（原文）

> Vision Language Action (VLA) models are mainstream in embodied intelligence but face high inference costs. Edge-Cloud Collaborative (ECC) inference offers an effective fix by easing edge-device computing pressure to meet real-time needs. However, existing ECC frameworks are suboptimal for VLA models due to two challenges: (1) Mainstream environment-oriented edge-cloud partitioning methods are susceptible to interference from visual noise; (2) Existing edge-cloud partitioning methods overlook the step-wise redundancy unique to embodied tasks, thereby disrupting the physical continuity of motion. To address these issues, we propose a novel ECC inference framework, termed RAPID. Specifically, we developed an implementation tailored to the proposed framework. Experiments demonstrate this achieves a speedup of up to 1.73x with only 5%~7% overhead.

