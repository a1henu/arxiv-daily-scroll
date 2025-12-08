---
layout: default
title: HiMoE-VLA: Hierarchical Mixture-of-Experts for Generalist Vision-Language-Action Policies
---

# HiMoE-VLA: Hierarchical Mixture-of-Experts for Generalist Vision-Language-Action Policies
**arXiv**：[2512.05693v1](https://arxiv.org/abs/2512.05693) · [PDF](https://arxiv.org/pdf/2512.05693.pdf)  
**作者**：Zhiying Du, Bei Liu, Yaobo Liang, Yichao Shen, Haidong Cao, Xiangyu Zheng, Zhiyuan Feng, Zuxuan Wu, Jiaolong Yang, Yu-Gang Jiang  

**一句话要点**：提出HiMoE-VLA框架以处理异构机器人数据，提升视觉-语言-动作策略的泛化能力。

**关键词**：视觉-语言-动作策略, 异构机器人数据, 分层混合专家, 泛化能力, 机器人演示数据

## 3 点简述
- 核心问题：机器人演示数据存在异构性，如本体、动作空间差异，影响模型集成与泛化。
- 方法要点：采用分层混合专家架构，自适应处理异构源，逐步抽象为共享知识表示。
- 实验或效果：在仿真和真实机器人平台上优于基线，实现更高准确性和跨机器人泛化。

## 摘要（原文）

> The development of foundation models for embodied intelligence critically depends on access to large-scale, high-quality robot demonstration data. Recent approaches have sought to address this challenge by training on large collections of heterogeneous robotic datasets. However, unlike vision or language data, robotic demonstrations exhibit substantial heterogeneity across embodiments and action spaces as well as other prominent variations such as senor configurations and action control frequencies. The lack of explicit designs for handling such heterogeneity causes existing methods to struggle with integrating diverse factors, thereby limiting their generalization and leading to degraded performance when transferred to new settings. In this paper, we present HiMoE-VLA, a novel vision-language-action (VLA) framework tailored to effectively handle diverse robotic data with heterogeneity. Specifically, we introduce a Hierarchical Mixture-of-Experts (HiMoE) architecture for the action module which adaptively handles multiple sources of heterogeneity across layers and gradually abstracts them into shared knowledge representations. Through extensive experimentation with simulation benchmarks and real-world robotic platforms, HiMoE-VLA demonstrates a consistent performance boost over existing VLA baselines, achieving higher accuracy and robust generalization across diverse robots and action spaces. The code and models are publicly available at https://github.com/ZhiyingDu/HiMoE-VLA.

