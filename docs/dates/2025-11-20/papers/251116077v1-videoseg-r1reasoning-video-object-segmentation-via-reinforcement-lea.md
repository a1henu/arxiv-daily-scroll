---
layout: default
title: VideoSeg-R1:Reasoning Video Object Segmentation via Reinforcement Learning
---

# VideoSeg-R1:Reasoning Video Object Segmentation via Reinforcement Learning
**arXiv**：[2511.16077v1](https://arxiv.org/abs/2511.16077) · [PDF](https://arxiv.org/pdf/2511.16077.pdf)  
**作者**：Zishan Xu, Yifu Guo, Yuquan Lu, Fengyu Yang, Junxin Li  

**一句话要点**：提出VideoSeg-R1框架，通过强化学习解决视频推理分割中的泛化与显式推理问题。

**关键词**：视频推理分割, 强化学习, 解耦架构, 任务难度感知, 显式推理链

## 3 点简述
- 传统方法依赖监督微调，泛化能力差且缺乏显式推理。
- 采用解耦架构，结合参考图像分割与视频掩码传播，并引入任务难度感知机制。
- 在多个基准测试中实现最先进性能，代码将开源。

## 摘要（原文）

> Traditional video reasoning segmentation methods rely on supervised fine-tuning, which limits generalization to out-of-distribution scenarios and lacks explicit reasoning. To address this, we propose \textbf{VideoSeg-R1}, the first framework to introduce reinforcement learning into video reasoning segmentation. It adopts a decoupled architecture that formulates the task as joint referring image segmentation and video mask propagation. It comprises three stages: (1) A hierarchical text-guided frame sampler to emulate human attention; (2) A reasoning model that produces spatial cues along with explicit reasoning chains; and (3) A segmentation-propagation stage using SAM2 and XMem. A task difficulty-aware mechanism adaptively controls reasoning length for better efficiency and accuracy. Extensive evaluations on multiple benchmarks demonstrate that VideoSeg-R1 achieves state-of-the-art performance in complex video reasoning and segmentation tasks. The code will be publicly available at https://github.com/euyis1019/VideoSeg-R1.

