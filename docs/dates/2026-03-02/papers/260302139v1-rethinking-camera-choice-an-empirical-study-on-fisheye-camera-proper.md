---
layout: default
title: Rethinking Camera Choice: An Empirical Study on Fisheye Camera Properties in Robotic Manipulation
---

# Rethinking Camera Choice: An Empirical Study on Fisheye Camera Properties in Robotic Manipulation
**arXiv**：[2603.02139v1](https://arxiv.org/abs/2603.02139) · [PDF](https://arxiv.org/pdf/2603.02139.pdf)  
**作者**：Han Xue, Nan Min, Xiaotong Liu, Wendi Chen, Yuan Fang, Jun Lv, Cewu Lu, Chuan Wen  

**一句话要点**：实证研究鱼眼相机特性，为机器人操作中的模仿学习提供指导

**关键词**：鱼眼相机, 机器人操作, 模仿学习, 场景泛化, 硬件泛化, 随机尺度增强

## 3 点简述
- 核心问题：鱼眼相机在机器人操作中广泛应用，但对其影响策略学习的系统性理解不足
- 方法要点：通过仿真和真实实验，分析鱼眼相机在空间定位、场景泛化和硬件泛化方面的特性
- 实验或效果：发现宽视场增强定位但依赖环境复杂度，提出随机尺度增强策略改善硬件泛化

## 摘要（原文）

> The adoption of fisheye cameras in robotic manipulation, driven by their exceptionally wide Field of View (FoV), is rapidly outpacing a systematic understanding of their downstream effects on policy learning. This paper presents the first comprehensive empirical study to bridge this gap, rigorously analyzing the properties of wrist-mounted fisheye cameras for imitation learning. Through extensive experiments in both simulation and the real world, we investigate three critical research questions: spatial localization, scene generalization, and hardware generalization. Our investigation reveals that: (1) The wide FoV significantly enhances spatial localization, but this benefit is critically contingent on the visual complexity of the environment. (2) Fisheye-trained policies, while prone to overfitting in simple scenes, unlock superior scene generalization when trained with sufficient environmental diversity. (3) While naive cross-camera transfer leads to failures, we identify the root cause as scale overfitting and demonstrate that hardware generalization performance can be improved with a simple Random Scale Augmentation (RSA) strategy. Collectively, our findings provide concrete, actionable guidance for the large-scale collection and effective use of fisheye datasets in robotic learning. More results and videos are available on https://robo-fisheye.github.io/

