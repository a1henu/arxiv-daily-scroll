---
layout: default
title: Chain of Event-Centric Causal Thought for Physically Plausible Video Generation
---

# Chain of Event-Centric Causal Thought for Physically Plausible Video Generation
**arXiv**：[2603.09094v1](https://arxiv.org/abs/2603.09094) · [PDF](https://arxiv.org/pdf/2603.09094.pdf)  
**作者**：Zixuan Wang, Yixin Hu, Haolan Wang, Feng Chen, Yan Liu, Wen Li, Yinjie Lei  

**一句话要点**：提出事件链因果推理与跨模态提示框架，以生成物理合理视频

**关键词**：物理合理视频生成, 因果推理, 事件链分解, 跨模态提示, 视频扩散模型, 物理公式约束

## 3 点简述
- 核心问题：视频扩散模型缺乏因果进展建模，导致物理现象生成不连贯
- 方法要点：设计物理驱动事件链推理模块，嵌入物理公式约束以分解提示为因果事件单元
- 实验或效果：在PhyGenBench和VideoPhy基准上实现优越性能，生成多样化物理领域视频

## 摘要（原文）

> Physically Plausible Video Generation (PPVG) has emerged as a promising avenue for modeling real-world physical phenomena. PPVG requires an understanding of commonsense knowledge, which remains a challenge for video diffusion models. Current approaches leverage commonsense reasoning capability of large language models to embed physical concepts into prompts. However, generation models often render physical phenomena as a single moment defined by prompts, due to the lack of conditioning mechanisms for modeling causal progression. In this paper, we view PPVG as generating a sequence of causally connected and dynamically evolving events. To realize this paradigm, we design two key modules: (1) Physics-driven Event Chain Reasoning. This module decomposes the physical phenomena described in prompts into multiple elementary event units, leveraging chain-of-thought reasoning. To mitigate causal ambiguity, we embed physical formulas as constraints to impose deterministic causal dependencies during reasoning. (2) Transition-aware Cross-modal Prompting (TCP). To maintain continuity between events, this module transforms causal event units into temporally aligned vision-language prompts. It summarizes discrete event descriptions to obtain causally consistent narratives, while progressively synthesizing visual keyframes of individual events by interactive editing. Comprehensive experiments on PhyGenBench and VideoPhy benchmarks demonstrate that our framework achieves superior performance in generating physically plausible videos across diverse physical domains. Our code will be released soon.

