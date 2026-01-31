---
layout: default
title: GAZELOAD A Multimodal Eye-Tracking Dataset for Mental Workload in Industrial Human-Robot Collaboration
---

# GAZELOAD A Multimodal Eye-Tracking Dataset for Mental Workload in Industrial Human-Robot Collaboration
**arXiv**：[2601.21829v1](https://arxiv.org/abs/2601.21829) · [PDF](https://arxiv.org/pdf/2601.21829.pdf)  
**作者**：Bsher Karbouj, Baha Eddin Gaaloul, Jorg Kruger  

**一句话要点**：提出GAZELOAD多模态眼动数据集，用于工业人机协作中的心理负荷估计。

**关键词**：心理负荷估计, 眼动追踪, 人机协作, 多模态数据集, 工业应用

## 3 点简述
- 核心问题：工业人机协作中缺乏同步眼动与环境数据的心理负荷评估数据集。
- 方法要点：在实验室组装测试中，收集26名参与者与协作机器人交互时的眼动信号、环境光照及任务上下文数据。
- 实验或效果：提供时间同步的CSV文件，支持算法开发和基准测试，用于心理负荷估计和环境影响研究。

## 摘要（原文）

> This article describes GAZELOAD, a multimodal dataset for mental workload estimation in industrial human-robot collaboration. The data were collected in a laboratory assembly testbed where 26 participants interacted with two collaborative robots (UR5 and Franka Emika Panda) while wearing Meta ARIA smart glasses. The dataset time-synchronizes eye-tracking signals (pupil diameter, fixations, saccades, eye gaze, gaze transition entropy, fixation dispersion index) with environmental real-time and continuous measurements (illuminance) and task and robot context (bench, task block, induced faults), under controlled manipulations of task difficulty and ambient conditions. For each participant and workload-graded task block, we provide CSV files with ocular metrics aggregated into 250 ms windows, environmental logs, and self-reported mental workload ratings on a 1-10 Likert scale, organized in participant-specific folders alongside documentation. These data can be used to develop and benchmark algorithms for mental workload estimation, feature extraction, and temporal modeling in realistic industrial HRC scenarios, and to investigate the influence of environmental factors such as lighting on eye-based workload markers.

