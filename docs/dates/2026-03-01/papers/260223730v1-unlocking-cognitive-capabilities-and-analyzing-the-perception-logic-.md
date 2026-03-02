---
layout: default
title: Unlocking Cognitive Capabilities and Analyzing the Perception-Logic Trade-off
---

# Unlocking Cognitive Capabilities and Analyzing the Perception-Logic Trade-off
**arXiv**：[2602.23730v1](https://arxiv.org/abs/2602.23730) · [PDF](https://arxiv.org/pdf/2602.23730.pdf)  
**作者**：Longyin Zhang, Shuo Sun, Yingxu He, Won Cheng Yi Lewis, Muhammad Huzaifah Bin Md Shahrin, Hardik Bhupendra Sailor, Heng Meng Jeremy Wong, Tarun Kumar Vangani, Yi Ma, Qiongqiong Wang, Minh Duc Pham, Ridong Jiang, Jingtao Li, Jingyi Liao, Zhuohan Liu, Yanfeng Lu, Manas Gupta, Ai Ti Aw  

**一句话要点**：提出MERaLiON2-Omni模型，通过解耦与集成感知与推理能力，针对东南亚地区优化多模态理解。

**关键词**：多模态大语言模型, 感知-推理解耦, 东南亚多语言, 生成-判断-精炼, 效率-稳定性悖论

## 3 点简述
- 核心问题：多模态大语言模型在感知与推理结合上存在挑战，尤其在东南亚等欠代表区域。
- 方法要点：采用渐进训练流程，先建立感知骨干，再通过生成-判断-精炼管道注入认知能力。
- 实验或效果：在SEA-Omni基准测试中揭示效率-稳定性悖论，推理提升抽象任务但导致感知不稳定。

## 摘要（原文）

> Recent advancements in Multimodal Large Language Models (MLLMs) pursue omni-perception capabilities, yet integrating robust sensory grounding with complex reasoning remains a challenge, particularly for underrepresented regions. In this report, we introduce the research preview of MERaLiON2-Omni (Alpha), a 10B-parameter multilingual omni-perception tailored for Southeast Asia (SEA). We present a progressive training pipeline that explicitly decouples and then integrates "System 1" (Perception) and "System 2" (Reasoning) capabilities. First, we establish a robust Perception Backbone by aligning region-specific audio-visual cues (e.g., Singlish code-switching, local cultural landmarks) with a multilingual LLM through orthogonal modality adaptation. Second, to inject cognitive capabilities without large-scale supervision, we propose a cost-effective Generate-Judge-Refine pipeline. By utilizing a Super-LLM to filter hallucinations and resolve conflicts via a consensus mechanism, we synthesize high-quality silver data that transfers textual Chain-of-Thought reasoning to multimodal scenarios.
>   Comprehensive evaluation on our newly introduced SEA-Omni Benchmark Suite reveals an Efficiency-Stability Paradox: while reasoning acts as a non-linear amplifier for abstract tasks (boosting mathematical and instruction-following performance significantly), it introduces instability in low-level sensory processing. Specifically, we identify Temporal Drift in long-context audio, where extended reasoning desynchronizes the model from acoustic timestamps, and Visual Over-interpretation, where logic overrides pixel-level reality. This report details the architecture, the data-efficient training recipe, and a diagnostic analysis of the trade-offs between robust perception and structured reasoning.

