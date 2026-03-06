---
layout: default
title: Evaluating the Search Agent in a Parallel World
---

# Evaluating the Search Agent in a Parallel World
**arXiv**：[2603.04751v1](https://arxiv.org/abs/2603.04751) · [PDF](https://arxiv.org/pdf/2603.04751.pdf)  
**作者**：Jiawei Chen, Xintian Shen, Lihao Zheng, Lifu Mu, Haoyi Sun, Ning Mao, Hao Ma, Tao Wei, Pan Zhou, Kun Zhan  

**一句话要点**：提出Mind-ParaWorld框架以解决搜索代理评估中的动态过时与归因模糊问题

**关键词**：搜索代理评估, 动态基准构建, 原子事实生成, 交互式基准, 归因模糊, 可复现性

## 3 点简述
- 核心问题：搜索代理评估面临高质量基准构建昂贵、静态基准动态过时、归因模糊和依赖商业引擎导致可复现性差。
- 方法要点：通过合成未来场景和问题，使用ParaWorld Law Model构建原子事实和唯一真值，并让代理与基于原子事实动态生成SERPs的ParaWorld Engine Model交互。
- 实验或效果：发布MPW-Bench基准，实验显示搜索代理在证据合成方面强，但在陌生环境中的证据收集、覆盖、判断和停止决策方面存在瓶颈。

## 摘要（原文）

> Integrating web search tools has significantly extended the capability of LLMs to address open-world, real-time, and long-tail problems. However, evaluating these Search Agents presents formidable challenges. First, constructing high-quality deep search benchmarks is prohibitively expensive, while unverified synthetic data often suffers from unreliable sources. Second, static benchmarks face dynamic obsolescence: as internet information evolves, complex queries requiring deep research often degrade into simple retrieval tasks due to increased popularity, and ground truths become outdated due to temporal shifts. Third, attribution ambiguity confounds evaluation, as an agent's performance is often dominated by its parametric memory rather than its actual search and reasoning capabilities. Finally, reliance on specific commercial search engines introduces variability that hampers reproducibility. To address these issues, we propose a novel framework, Mind-ParaWorld, for evaluating Search Agents in a Parallel World. Specifically, MPW samples real-world entity names to synthesize future scenarios and questions situated beyond the model's knowledge cutoff. A ParaWorld Law Model then constructs a set of indivisible Atomic Facts and a unique ground-truth for each question. During evaluation, instead of retrieving real-world results, the agent interacts with a ParaWorld Engine Model that dynamically generates SERPs grounded in these inviolable Atomic Facts. We release MPW-Bench, an interactive benchmark spanning 19 domains with 1,608 instances. Experiments across three evaluation settings show that, while search agents are strong at evidence synthesis given complete information, their performance is limited not only by evidence collection and coverage in unfamiliar search environments, but also by unreliable evidence sufficiency judgment and when-to-stop decisions-bottlenecks.

