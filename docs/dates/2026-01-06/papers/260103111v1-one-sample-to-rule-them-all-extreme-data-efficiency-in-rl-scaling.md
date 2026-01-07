---
layout: default
title: One Sample to Rule Them All: Extreme Data Efficiency in RL Scaling
---

# One Sample to Rule Them All: Extreme Data Efficiency in RL Scaling
**arXiv**：[2601.03111v1](https://arxiv.org/abs/2601.03111) · [PDF](https://arxiv.org/pdf/2601.03111.pdf)  
**作者**：Yiyuan Li, Zhen Huang, Yanan Wu, Weixun Wang, Xuefeng Li, Yijia Luo, Wenbo Su, Bo Zheng, Pengfei Liu  

**一句话要点**：提出多学科学习框架，通过单样本强化学习提升大语言模型跨领域推理能力

**关键词**：强化学习, 大语言模型, 单样本学习, 多学科推理, 样本工程

## 3 点简述
- 挑战大语言模型强化学习需大量高质量样本的假设，探索单样本学习的有效性
- 引入多学科学习框架，设计单一样本以激发跨学科推理影响
- 实验显示单数学推理样本能显著提升物理、化学、生物等多领域性能

## 摘要（原文）

> The reasoning ability of large language models (LLMs) can be unleashed with reinforcement learning (RL) (OpenAI, 2024; DeepSeek-AI et al., 2025a; Zeng et al., 2025). The success of existing RL attempts in LLMs usually relies on high-quality samples of thousands or beyond. In this paper, we challenge fundamental assumptions about data requirements in RL for LLMs by demonstrating the remarkable effectiveness of one-shot learning. Specifically, we introduce polymath learning, a framework for designing one training sample that elicits multidisciplinary impact. We present three key findings: (1) A single, strategically selected math reasoning sample can produce significant performance improvements across multiple domains, including physics, chemistry, and biology with RL; (2) The math skills salient to reasoning suggest the characteristics of the optimal polymath sample; and (3) An engineered synthetic sample that integrates multidiscipline elements outperforms training with individual samples that naturally occur. Our approach achieves superior performance to training with larger datasets across various reasoning benchmarks, demonstrating that sample quality and design, rather than quantity, may be the key to unlock enhanced reasoning capabilities in language models. Our results suggest a shift, dubbed as sample engineering, toward precision engineering of training samples rather than simply increasing data volume.

