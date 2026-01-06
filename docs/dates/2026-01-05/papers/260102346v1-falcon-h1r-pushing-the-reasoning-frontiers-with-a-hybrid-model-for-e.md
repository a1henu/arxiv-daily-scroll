---
layout: default
title: Falcon-H1R: Pushing the Reasoning Frontiers with a Hybrid Model for Efficient Test-Time Scaling
---

# Falcon-H1R: Pushing the Reasoning Frontiers with a Hybrid Model for Efficient Test-Time Scaling
**arXiv**：[2601.02346v1](https://arxiv.org/abs/2601.02346) · [PDF](https://arxiv.org/pdf/2601.02346.pdf)  
**作者**：Falcon LLM Team, Iheb Chaabane, Puneesh Khanna, Suhail Mohmad, Slim Frikha, Shi Hu, Abdalgader Abubaker, Reda Alami, Mikhail Lubinets, Mohamed El Amine Seddik, Hakim Hacid  

**一句话要点**：提出Falcon-H1R混合模型，通过高效训练与架构设计实现小模型在推理任务中的竞争性能与测试时扩展。

**关键词**：小语言模型, 推理优化, 混合并行架构, 测试时扩展, 参数效率, 链式思维生成

## 3 点简述
- 核心问题：小语言模型在推理任务中性能不足，需提升效率与准确性。
- 方法要点：采用混合并行架构、高效监督微调与强化学习缩放，结合DeepConf方法优化测试时扩展。
- 实验或效果：在多个推理基准上匹配或超越更大模型，实现更快推理、更高准确性和更低计算成本。

## 摘要（原文）

> This work introduces Falcon-H1R, a 7B-parameter reasoning-optimized model that establishes the feasibility of achieving competitive reasoning performance with small language models (SLMs). Falcon-H1R stands out for its parameter efficiency, consistently matching or outperforming SOTA reasoning models that are $2\times$ to $7\times$ larger across a variety of reasoning-intensive benchmarks. These results underscore the importance of careful data curation and targeted training strategies (via both efficient SFT and RL scaling) in delivering significant performance gains without increasing model size. Furthermore, Falcon-H1R advances the 3D limits of reasoning efficiency by combining faster inference (through its hybrid-parallel architecture design), token efficiency, and higher accuracy. This unique blend makes Falcon-H1R-7B a practical backbone for scaling advanced reasoning systems, particularly in scenarios requiring extensive chain-of-thoughts generation and parallel test-time scaling. Leveraging the recently introduced DeepConf approach, Falcon-H1R achieves state-of-the-art test-time scaling efficiency, offering substantial improvements in both accuracy and computational cost. As a result, Falcon-H1R demonstrates that compact models, through targeted model training and architectural choices, can deliver robust and scalable reasoning performance.

