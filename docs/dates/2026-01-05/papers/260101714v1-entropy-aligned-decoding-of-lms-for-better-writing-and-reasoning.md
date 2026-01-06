---
layout: default
title: Entropy-Aligned Decoding of LMs for Better Writing and Reasoning
---

# Entropy-Aligned Decoding of LMs for Better Writing and Reasoning
**arXiv**：[2601.01714v1](https://arxiv.org/abs/2601.01714) · [PDF](https://arxiv.org/pdf/2601.01714.pdf)  
**作者**：Kareem Ahmed, Sameer Singh  

**一句话要点**：提出EPIC解码方法，通过熵对齐提升语言模型在写作和推理任务中的生成质量。

**关键词**：语言模型解码, 熵对齐, 生成质量, 创意写作, 数学推理, 摘要任务

## 3 点简述
- 核心问题：传统解码算法基于贪婪启发式，导致生成文本同质化、重复且不连贯。
- 方法要点：EPIC引入未来轨迹熵，在解码时对齐采样分布熵与数据不确定性，实现超参数自由且高效的精确采样。
- 实验或效果：在创意写作、摘要和数学推理任务中，EPIC优于基线，提升偏好胜率和多样性、忠实度指标。

## 摘要（原文）

> Language models (LMs) are trained on billions of tokens in an attempt to recover the true language distribution. Still, vanilla random sampling from LMs yields low quality generations. Decoding algorithms attempt to restrict the LM distribution to a set of high-probability continuations, but rely on greedy heuristics that introduce myopic distortions, yielding sentences that are homogeneous, repetitive and incoherent. In this paper, we introduce EPIC, a hyperparameter-free decoding approach that incorporates the entropy of future trajectories into LM decoding. EPIC explicitly regulates the amount of uncertainty expressed at every step of generation, aligning the sampling distribution's entropy to the aleatoric (data) uncertainty. Through Entropy-Aware Lazy Gumbel-Max sampling, EPIC manages to be exact, while also being efficient, requiring only a sublinear number of entropy evaluations per step. Unlike current baselines, EPIC yields sampling distributions that are empirically well-aligned with the entropy of the underlying data distribution. Across creative writing and summarization tasks, EPIC consistently improves LM-as-judge preference win-rates over widely used decoding strategies. These preference gains are complemented by automatic metrics, showing that EPIC produces more diverse generations and more faithful summaries. We also evaluate EPIC on mathematical reasoning, where it outperforms all baselines.

