---
layout: default
title: See-Control: A Multimodal Agent Framework for Smartphone Interaction with a Robotic Arm
---

# See-Control: A Multimodal Agent Framework for Smartphone Interaction with a Robotic Arm
**arXiv**：[2512.08629v1](https://arxiv.org/abs/2512.08629) · [PDF](https://arxiv.org/pdf/2512.08629.pdf)  
**作者**：Haoyu Zhao, Weizhong Ding, Yuhao Yang, Zheng Tian, Linyi Yang, Kun Shao, Jun Wang  

**一句话要点**：提出See-Control框架，通过低自由度机械臂直接物理交互实现智能手机操作，提供平台无关解决方案。

**关键词**：多模态大语言模型, 智能手机操作, 机械臂控制, 平台无关性, 物理交互, 基准数据集

## 3 点简述
- 核心问题：现有基于ADB的智能手机操作代理仅适用于Android设备，限制了应用范围。
- 方法要点：构建包含基准、MLLM代理和标注数据集的框架，生成机械臂控制命令，无需ADB或系统后端访问。
- 实验或效果：引入155个任务的ESO基准和丰富标注数据集，为未来研究提供资源，促进数字代理与物理世界融合。

## 摘要（原文）

> Recent advances in Multimodal Large Language Models (MLLMs) have enabled their use as intelligent agents for smartphone operation. However, existing methods depend on the Android Debug Bridge (ADB) for data transmission and action execution, limiting their applicability to Android devices. In this work, we introduce the novel Embodied Smartphone Operation (ESO) task and present See-Control, a framework that enables smartphone operation via direct physical interaction with a low-DoF robotic arm, offering a platform-agnostic solution. See-Control comprises three key components: (1) an ESO benchmark with 155 tasks and corresponding evaluation metrics; (2) an MLLM-based embodied agent that generates robotic control commands without requiring ADB or system back-end access; and (3) a richly annotated dataset of operation episodes, offering valuable resources for future research. By bridging the gap between digital agents and the physical world, See-Control provides a concrete step toward enabling home robots to perform smartphone-dependent tasks in realistic environments.

