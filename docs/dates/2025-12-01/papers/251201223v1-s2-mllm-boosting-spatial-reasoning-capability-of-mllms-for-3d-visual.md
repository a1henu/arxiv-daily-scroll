---
layout: default
title: S$^2$-MLLM: Boosting Spatial Reasoning Capability of MLLMs for 3D Visual Grounding with Structural Guidance
---

# S$^2$-MLLM: Boosting Spatial Reasoning Capability of MLLMs for 3D Visual Grounding with Structural Guidance
**arXiv**：[2512.01223v1](https://arxiv.org/abs/2512.01223) · [PDF](https://arxiv.org/pdf/2512.01223.pdf)  
**作者**：Beining Xu, Siting Zhu, Zhao Jin, Junxian Li, Hesheng Wang  

**一句话要点**：提出S^2-MLLM框架，通过隐式空间推理增强MLLMs在3D视觉定位中的空间理解能力。

**关键词**：3D视觉定位, 多模态大语言模型, 空间推理, 结构引导, 注意力机制, 位置编码

## 3 点简述
- 核心问题：MLLMs处理2D视觉输入，难以从有限视角理解3D场景空间结构，现有方法依赖点云重建导致效率低下。
- 方法要点：引入空间引导策略，利用前馈3D重建的结构感知，通过结构增强模块结合注意力机制和多级位置编码提升空间推理。
- 实验或效果：在ScanRefer、Nr3D和Sr3D数据集上验证，S^2-MLLM在性能、泛化性和效率方面优于现有方法。

## 摘要（原文）

> 3D Visual Grounding (3DVG) focuses on locating objects in 3D scenes based on natural language descriptions, serving as a fundamental task for embodied AI and robotics. Recent advances in Multi-modal Large Language Models (MLLMs) have motivated research into extending them to 3DVG. However, MLLMs primarily process 2D visual inputs and struggle with understanding 3D spatial structure of scenes solely from these limited perspectives. Existing methods mainly utilize viewpoint-dependent rendering of reconstructed point clouds to provide explicit structural guidance for MLLMs in 3DVG tasks, leading to inefficiency and limited spatial reasoning. To address this issue, we propose S$^2$-MLLM, an efficient framework that enhances spatial reasoning in MLLMs through implicit spatial reasoning. We introduce a spatial guidance strategy that leverages the structure awareness of feed-forward 3D reconstruction. By acquiring 3D structural understanding during training, our model can implicitly reason about 3D scenes without relying on inefficient point cloud reconstruction. Moreover, we propose a structure-enhanced module (SE), which first employs intra-view and inter-view attention mechanisms to capture dependencies within views and correspondences across views. The module further integrates multi-level position encoding to associate visual representations with spatial positions and viewpoint information, enabling more accurate structural understanding. Extensive experiments demonstrate that S$^2$-MLLM unifies superior performance, generalization, and efficiency, achieving significant performance over existing methods across the ScanRefer, Nr3D, and Sr3D datasets. Code will be available upon acceptance.

