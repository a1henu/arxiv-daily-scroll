---
layout: default
title: Integrating Fine-Grained Audio-Visual Evidence for Robust Multimodal Emotion Reasoning
---

# Integrating Fine-Grained Audio-Visual Evidence for Robust Multimodal Emotion Reasoning
**arXiv**：[2601.18321v1](https://arxiv.org/abs/2601.18321) · [PDF](https://arxiv.org/pdf/2601.18321.pdf)  
**作者**：Zhixian Zhao, Wenjie Tian, Xiaohai Tian, Jun Zhang, Lei Xie  

**一句话要点**：提出SABER-LLM框架以解决多模态情感推理中的细粒度感知不足问题

**关键词**：多模态情感推理, 细粒度感知, 结构化证据分解, 一致性优化, 大规模数据集, 幻觉缓解

## 3 点简述
- 当前多模态大语言模型在细粒度感知上受限，易产生幻觉，尤其在视觉和声学线索微妙或矛盾时
- 构建SABER大规模情感推理数据集，并采用结构化证据分解和一致性感知优化方法
- 在多个基准测试中显著优于开源基线，并在复杂情感动态解码上达到与闭源模型竞争的鲁棒性

## 摘要（原文）

> Multimodal emotion analysis is shifting from static classification to generative reasoning. Beyond simple label prediction, robust affective reasoning must synthesize fine-grained signals such as facial micro-expressions and prosodic which shifts to decode the latent causality within complex social contexts. However, current Multimodal Large Language Models (MLLMs) face significant limitations in fine-grained perception, primarily due to data scarcity and insufficient cross-modal fusion. As a result, these models often exhibit unimodal dominance which leads to hallucinations in complex multimodal interactions, particularly when visual and acoustic cues are subtle, ambiguous, or even contradictory (e.g., in sarcastic scenery). To address this, we introduce SABER-LLM, a framework designed for robust multimodal reasoning. First, we construct SABER, a large-scale emotion reasoning dataset comprising 600K video clips, annotated with a novel six-dimensional schema that jointly captures audiovisual cues and causal logic. Second, we propose the structured evidence decomposition paradigm, which enforces a "perceive-then-reason" separation between evidence extraction and reasoning to alleviate unimodal dominance. The ability to perceive complex scenes is further reinforced by consistency-aware direct preference optimization, which explicitly encourages alignment among modalities under ambiguous or conflicting perceptual conditions. Experiments on EMER, EmoBench-M, and SABER-Test demonstrate that SABER-LLM significantly outperforms open-source baselines and achieves robustness competitive with closed-source models in decoding complex emotional dynamics. The dataset and model are available at https://github.com/zxzhao0/SABER-LLM.

