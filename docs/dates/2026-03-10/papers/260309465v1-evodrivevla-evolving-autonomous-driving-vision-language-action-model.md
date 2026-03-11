---
layout: default
title: EvoDriveVLA: Evolving Autonomous Driving Vision-Language-Action Model via Collaborative Perception-Planning Distillation
---

# EvoDriveVLA: Evolving Autonomous Driving Vision-Language-Action Model via Collaborative Perception-Planning Distillation
**arXiv**：[2603.09465v1](https://arxiv.org/abs/2603.09465) · [PDF](https://arxiv.org/pdf/2603.09465.pdf)  
**作者**：Jiajun Cao, Xiaoan Zhang, Xiaobao Wei, Liyuqiu Huang, Wang Zijian, Hanzhen Zhang, Zhengyu Jia, Wei Mao, Hao Wang, Xianming Liu, Shuchang Zhou Liu, Yang Wang, Shanghang Zhang  

**一句话要点**：提出EvoDriveVLA框架，通过协同感知-规划蒸馏解决自动驾驶视觉-语言-动作模型的感知退化和规划不稳定问题。

**关键词**：自动驾驶, 视觉-语言-动作模型, 协同蒸馏, 感知规划, 轨迹优化, 自锚定约束

## 3 点简述
- 核心问题：视觉编码器解冻后感知退化，长期规划中累积不稳定性。
- 方法要点：结合自锚定视觉蒸馏和先知引导轨迹蒸馏，优化感知表示和轨迹预测。
- 实验或效果：在开环评估中达到SOTA性能，闭环评估中显著提升性能。

## 摘要（原文）

> Vision-Language-Action models have shown great promise for autonomous driving, yet they suffer from degraded perception after unfreezing the visual encoder and struggle with accumulated instability in long-term planning. To address these challenges, we propose EvoDriveVLA-a novel collaborative perception-planning distillation framework that integrates self-anchored perceptual constraints and oracle-guided trajectory optimization. Specifically, self-anchored visual distillation leverages self-anchor teacher to deliver visual anchoring constraints, regularizing student representations via trajectory-guided key-region awareness. In parallel, oracle-guided trajectory distillation employs a future-aware oracle teacher with coarse-to-fine trajectory refinement and Monte Carlo dropout sampling to produce high-quality trajectory candidates, thereby selecting the optimal trajectory to guide the student's prediction. EvoDriveVLA achieves SOTA performance in open-loop evaluation and significantly enhances performance in closed-loop evaluation. Our code is available at: https://github.com/hey-cjj/EvoDriveVLA.

