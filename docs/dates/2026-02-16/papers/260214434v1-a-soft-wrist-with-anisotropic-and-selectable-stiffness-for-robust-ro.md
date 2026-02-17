---
layout: default
title: A Soft Wrist with Anisotropic and Selectable Stiffness for Robust Robot Learning in Contact-rich Manipulation
---

# A Soft Wrist with Anisotropic and Selectable Stiffness for Robust Robot Learning in Contact-rich Manipulation
**arXiv**：[2602.14434v1](https://arxiv.org/abs/2602.14434) · [PDF](https://arxiv.org/pdf/2602.14434.pdf)  
**作者**：Steven Oh, Tomoya Takahashi, Cristian C. Beltran-Hernandez, Yuki Kuroda, Masashi Hamaya  

**一句话要点**：提出CLAW软腕机构，通过各向异性可调刚度解决非结构化环境中接触丰富操作的鲁棒性挑战。

**关键词**：软腕机构, 各向异性刚度, 接触丰富操作, 机器人学习, 模仿学习, 低成本设计

## 3 点简述
- 核心问题：非结构化环境中的接触丰富操作易受意外碰撞影响，现有软末端执行器在变形范围、刚度控制或实用性方面存在局限。
- 方法要点：CLAW采用正交叶片弹簧和带锁定机制的旋转关节，实现大变形、各向异性可调刚度，设计简单轻量低成本。
- 实验或效果：在模仿学习评估中，CLAW在基准插孔任务中成功率76%，优于Fin Ray夹爪（43%）和刚性夹爪（36%），能处理精密装配和精细操作。

## 摘要（原文）

> Contact-rich manipulation tasks in unstructured environments pose significant robustness challenges for robot learning, where unexpected collisions can cause damage and hinder policy acquisition. Existing soft end-effectors face fundamental limitations: they either provide a limited deformation range, lack directional stiffness control, or require complex actuation systems that compromise practicality. This study introduces CLAW (Compliant Leaf-spring Anisotropic soft Wrist), a novel soft wrist mechanism that addresses these limitations through a simple yet effective design using two orthogonal leaf springs and rotary joints with a locking mechanism. CLAW provides large 6-degree-of-freedom deformation (40mm lateral, 20mm vertical), anisotropic stiffness that is tunable across three distinct modes, while maintaining lightweight construction (330g) at low cost ($550). Experimental evaluations using imitation learning demonstrate that CLAW achieves 76% success rate in benchmark peg-insertion tasks, outperforming both the Fin Ray gripper (43%) and rigid gripper alternatives (36%). CLAW successfully handles diverse contact-rich scenarios, including precision assembly with tight tolerances and delicate object manipulation, demonstrating its potential to enable robust robot learning in contact-rich domains. Project page: https://project-page-manager.github.io/CLAW/

