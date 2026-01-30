---
layout: default
title: DynamicVLA: A Vision-Language-Action Model for Dynamic Object Manipulation
---

# DynamicVLA: A Vision-Language-Action Model for Dynamic Object Manipulation
**arXiv**：[2601.22153v1](https://arxiv.org/abs/2601.22153) · [PDF](https://arxiv.org/pdf/2601.22153.pdf)  
**作者**：Haozhe Xie, Beichen Wen, Jiarui Zheng, Zhaoxi Chen, Fangzhou Hong, Haiwen Diao, Ziwei Liu  

**一句话要点**：提出DynamicVLA框架以解决动态物体操作中感知与控制的挑战

**关键词**：动态物体操作, 视觉-语言-动作模型, 时序推理, 闭环适应, 合成数据收集, 基准测试

## 3 点简述
- 核心问题：VLA模型在动态场景中因缺乏快速感知、时序预测和连续控制能力而表现不佳
- 方法要点：通过紧凑VLA架构、连续推理和潜在感知动作流实现时序推理与闭环适应
- 实验或效果：在DOM基准上评估，显示响应速度、感知和泛化能力显著提升

## 摘要（原文）

> Manipulating dynamic objects remains an open challenge for Vision-Language-Action (VLA) models, which, despite strong generalization in static manipulation, struggle in dynamic scenarios requiring rapid perception, temporal anticipation, and continuous control. We present DynamicVLA, a framework for dynamic object manipulation that integrates temporal reasoning and closed-loop adaptation through three key designs: 1) a compact 0.4B VLA using a convolutional vision encoder for spatially efficient, structurally faithful encoding, enabling fast multimodal inference; 2) Continuous Inference, enabling overlapping reasoning and execution for lower latency and timely adaptation to object motion; and 3) Latent-aware Action Streaming, which bridges the perception-execution gap by enforcing temporally aligned action execution. To fill the missing foundation of dynamic manipulation data, we introduce the Dynamic Object Manipulation (DOM) benchmark, built from scratch with an auto data collection pipeline that efficiently gathers 200K synthetic episodes across 2.8K scenes and 206 objects, and enables fast collection of 2K real-world episodes without teleoperation. Extensive evaluations demonstrate remarkable improvements in response speed, perception, and generalization, positioning DynamicVLA as a unified framework for general dynamic object manipulation across embodiments.

