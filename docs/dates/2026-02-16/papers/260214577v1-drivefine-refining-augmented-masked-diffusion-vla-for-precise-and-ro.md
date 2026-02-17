---
layout: default
title: DriveFine: Refining-Augmented Masked Diffusion VLA for Precise and Robust Driving
---

# DriveFine: Refining-Augmented Masked Diffusion VLA for Precise and Robust Driving
**arXiv**：[2602.14577v1](https://arxiv.org/abs/2602.14577) · [PDF](https://arxiv.org/pdf/2602.14577.pdf)  
**作者**：Chenxu Dang, Sining Ang, Yongkang Li, Haochen Tian, Jie Wang, Guang Li, Hangjun Ye, Jie Ma, Long Chen, Yan Wang  

**一句话要点**：提出DriveFine，结合掩码扩散与专家选择以提升自动驾驶VLA模型的精确性和鲁棒性。

**关键词**：自动驾驶规划, 视觉-语言-动作模型, 掩码扩散, 专家混合, 强化学习, 模态对齐

## 3 点简述
- 核心问题：现有扩散和基于令牌的自动驾驶规划器存在模态对齐困难、累积因果错误等互补弱点。
- 方法要点：设计块状MoE结构，在生成专家上无缝注入精炼专家，支持推理时显式专家选择和训练时梯度阻断。
- 实验或效果：在NAVSIM v1、v2和Navhard基准测试中表现出强效性和鲁棒性，代码将开源。

## 摘要（原文）

> Vision-Language-Action (VLA) models for autonomous driving increasingly adopt generative planners trained with imitation learning followed by reinforcement learning. Diffusion-based planners suffer from modality alignment difficulties, low training efficiency, and limited generalization. Token-based planners are plagued by cumulative causal errors and irreversible decoding. In summary, the two dominant paradigms exhibit complementary strengths and weaknesses. In this paper, we propose DriveFine, a masked diffusion VLA model that combines flexible decoding with self-correction capabilities. In particular, we design a novel plug-and-play block-MoE, which seamlessly injects a refinement expert on top of the generation expert. By enabling explicit expert selection during inference and gradient blocking during training, the two experts are fully decoupled, preserving the foundational capabilities and generic patterns of the pretrained weights, which highlights the flexibility and extensibility of the block-MoE design. Furthermore, we design a hybrid reinforcement learning strategy that encourages effective exploration of refinement expert while maintaining training stability. Extensive experiments on NAVSIM v1, v2, and Navhard benchmarks demonstrate that DriveFine exhibits strong efficacy and robustness. The code will be released at https://github.com/MSunDYY/DriveFine.

