---
layout: default
title: Echo: Towards Advanced Audio Comprehension via Audio-Interleaved Reasoning
---

# Echo: Towards Advanced Audio Comprehension via Audio-Interleaved Reasoning
**arXiv**：[2602.11909v1](https://arxiv.org/abs/2602.11909) · [PDF](https://arxiv.org/pdf/2602.11909.pdf)  
**作者**：Daiqing Wu, Xuan Zhang, Dongbao Yang, Jiashu Yao, Longfei Chen, Qingsong Liu, Sicheng Zhao, Can Ma, Yangyang Kang, Yu Zhou  

**一句话要点**：提出音频交织推理方法以解决大型音频语言模型在复杂音频理解中的信息瓶颈问题。

**关键词**：音频交织推理, 大型音频语言模型, 音频理解, 强化学习, 监督微调, 结构化数据生成

## 3 点简述
- 当前大型音频语言模型通过一次性编码音频内容，存在信息瓶颈，限制了复杂音频理解能力。
- 受人类认知启发，提出音频交织推理，将音频作为主动推理组件，支持持续音频参与和基于感知的分析。
- 通过两阶段训练框架和结构化数据生成，Echo模型在音频理解基准测试中展现出整体优越性。

## 摘要（原文）

> The maturation of Large Audio Language Models (LALMs) has raised growing expectations for them to comprehend complex audio much like humans. Current efforts primarily replicate text-based reasoning by contextualizing audio content through a one-time encoding, which introduces a critical information bottleneck. Drawing inspiration from human cognition, we propose audio-interleaved reasoning to break through this bottleneck. It treats audio as an active reasoning component, enabling sustained audio engagement and perception-grounded analysis. To instantiate it, we introduce a two-stage training framework, first teaching LALMs to localize salient audio segments through supervised fine-tuning, and then incentivizing proficient re-listening via reinforcement learning. In parallel, a structured data generation pipeline is developed to produce high-quality training data. Consequently, we present Echo, a LALM capable of dynamically re-listening to audio in demand during reasoning. On audio comprehension benchmarks, Echo achieves overall superiority in both challenging expert-level and general-purpose tasks. Comprehensive analysis further confirms the efficiency and generalizability of audio-interleaved reasoning, establishing it as a promising direction for advancing audio comprehension. Project page: https://github.com/wdqqdw/Echo.

