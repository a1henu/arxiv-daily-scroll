---
layout: default
title: MOBA: A Material-Oriented Backdoor Attack against LiDAR-based 3D Object Detection Systems
---

# MOBA: A Material-Oriented Backdoor Attack against LiDAR-based 3D Object Detection Systems
**arXiv**：[2511.09999v1](https://arxiv.org/abs/2511.09999) · [PDF](https://arxiv.org/pdf/2511.09999.pdf)  
**作者**：Saket S. Chaturvedi, Gaurav Bagwe, Lan Zhang, Pan He, Xiaoyong Yuan  

**一句话要点**：提出MOBA以解决LiDAR 3D检测中物理后门攻击的材料模拟问题

**关键词**：LiDAR 3D物体检测, 后门攻击, 材料模拟, 物理可实现性, BRDF模型, 攻击鲁棒性

## 3 点简述
- 现有后门攻击缺乏物理可实现性，因忽略材料依赖的LiDAR反射特性
- MOBA通过建模材料属性，选择TiO₂作为触发材料并开发模拟管道
- 实验显示攻击成功率93.50%，优于先前方法超41%

## 摘要（原文）

> LiDAR-based 3D object detection is widely used in safety-critical systems. However, these systems remain vulnerable to backdoor attacks that embed hidden malicious behaviors during training. A key limitation of existing backdoor attacks is their lack of physical realizability, primarily due to the digital-to-physical domain gap. Digital triggers often fail in real-world settings because they overlook material-dependent LiDAR reflection properties. On the other hand, physically constructed triggers are often unoptimized, leading to low effectiveness or easy detectability.This paper introduces Material-Oriented Backdoor Attack (MOBA), a novel framework that bridges the digital-physical gap by explicitly modeling the material properties of real-world triggers. MOBA tackles two key challenges in physical backdoor design: 1) robustness of the trigger material under diverse environmental conditions, 2) alignment between the physical trigger's behavior and its digital simulation. First, we propose a systematic approach to selecting robust trigger materials, identifying titanium dioxide (TiO_2) for its high diffuse reflectivity and environmental resilience. Second, to ensure the digital trigger accurately mimics the physical behavior of the material-based trigger, we develop a novel simulation pipeline that features: (1) an angle-independent approximation of the Oren-Nayar BRDF model to generate realistic LiDAR intensities, and (2) a distance-aware scaling mechanism to maintain spatial consistency across varying depths. We conduct extensive experiments on state-of-the-art LiDAR-based and Camera-LiDAR fusion models, showing that MOBA achieves a 93.50% attack success rate, outperforming prior methods by over 41%. Our work reveals a new class of physically realizable threats and underscores the urgent need for defenses that account for material-level properties in real-world environments.

