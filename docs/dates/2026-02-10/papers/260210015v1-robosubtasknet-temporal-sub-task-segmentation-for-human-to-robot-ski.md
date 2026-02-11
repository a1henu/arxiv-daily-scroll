---
layout: default
title: RoboSubtaskNet: Temporal Sub-task Segmentation for Human-to-Robot Skill Transfer in Real-World Environments
---

# RoboSubtaskNet: Temporal Sub-task Segmentation for Human-to-Robot Skill Transfer in Real-World Environments
**arXiv**：[2602.10015v1](https://arxiv.org/abs/2602.10015) · [PDF](https://arxiv.org/pdf/2602.10015.pdf)  
**作者**：Dharmendra Sharma, Archit Sharma, John Reberio, Vaibhav Kesharwani, Peeyush Thakur, Narendra Kumar Dhar, Laxmidhar Behera  

**一句话要点**：提出RoboSubtaskNet框架，用于现实环境中人机协作的时序子任务分割以实现技能转移。

**关键词**：时序子任务分割, 人机技能转移, 长视频理解, 机器人操作, 注意力机制, 复合损失函数

## 3 点简述
- 核心问题：在长未修剪视频中定位和分类细粒度子任务，以支持安全的人机协作，需生成机器人可执行的标签。
- 方法要点：结合注意力增强的I3D特征与改进的MS-TCN，采用斐波那契膨胀计划捕获短时程过渡，使用复合损失函数减少过分割。
- 实验或效果：在GTEA、Breakfast和RoboSubtask数据集上优于基线，并在7自由度机械臂上验证端到端管道，任务成功率约91.25%。

## 摘要（原文）

> Temporally locating and classifying fine-grained sub-task segments in long, untrimmed videos is crucial to safe human-robot collaboration. Unlike generic activity recognition, collaborative manipulation requires sub-task labels that are directly robot-executable. We present RoboSubtaskNet, a multi-stage human-to-robot sub-task segmentation framework that couples attention-enhanced I3D features (RGB plus optical flow) with a modified MS-TCN employing a Fibonacci dilation schedule to capture better short-horizon transitions such as reach-pick-place. The network is trained with a composite objective comprising cross-entropy and temporal regularizers (truncated MSE and a transition-aware term) to reduce over-segmentation and to encourage valid sub-task progressions. To close the gap between vision benchmarks and control, we introduce RoboSubtask, a dataset of healthcare and industrial demonstrations annotated at the sub-task level and designed for deterministic mapping to manipulator primitives. Empirically, RoboSubtaskNet outperforms MS-TCN and MS-TCN++ on GTEA and our RoboSubtask benchmark (boundary-sensitive and sequence metrics), while remaining competitive on the long-horizon Breakfast benchmark. Specifically, RoboSubtaskNet attains F1 @ 50 = 79.5%, Edit = 88.6%, Acc = 78.9% on GTEA; F1 @ 50 = 30.4%, Edit = 52.0%, Acc = 53.5% on Breakfast; and F1 @ 50 = 94.2%, Edit = 95.6%, Acc = 92.2% on RoboSubtask. We further validate the full perception-to-execution pipeline on a 7-DoF Kinova Gen3 manipulator, achieving reliable end-to-end behavior in physical trials (overall task success approx 91.25%). These results demonstrate a practical path from sub-task level video understanding to deployed robotic manipulation in real-world settings.

