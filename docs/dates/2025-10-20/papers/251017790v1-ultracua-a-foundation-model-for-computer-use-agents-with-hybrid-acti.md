---
layout: default
title: UltraCUA: A Foundation Model for Computer Use Agents with Hybrid Action
---

# UltraCUA: A Foundation Model for Computer Use Agents with Hybrid Action
**arXiv**：[2510.17790v1](https://arxiv.org/abs/2510.17790) · [PDF](https://arxiv.org/pdf/2510.17790.pdf)  
**作者**：Yuhao Yang, Zhen Yang, Zi-Yi Dou, Anh Nguyen, Keen You, Omar Attia, Andrew Szot, Michael Feng, Ram Ramrakhya, Alexander Toshev, Chao Huang, Yinfei Yang, Zhe Gan  

**一句话要点**：提出UltraCUA基础模型，通过混合动作解决计算机使用代理的失败传播与效率瓶颈问题。

**关键词**：计算机使用代理, 混合动作, 基础模型, 强化学习, 程序化工具调用, GUI自动化

## 3 点简述
- 核心问题：计算机使用代理依赖原始GUI动作，易导致错误传播和性能瓶颈。
- 方法要点：结合GUI原始动作与高级程序化工具调用，实现混合动作机制。
- 实验效果：在OSWorld和WindowsAgentArena上显著提升成功率和执行效率。

## 摘要（原文）

> Multimodal agents for computer use rely exclusively on primitive actions
> (click, type, scroll) that require accurate visual grounding and lengthy
> execution chains, leading to cascading failures and performance bottlenecks.
> While other agents leverage rich programmatic interfaces (APIs, MCP servers,
> tools), computer-use agents (CUAs) remain isolated from these capabilities. We
> present UltraCUA, a foundation model that bridges this gap through hybrid
> action -- seamlessly integrating GUI primitives with high-level programmatic
> tool calls. To achieve this, our approach comprises four key components: (1) an
> automated pipeline that scales programmatic tools from software documentation,
> open-source repositories, and code generation; (2) a synthetic data engine
> producing over 17,000 verifiable tasks spanning real-world computer-use
> scenarios; (3) a large-scale high-quality hybrid action trajectory collection
> with both low-level GUI actions and high-level programmatic tool calls; and (4)
> a two-stage training pipeline combining supervised fine-tuning with online
> reinforcement learning, enabling strategic alternation between low-level and
> high-level actions. Experiments with our 7B and 32B models demonstrate
> substantial improvements over state-of-the-art agents. On OSWorld, UltraCUA
> models achieve an average 22% relative improvement over base models, while
> being 11% faster in terms of steps. Out-of-domain evaluation on
> WindowsAgentArena shows our model reaches 21.7% success rate, outperforming
> baselines trained on Windows data. The hybrid action mechanism proves critical,
> reducing error propagation while maintaining execution efficiency.

