---
layout: default
title: SMTrack: State-Aware Mamba for Efficient Temporal Modeling in Visual Tracking
---

# SMTrack: State-Aware Mamba for Efficient Temporal Modeling in Visual Tracking
**arXiv**：[2602.01677v1](https://arxiv.org/abs/2602.01677) · [PDF](https://arxiv.org/pdf/2602.01677.pdf)  
**作者**：Yinchao Ma, Dengqing Yang, Zhangyu He, Wenfei Yang, Tianzhu Zhang  

**一句话要点**：提出SMTrack，基于状态感知Mamba实现高效时序建模以增强视觉跟踪鲁棒性。

**关键词**：视觉跟踪, 时序建模, 状态空间模型, Mamba架构, 计算效率

## 3 点简述
- 核心问题：传统CNN和Transformer在视觉跟踪中建模长程时序依赖时存在计算成本高或需定制模块的局限。
- 方法要点：引入选择性状态感知空间模型，通过状态参数捕获多样时序线索，实现线性复杂度训练和隐藏状态传播。
- 实验或效果：实验表明SMTrack在低计算成本下实现优异性能，无需复杂定制模块。

## 摘要（原文）

> Visual tracking aims to automatically estimate the state of a target object in a video sequence, which is challenging especially in dynamic scenarios. Thus, numerous methods are proposed to introduce temporal cues to enhance tracking robustness. However, conventional CNN and Transformer architectures exhibit inherent limitations in modeling long-range temporal dependencies in visual tracking, often necessitating either complex customized modules or substantial computational costs to integrate temporal cues. Inspired by the success of the state space model, we propose a novel temporal modeling paradigm for visual tracking, termed State-aware Mamba Tracker (SMTrack), providing a neat pipeline for training and tracking without needing customized modules or substantial computational costs to build long-range temporal dependencies. It enjoys several merits. First, we propose a novel selective state-aware space model with state-wise parameters to capture more diverse temporal cues for robust tracking. Second, SMTrack facilitates long-range temporal interactions with linear computational complexity during training. Third, SMTrack enables each frame to interact with previously tracked frames via hidden state propagation and updating, which releases computational costs of handling temporal cues during tracking. Extensive experimental results demonstrate that SMTrack achieves promising performance with low computational costs.

