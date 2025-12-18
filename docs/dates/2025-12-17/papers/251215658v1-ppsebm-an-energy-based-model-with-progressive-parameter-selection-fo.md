---
layout: default
title: PPSEBM: An Energy-Based Model with Progressive Parameter Selection for Continual Learning
---

# PPSEBM: An Energy-Based Model with Progressive Parameter Selection for Continual Learning
**arXiv**：[2512.15658v1](https://arxiv.org/abs/2512.15658) · [PDF](https://arxiv.org/pdf/2512.15658.pdf)  
**作者**：Xiaodi Li, Dingcheng Li, Rujun Gao, Mahmoud Zamani, Feng Mi, Latifur Khan  

**一句话要点**：提出PPSEBM框架，结合能量模型与渐进参数选择以解决自然语言处理中的灾难性遗忘问题

**关键词**：持续学习, 灾难性遗忘, 能量模型, 渐进参数选择, 自然语言处理

## 3 点简述
- 核心问题：持续学习中灾难性遗忘导致模型遗忘旧任务知识
- 方法要点：渐进参数选择分配任务特定参数，能量模型生成旧任务伪样本指导选择
- 实验或效果：在多种NLP基准测试中优于现有持续学习方法，有效缓解遗忘

## 摘要（原文）

> Continual learning remains a fundamental challenge in machine learning, requiring models to learn from a stream of tasks without forgetting previously acquired knowledge. A major obstacle in this setting is catastrophic forgetting, where performance on earlier tasks degrades as new tasks are learned. In this paper, we introduce PPSEBM, a novel framework that integrates an Energy-Based Model (EBM) with Progressive Parameter Selection (PPS) to effectively address catastrophic forgetting in continual learning for natural language processing tasks. In PPSEBM, progressive parameter selection allocates distinct, task-specific parameters for each new task, while the EBM generates representative pseudo-samples from prior tasks. These generated samples actively inform and guide the parameter selection process, enhancing the model's ability to retain past knowledge while adapting to new tasks. Experimental results on diverse NLP benchmarks demonstrate that PPSEBM outperforms state-of-the-art continual learning methods, offering a promising and robust solution to mitigate catastrophic forgetting.

