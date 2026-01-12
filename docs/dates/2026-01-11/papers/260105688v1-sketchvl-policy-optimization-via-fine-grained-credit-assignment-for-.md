---
layout: default
title: SketchVL: Policy Optimization via Fine-Grained Credit Assignment for Chart Understanding and More
---

# SketchVL: Policy Optimization via Fine-Grained Credit Assignment for Chart Understanding and More
**arXiv**：[2601.05688v1](https://arxiv.org/abs/2601.05688) · [PDF](https://arxiv.org/pdf/2601.05688.pdf)  
**作者**：Muye Huang, Lingling Zhang, Yifei Li, Yaqiang Wu, Jun Liu  

**一句话要点**：提出SketchVL模型与FinePO算法，通过细粒度信用分配优化图表理解等任务

**关键词**：图表理解, 多模态大语言模型, 强化学习, 信用分配, 细粒度推理, 过程奖励模型

## 3 点简述
- 核心问题：多模态大语言模型在强化学习中面临轨迹级信用分配不足，无法区分响应内正确与错误推理步骤
- 方法要点：SketchVL在图像上绘制中间推理标记，FinePO算法利用FinePRM对每个绘制动作评分，实现细粒度强化信号
- 实验或效果：在图表、自然图像和数学数据集上平均性能提升7.23%，为训练推理模型提供新方向

## 摘要（原文）

> Charts are high-density visual carriers of complex data and medium for information extraction and analysis. Due to the need for precise and complex visual reasoning, automated chart understanding poses a significant challenge to existing Multimodal Large Language Models (MLLMs). Many MLLMs trained with reinforcement learning (RL) face the challenge of credit assignment. Their advantage estimation, typically performed at the trajectory level, cannot distinguish between correct and incorrect reasoning steps within a single generated response. To address this limitation, we introduce SketchVL, a novel MLLM that optimized with FinePO, a new RL algorithm designed for fine-grained credit assignment within each trajectory. SketchVL's methodology involves drawing its intermediate reasoning steps as markers on the image and feeding the annotated image back to itself, creating a robust, multi-step reasoning process. During training, the FinePO algorithm leverages a Fine-grained Process Reward Model (FinePRM) to score each drawing action within a trajectory, thereby precisely assigning credit for each step. This mechanism allows FinePO to more strongly reward correct tokens when a trajectory is globally successful, and more heavily penalize incorrect tokens when the trajectory is globally suboptimal, thus achieving fine-grained reinforcement signals. Experiments show that SketchVL learns to align its step-level behavior with the FinePRM, achieving an average performance gain of 7.23\% over its base model across chart datasets, natural image datasets, and mathematics, providing a promising new direction for training powerful reasoning models.

