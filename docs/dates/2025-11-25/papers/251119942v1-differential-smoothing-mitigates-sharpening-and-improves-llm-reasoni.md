---
layout: default
title: Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning
---

# Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning
**arXiv**：[2511.19942v1](https://arxiv.org/abs/2511.19942) · [PDF](https://arxiv.org/pdf/2511.19942.pdf)  
**作者**：Jingchu Gai, Guanning Zeng, Huaqing Zhang, Aditi Raghunathan  

**一句话要点**：提出差分平滑方法以缓解强化学习微调中的多样性崩溃问题

**关键词**：强化学习微调, 多样性崩溃, 差分平滑, 语言模型推理, 数学推理, 奖励修改

## 3 点简述
- 核心问题：强化学习微调导致多样性崩溃，输出缺乏多样性
- 方法要点：基于正确轨迹应用差分平滑，理论上提升正确性和多样性
- 实验或效果：在1B至7B模型上实验，Pass@1和Pass@k指标提升，AIME24数据集改进6.7%

## 摘要（原文）

> It is widely recognized that reinforcement learning (RL) fine-tuning of large language models often leads to \textit{diversity collapse}, where outputs lack variety. Prior work has proposed a range of heuristics to counteract this effect, but these methods are ad hoc: they frequently trade off correctness for diversity, their effectiveness varies across tasks, and in some cases they even contradict one another. In this work, we place these observations on a rigorous foundation. We first provide a formal proof of why RL fine-tuning exhibits diversity collapse via a selection and reinforcement bias. Next, we make a key observation that any reward modification to address diversity collapse only needs to be applied on the correct trajectories. Building directly on this analysis, we introduce a principled method -- \textit{differential smoothing} -- that provably improves both correctness and diversity, outperforming vanilla RL as well as widely used entropy-based heuristics. Our theory precisely characterizes when existing heuristics help and why they fail, while showing that differential smoothing is universally superior. Extensive experiments with models from 1B to 7B parameters, across domains including CountDown and real-world mathematical reasoning, demonstrate consistent gains. Differential smoothing improves both Pass@1 and Pass@k, with up to 6.7\% improvements on AIME24 dataset.

