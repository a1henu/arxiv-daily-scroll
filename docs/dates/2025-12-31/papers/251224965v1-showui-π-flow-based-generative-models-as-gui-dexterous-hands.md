---
layout: default
title: ShowUI-$π$: Flow-based Generative Models as GUI Dexterous Hands
---

# ShowUI-$π$: Flow-based Generative Models as GUI Dexterous Hands
**arXiv**：[2512.24965v1](https://arxiv.org/abs/2512.24965) · [PDF](https://arxiv.org/pdf/2512.24965.pdf)  
**作者**：Siyuan Hu, Kevin Qinghong Lin, Mike Zheng Shou  

**一句话要点**：提出ShowUI-π，基于流生成模型实现GUI灵巧操作，解决现有代理无法处理连续拖拽轨迹的问题。

**关键词**：GUI代理, 流生成模型, 连续拖拽, 动作生成, 基准评估

## 3 点简述
- 核心问题：现有GUI代理依赖离散点击预测，无法执行需连续感知与调整的拖拽操作。
- 方法要点：统一离散-连续动作，通过流生成模型预测增量光标调整，确保轨迹平滑稳定。
- 实验效果：在ScreenDrag基准上，ShowUI-π以450M参数达到26.98分，优于现有代理。

## 摘要（原文）

> Building intelligent agents capable of dexterous manipulation is essential for achieving human-like automation in both robotics and digital environments. However, existing GUI agents rely on discrete click predictions (x,y), which prohibits free-form, closed-loop trajectories (e.g. dragging a progress bar) that require continuous, on-the-fly perception and adjustment. In this work, we develop ShowUI-$π$, the first flow-based generative model as GUI dexterous hand, featuring the following designs: (i) Unified Discrete-Continuous Actions, integrating discrete clicks and continuous drags within a shared model, enabling flexible adaptation across diverse interaction modes; (ii) Flow-based Action Generation for drag modeling, which predicts incremental cursor adjustments from continuous visual observations via a lightweight action expert, ensuring smooth and stable trajectories; (iii) Drag Training data and Benchmark, where we manually collect and synthesize 20K drag trajectories across five domains (e.g. PowerPoint, Adobe Premiere Pro), and introduce ScreenDrag, a benchmark with comprehensive online and offline evaluation protocols for assessing GUI agents' drag capabilities. Our experiments show that proprietary GUI agents still struggle on ScreenDrag (e.g. Operator scores 13.27, and the best Gemini-2.5-CUA reaches 22.18). In contrast, ShowUI-$π$ achieves 26.98 with only 450M parameters, underscoring both the difficulty of the task and the effectiveness of our approach. We hope this work advances GUI agents toward human-like dexterous control in digital world. The code is available at https://github.com/showlab/showui-pi.

