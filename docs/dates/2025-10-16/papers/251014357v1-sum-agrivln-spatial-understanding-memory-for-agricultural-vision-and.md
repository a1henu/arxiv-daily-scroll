---
layout: default
title: SUM-AgriVLN: Spatial Understanding Memory for Agricultural Vision-and-Language Navigation
---

# SUM-AgriVLN: Spatial Understanding Memory for Agricultural Vision-and-Language Navigation
**arXiv**：[2510.14357v1](https://arxiv.org/abs/2510.14357) · [PDF](https://arxiv.org/pdf/2510.14357.pdf)  
**作者**：Xiaobei Zhao, Xingqi Lyu, Xiang Li  

**一句话要点**：提出空间理解记忆模块以提升农业视觉语言导航中的重复指令处理能力

**关键词**：农业机器人导航, 视觉语言导航, 空间记忆, 3D重建, A2A基准

## 3 点简述
- 农业机器人导航中，重复指令缺乏空间上下文利用，导致导航效率受限。
- SUM模块通过3D重建与表示保存空间记忆，增强对过去经验的利用。
- 在A2A基准测试中，成功率从0.47提升至0.54，导航误差略有增加。

## 摘要（原文）

> Agricultural robots are emerging as powerful assistants across a wide range
> of agricultural tasks, nevertheless, still heavily rely on manual operation or
> fixed rail systems for movement. The AgriVLN method and the A2A benchmark
> pioneeringly extend Vision-and-Language Navigation (VLN) to the agricultural
> domain, enabling robots to navigate to the target positions following the
> natural language instructions. In practical agricultural scenarios, navigation
> instructions often repeatedly occur, yet AgriVLN treat each instruction as an
> independent episode, overlooking the potential of past experiences to provide
> spatial context for subsequent ones. To bridge this gap, we propose the method
> of Spatial Understanding Memory for Agricultural Vision-and-Language Navigation
> (SUM-AgriVLN), in which the SUM module employs spatial understanding and save
> spatial memory through 3D reconstruction and representation. When evaluated on
> the A2A benchmark, our SUM-AgriVLN effectively improves Success Rate from 0.47
> to 0.54 with slight sacrifice on Navigation Error from 2.91m to 2.93m,
> demonstrating the state-of-the-art performance in the agricultural domain.
> Code: https://github.com/AlexTraveling/SUM-AgriVLN.

