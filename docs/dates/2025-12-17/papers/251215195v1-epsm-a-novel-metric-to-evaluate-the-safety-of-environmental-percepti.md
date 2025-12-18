---
layout: default
title: EPSM: A Novel Metric to Evaluate the Safety of Environmental Perception in Autonomous Driving
---

# EPSM: A Novel Metric to Evaluate the Safety of Environmental Perception in Autonomous Driving
**arXiv**：[2512.15195v1](https://arxiv.org/abs/2512.15195) · [PDF](https://arxiv.org/pdf/2512.15195.pdf)  
**作者**：Jörg Gamerdinger, Sven Teufel, Stephan Amann, Lukas Marc Listl, Oliver Bringmann  

**一句话要点**：提出EPSM安全度量框架，以评估自动驾驶中环境感知的安全性

**关键词**：自动驾驶安全, 环境感知评估, 安全度量, 物体检测, 车道检测, DeepAccident数据集

## 3 点简述
- 核心问题：传统性能指标如精确率、召回率无法评估感知系统的安全相关方面，可能导致严重事故。
- 方法要点：集成轻量级物体安全度量和车道安全度量，量化检测错误的风险和任务间相互依赖。
- 实验或效果：使用DeepAccident数据集验证，能识别传统指标忽略的安全关键感知错误。

## 摘要（原文）

> Extensive evaluation of perception systems is crucial for ensuring the safety of intelligent vehicles in complex driving scenarios. Conventional performance metrics such as precision, recall and the F1-score assess the overall detection accuracy, but they do not consider the safety-relevant aspects of perception. Consequently, perception systems that achieve high scores in these metrics may still cause misdetections that could lead to severe accidents. Therefore, it is important to evaluate not only the overall performance of perception systems, but also their safety. We therefore introduce a novel safety metric for jointly evaluating the most critical perception tasks, object and lane detection. Our proposed framework integrates a new, lightweight object safety metric that quantifies the potential risk associated with object detection errors, as well as an lane safety metric including the interdependence between both tasks that can occur in safety evaluation. The resulting combined safety score provides a unified, interpretable measure of perception safety performance. Using the DeepAccident dataset, we demonstrate that our approach identifies safety critical perception errors that conventional performance metrics fail to capture. Our findings emphasize the importance of safety-centric evaluation methods for perception systems in autonomous driving.

