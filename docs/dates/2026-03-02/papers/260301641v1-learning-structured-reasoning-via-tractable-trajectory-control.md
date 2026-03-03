---
layout: default
title: Learning Structured Reasoning via Tractable Trajectory Control
---

# Learning Structured Reasoning via Tractable Trajectory Control
**arXiv**：[2603.01641v1](https://arxiv.org/abs/2603.01641) · [PDF](https://arxiv.org/pdf/2603.01641.pdf)  
**作者**：Po-Nien Kung, Zhen Yang, Jeffrey Luo, Cheng-Fu Yang, Haikang Deng, Zi-Yi Dou, Yinfei Yang, Nanyun Peng, Zhe Gan, Kai-Wei Chang  

**一句话要点**：提出Ctrl-R框架，通过可控轨迹控制学习结构化推理，以解决大语言模型推理模式稀疏问题。

**关键词**：结构化推理, 可控轨迹控制, 强化学习, 大语言模型, 数学推理

## 3 点简述
- 核心问题：大语言模型在无约束采样中复杂推理轨迹稀疏，标准强化学习难以保证获取多样推理行为。
- 方法要点：通过结构化推理范式，在强化学习过程中主动引导轨迹探索，激励多样推理模式的学习。
- 实验或效果：在数学推理任务上，Ctrl-R实现有效探索和内化，提升语言和视觉语言模型性能。

## 摘要（原文）

> Large language models can exhibit emergent reasoning behaviors, often manifested as recurring lexical patterns (e.g., "wait," indicating verification). However, complex reasoning trajectories remain sparse in unconstrained sampling, and standard RL often fails to guarantee the acquisition of diverse reasoning behaviors. We propose a systematic discovery and reinforcement of diverse reasoning patterns through structured reasoning, a paradigm that requires targeted exploration of specific reasoning patterns during the RL process. To this end, we propose Ctrl-R, a framework for learning structured reasoning via tractable trajectory control that actively guides the rollout process, incentivizing the exploration of diverse reasoning patterns that are critical for complex problem-solving. The resulting behavior policy enables accurate importance-sampling estimation, supporting unbiased on-policy optimization. We further introduce a power-scaling factor on the importance-sampling weights, allowing the policy to selectively learn from exploratory, out-of-distribution trajectories while maintaining stable optimization. Experiments demonstrate that Ctrl-R enables effective exploration and internalization of previously unattainable reasoning patterns, yielding consistent improvements across language and vision-language models on mathematical reasoning tasks.

