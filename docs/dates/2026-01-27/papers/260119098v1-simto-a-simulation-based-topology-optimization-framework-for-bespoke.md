---
layout: default
title: SimTO: A simulation-based topology optimization framework for bespoke soft robotic grippers
---

# SimTO: A simulation-based topology optimization framework for bespoke soft robotic grippers
**arXiv**：[2601.19098v1](https://arxiv.org/abs/2601.19098) · [PDF](https://arxiv.org/pdf/2601.19098.pdf)  
**作者**：Kurt Enkera, Josh Pinskier, Marcus Gallagher, David Howard  

**一句话要点**：提出SimTO框架，通过仿真提取负载实现软体抓取器的拓扑优化，以处理特征丰富物体

**关键词**：软体机器人, 拓扑优化, 仿真框架, 抓取器设计, 特征丰富物体

## 3 点简述
- 核心问题：现有软体抓取器难以安全抓取特征丰富物体，拓扑优化需预定义负载但负载未知
- 方法要点：基于接触物理仿真自动提取负载，消除手动指定，实现高分辨率拓扑优化
- 实验或效果：生成定制化抓取器，对特征丰富物体高度专业化，并能泛化到未见物体

## 摘要（原文）

> Soft robotic grippers are essential for grasping delicate, geometrically complex objects in manufacturing, healthcare and agriculture. However, existing grippers struggle to grasp feature-rich objects with high topological variability, including gears with sharp tooth profiles on automotive assembly lines, corals with fragile protrusions, or vegetables with irregular branching structures like broccoli. Unlike simple geometric primitives such as cubes or spheres, feature-rich objects lack a clear "optimal" contact surface, making them both difficult to grasp and susceptible to damage when grasped by existing gripper designs. Safe handling of such objects therefore requires specialized soft grippers whose morphology is tailored to the object's features. Topology optimization offers a promising approach for producing specialized grippers, but its utility is limited by the requirement for pre-defined load cases. For soft grippers interacting with feature-rich objects, these loads arise from hundreds of unpredictable gripper-object contact forces during grasping and are unknown a priori. To address this problem, we introduce SimTO, a framework that enables high-resolution topology optimization by automatically extracting load cases from a contact-based physics simulator, eliminating the need for manual load specification. Given an arbitrary feature-rich object, SimTO produces highly customized soft grippers with fine-grained morphological features tailored to the object geometry. Numerical results show our designs are not only highly specialized to feature-rich objects, but also generalize to unseen objects.

