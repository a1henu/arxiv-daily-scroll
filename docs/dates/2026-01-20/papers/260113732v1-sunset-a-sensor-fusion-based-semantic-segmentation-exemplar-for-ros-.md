---
layout: default
title: SUNSET -- A Sensor-fUsioN based semantic SegmEnTation exemplar for ROS-based self-adaptation
---

# SUNSET -- A Sensor-fUsioN based semantic SegmEnTation exemplar for ROS-based self-adaptation
**arXiv**：[2601.13732v1](https://arxiv.org/abs/2601.13732) · [PDF](https://arxiv.org/pdf/2601.13732.pdf)  
**作者**：Andreas Wiedholz, Rafael Paintner, Julian Gleißner, Alwin Hoffmann, Tobias Huber  

**一句话要点**：提出SUNSET以在动态环境中评估基于架构的自适应方法

**关键词**：传感器融合, 语义分割, 自适应系统, ROS2, 不确定性评估

## 3 点简述
- 核心问题：机器人软件在动态环境中面临不确定性和并发故障，需自适应性方法
- 方法要点：基于ROS2实现传感器融合语义分割管道，可注入不确定性以模拟性能退化
- 实验或效果：提供可重复评估框架，支持自愈和自优化，包含基线控制器和文档

## 摘要（原文）

> The fact that robots are getting deployed more often in dynamic environments, together with the increasing complexity of their software systems, raises the need for self-adaptive approaches. In these environments robotic software systems increasingly operate amid (1) uncertainties, where symptoms are easy to observe but root causes are ambiguous, or (2) multiple uncertainties appear concurrently. We present SUNSET, a ROS2-based exemplar that enables rigorous, repeatable evaluation of architecture-based self-adaptation in such conditions. It implements a sensor fusion semantic-segmentation pipeline driven by a trained Machine Learning (ML) model whose input preprocessing can be perturbed to induce realistic performance degradations. The exemplar exposes five observable symptoms, where each can be caused by different root causes and supports concurrent uncertainties spanning self-healing and self-optimisation. SUNSET includes the segmentation pipeline, a trained ML model, uncertainty-injection scripts, a baseline controller, and step-by-step integration and evaluation documentation to facilitate reproducible studies and fair comparison.

