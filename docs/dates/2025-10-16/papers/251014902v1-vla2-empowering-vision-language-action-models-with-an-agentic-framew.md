---
layout: default
title: VLA^2: Empowering Vision-Language-Action Models with an Agentic Framework for Unseen Concept Manipulation
---

# VLA^2: Empowering Vision-Language-Action Models with an Agentic Framework for Unseen Concept Manipulation
**arXiv**：[2510.14902v1](https://arxiv.org/abs/2510.14902) · [PDF](https://arxiv.org/pdf/2510.14902.pdf)  
**作者**：Han Zhao, Jiaxuan Zhang, Wenxuan Song, Pengxiang Ding, Donglin Wang  

**一句话要点**：提出VLA^2代理框架以解决视觉-语言-动作模型对未见概念操纵的泛化失败问题

**关键词**：视觉-语言-动作模型, 代理框架, 泛化能力, 未见概念操纵, 外部知识集成

## 3 点简述
- 核心问题：VLA模型在处理训练数据外的物体概念时成功率显著下降
- 方法要点：利用OpenVLA作为执行骨干，集成外部模块提供目标物体知识
- 实验或效果：在硬级泛化基准上成功率提升44.2%，平均提升20.2%

## 摘要（原文）

> Current vision-language-action (VLA) models, pre-trained on large-scale
> robotic data, exhibit strong multi-task capabilities and generalize well to
> variations in visual and language instructions for manipulation. However, their
> success rate drops significantly when faced with object concepts outside the
> training data, such as unseen object descriptions and textures in the dataset.
> To address this, we propose a novel agentic framework, VLA^2, which leverages
> OpenVLA as the execution backbone and effectively leverages external modules
> such as web retrieval and object detection to provide visual and textual
> knowledge about target objects to the VLA. This approach mitigates
> generalization failure when handling out-of-distribution objects. Based on the
> LIBERO simulation environment, we introduced novel objects and object
> descriptions to construct a new evaluation benchmark with three difficulty
> levels to test the effectiveness of our method. Our framework successfully
> outperformed the current state-of-the-art models on our designed hard-level
> generalization benchmark. Compared to the standalone OpenVLA baseline, VLA^2
> achieves a 44.2% improvement in the success rate in the hard-level benchmark
> and an average improvement of 20.2% in all customized environments without any
> performance degradation on in-domain tasks. Project website:
> https://vla-2.github.io.

