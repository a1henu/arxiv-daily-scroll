---
layout: default
title: MVISTA-4D: View-Consistent 4D World Model with Test-Time Action Inference for Robotic Manipulation
---

# MVISTA-4D: View-Consistent 4D World Model with Test-Time Action Inference for Robotic Manipulation
**arXiv**：[2602.09878v1](https://arxiv.org/abs/2602.09878) · [PDF](https://arxiv.org/pdf/2602.09878.pdf)  
**作者**：Jiaxu Wang, Yicheng Jiang, Tianlun He, Jingkai Sun, Qiang Zhang, Junhao He, Jiahang Cao, Zesen Gan, Mingyuan Sun, Qiming Shao, Xiangyu Yue  

**一句话要点**：提出MVISTA-4D，通过视图一致4D世界模型与测试时动作优化解决机器人操作中的场景动态预测问题。

**关键词**：4D世界模型, 机器人操作, 视图一致性生成, 测试时动作推断, 跨模态融合, 场景动态预测

## 3 点简述
- 现有方法局限于图像预测或部分3D几何推理，难以预测完整4D场景动态。
- 模型基于单视图RGBD输入，生成任意视图RGBD，并通过特征融合确保跨视图和跨模态一致性。
- 实验在三个数据集上验证了4D场景生成和下游操作性能，并通过消融研究提供设计见解。

## 摘要（原文）

> World-model-based imagine-then-act becomes a promising paradigm for robotic manipulation, yet existing approaches typically support either purely image-based forecasting or reasoning over partial 3D geometry, limiting their ability to predict complete 4D scene dynamics. This work proposes a novel embodied 4D world model that enables geometrically consistent, arbitrary-view RGBD generation: given only a single-view RGBD observation as input, the model imagines the remaining viewpoints, which can then be back-projected and fused to assemble a more complete 3D structure across time. To efficiently learn the multi-view, cross-modality generation, we explicitly design cross-view and cross-modality feature fusion that jointly encourage consistency between RGB and depth and enforce geometric alignment across views. Beyond prediction, converting generated futures into actions is often handled by inverse dynamics, which is ill-posed because multiple actions can explain the same transition. We address this with a test-time action optimization strategy that backpropagates through the generative model to infer a trajectory-level latent best matching the predicted future, and a residual inverse dynamics model that turns this trajectory prior into accurate executable actions. Experiments on three datasets demonstrate strong performance on both 4D scene generation and downstream manipulation, and ablations provide practical insights into the key design choices.

