---
layout: default
title: Running VLAs at Real-time Speed
---

# Running VLAs at Real-time Speed
**arXiv**：[2510.26742v1](https://arxiv.org/abs/2510.26742) · [PDF](https://arxiv.org/pdf/2510.26742.pdf)  
**作者**：Yunchao Ma, Yizhuang Zhou, Yunhuan Yang, Tiancai Wang, Haoqiang Fan  

**一句话要点**：提出优化策略实现多视角VLA实时运行，用于动态机器人控制

**关键词**：视觉语言动作模型, 实时推理, 机器人控制, 多视角视觉, 模型优化, 动态任务

## 3 点简述
- 核心问题：大型VLA模型在动态任务中难以达到实时性能
- 方法要点：引入多种策略消除模型推理开销，提升帧率和轨迹频率
- 实验或效果：在抓取下落笔任务中实现100%成功率，验证实时可行性

## 摘要（原文）

> In this paper, we show how to run pi0-level multi-view VLA at 30Hz frame rate
> and at most 480Hz trajectory frequency using a single consumer GPU. This
> enables dynamic and real-time tasks that were previously believed to be
> unattainable by large VLA models. To achieve it, we introduce a bag of
> strategies to eliminate the overheads in model inference. The real-world
> experiment shows that the pi0 policy with our strategy achieves a 100% success
> rate in grasping a falling pen task. Based on the results, we further propose a
> full streaming inference framework for real-time robot control of VLA. Code is
> available at https://github.com/Dexmal/realtime-vla.

