---
layout: default
title: Group-Evolving Agents: Open-Ended Self-Improvement via Experience Sharing
---

# Group-Evolving Agents: Open-Ended Self-Improvement via Experience Sharing
**arXiv**：[2602.04837v1](https://arxiv.org/abs/2602.04837) · [PDF](https://arxiv.org/pdf/2602.04837.pdf)  
**作者**：Zhaotian Weng, Antonis Antoniades, Deepak Nathani, Zhen Zhang, Xiao Pu, Xin Eric Wang  

**一句话要点**：提出群体演化代理以通过经验共享实现开放式自我改进，解决编码任务中探索多样性利用不足的问题。

**关键词**：开放式自我改进, 群体演化, 经验共享, 编码基准测试, 进化算法

## 3 点简述
- 核心问题：现有开放式自我演化方法采用树状结构，导致进化分支隔离，探索多样性利用效率低。
- 方法要点：引入群体演化代理，以代理群体为基本进化单元，支持进化过程中显式经验共享与重用。
- 实验或效果：在编码基准测试中显著优于现有自我演化方法，匹配或超越人工设计框架，提升长期进展与鲁棒性。

## 摘要（原文）

> Open-ended self-improving agents can autonomously modify their own structural designs to advance their capabilities and overcome the limits of pre-defined architectures, thus reducing reliance on human intervention. We introduce Group-Evolving Agents (GEA), a new paradigm for open-ended self-improvements, which treats a group of agents as the fundamental evolutionary unit, enabling explicit experience sharing and reuse within the group throughout evolution. Unlike existing open-ended self-evolving paradigms that adopt tree-structured evolution, GEA overcomes the limitation of inefficient utilization of exploratory diversity caused by isolated evolutionary branches. We evaluate GEA on challenging coding benchmarks, where it significantly outperforms state-of-the-art self-evolving methods (71.0% vs. 56.7% on SWE-bench Verified, 88.3% vs. 68.3% on Polyglot) and matches or exceeds top human-designed agent frameworks (71.8% and 52.0% on two benchmarks, respectively). Analysis reveals that GEA more effectively converts early-stage exploratory diversity into sustained, long-term progress, achieving stronger performance under the same number of evolved agents. Furthermore, GEA exhibits consistent transferability across different coding models and greater robustness, fixing framework-level bugs in 1.4 iterations on average, versus 5 for self-evolving methods.

