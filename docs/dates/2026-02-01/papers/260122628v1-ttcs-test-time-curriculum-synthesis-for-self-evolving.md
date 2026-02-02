---
layout: default
title: TTCS: Test-Time Curriculum Synthesis for Self-Evolving
---

# TTCS: Test-Time Curriculum Synthesis for Self-Evolving
**arXiv**：[2601.22628v1](https://arxiv.org/abs/2601.22628) · [PDF](https://arxiv.org/pdf/2601.22628.pdf)  
**作者**：Chengyi Yang, Zhishang Xiang, Yunbo Tang, Zongpei Teng, Chengsong Huang, Fei Long, Yuhan Liu, Jinsong Su  

**一句话要点**：提出TTCS框架，通过协同进化的测试时课程合成解决大语言模型在困难推理问题上的适应难题。

**关键词**：测试时训练, 课程学习, 大语言模型, 推理能力, 自进化, 协同优化

## 3 点简述
- 核心问题：现有测试时训练方法因原始测试题难度高和测试集规模小，导致伪标签质量低和在线更新不稳定。
- 方法要点：初始化问题合成器和推理求解器，通过迭代优化生成渐进式挑战性问题，并基于自一致性奖励更新模型。
- 实验或效果：在数学基准上增强推理能力，可迁移至通用任务，支持不同大语言模型骨干的动态自进化。

## 摘要（原文）

> Test-Time Training offers a promising way to improve the reasoning ability of large language models (LLMs) by adapting the model using only the test questions. However, existing methods struggle with difficult reasoning problems for two reasons: raw test questions are often too difficult to yield high-quality pseudo-labels, and the limited size of test sets makes continuous online updates prone to instability. To address these limitations, we propose TTCS, a co-evolving test-time training framework. Specifically, TTCS initializes two policies from the same pretrained model: a question synthesizer and a reasoning solver. These policies evolve through iterative optimization: the synthesizer generates progressively challenging question variants conditioned on the test questions, creating a structured curriculum tailored to the solver's current capability, while the solver updates itself using self-consistency rewards computed from multiple sampled responses on both original test and synthetic questions. Crucially, the solver's feedback guides the synthesizer to generate questions aligned with the model's current capability, and the generated question variants in turn stabilize the solver's test-time training. Experiments show that TTCS consistently strengthens the reasoning ability on challenging mathematical benchmarks and transfers to general-domain tasks across different LLM backbones, highlighting a scalable path towards dynamically constructing test-time curricula for self-evolving. Our code and implementation details are available at https://github.com/XMUDeepLIT/TTCS.

