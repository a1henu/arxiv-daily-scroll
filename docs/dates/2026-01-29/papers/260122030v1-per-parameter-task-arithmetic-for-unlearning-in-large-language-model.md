---
layout: default
title: Per-parameter Task Arithmetic for Unlearning in Large Language Models
---

# Per-parameter Task Arithmetic for Unlearning in Large Language Models
**arXiv**：[2601.22030v1](https://arxiv.org/abs/2601.22030) · [PDF](https://arxiv.org/pdf/2601.22030.pdf)  
**作者**：Chengyi Cai, Zesheng Ye, Jiangchao Yao, Jianzhong Qi, Bo Han, Xiaolu Zhang, Feng Liu, Jun Zhou  

**一句话要点**：提出参数级任务算术以解决大语言模型遗忘中的过度遗忘问题

**关键词**：大语言模型遗忘, 任务算术, 参数重要性, 梯度估计, Fisher信息, 模型效用

## 3 点简述
- 核心问题：任务算术遗忘法在移除隐私信息时可能导致过度遗忘，损害模型其他信息的保留能力
- 方法要点：通过梯度或Fisher信息估计每个参数对遗忘与保留的相对重要性，对任务向量进行参数级缩放调整
- 实验或效果：在广泛实验中，PerTA在遗忘效果和模型整体效用上优于标准任务向量，并常超越基于训练的遗忘方法

## 摘要（原文）

> In large language model (LLM) unlearning, private information is required to be removed. Task arithmetic unlearns by subtracting a specific task vector (TV)--defined as the parameter difference between a privacy-information-tuned model and the original model. While efficient, it can cause over-forgetting by disrupting parameters essential for retaining other information. Motivated by the observation that each parameter exhibits different importance for forgetting versus retention, we propose a per-parameter task arithmetic (PerTA) mechanism to rescale the TV, allowing per-parameter adjustment. These weights quantify the relative importance of each parameter for forgetting versus retention, estimated via gradients (i.e., PerTA-grad) or the diagonal Fisher information approximation (i.e., PerTA-fisher). Moreover, we discuss the effectiveness of PerTA, extend it to a more general form, and provide further analysis. Extensive experiments demonstrate that PerTA consistently improves upon standard TV, and in many cases surpasses widely used training-based unlearning methods in both forgetting effectiveness and overall model utility. By retaining the efficiency of task arithmetic while mitigating over-forgetting, PerTA offers a principled and practical framework for LLM unlearning.

