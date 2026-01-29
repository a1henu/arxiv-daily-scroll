---
layout: default
title: SERA: Soft-Verified Efficient Repository Agents
---

# SERA: Soft-Verified Efficient Repository Agents
**arXiv**：[2601.20789v1](https://arxiv.org/abs/2601.20789) · [PDF](https://arxiv.org/pdf/2601.20789.pdf)  
**作者**：Ethan Shen, Danny Tormoen, Saurabh Shah, Ali Farhadi, Tim Dettmers  

**一句话要点**：提出SERA方法以高效训练专用于私有代码库的开源编码代理

**关键词**：编码代理, 监督微调, 合成数据生成, 私有代码库专业化, 开源模型

## 3 点简述
- 核心问题：开源编码代理训练成本高，难以针对私有代码库进行专业化。
- 方法要点：使用Soft Verified Generation生成合成轨迹，结合监督微调实现高效训练。
- 实验或效果：SERA性能媲美前沿开源模型，训练成本降低26至57倍。

## 摘要（原文）

> Open-weight coding agents should hold a fundamental advantage over closed-source systems: they can be specialized to private codebases, encoding repository-specific information directly in their weights. Yet the cost and complexity of training has kept this advantage theoretical. We show it is now practical. We present Soft-Verified Efficient Repository Agents (SERA), an efficient method for training coding agents that enables the rapid and cheap creation of agents specialized to private codebases. Using only supervised finetuning (SFT), SERA achieves state-of-the-art results among fully open-source (open data, method, code) models while matching the performance of frontier open-weight models like Devstral-Small-2. Creating SERA models is 26x cheaper than reinforcement learning and 57x cheaper than previous synthetic data methods to reach equivalent performance. Our method, Soft Verified Generation (SVG), generates thousands of trajectories from a single code repository. Combined with cost-efficiency, this enables specialization to private codebases. Beyond repository specialization, we apply SVG to a larger corpus of codebases, generating over 200,000 synthetic trajectories. We use this dataset to provide detailed analysis of scaling laws, ablations, and confounding factors for training coding agents. Overall, we believe our work will greatly accelerate research on open coding agents and showcase the advantage of open-source models that can specialize to private codebases. We release SERA as the first model in Ai2's Open Coding Agents series, along with all our code, data, and Claude Code integration to support the research community.

