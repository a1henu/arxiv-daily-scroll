---
layout: default
title: TACLer: Tailored Curriculum Reinforcement Learning for Efficient Reasoning
---

# TACLer: Tailored Curriculum Reinforcement Learning for Efficient Reasoning
**arXiv**：[2601.21711v1](https://arxiv.org/abs/2601.21711) · [PDF](https://arxiv.org/pdf/2601.21711.pdf)  
**作者**：Huiyuan Lai, Malvina Nissim  

**一句话要点**：提出TACLer框架，通过定制化课程强化学习提升大语言模型推理效率与性能

**关键词**：课程强化学习, 大语言模型推理, 思维链优化, 计算效率提升, 混合推理范式

## 3 点简述
- 核心问题：长链思维推理训练计算成本高且易产生冗余步骤，影响效率与准确性。
- 方法要点：采用模型定制化课程学习，分阶段增加数据复杂度，结合Thinking/NoThinking混合推理范式平衡精度与效率。
- 实验或效果：训练计算成本降低超50%，推理令牌使用减少超42%，在四个数学数据集上准确率提升超9%。

## 摘要（原文）

> Large Language Models (LLMs) have shown remarkable performance on complex reasoning tasks, especially when equipped with long chain-of-thought (CoT) reasoning. However, eliciting long CoT typically requires large-scale reinforcement learning (RL) training, while often leading to overthinking with redundant intermediate steps. To improve learning and reasoning efficiency, while preserving or even enhancing performance, we propose TACLer, a model-tailored curriculum reinforcement learning framework that gradually increases the complexity of the data based on the model's proficiency in multi-stage RL training. TACLer features two core components: (i) tailored curriculum learning that determines what knowledge the model lacks and needs to learn in progressive stages; (ii) a hybrid Thinking/NoThinking reasoning paradigm that balances accuracy and efficiency by enabling or disabling the Thinking mode. Our experiments show that TACLer yields a twofold advantage in learning and reasoning: (i) it reduces computational cost, cutting training compute by over 50% compared to long thinking models and reducing inference token usage by over 42% relative to the base model; and (ii) it improves accuracy by over 9% on the base model, consistently outperforming state-of-the-art Nothinking and Thinking baselines across four math datasets with complex problems.

