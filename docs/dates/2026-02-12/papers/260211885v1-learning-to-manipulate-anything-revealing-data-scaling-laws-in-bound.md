---
layout: default
title: Learning to Manipulate Anything: Revealing Data Scaling Laws in Bounding-Box Guided Policies
---

# Learning to Manipulate Anything: Revealing Data Scaling Laws in Bounding-Box Guided Policies
**arXiv**：[2602.11885v1](https://arxiv.org/abs/2602.11885) · [PDF](https://arxiv.org/pdf/2602.11885.pdf)  
**作者**：Yihao Wu, Jinming Ma, Junbo Tan, Yanzhao Yu, Shoujie Li, Mingliang Zhou, Diyun Xiang, Xueqian Wang  

**一句话要点**：提出边界框引导策略以解决语义操作泛化问题，揭示数据缩放定律。

**关键词**：语义操作, 边界框引导, 扩散策略, 数据缩放定律, 自动标注, 机器人泛化

## 3 点简述
- 核心问题：基于扩散的策略在语义操作中泛化有限，文本指令在复杂环境中难以准确定位目标对象。
- 方法要点：利用边界框指令直接指定目标对象，设计Label-UMI设备自动标注数据，提出语义-运动解耦框架。
- 实验或效果：通过大规模实验验证有效性，揭示性能与边界框对象数量的幂律关系，实现85%成功率。

## 摘要（原文）

> Diffusion-based policies show limited generalization in semantic manipulation, posing a key obstacle to the deployment of real-world robots. This limitation arises because relying solely on text instructions is inadequate to direct the policy's attention toward the target object in complex and dynamic environments. To solve this problem, we propose leveraging bounding-box instruction to directly specify target object, and further investigate whether data scaling laws exist in semantic manipulation tasks. Specifically, we design a handheld segmentation device with an automated annotation pipeline, Label-UMI, which enables the efficient collection of demonstration data with semantic labels. We further propose a semantic-motion-decoupled framework that integrates object detection and bounding-box guided diffusion policy to improve generalization and adaptability in semantic manipulation. Throughout extensive real-world experiments on large-scale datasets, we validate the effectiveness of the approach, and reveal a power-law relationship between generalization performance and the number of bounding-box objects. Finally, we summarize an effective data collection strategy for semantic manipulation, which can achieve 85\% success rates across four tasks on both seen and unseen objects. All datasets and code will be released to the community.

