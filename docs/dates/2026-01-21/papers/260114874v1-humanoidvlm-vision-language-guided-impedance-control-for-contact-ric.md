---
layout: default
title: HumanoidVLM: Vision-Language-Guided Impedance Control for Contact-Rich Humanoid Manipulation
---

# HumanoidVLM: Vision-Language-Guided Impedance Control for Contact-Rich Humanoid Manipulation
**arXiv**：[2601.14874v1](https://arxiv.org/abs/2601.14874) · [PDF](https://arxiv.org/pdf/2601.14874.pdf)  
**作者**：Yara Mahmoud, Yasheerah Yaqoot, Miguel Altamirano Cabrera, Dzmitry Tsetserukou  

**一句话要点**：提出HumanoidVLM框架，通过视觉语言检索实现人形机器人自适应阻抗控制与抓取配置。

**关键词**：人形机器人控制, 视觉语言模型, 阻抗控制, 检索增强生成, 自适应抓取

## 3 点简述
- 核心问题：人形机器人依赖固定阻抗参数，难以适应多样接触任务。
- 方法要点：结合视觉语言模型与检索增强生成，从图像检索实验验证的阻抗参数和抓取角度。
- 实验或效果：在14个视觉场景中检索准确率达93%，实际交互稳定，跟踪误差小。

## 摘要（原文）

> Humanoid robots must adapt their contact behavior to diverse objects and tasks, yet most controllers rely on fixed, hand-tuned impedance gains and gripper settings. This paper introduces HumanoidVLM, a vision-language driven retrieval framework that enables the Unitree G1 humanoid to select task-appropriate Cartesian impedance parameters and gripper configurations directly from an egocentric RGB image. The system couples a vision-language model for semantic task inference with a FAISS-based Retrieval-Augmented Generation (RAG) module that retrieves experimentally validated stiffness-damping pairs and object-specific grasp angles from two custom databases, and executes them through a task-space impedance controller for compliant manipulation. We evaluate HumanoidVLM on 14 visual scenarios and achieve a retrieval accuracy of 93%. Real-world experiments show stable interaction dynamics, with z-axis tracking errors typically within 1-3.5 cm and virtual forces consistent with task-dependent impedance settings. These results demonstrate the feasibility of linking semantic perception with retrieval-based control as an interpretable path toward adaptive humanoid manipulation.

