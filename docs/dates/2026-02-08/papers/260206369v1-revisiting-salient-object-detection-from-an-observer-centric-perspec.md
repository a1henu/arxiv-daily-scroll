---
layout: default
title: Revisiting Salient Object Detection from an Observer-Centric Perspective
---

# Revisiting Salient Object Detection from an Observer-Centric Perspective
**arXiv**：[2602.06369v1](https://arxiv.org/abs/2602.06369) · [PDF](https://arxiv.org/pdf/2602.06369.pdf)  
**作者**：Fuxi Zhang, Yifan Wang, Hengrun Zhao, Zhuohan Sun, Changxing Xia, Lijun Wang, Huchuan Lu, Yangrui Shao, Chen Yang, Long Teng  

**一句话要点**：提出观察者中心显著目标检测以解决主观感知多样性问题

**关键词**：显著目标检测, 观察者中心, 多模态大语言模型, 个性化预测, 数据集构建

## 3 点简述
- 现有方法将显著目标检测视为客观预测任务，忽略人类感知的模糊性和多样性
- 提出OC-SOD方法，结合视觉线索和观察者特定因素进行个性化预测
- 构建OC-SODBench数据集并设计OC-SODAgent基线，实验验证有效性

## 摘要（原文）

> Salient object detection is inherently a subjective problem, as observers with different priors may perceive different objects as salient. However, existing methods predominantly formulate it as an objective prediction task with a single groundtruth segmentation map for each image, which renders the problem under-determined and fundamentally ill-posed. To address this issue, we propose Observer-Centric Salient Object Detection (OC-SOD), where salient regions are predicted by considering not only the visual cues but also the observer-specific factors such as their preferences or intents. As a result, this formulation captures the intrinsic ambiguity and diversity of human perception, enabling personalized and context-aware saliency prediction. By leveraging multi-modal large language models, we develop an efficient data annotation pipeline and construct the first OC-SOD dataset named OC-SODBench, comprising 33k training, validation and test images with 152k textual prompts and object pairs. Built upon this new dataset, we further design OC-SODAgent, an agentic baseline which performs OC-SOD via a human-like "Perceive-Reflect-Adjust" process. Extensive experiments on our proposed OC-SODBench have justified the effectiveness of our contribution. Through this observer-centric perspective, we aim to bridge the gap between human perception and computational modeling, offering a more realistic and flexible understanding of what makes an object truly "salient." Code and dataset are publicly available at: https://github.com/Dustzx/OC_SOD

