---
layout: default
title: Demo-ICL: In-Context Learning for Procedural Video Knowledge Acquisition
---

# Demo-ICL: In-Context Learning for Procedural Video Knowledge Acquisition
**arXiv**：[2602.08439v1](https://arxiv.org/abs/2602.08439) · [PDF](https://arxiv.org/pdf/2602.08439.pdf)  
**作者**：Yuhao Dong, Shulin Tian, Shuai Liu, Shuangrui Ding, Yuhang Zang, Xiaoyi Dong, Yuhang Cao, Jiaqi Wang, Ziwei Liu  

**一句话要点**：提出Demo-ICL任务与基准，通过演示驱动视频上下文学习解决多模态大模型动态知识获取问题。

**关键词**：视频上下文学习, 多模态大语言模型, 演示驱动学习, 基准评估, 两阶段训练

## 3 点简述
- 核心问题：现有视频基准主要评估静态知识，而非从动态上下文示例中学习的能力。
- 方法要点：开发Demo-ICL模型，采用视频监督微调和信息辅助直接偏好优化的两阶段训练策略。
- 实验或效果：构建Demo-ICL-Bench基准，实验验证其挑战性及Demo-ICL的有效性。

## 摘要（原文）

> Despite the growing video understanding capabilities of recent Multimodal Large Language Models (MLLMs), existing video benchmarks primarily assess understanding based on models' static, internal knowledge, rather than their ability to learn and adapt from dynamic, novel contexts from few examples. To bridge this gap, we present Demo-driven Video In-Context Learning, a novel task focused on learning from in-context demonstrations to answer questions about the target videos. Alongside this, we propose Demo-ICL-Bench, a challenging benchmark designed to evaluate demo-driven video in-context learning capabilities. Demo-ICL-Bench is constructed from 1200 instructional YouTube videos with associated questions, from which two types of demonstrations are derived: (i) summarizing video subtitles for text demonstration; and (ii) corresponding instructional videos as video demonstrations. To effectively tackle this new challenge, we develop Demo-ICL, an MLLM with a two-stage training strategy: video-supervised fine-tuning and information-assisted direct preference optimization, jointly enhancing the model's ability to learn from in-context examples. Extensive experiments with state-of-the-art MLLMs confirm the difficulty of Demo-ICL-Bench, demonstrate the effectiveness of Demo-ICL, and thereby unveil future research directions.

