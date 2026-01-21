---
layout: default
title: Human Values in a Single Sentence: Moral Presence, Hierarchies, and Transformer Ensembles on the Schwartz Continuum
---

# Human Values in a Single Sentence: Moral Presence, Hierarchies, and Transformer Ensembles on the Schwartz Continuum
**arXiv**：[2601.14172v1](https://arxiv.org/abs/2601.14172) · [PDF](https://arxiv.org/pdf/2601.14172.pdf)  
**作者**：Víctor Yeste, Paolo Rosso  

**一句话要点**：提出基于Transformer集成与轻量信号的方法，在单句新闻与政治宣言中检测施瓦茨价值观，应对稀疏道德线索与类别不平衡。

**关键词**：人类价值检测, 施瓦茨价值观, Transformer集成, 类别不平衡, 轻量信号, 单句分析

## 3 点简述
- 研究单句层面检测施瓦茨动机连续体中的19种价值观，作为文本中人类价值检测的具体任务。
- 比较了基于DeBERTa的直接多标签分类器与存在门控层次结构，并评估了指令调优LLMs在零/少样本和QLoRA设置下的表现。
- 通过软投票监督集成达到宏观F1 0.332，超越最佳单模型和先前基线，轻量信号与小集成提供最可靠改进。

## 摘要（原文）

> We study sentence-level identification of the 19 values in the Schwartz motivational continuum as a concrete formulation of human value detection in text. The setting - out-of-context sentences from news and political manifestos - features sparse moral cues and severe class imbalance. This combination makes fine-grained sentence-level value detection intrinsically difficult, even for strong modern neural models. We first operationalize a binary moral presence task ("does any value appear?") and show that it is learnable from single sentences (positive-class F1 $\approx$ 0.74 with calibrated thresholds). We then compare a presence-gated hierarchy to a direct multi-label classifier under matched compute, both based on DeBERTa-base and augmented with lightweight signals (prior-sentence context, LIWC-22/eMFD/MJD lexica, and topic features). The hierarchy does not outperform direct prediction, indicating that gate recall limits downstream gains. We also benchmark instruction-tuned LLMs - Gemma 2 9B, Llama 3.1 8B, Mistral 8B, and Qwen 2.5 7B - in zero-/few-shot and QLoRA setups and build simple ensembles; a soft-vote supervised ensemble reaches macro-F1 0.332, significantly surpassing the best single supervised model and exceeding prior English-only baselines. Overall, in this scenario, lightweight signals and small ensembles yield the most reliable improvements, while hierarchical gating offers limited benefit. We argue that, under an 8 GB single-GPU constraint and at the 7-9B scale, carefully tuned supervised encoders remain a strong and compute-efficient baseline for structured human value detection, and we outline how richer value structure and sentence-in-document context could further improve performance.

