---
layout: default
title: SketchThinker-R1: Towards Efficient Sketch-Style Reasoning in Large Multimodal Models
---

# SketchThinker-R1: Towards Efficient Sketch-Style Reasoning in Large Multimodal Models
**arXiv**：[2601.02825v1](https://arxiv.org/abs/2601.02825) · [PDF](https://arxiv.org/pdf/2601.02825.pdf)  
**作者**：Ruiyang Zhang, Dongzhan Zhou, Zhedong Zheng  

**一句话要点**：提出SketchThinker-R1以提升大型多模态模型推理效率，通过草图式推理减少计算开销。

**关键词**：草图式推理, 推理效率, 多模态模型, 强化学习, 令牌成本优化

## 3 点简述
- 核心问题：大型多模态模型的长推理过程导致高计算开销，如令牌成本和响应时间增加。
- 方法要点：采用三阶段方法，包括草图模式冷启动、训练SketchJudge奖励模型和草图思维强化学习。
- 实验或效果：在四个基准测试中，推理令牌成本降低超过64%，同时保持答案准确性。

## 摘要（原文）

> Despite the empirical success of extensive, step-by-step reasoning in large multimodal models, long reasoning processes inevitably incur substantial computational overhead, i.e., in terms of higher token costs and increased response time, which undermines inference efficiency. In contrast, humans often employ sketch-style reasoning: a concise, goal-directed cognitive process that prioritizes salient information and enables efficient problem-solving. Inspired by this cognitive efficiency, we propose SketchThinker-R1, which incentivizes sketch-style reasoning ability in large multimodal models. Our method consists of three primary stages. In the Sketch-Mode Cold Start stage, we convert standard long reasoning process into sketch-style reasoning and finetune base multimodal model, instilling initial sketch-style reasoning capability. Next, we train SketchJudge Reward Model, which explicitly evaluates thinking process of model and assigns higher scores to sketch-style reasoning. Finally, we conduct Sketch-Thinking Reinforcement Learning under supervision of SketchJudge to further generalize sketch-style reasoning ability. Experimental evaluation on four benchmarks reveals that our SketchThinker-R1 achieves over 64% reduction in reasoning token cost without compromising final answer accuracy. Qualitative analysis further shows that sketch-style reasoning focuses more on key cues during problem solving.

