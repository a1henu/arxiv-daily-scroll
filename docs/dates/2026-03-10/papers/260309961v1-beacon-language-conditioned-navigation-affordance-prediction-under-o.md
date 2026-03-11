---
layout: default
title: BEACON: Language-Conditioned Navigation Affordance Prediction under Occlusion
---

# BEACON: Language-Conditioned Navigation Affordance Prediction under Occlusion
**arXiv**：[2603.09961v1](https://arxiv.org/abs/2603.09961) · [PDF](https://arxiv.org/pdf/2603.09961.pdf)  
**作者**：Xinyu Gao, Gang Chen, Javier Alonso-Mora  

**一句话要点**：提出BEACON方法，通过鸟瞰图预测解决语言引导导航中目标被遮挡的问题。

**关键词**：语言条件导航, 鸟瞰图预测, 遮挡处理, 视觉语言模型, 机器人导航

## 3 点简述
- 核心问题：现有视觉语言模型在图像空间预测，难以处理目标被家具或移动人物遮挡的情况。
- 方法要点：结合语言指令和四向RGB-D观测，将空间线索注入视觉语言模型，融合深度特征预测鸟瞰图热图。
- 实验或效果：在Habitat模拟器构建的遮挡数据集上，验证了方法有效性，平均准确率提升22.74个百分点。

## 摘要（原文）

> Language-conditioned local navigation requires a robot to infer a nearby traversable target location from its current observation and an open-vocabulary, relational instruction. Existing vision-language spatial grounding methods usually rely on vision-language models (VLMs) to reason in image space, producing 2D predictions tied to visible pixels. As a result, they struggle to infer target locations in occluded regions, typically caused by furniture or moving humans. To address this issue, we propose BEACON, which predicts an ego-centric Bird's-Eye View (BEV) affordance heatmap over a bounded local region including occluded areas. Given an instruction and surround-view RGB-D observations from four directions around the robot, BEACON predicts the BEV heatmap by injecting spatial cues into a VLM and fusing the VLM's output with depth-derived BEV features. Using an occlusion-aware dataset built in the Habitat simulator, we conduct detailed experimental analysis to validate both our BEV space formulation and the design choices of each module. Our method improves the accuracy averaged across geodesic thresholds by 22.74 percentage points over the state-of-the-art image-space baseline on the validation subset with occluded target locations. Our project page is: https://xin-yu-gao.github.io/beacon.

