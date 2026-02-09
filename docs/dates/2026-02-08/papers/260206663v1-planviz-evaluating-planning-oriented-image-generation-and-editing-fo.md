---
layout: default
title: PlanViz: Evaluating Planning-Oriented Image Generation and Editing for Computer-Use Tasks
---

# PlanViz: Evaluating Planning-Oriented Image Generation and Editing for Computer-Use Tasks
**arXiv**：[2602.06663v1](https://arxiv.org/abs/2602.06663) · [PDF](https://arxiv.org/pdf/2602.06663.pdf)  
**作者**：Junxian Li, Kai Liu, Leyang Chen, Weida Wang, Zhixin Wang, Jiaqi Xu, Fan Li, Renjing Pei, Linghe Kong, Yulun Zhang  

**一句话要点**：提出PlanViz基准以评估统一多模态模型在计算机使用任务中的规划导向图像生成与编辑能力

**关键词**：规划导向图像生成, 计算机使用任务, 统一多模态模型, 基准评估, 空间推理, 过程理解

## 3 点简述
- 核心问题：统一多模态模型在计算机使用任务中的规划能力（如空间推理和过程理解）尚未充分探索
- 方法要点：设计三个新子任务（路线规划、工作图表、网页UI显示），并引入PlanScore进行任务自适应评估
- 实验或效果：通过实验揭示模型的关键局限性，为未来研究提供方向

## 摘要（原文）

> Unified multimodal models (UMMs) have shown impressive capabilities in generating natural images and supporting multimodal reasoning. However, their potential in supporting computer-use planning tasks, which are closely related to our lives, remain underexplored. Image generation and editing in computer-use tasks require capabilities like spatial reasoning and procedural understanding, and it is still unknown whether UMMs have these capabilities to finish these tasks or not. Therefore, we propose PlanViz, a new benchmark designed to evaluate image generation and editing for computer-use tasks. To achieve the goal of our evaluation, we focus on sub-tasks which frequently involve in daily life and require planning steps. Specifically, three new sub-tasks are designed: route planning, work diagramming, and web&UI displaying. We address challenges in data quality ensuring by curating human-annotated questions and reference images, and a quality control process. For challenges of comprehensive and exact evaluation, a task-adaptive score, PlanScore, is proposed. The score helps understanding the correctness, visual quality and efficiency of generated images. Through experiments, we highlight key limitations and opportunities for future research on this topic.

