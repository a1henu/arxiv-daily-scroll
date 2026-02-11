---
layout: default
title: Rethinking Visual-Language-Action Model Scaling: Alignment, Mixture, and Regularization
---

# Rethinking Visual-Language-Action Model Scaling: Alignment, Mixture, and Regularization
**arXiv**：[2602.09722v1](https://arxiv.org/abs/2602.09722) · [PDF](https://arxiv.org/pdf/2602.09722.pdf)  
**作者**：Ye Wang, Sipeng Zheng, Hao Luo, Wanpeng Zhang, Haoqi Yuan, Chaoyi Xu, Haiweng Xu, Yicheng Feng, Mingyang Yu, Zhiyu Kang, Zongqing Lu, Qin Jin  

**一句话要点**：系统研究视觉-语言-动作模型缩放，挑战异构机器人数据训练假设

**关键词**：视觉-语言-动作模型, 机器人控制, 异构数据缩放, 跨具身迁移, 训练正则化, 实验偏差控制

## 3 点简述
- 核心问题：标准数据缩放方法在异构机器人数据中是否有效，需重新评估训练选择。
- 方法要点：通过统一末端执行器相对动作表示、分析数据混合策略和训练正则化，进行控制性消融研究。
- 实验或效果：引入分组盲集成协议减少偏差，在仿真和真实机器人实验中验证设计决策。

## 摘要（原文）

> While Vision-Language-Action (VLA) models show strong promise for generalist robot control, it remains unclear whether -- and under what conditions -- the standard "scale data" recipe translates to robotics, where training data is inherently heterogeneous across embodiments, sensors, and action spaces. We present a systematic, controlled study of VLA scaling that revisits core training choices for pretraining across diverse robots. Using a representative VLA framework that combines a vision-language backbone with flow-matching, we ablate key design decisions under matched conditions and evaluate in extensive simulation and real-robot experiments. To improve the reliability of real-world results, we introduce a Grouped Blind Ensemble protocol that blinds operators to model identity and separates policy execution from outcome judgment, reducing experimenter bias. Our analysis targets three dimensions of VLA scaling. (1) Physical alignment: we show that a unified end-effector (EEF)-relative action representation is critical for robust cross-embodiment transfer. (2) Embodiment mixture: we find that naively pooling heterogeneous robot datasets often induces negative transfer rather than gains, underscoring the fragility of indiscriminate data scaling. (3) Training regularization: we observe that intuitive strategies, such as sensory dropout and multi-stage fine-tuning, do not consistently improve performance at scale. Together, this study challenge some common assumptions about embodied scaling and provide practical guidance for training large-scale VLA policies from diverse robotic data. Project website: https://research.beingbeyond.com/rethink_vla

