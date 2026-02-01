---
layout: default
title: Retrieval-Infused Reasoning Sandbox: A Benchmark for Decoupling Retrieval and Reasoning Capabilities
---

# Retrieval-Infused Reasoning Sandbox: A Benchmark for Decoupling Retrieval and Reasoning Capabilities
**arXiv**：[2601.21937v1](https://arxiv.org/abs/2601.21937) · [PDF](https://arxiv.org/pdf/2601.21937.pdf)  
**作者**：Shuangshuang Ying, Zheyu Wang, Yunjian Peng, Jin Chen, Yuhao Wu, Hongbin Lin, Dingyu He, Siyi Liu, Gengchen Yu, YinZhu Piao, Yuchen Wu, Xin Gui, Zhongyuan Peng, Xin Li, Xeron Du, Libo Qin, YiXin Cao, Ge Zhang  

**一句话要点**：提出DeR2基准以解耦检索与推理能力，评估大语言模型在科学新信息上的推理表现。

**关键词**：检索增强推理, 基准测试, 文档基础推理, 大语言模型评估, 科学信息处理, 错误归因

## 3 点简述
- 核心问题：现有基准混淆检索与推理，且受参数记忆和网络波动影响，难以评估大语言模型对新颖科学信息的推理能力。
- 方法要点：通过四种证据访问机制（仅指令、概念、相关文档、全文档集）隔离文档基础推理，实现检索损失与推理损失的可解释分离。
- 实验或效果：实验显示先进模型表现差异大，部分模型在全文档集下表现更差，揭示推理脆弱性和概念误用问题。

## 摘要（原文）

> Despite strong performance on existing benchmarks, it remains unclear whether large language models can reason over genuinely novel scientific information. Most evaluations score end-to-end RAG pipelines, where reasoning is confounded with retrieval and toolchain choices, and the signal is further contaminated by parametric memorization and open-web volatility. We introduce DeR2, a controlled deep-research sandbox that isolates document-grounded reasoning while preserving core difficulties of deep search: multi-step synthesis, denoising, and evidence-based conclusion making. DeR2 decouples evidence access from reasoning via four regimes--Instruction-only, Concepts (gold concepts without documents), Related-only (only relevant documents), and Full-set (relevant documents plus topically related distractors)--yielding interpretable regime gaps that operationalize retrieval loss vs. reasoning loss and enable fine-grained error attribution. To prevent parametric leakage, we apply a two-phase validation that requires parametric failure without evidence while ensuring oracle-concept solvability. To ensure reproducibility, each instance provides a frozen document library (drawn from 2023-2025 theoretical papers) with expert-annotated concepts and validated rationales. Experiments across a diverse set of state-of-the-art foundation models reveal substantial variation and significant headroom: some models exhibit mode-switch fragility, performing worse with the Full-set than with Instruction-only, while others show structural concept misuse, correctly naming concepts but failing to execute them as procedures.

