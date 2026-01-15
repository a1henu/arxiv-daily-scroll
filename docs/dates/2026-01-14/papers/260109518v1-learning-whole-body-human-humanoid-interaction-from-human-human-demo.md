---
layout: default
title: Learning Whole-Body Human-Humanoid Interaction from Human-Human Demonstrations
---

# Learning Whole-Body Human-Humanoid Interaction from Human-Human Demonstrations
**arXiv**：[2601.09518v1](https://arxiv.org/abs/2601.09518) · [PDF](https://arxiv.org/pdf/2601.09518.pdf)  
**作者**：Wei-Jin Huang, Yue-Yi Zhang, Yi-Lin Wei, Zhi-Wei Xia, Juantao Tan, Yuan-Ming Li, Zhilin Zhao, Wei-Shi Zheng  

**一句话要点**：提出PAIR和D-STAR框架，从人-人交互数据学习人形机器人全身交互

**关键词**：人形机器人交互, 物理感知重定向, 分层策略学习, 扩散模型, 全身运动控制, 人-人交互数据

## 3 点简述
- 核心问题：人-人形交互数据稀缺，标准重定向破坏接触，模仿学习缺乏交互理解
- 方法要点：PAIR基于接触保持物理一致性，D-STAR解耦时空推理以生成同步行为
- 实验或效果：通过模拟验证，性能显著优于基线，实现从人-人数据学习复杂交互

## 摘要（原文）

> Enabling humanoid robots to physically interact with humans is a critical frontier, but progress is hindered by the scarcity of high-quality Human-Humanoid Interaction (HHoI) data. While leveraging abundant Human-Human Interaction (HHI) data presents a scalable alternative, we first demonstrate that standard retargeting fails by breaking the essential contacts. We address this with PAIR (Physics-Aware Interaction Retargeting), a contact-centric, two-stage pipeline that preserves contact semantics across morphology differences to generate physically consistent HHoI data. This high-quality data, however, exposes a second failure: conventional imitation learning policies merely mimic trajectories and lack interactive understanding. We therefore introduce D-STAR (Decoupled Spatio-Temporal Action Reasoner), a hierarchical policy that disentangles when to act from where to act. In D-STAR, Phase Attention (when) and a Multi-Scale Spatial module (where) are fused by the diffusion head to produce synchronized whole-body behaviors beyond mimicry. By decoupling these reasoning streams, our model learns robust temporal phases without being distracted by spatial noise, leading to responsive, synchronized collaboration. We validate our framework through extensive and rigorous simulations, demonstrating significant performance gains over baseline approaches and a complete, effective pipeline for learning complex whole-body interactions from HHI data.

