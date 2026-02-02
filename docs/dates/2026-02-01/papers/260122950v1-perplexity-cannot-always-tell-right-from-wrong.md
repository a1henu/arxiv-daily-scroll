---
layout: default
title: Perplexity Cannot Always Tell Right from Wrong
---

# Perplexity Cannot Always Tell Right from Wrong
**arXiv**：[2601.22950v1](https://arxiv.org/abs/2601.22950) · [PDF](https://arxiv.org/pdf/2601.22950.pdf)  
**作者**：Petar Veličković, Federico Barbero, Christos Perivolaropoulos, Simon Osindero, Razvan Pascanu  

**一句话要点**：证明困惑度在Transformer模型选择中可能不适用，揭示其与准确性的不一致性。

**关键词**：困惑度, Transformer模型, 模型选择, 连续性理论, 准确性评估

## 3 点简述
- 核心问题：困惑度作为模型质量指标存在局限性，可能无法可靠选择更准确的模型。
- 方法要点：利用Transformer连续性理论，证明存在低困惑度但预测错误的序列。
- 实验或效果：通过分析等困惑度图，发现模型置信度增加需伴随准确性提升才能被选中。

## 摘要（原文）

> Perplexity -- a function measuring a model's overall level of "surprise" when encountering a particular output -- has gained significant traction in recent years, both as a loss function and as a simple-to-compute metric of model quality. Prior studies have pointed out several limitations of perplexity, often from an empirical manner. Here we leverage recent results on Transformer continuity to show in a rigorous manner how perplexity may be an unsuitable metric for model selection. Specifically, we prove that, if there is any sequence that a compact decoder-only Transformer model predicts accurately and confidently -- a necessary pre-requisite for strong generalisation -- it must imply existence of another sequence with very low perplexity, but not predicted correctly by that same model. Further, by analytically studying iso-perplexity plots, we find that perplexity will not always select for the more accurate model -- rather, any increase in model confidence must be accompanied by a commensurate rise in accuracy for the new model to be selected.

