---
layout: default
title: TIMID: Time-Dependent Mistake Detection in Videos of Robot Executions
---

# TIMID: Time-Dependent Mistake Detection in Videos of Robot Executions
**arXiv**：[2603.09782v1](https://arxiv.org/abs/2603.09782) · [PDF](https://arxiv.org/pdf/2603.09782.pdf)  
**作者**：Nerea Gallego, Fernando Salanova, Claudio Mannarano, Cristian Mahulea, Eduardo Montijano  

**一句话要点**：提出TIMID架构以检测机器人执行高级任务中的时间依赖性错误

**关键词**：视频异常检测, 机器人执行错误, 时间依赖性错误, 弱监督学习, 仿真到真实迁移, 帧级预测

## 3 点简述
- 核心问题：现有视频异常检测框架难以识别复杂时空任务违规，如时间依赖性错误
- 方法要点：基于VAD架构，输入视频和任务提示，输出帧级错误检测，支持弱监督训练
- 实验或效果：TIMID成功检测多种时间错误，优于现成视觉语言模型，提供仿真到真实评估数据集

## 摘要（原文）

> As robotic systems execute increasingly difficult task sequences, so does the number of ways in which they can fail. Video Anomaly Detection (VAD) frameworks typically focus on singular, low-level kinematic or action failures, struggling to identify more complex temporal or spatial task violations, because they do not necessarily manifest as low-level execution errors. To address this problem, the main contribution of this paper is a new VAD-inspired architecture, TIMID, which is able to detect robot time-dependent mistakes when executing high-level tasks. Our architecture receives as inputs a video and prompts of the task and the potential mistake, and returns a frame-level prediction in the video of whether the mistake is present or not. By adopting a VAD formulation, the model can be trained with weak supervision, requiring only a single label per video. Additionally, to alleviate the problem of data scarcity of incorrect executions, we introduce a multi-robot simulation dataset with controlled temporal errors and real executions for zero-shot sim-to-real evaluation. Our experiments demonstrate that out-of-the-box VLMs lack the explicit temporal reasoning required for this task, whereas our framework successfully detects different types of temporal errors. Project: https://ropertunizar.github.io/TIMID/

