---
layout: default
title: MTBBench: A Multimodal Sequential Clinical Decision-Making Benchmark in Oncology
---

# MTBBench: A Multimodal Sequential Clinical Decision-Making Benchmark in Oncology
**arXiv**：[2511.20490v1](https://arxiv.org/abs/2511.20490) · [PDF](https://arxiv.org/pdf/2511.20490.pdf)  
**作者**：Kiril Vasilev, Alexandre Misrahi, Eeshaan Jain, Phil F Cheng, Petros Liakopoulos, Olivier Michielin, Michael Moor, Charlotte Bunne  

**一句话要点**：提出MTBBench基准以模拟肿瘤分子委员会的多模态序列临床决策

**关键词**：多模态大语言模型, 临床决策基准, 肿瘤分子委员会, 纵向数据推理, 工具增强框架

## 3 点简述
- 现有基准无法捕捉真实临床工作流的多模态和纵向复杂性
- 引入模拟MTB决策的基准，包含临床验证的多模态和时序问题
- 基准显示LLMs可靠性不足，但工具框架可提升任务性能达11.2%

## 摘要（原文）

> Multimodal Large Language Models (LLMs) hold promise for biomedical reasoning, but current benchmarks fail to capture the complexity of real-world clinical workflows. Existing evaluations primarily assess unimodal, decontextualized question-answering, overlooking multi-agent decision-making environments such as Molecular Tumor Boards (MTBs). MTBs bring together diverse experts in oncology, where diagnostic and prognostic tasks require integrating heterogeneous data and evolving insights over time. Current benchmarks lack this longitudinal and multimodal complexity. We introduce MTBBench, an agentic benchmark simulating MTB-style decision-making through clinically challenging, multimodal, and longitudinal oncology questions. Ground truth annotations are validated by clinicians via a co-developed app, ensuring clinical relevance. We benchmark multiple open and closed-source LLMs and show that, even at scale, they lack reliability -- frequently hallucinating, struggling with reasoning from time-resolved data, and failing to reconcile conflicting evidence or different modalities. To address these limitations, MTBBench goes beyond benchmarking by providing an agentic framework with foundation model-based tools that enhance multi-modal and longitudinal reasoning, leading to task-level performance gains of up to 9.0% and 11.2%, respectively. Overall, MTBBench offers a challenging and realistic testbed for advancing multimodal LLM reasoning, reliability, and tool-use with a focus on MTB environments in precision oncology.

