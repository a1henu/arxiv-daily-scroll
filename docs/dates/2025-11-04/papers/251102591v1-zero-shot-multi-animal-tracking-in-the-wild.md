---
layout: default
title: Zero-Shot Multi-Animal Tracking in the Wild
---

# Zero-Shot Multi-Animal Tracking in the Wild
**arXiv**：[2511.02591v1](https://arxiv.org/abs/2511.02591) · [PDF](https://arxiv.org/pdf/2511.02591.pdf)  
**作者**：Jan Frederik Meier, Timo Lüddecke  

**一句话要点**：提出零样本多动物追踪框架，结合基础模型解决野外场景适应性问题

**关键词**：零样本学习, 多动物追踪, 基础模型, 野外视觉, 目标检测, 视频追踪

## 3 点简述
- 核心问题：野外多动物追踪因栖息地、运动模式和物种外观变化而具挑战性
- 方法要点：集成Grounding Dino检测器和SAM 2追踪器，无需重训练或超参数调整
- 实验或效果：在多个数据集上评估，跨物种和环境表现一致且强劲

## 摘要（原文）

> Multi-animal tracking is crucial for understanding animal ecology and
> behavior. However, it remains a challenging task due to variations in habitat,
> motion patterns, and species appearance. Traditional approaches typically
> require extensive model fine-tuning and heuristic design for each application
> scenario. In this work, we explore the potential of recent vision foundation
> models for zero-shot multi-animal tracking. By combining a Grounding Dino
> object detector with the Segment Anything Model 2 (SAM 2) tracker and carefully
> designed heuristics, we develop a tracking framework that can be applied to new
> datasets without any retraining or hyperparameter adaptation. Evaluations on
> ChimpAct, Bird Flock Tracking, AnimalTrack, and a subset of GMOT-40 demonstrate
> strong and consistent performance across diverse species and environments. The
> code is available at https://github.com/ecker-lab/SAM2-Animal-Tracking.

