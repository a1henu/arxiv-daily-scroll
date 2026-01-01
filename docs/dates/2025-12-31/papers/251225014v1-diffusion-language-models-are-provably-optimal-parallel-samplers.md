---
layout: default
title: Diffusion Language Models are Provably Optimal Parallel Samplers
---

# Diffusion Language Models are Provably Optimal Parallel Samplers
**arXiv**：[2512.25014v1](https://arxiv.org/abs/2512.25014) · [PDF](https://arxiv.org/pdf/2512.25014.pdf)  
**作者**：Haozhe Jiang, Nika Haghtalab, Lijie Chen  

**一句话要点**：证明扩散语言模型在并行采样中具有最优性，并倡导启用修订机制以提升表达能力

**关键词**：扩散语言模型, 并行采样, 思维链, 最优性证明, 修订机制, 表达能力分析

## 3 点简述
- 核心问题：扩散语言模型作为并行采样器的理论效率与表达能力基础
- 方法要点：形式化并行采样模型，证明带思维链的扩散语言模型可最优模拟任何并行算法
- 实验或效果：证明启用修订或重掩码可优化空间复杂度，并建立严格表达能力差距

## 摘要（原文）

> Diffusion language models (DLMs) have emerged as a promising alternative to autoregressive models for faster inference via parallel token generation. We provide a rigorous foundation for this advantage by formalizing a model of parallel sampling and showing that DLMs augmented with polynomial-length chain-of-thought (CoT) can simulate any parallel sampling algorithm using an optimal number of sequential steps. Consequently, whenever a target distribution can be generated using a small number of sequential steps, a DLM can be used to generate the distribution using the same number of optimal sequential steps. However, without the ability to modify previously revealed tokens, DLMs with CoT can still incur large intermediate footprints. We prove that enabling remasking (converting unmasked tokens to masks) or revision (converting unmasked tokens to other unmasked tokens) together with CoT further allows DLMs to simulate any parallel sampling algorithm with optimal space complexity. We further justify the advantage of revision by establishing a strict expressivity gap: DLMs with revision or remasking are strictly more expressive than those without. Our results not only provide a theoretical justification for the promise of DLMs as the most efficient parallel sampler, but also advocate for enabling revision in DLMs.

