---
layout: default
title: ChatUMM: Robust Context Tracking for Conversational Interleaved Generation
---

# ChatUMM: Robust Context Tracking for Conversational Interleaved Generation
**arXiv**：[2602.06442v1](https://arxiv.org/abs/2602.06442) · [PDF](https://arxiv.org/pdf/2602.06442.pdf)  
**作者**：Wenxun Dai, Zhiyuan Zhao, Yule Zhong, Yiji Cheng, Jianwei Zhang, Linqing Wang, Shiyi Zhang, Yunlong Lin, Runze He, Fellix Song, Wayne Zhuang, Yong Liu, Haoji Zhang, Yansong Tang, Qinglin Lu, Chunyu Wang  

**一句话要点**：提出ChatUMM以解决统一多模态模型在连续对话中上下文跟踪的挑战

**关键词**：统一多模态模型, 上下文跟踪, 交错多轮训练, 对话数据合成, 视觉理解, 指令引导编辑

## 3 点简述
- 核心问题：统一多模态模型局限于单轮交互，缺乏连续对话中的上下文跟踪能力。
- 方法要点：采用交错多轮训练策略和系统对话数据合成流水线，增强模型在交错多模态生成中的鲁棒性。
- 实验或效果：在视觉理解和指令引导编辑基准上达到开源统一模型的最优性能，并在多轮场景中展现优越鲁棒性。

## 摘要（原文）

> Unified multimodal models (UMMs) have achieved remarkable progress yet remain constrained by a single-turn interaction paradigm, effectively functioning as solvers for independent requests rather than assistants in continuous dialogue. To bridge this gap, we present ChatUMM. As a conversational unified model, it excels at robust context tracking to sustain interleaved multimodal generation. ChatUMM derives its capabilities from two key innovations: an interleaved multi-turn training strategy that models serialized text-image streams as a continuous conversational flow, and a systematic conversational data synthesis pipeline. This pipeline transforms a diverse set of standard single-turn datasets into fluid dialogues through three progressive stages: constructing basic stateful dialogues, enforcing long-range dependency resolution via ``distractor'' turns with history-dependent query rewriting, and synthesizing naturally interleaved multimodal responses. Extensive evaluations demonstrate that ChatUMM achieves state-of-the-art performance among open-source unified models on visual understanding and instruction-guided editing benchmarks, while maintaining competitive fidelity in text-to-image generation. Notably, ChatUMM exhibits superior robustness in complex multi-turn scenarios, ensuring fluid, context-aware dialogues.

