---
layout: default
title: DySL-VLA: Efficient Vision-Language-Action Model Inference via Dynamic-Static Layer-Skipping for Robot Manipulation
---

# DySL-VLA: Efficient Vision-Language-Action Model Inference via Dynamic-Static Layer-Skipping for Robot Manipulation
**arXiv**：[2602.22896v1](https://arxiv.org/abs/2602.22896) · [PDF](https://arxiv.org/pdf/2602.22896.pdf)  
**作者**：Zebin Yang, Yijiahao Qi, Tong Xie, Bo Yu, Shaoshan Liu, Meng Li  

**一句话要点**：提出DySL-VLA框架，通过动态-静态层跳过机制高效推理视觉-语言-动作模型，用于机器人操作任务。

**关键词**：视觉-语言-动作模型, 动态层跳过, 机器人操作, 知识蒸馏, 高效推理, 实时性能

## 3 点简述
- 核心问题：视觉-语言-动作模型计算成本高，阻碍实时机器人应用。
- 方法要点：基于动作重要性动态跳过模型层，结合先验-后验跳过指导和两阶段知识蒸馏训练。
- 实验或效果：在Calvin数据集上提升成功率，减少参数并加速推理，相比基线实现3.75倍加速。

## 摘要（原文）

> Vision-Language-Action (VLA) models have shown remarkable success in robotic tasks like manipulation by fusing a language model's reasoning with a vision model's 3D understanding. However, their high computational cost remains a major obstacle for real-world applications that require real-time performance. We observe that the actions within a task have varying levels of importance: critical steps demand high precision, while less important ones can tolerate more variance. Leveraging this insight, we propose DySL-VLA, a novel framework that addresses computational cost by dynamically skipping VLA layers based on each action's importance. DySL-VLA categorizes its layers into two types: informative layers, which are consistently executed, and incremental layers, which can be selectively skipped. To intelligently skip layers without sacrificing accuracy, we invent a prior-post skipping guidance mechanism to determine when to initiate layer-skipping. We also propose a skip-aware two-stage knowledge distillation algorithm to efficiently train a standard VLA into a DySL-VLA. Our experiments indicate that DySL-VLA achieves 2.1% improvement in success length over Deer-VLA on the Calvin dataset, while simultaneously reducing trainable parameters by a factor of 85.7 and providing a 3.75x speedup relative to the RoboFlamingo baseline at iso-accuracy. Our code is available on https://github.com/PKU-SEC-Lab/DYSL_VLA.

