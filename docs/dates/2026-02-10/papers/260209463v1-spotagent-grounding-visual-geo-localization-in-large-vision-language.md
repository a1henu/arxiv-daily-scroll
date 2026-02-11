---
layout: default
title: SpotAgent: Grounding Visual Geo-localization in Large Vision-Language Models through Agentic Reasoning
---

# SpotAgent: Grounding Visual Geo-localization in Large Vision-Language Models through Agentic Reasoning
**arXiv**：[2602.09463v1](https://arxiv.org/abs/2602.09463) · [PDF](https://arxiv.org/pdf/2602.09463.pdf)  
**作者**：Furong Jia, Ling Dai, Wenjin Deng, Fan Zhang, Chen Hu, Daxin Jiang, Yu Liu  

**一句话要点**：提出SpotAgent框架，通过代理推理解决视觉地理定位中稀疏、长尾和模糊场景的挑战。

**关键词**：视觉地理定位, 大型视觉语言模型, 代理推理, 工具辅助验证, 强化学习, 空间感知过滤

## 3 点简述
- 核心问题：大型视觉语言模型在视觉线索稀疏、长尾和高度模糊的真实场景中易产生未经验证的幻觉预测。
- 方法要点：将地理定位形式化为代理推理过程，结合视觉解释与工具辅助验证，采用三阶段后训练流程提升模型能力。
- 实验或效果：在标准基准测试中实现最先进性能，有效减少幻觉并提供精确可验证的地理定位结果。

## 摘要（原文）

> Large Vision-Language Models (LVLMs) have demonstrated strong reasoning capabilities in geo-localization, yet they often struggle in real-world scenarios where visual cues are sparse, long-tailed, and highly ambiguous. Previous approaches, bound by internal knowledge, often fail to provide verifiable results, yielding confident but ungrounded predictions when faced with confounded evidence. To address these challenges, we propose SpotAgent, a framework that formalizes geo-localization into an agentic reasoning process that leverages expert-level reasoning to synergize visual interpretation with tool-assisted verification. SpotAgent actively explores and verifies visual cues by leveraging external tools (e.g., web search, maps) through a ReAct diagram. We introduce a 3-stage post-training pipeline starting with a Supervised Fine-Tuning (SFT) stage for basic alignment, followed by an Agentic Cold Start phase utilizing high-quality trajectories synthesized via a Multi-Agent framework, aiming to instill tool-calling expertise. Subsequently, the model's reasoning capabilities are refined through Reinforcement Learning. We propose a Spatially-Aware Dynamic Filtering strategy to enhance the efficiency of the RL stage by prioritizing learnable samples based on spatial difficulty. Extensive experiments on standard benchmarks demonstrate that SpotAgent achieves state-of-the-art performance, effectively mitigating hallucinations while delivering precise and verifiable geo-localization.

