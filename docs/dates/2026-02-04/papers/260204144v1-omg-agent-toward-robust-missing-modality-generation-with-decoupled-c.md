---
layout: default
title: OMG-Agent: Toward Robust Missing Modality Generation with Decoupled Coarse-to-Fine Agentic Workflows
---

# OMG-Agent: Toward Robust Missing Modality Generation with Decoupled Coarse-to-Fine Agentic Workflows
**arXiv**：[2602.04144v1](https://arxiv.org/abs/2602.04144) · [PDF](https://arxiv.org/pdf/2602.04144.pdf)  
**作者**：Ruiting Dai, Zheyu Wang, Haoyu Yang, Yihan Liu, Chengzhi Wang, Zekun Zhang, Zishan Huang, Jiaman Cen, Lisi Mo  

**一句话要点**：提出OMG-Agent框架，通过解耦的粗到细代理工作流解决多模态数据缺失下的鲁棒生成问题。

**关键词**：多模态生成, 代理工作流, 语义规划, 证据检索, 鲁棒性, 数据缺失

## 3 点简述
- 核心问题：多模态数据不完整导致系统不可靠，现有方法受限于语义-细节纠缠和检索僵化。
- 方法要点：采用动态代理工作流，分阶段进行语义规划、证据检索和细节执行，以解耦逻辑推理与信号合成。
- 实验或效果：在多个基准测试中超越现有方法，在极端缺失率下保持鲁棒性，如CMU-MOSI上提升2.6分。

## 摘要（原文）

> Data incompleteness severely impedes the reliability of multimodal systems. Existing reconstruction methods face distinct bottlenecks: conventional parametric/generative models are prone to hallucinations due to over-reliance on internal memory, while retrieval-augmented frameworks struggle with retrieval rigidity. Critically, these end-to-end architectures are fundamentally constrained by Semantic-Detail Entanglement -- a structural conflict between logical reasoning and signal synthesis that compromises fidelity. In this paper, we present \textbf{\underline{O}}mni-\textbf{\underline{M}}odality \textbf{\underline{G}}eneration Agent (\textbf{OMG-Agent}), a novel framework that shifts the paradigm from static mapping to a dynamic coarse-to-fine Agentic Workflow. By mimicking a \textit{deliberate-then-act} cognitive process, OMG-Agent explicitly decouples the task into three synergistic stages: (1) an MLLM-driven Semantic Planner that resolves input ambiguity via Progressive Contextual Reasoning, creating a deterministic structured semantic plan; (2) a non-parametric Evidence Retriever that grounds abstract semantics in external knowledge; and (3) a Retrieval-Injected Executor that utilizes retrieved evidence as flexible feature prompts to overcome rigidity and synthesize high-fidelity details. Extensive experiments on multiple benchmarks demonstrate that OMG-Agent consistently surpasses state-of-the-art methods, maintaining robustness under extreme missingness, e.g., a $2.6$-point gain on CMU-MOSI at $70$\% missing rates.

