---
layout: default
title: Dynamic Worlds, Dynamic Humans: Generating Virtual Human-Scene Interaction Motion in Dynamic Scenes
---

# Dynamic Worlds, Dynamic Humans: Generating Virtual Human-Scene Interaction Motion in Dynamic Scenes
**arXiv**：[2601.19484v1](https://arxiv.org/abs/2601.19484) · [PDF](https://arxiv.org/pdf/2601.19484.pdf)  
**作者**：Yin Wang, Zhiying Leng, Haitian Liu, Frederick W. B. Li, Mu Li, Xiaohui Liang  

**一句话要点**：提出Dyn-HSI认知架构以生成动态场景中虚拟人-场景交互运动

**关键词**：动态场景交互, 虚拟人运动生成, 认知架构, 扩散模型, 经验记忆, 场景感知导航

## 3 点简述
- 核心问题：现有方法将场景视为静态，与现实动态场景不符。
- 方法要点：引入视觉、记忆、控制三组件，模拟人类感知与决策过程。
- 实验或效果：构建动态基准Dyn-Scenes，实验显示在静态和动态场景中均优于现有方法。

## 摘要（原文）

> Scenes are continuously undergoing dynamic changes in the real world. However, existing human-scene interaction generation methods typically treat the scene as static, which deviates from reality. Inspired by world models, we introduce Dyn-HSI, the first cognitive architecture for dynamic human-scene interaction, which endows virtual humans with three humanoid components. (1)Vision (human eyes): we equip the virtual human with a Dynamic Scene-Aware Navigation, which continuously perceives changes in the surrounding environment and adaptively predicts the next waypoint. (2)Memory (human brain): we equip the virtual human with a Hierarchical Experience Memory, which stores and updates experiential data accumulated during training. This allows the model to leverage prior knowledge during inference for context-aware motion priming, thereby enhancing both motion quality and generalization. (3) Control (human body): we equip the virtual human with Human-Scene Interaction Diffusion Model, which generates high-fidelity interaction motions conditioned on multimodal inputs. To evaluate performance in dynamic scenes, we extend the existing static human-scene interaction datasets to construct a dynamic benchmark, Dyn-Scenes. We conduct extensive qualitative and quantitative experiments to validate Dyn-HSI, showing that our method consistently outperforms existing approaches and generates high-quality human-scene interaction motions in both static and dynamic settings.

