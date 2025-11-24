---
layout: default
title: OmniPT: Unleashing the Potential of Large Vision Language Models for Pedestrian Tracking and Understanding
---

# OmniPT: Unleashing the Potential of Large Vision Language Models for Pedestrian Tracking and Understanding
**arXiv**：[2511.17053v1](https://arxiv.org/abs/2511.17053) · [PDF](https://arxiv.org/pdf/2511.17053.pdf)  
**作者**：Teng Fu, Mengyang Zhao, Ke Niu, Kaixin Peng, Bin Li  

**一句话要点**：提出OmniPT框架，利用大视觉语言模型统一行人跟踪与语义理解任务

**关键词**：行人跟踪, 大视觉语言模型, 强化学习训练, 语义理解, 统一框架

## 3 点简述
- 核心问题：大视觉语言模型在实例级任务如行人跟踪中性能不足，需结合高级语义理解
- 方法要点：采用RL-中期训练-SFT-RL训练流程，使模型输出格式化边界框并提升跟踪能力
- 实验或效果：在跟踪基准测试中表现优于先前方法，验证了框架有效性

## 摘要（原文）

> LVLMs have been shown to perform excellently in image-level tasks such as VQA and caption. However, in many instance-level tasks, such as visual grounding and object detection, LVLMs still show performance gaps compared to previous expert models. Meanwhile, although pedestrian tracking is a classical task, there have been a number of new topics in combining object tracking and natural language, such as Referring MOT, Cross-view Referring MOT, and Semantic MOT. These tasks emphasize that models should understand the tracked object at an advanced semantic level, which is exactly where LVLMs excel. In this paper, we propose a new unified Pedestrian Tracking framework, namely OmniPT, which can track, track based on reference and generate semantic understanding of tracked objects interactively. We address two issues: how to model the tracking task into a task that foundation models can perform, and how to make the model output formatted answers. To this end, we implement a training phase consisting of RL-Mid Training-SFT-RL. Based on the pre-trained weights of the LVLM, we first perform a simple RL phase to enable the model to output fixed and supervisable bounding box format. Subsequently, we conduct a mid-training phase using a large number of pedestrian-related datasets. Finally, we perform supervised fine-tuning on several pedestrian tracking datasets, and then carry out another RL phase to improve the model's tracking performance and enhance its ability to follow instructions. We conduct experiments on tracking benchmarks and the experimental results demonstrate that the proposed method can perform better than the previous methods.

