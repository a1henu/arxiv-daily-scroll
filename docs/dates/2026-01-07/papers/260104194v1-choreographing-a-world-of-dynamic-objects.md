---
layout: default
title: Choreographing a World of Dynamic Objects
---

# Choreographing a World of Dynamic Objects
**arXiv**：[2601.04194v1](https://arxiv.org/abs/2601.04194) · [PDF](https://arxiv.org/pdf/2601.04194.pdf)  
**作者**：Yanzhe Lyu, Chen Geng, Karthik Dharmarajan, Yunzhi Zhang, Hadi Alzayer, Shangzhe Wu, Jiajun Wu  

**一句话要点**：提出CHORD通用生成管道，基于视频蒸馏生成动态4D场景，实现多体交互模拟。

**关键词**：4D场景生成, 视频蒸馏, 拉格朗日运动, 通用生成模型, 动态对象交互

## 3 点简述
- 核心问题：传统基于规则或大规模数据的方法难以通用生成动态4D场景的多样交互。
- 方法要点：通过蒸馏从2D视频的欧拉表示中提取拉格朗日运动信息，实现类别无关的生成。
- 实验或效果：在多种多体4D动态生成中验证有效性，并应用于机器人操作策略生成。

## 摘要（原文）

> Dynamic objects in our physical 4D (3D + time) world are constantly evolving, deforming, and interacting with other objects, leading to diverse 4D scene dynamics. In this paper, we present a universal generative pipeline, CHORD, for CHOReographing Dynamic objects and scenes and synthesizing this type of phenomena. Traditional rule-based graphics pipelines to create these dynamics are based on category-specific heuristics, yet are labor-intensive and not scalable. Recent learning-based methods typically demand large-scale datasets, which may not cover all object categories in interest. Our approach instead inherits the universality from the video generative models by proposing a distillation-based pipeline to extract the rich Lagrangian motion information hidden in the Eulerian representations of 2D videos. Our method is universal, versatile, and category-agnostic. We demonstrate its effectiveness by conducting experiments to generate a diverse range of multi-body 4D dynamics, show its advantage compared to existing methods, and demonstrate its applicability in generating robotics manipulation policies. Project page: https://yanzhelyu.github.io/chord

