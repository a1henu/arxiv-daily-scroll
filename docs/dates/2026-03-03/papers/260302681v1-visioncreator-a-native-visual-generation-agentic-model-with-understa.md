---
layout: default
title: VisionCreator: A Native Visual-Generation Agentic Model with Understanding, Thinking, Planning and Creation
---

# VisionCreator: A Native Visual-Generation Agentic Model with Understanding, Thinking, Planning and Creation
**arXiv**：[2603.02681v1](https://arxiv.org/abs/2603.02681) · [PDF](https://arxiv.org/pdf/2603.02681.pdf)  
**作者**：Jinxiang Lai, Zexin Lu, Jiajun He, Rongwei Quan, Wenzhe Zhao, Qinyu Yang, Qi Chen, Qin Lin, Chuyue Li, Tao Gao, Yuhao Shan, Shuai Shao, Song Guo, Qinglin Lu  

**一句话要点**：提出VisionCreator以解决视觉内容创作中理解、规划与生成一体化难题

**关键词**：视觉生成代理模型, UTPC框架, 渐进专业化训练, 虚拟强化学习, 视觉创作基准

## 3 点简述
- 核心问题：视觉创作需专业知识和流程规划，现有模型或缺乏创意或依赖人工流程。
- 方法要点：构建UTPC框架，通过元认知生成数据和渐进训练优化端到端学习。
- 实验或效果：在VisGenBench上评估，8B/32B模型性能优于更大闭源模型。

## 摘要（原文）

> Visual content creation tasks demand a nuanced understanding of design conventions and creative workflows-capabilities challenging for general models, while workflow-based agents lack specialized knowledge for autonomous creative planning. To overcome these challenges, we propose VisionCreator, a native visual-generation agentic model that unifies Understanding, Thinking, Planning, and Creation (UTPC) capabilities within an end-to-end learnable framework. Our work introduces four key contributions: (i) VisGenData-4k and its construction methodology using metacognition-based VisionAgent to generate high-quality creation trajectories with explicit UTPC structures; (ii) The VisionCreator agentic model, optimized through Progressive Specialization Training (PST) and Virtual Reinforcement Learning (VRL) within a high-fidelity simulated environment, enabling stable and efficient acquisition of UTPC capabilities for complex creation tasks; (iii) VisGenBench, a comprehensive benchmark featuring 1.2k test samples across diverse scenarios for standardized evaluation of multi-step visual creation capabilities; (iv) Remarkably, our VisionCreator-8B/32B models demonstrate superior performance over larger closed-source models across multiple evaluation dimensions. Overall, this work provides a foundation for future research in visual-generation agentic systems.

