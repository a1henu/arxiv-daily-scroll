---
layout: default
title: DeepSport: A Multimodal Large Language Model for Comprehensive Sports Video Reasoning via Agentic Reinforcement Learning
---

# DeepSport: A Multimodal Large Language Model for Comprehensive Sports Video Reasoning via Agentic Reinforcement Learning
**arXiv**：[2511.12908v1](https://arxiv.org/abs/2511.12908) · [PDF](https://arxiv.org/pdf/2511.12908.pdf)  
**作者**：Junbo Zou, Haotian Xia, Zhen Ye, Shengjie Zhang, Christopher Lai, Vicente Ordonez, Weining Shen, Hanjie Chen  

**一句话要点**：提出DeepSport多模态大模型，通过代理强化学习解决多运动视频理解问题

**关键词**：多模态大语言模型, 体育视频理解, 代理强化学习, 数据蒸馏, 端到端训练, 多任务学习

## 3 点简述
- 核心问题：体育视频理解需处理高速动态、复杂规则和长时序上下文，现有方法局限于单运动或特定任务
- 方法要点：采用端到端训练，结合监督微调和强化学习，使用门控工具奖励优化推理过程
- 实验或效果：在6.7k问题测试集上达到最优性能，显著超越专有和开源基线模型

## 摘要（原文）

> Sports video understanding presents unique challenges, requiring models to perceive high-speed dynamics, comprehend complex rules, and reason over long temporal contexts. While Multimodal Large Language Models (MLLMs) have shown promise in genral domains, the current state of research in sports remains narrowly focused: existing approaches are either single-sport centric, limited to specific tasks, or rely on training-free paradigms that lack robust, learned reasoning process. To address this gap, we introduce DeepSport, the first end-to-end trained MLLM framework designed for multi-task, multi-sport video understanding. DeepSport shifts the paradigm from passive frame processing to active, iterative reasoning, empowering the model to ``think with videos'' by dynamically interrogating content via a specialized frame-extraction tool. To enable this, we propose a data distillation pipeline that synthesizes high-quality Chain-of-Thought (CoT) trajectories from 10 diverse data source, creating a unified resource of 78k training data. We then employ a two-stage training strategy, Supervised Fine-Tuning (SFT) followed by Reinforcement Learning (RL) with a novel gated tool-use reward, to optimize the model's reasoning process. Extensive experiments on the testing benchmark of 6.7k questions demonstrate that DeepSport achieves state-of-the-art performance, significantly outperforming baselines of both proprietary model and open-source models. Our work establishes a new foundation for domain-specific video reasoning to address the complexities of diverse sports.

