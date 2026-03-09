---
layout: default
title: Offline Materials Optimization with CliqueFlowmer
---

# Offline Materials Optimization with CliqueFlowmer
**arXiv**：[2603.06082v1](https://arxiv.org/abs/2603.06082) · [PDF](https://arxiv.org/pdf/2603.06082.pdf)  
**作者**：Jakub Grudzien Kuba, Benjamin Kurt Miller, Sergey Levine, Pieter Abbeel  

**一句话要点**：提出CliqueFlowmer以解决离线材料优化中生成模型探索不足的问题

**关键词**：离线模型优化, 材料发现, 生成模型, Transformer, 流生成, 开源代码

## 3 点简述
- 核心问题：生成模型因最大似然训练难以大胆探索材料空间中的有吸引力区域
- 方法要点：结合基于团的离线模型优化与Transformer和流生成，直接优化目标属性
- 实验或效果：验证优化能力，生成材料性能显著优于生成基线，并开源代码

## 摘要（原文）

> Recent advances in deep learning inspired neural network-based approaches to computational materials discovery (CMD). A plethora of problems in this field involve finding materials that optimize a target property. Nevertheless, the increasingly popular generative modeling methods are ineffective at boldly exploring attractive regions of the materials space due to their maximum likelihood training. In this work, we offer an alternative CMD technique based on offline model-based optimization (MBO) that fuses direct optimization of a target material property into generation. To that end, we introduce a domain-specific model, dubbed CliqueFlowmer, that incorporates recent advances of clique-based MBO into transformer and flow generation. We validate CliqueFlowmer's optimization abilities and show that materials it produces strongly outperform those provided by generative baselines. To enable employment of CliqueFlowmer in specialized materials optimization problems and support interdisciplinary research, we open-source our code at https://github.com/znowu/CliqueFlowmer.

