---
layout: default
title: sui-1: Grounded and Verifiable Long-Form Summarization
---

# sui-1: Grounded and Verifiable Long-Form Summarization
**arXiv**：[2601.08472v1](https://arxiv.org/abs/2601.08472) · [PDF](https://arxiv.org/pdf/2601.08472.pdf)  
**作者**：Benedikt Droste, Jan Philipp Harries, Maximilian Idahl, Björn Plüster  

**一句话要点**：提出sui-1模型以解决长文本摘要中不可验证的生成问题，适用于政府和法律分析等合规敏感领域。

**关键词**：长文本摘要, 引用基础摘要, 合成数据生成, 多语言训练, 合规敏感应用, 模型验证

## 3 点简述
- 核心问题：大型语言模型常生成看似合理但不可靠的摘要，用户无法根据源文本验证，这在合规敏感领域尤为关键。
- 方法要点：sui-1是一个24B参数模型，通过合成数据管道结合思维链提示和多阶段验证，生成带内联引用的摘要，使每个声明可追溯至源句子。
- 实验或效果：评估显示sui-1显著优于所有测试的开放权重基线，包括参数多3倍的模型，证明任务特定训练在引用基础摘要中优于单纯规模扩展。

## 摘要（原文）

> Large language models frequently generate plausible but unfaithful summaries that users cannot verify against source text, a critical limitation in compliance-sensitive domains such as government and legal analysis. We present sui-1, a 24B parameter model that produces abstractive summaries with inline citations, enabling users to trace each claim to its source sentence. Our synthetic data pipeline combines chain-of-thought prompting with multi-stage verification, generating over 22,000 high-quality training examples across five languages from diverse sources including parliamentary documents, web text, and Wikipedia. Evaluation shows sui-1 significantly outperforms all tested open-weight baselines, including models with 3x more parameters. These results demonstrate that task-specific training substantially outperforms scale alone for citation-grounded summarization. Model weights and an interactive demo are publicly available.

