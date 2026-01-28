---
layout: default
title: Exploring Weaknesses in Function Call Models via Reinforcement Learning: An Adversarial Data Augmentation Approach
---

# Exploring Weaknesses in Function Call Models via Reinforcement Learning: An Adversarial Data Augmentation Approach
**arXiv**：[2601.19122v1](https://arxiv.org/abs/2601.19122) · [PDF](https://arxiv.org/pdf/2601.19122.pdf)  
**作者**：Weiran Guo, Bing Bo, Shaoxiang Wu, Jingsheng Yang  

**一句话要点**：提出基于强化学习的对抗性数据增强方法，以提升函数调用大语言模型的鲁棒性。

**关键词**：函数调用模型, 对抗性数据增强, 强化学习, 大语言模型, 鲁棒性提升

## 3 点简述
- 核心问题：现有方法依赖固定模式数据，限制函数调用模型的泛化与鲁棒性。
- 方法要点：使用强化学习训练查询模型，生成对抗性查询挑战函数调用模型。
- 实验或效果：通过迭代对抗训练，系统识别并纠正模型弱点，增强与外部工具交互能力。

## 摘要（原文）

> Function call capabilities have become crucial for Large Language Models (LLMs), enabling them to interact more effectively with external tools and APIs. Existing methods for improving the function call capabilities of LLMs rely on data obtained either through manual annotation or automated generation by models, and use this data to finetune the LLMs. However, these methods often lack targeted design and are constrained by fixed patterns and data distributions, which limits their effectiveness in enhancing the generalization and robustness of function call LLMs. To address this limitation, we propose a novel adversarial data augmentation method that employs reinforcement learning to systematically identify and target the weaknesses of function call LLMs. Our training framework introduces a query model trained with reinforcement learning (RL) to generate adversarial queries that are specifically designed to challenge function call (FC) models. This approach adopts a zero sum game formulation, where the query model and the FC model engage in iterative alternating training. Overall, our method advances the development of more robust FC models and provides a systematic way to identify and correct weaknesses in the ability of LLMs to interact with external tools.

