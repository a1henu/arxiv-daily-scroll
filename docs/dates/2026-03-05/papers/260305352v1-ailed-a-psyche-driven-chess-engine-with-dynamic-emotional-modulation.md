---
layout: default
title: Ailed: A Psyche-Driven Chess Engine with Dynamic Emotional Modulation
---

# Ailed: A Psyche-Driven Chess Engine with Dynamic Emotional Modulation
**arXiv**：[2603.05352v1](https://arxiv.org/abs/2603.05352) · [PDF](https://arxiv.org/pdf/2603.05352.pdf)  
**作者**：Diego Armando Resendez Prado  

**一句话要点**：提出基于人格与心理动态调制的象棋引擎框架，以模拟人类棋手行为变异性。

**关键词**：象棋引擎, 行为模拟, 动态调制, 概率分布调整, 信号处理, 人类棋手模式

## 3 点简述
- 核心问题：传统象棋引擎缺乏人类棋手在压力或自信下的行为变异性，无法模拟如失误或超常发挥等现象。
- 方法要点：将人格（静态预设）与心理（动态标量ψ_t）结合，通过音频信号链实时调整走棋概率分布，不依赖底层引擎。
- 实验或效果：在12,414局对战中，框架在压力下竞争得分从50.8%降至30.1%，过自信时与原始引擎一致性达66%，行为变化源自信号链而非底层模型。

## 摘要（原文）

> Chess engines passed human strength years ago, but they still don't play like humans. A grandmaster under clock pressure blunders in ways a club player on a hot streak never would. Conventional engines capture none of this.
>   This paper proposes a personality x psyche decomposition to produce behavioral variability in chess play, drawing on patterns observed in human games. Personality is static -- a preset that pins down the engine's character. Psyche is dynamic -- a bounded scalar ψ_t \in [-100, +100], recomputed from five positional factors after every move. These two components feed into an audio-inspired signal chain (noise gate, compressor/expander, five-band equalizer, saturation limiter) that reshapes move probability distributions on the fly. The chain doesn't care what engine sits behind it: any system that outputs move probabilities will do. It needs no search and carries no state beyond ψ_t.
>   I test the framework across 12,414 games against Maia2-1100, feeding it two probability sources that differ by ~2,800x in training data. Both show the same monotonic gradient in top-move agreement (~20-25 pp spread from stress to overconfidence), which tells us the behavioral variation comes from the signal chain, not from the model underneath. When the psyche runs overconfident, the chain mostly gets out of the way (66% agreement with vanilla Maia2). Under stress, the competitive score falls from 50.8% to 30.1%. The patterns are reminiscent of tilt and overconfidence as described in human play, but I should be upfront: this study includes no human-subject validation.

