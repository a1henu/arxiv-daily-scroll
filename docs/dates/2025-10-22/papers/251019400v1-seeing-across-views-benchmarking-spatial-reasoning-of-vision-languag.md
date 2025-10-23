---
layout: default
title: Seeing Across Views: Benchmarking Spatial Reasoning of Vision-Language Models in Robotic Scenes
---

# Seeing Across Views: Benchmarking Spatial Reasoning of Vision-Language Models in Robotic Scenes
**arXiv**：[2510.19400v1](https://arxiv.org/abs/2510.19400) · [PDF](https://arxiv.org/pdf/2510.19400.pdf)  
**作者**：Zhiyuan Feng, Zhaolu Kang, Qijie Wang, Zhiying Du, Jiongrui Yan, Shubin Shi, Chengbo Yuan, Huizhi Liang, Yu Deng, Qixiu Li, Rushuai Yang, Arctanx An, Leqi Zheng, Weijie Wang, Shawn Chen, Sicheng Xu, Yaobo Liang, Jiaolong Yang, Baining Guo  

**一句话要点**：提出MV-RoboBench基准以评估视觉语言模型在机器人场景中的多视角空间推理能力

**关键词**：视觉语言模型, 多视角空间推理, 机器人基准, 空间理解, 机器人执行, 评估协议

## 3 点简述
- 核心问题：视觉语言模型在多视角机器人感知中的空间推理能力未被充分探索
- 方法要点：构建包含1.7k问答项的基准，涵盖空间理解和机器人执行任务
- 实验或效果：评估显示现有模型性能远低于人类，揭示多视角推理挑战

## 摘要（原文）

> Vision-language models (VLMs) are essential to Embodied AI, enabling robots
> to perceive, reason, and act in complex environments. They also serve as the
> foundation for the recent Vision-Language-Action (VLA) models. Yet most
> evaluations of VLMs focus on single-view settings, leaving their ability to
> integrate multi-view information underexplored. At the same time, multi-camera
> setups are increasingly standard in robotic platforms, as they provide
> complementary perspectives to mitigate occlusion and depth ambiguity. Whether
> VLMs can effectively leverage such multi-view inputs for robotic reasoning
> therefore remains an open question. To bridge this gap, we introduce
> MV-RoboBench, a benchmark specifically designed to evaluate the multi-view
> spatial reasoning capabilities of VLMs in robotic manipulation. MV-RoboBench
> consists of 1.7k manually curated QA items across eight subtasks, divided into
> two primary categories: spatial understanding and robotic execution. We
> evaluate a diverse set of existing VLMs, including both open-source and
> closed-source models, along with enhanced versions incorporating CoT-inspired
> techniques. The results show that state-of-the-art models remain far below
> human performance, underscoring the substantial challenges VLMs face in
> multi-view robotic perception. Additionally, our analysis uncovers two key
> findings: (i) spatial intelligence and robotic task execution are positively
> correlated in multi-view robotic scenarios; and (ii) strong performance on
> existing general-purpose single-view spatial understanding benchmarks does not
> reliably translate to success in the robotic spatial tasks assessed by our
> benchmark. We release MV-RoboBench as an open resource to foster progress in
> spatially grounded VLMs and VLAs, providing not only data but also a
> standardized evaluation protocol for multi-view embodied reasoning.

