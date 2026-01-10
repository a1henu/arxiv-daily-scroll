---
layout: default
title: AgentOCR: Reimagining Agent History via Optical Self-Compression
---

# AgentOCR: Reimagining Agent History via Optical Self-Compression
**arXiv**：[2601.04786v1](https://arxiv.org/abs/2601.04786) · [PDF](https://arxiv.org/pdf/2601.04786.pdf)  
**作者**：Lang Feng, Fuchao Yang, Feng Chen, Xin Cheng, Haiyang Xu, Zhenglin Wan, Ming Yan, Bo An  

**一句话要点**：提出AgentOCR框架，通过视觉压缩解决多轮交互中文本历史膨胀问题

**关键词**：智能体系统, 视觉压缩, 分段缓存, 自压缩训练, 令牌效率, 多轮交互

## 3 点简述
- 核心问题：多轮交互中文本历史导致令牌预算和内存使用快速增长，阻碍智能体系统部署
- 方法要点：将历史表示为紧凑图像，利用分段光学缓存消除冗余渲染，并引入自压缩机制平衡任务成功与令牌效率
- 实验或效果：在ALFWorld和搜索QA基准上，保持95%以上性能，减少超50%令牌消耗，渲染速度提升20倍

## 摘要（原文）

> Recent advances in large language models (LLMs) enable agentic systems trained with reinforcement learning (RL) over multi-turn interaction trajectories, but practical deployment is bottlenecked by rapidly growing textual histories that inflate token budgets and memory usage. We introduce AgentOCR, a framework that exploits the superior information density of visual tokens by representing the accumulated observation-action history as a compact rendered image. To make multi-turn rollouts scalable, AgentOCR proposes segment optical caching. By decomposing history into hashable segments and maintaining a visual cache, this mechanism eliminates redundant re-rendering. Beyond fixed rendering, AgentOCR introduces agentic self-compression, where the agent actively emits a compression rate and is trained with compression-aware reward to adaptively balance task success and token efficiency. We conduct extensive experiments on challenging agentic benchmarks, ALFWorld and search-based QA. Remarkably, results demonstrate that AgentOCR preserves over 95\% of text-based agent performance while substantially reducing token consumption (>50\%), yielding consistent token and memory efficiency. Our further analysis validates a 20x rendering speedup from segment optical caching and the effective strategic balancing of self-compression.

