---
layout: default
title: See Once, Then Act: Vision-Language-Action Model with Task Learning from One-Shot Video Demonstrations
---

# See Once, Then Act: Vision-Language-Action Model with Task Learning from One-Shot Video Demonstrations
**arXiv**：[2512.07582v1](https://arxiv.org/abs/2512.07582) · [PDF](https://arxiv.org/pdf/2512.07582.pdf)  
**作者**：Guangyan Chen, Meiling Wang, Qi Shao, Zichen Zhou, Weixin Mao, Te Cui, Minzhao Zhu, Yinan Deng, Luojie Yang, Zhanqi Zhang, Yi Yang, Hua Chen, Yufeng Yue  

**一句话要点**：提出ViVLA模型，通过单次视频演示实现机器人任务学习，提升泛化能力。

**关键词**：视觉-语言-动作模型, 单次学习, 机器人操作, 知识蒸馏, 泛化能力, 视频演示

## 3 点简述
- 现有视觉-语言-动作模型泛化能力有限，难以适应新任务。
- ViVLA联合处理演示视频与机器人观测，预测动作序列以蒸馏知识。
- 实验显示在未见任务上提升超30%，跨具身视频保持超35%增益。

## 摘要（原文）

> Developing robust and general-purpose manipulation policies represents a fundamental objective in robotics research. While Vision-Language-Action (VLA) models have demonstrated promising capabilities for end-to-end robot control, existing approaches still exhibit limited generalization to tasks beyond their training distributions. In contrast, humans possess remarkable proficiency in acquiring novel skills by simply observing others performing them once. Inspired by this capability, we propose ViVLA, a generalist robotic manipulation policy that achieves efficient task learning from a single expert demonstration video at test time. Our approach jointly processes an expert demonstration video alongside the robot's visual observations to predict both the demonstrated action sequences and subsequent robot actions, effectively distilling fine-grained manipulation knowledge from expert behavior and transferring it seamlessly to the agent. To enhance the performance of ViVLA, we develop a scalable expert-agent pair data generation pipeline capable of synthesizing paired trajectories from easily accessible human videos, further augmented by curated pairs from publicly available datasets. This pipeline produces a total of 892,911 expert-agent samples for training ViVLA. Experimental results demonstrate that our ViVLA is able to acquire novel manipulation skills from only a single expert demonstration video at test time. Our approach achieves over 30% improvement on unseen LIBERO tasks and maintains above 35% gains with cross-embodiment videos. Real-world experiments demonstrate effective learning from human videos, yielding more than 38% improvement on unseen tasks.

