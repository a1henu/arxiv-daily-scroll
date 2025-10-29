---
layout: default
title: SCOPE: Saliency-Coverage Oriented Token Pruning for Efficient Multimodel LLMs
---

# SCOPE: Saliency-Coverage Oriented Token Pruning for Efficient Multimodel LLMs
**arXiv**：[2510.24214v1](https://arxiv.org/abs/2510.24214) · [PDF](https://arxiv.org/pdf/2510.24214.pdf)  
**作者**：Jinhong Deng, Wen Li, Joey Tianyi Zhou, Yang He  

**一句话要点**：提出SCOPE方法以解决多模态大模型中视觉令牌冗余问题，提升语义完整性。

**关键词**：多模态大语言模型, 视觉令牌剪枝, 语义完整性, 显著性与覆盖度, 高效计算

## 3 点简述
- 现有视觉令牌剪枝方法依赖注意力分数，导致语义不完整。
- SCOPE联合建模显著性和覆盖度，迭代选择令牌以优化语义保留。
- 在LLaVA模型上实验，SCOPE在多个基准上优于先前方法。

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) typically process a large number of
> visual tokens, leading to considerable computational overhead, even though many
> of these tokens are redundant. Existing visual token pruning methods primarily
> focus on selecting the most salient tokens based on attention scores, resulting
> in the semantic incompleteness of the selected tokens. In this paper, we
> propose a novel visual token pruning strategy, called
> \textbf{S}aliency-\textbf{C}overage \textbf{O}riented token \textbf{P}runing
> for \textbf{E}fficient MLLMs (SCOPE), to jointly model both the saliency and
> coverage of the selected visual tokens to better preserve semantic
> completeness. Specifically, we introduce a set-coverage for a given set of
> selected tokens, computed based on the token relationships. We then define a
> token-coverage gain for each unselected token, quantifying how much additional
> coverage would be obtained by including it. By integrating the saliency score
> into the token-coverage gain, we propose our SCOPE score and iteratively select
> the token with the highest SCOPE score. We conduct extensive experiments on
> multiple vision-language understanding benchmarks using the LLaVA-1.5 and
> LLaVA-Next models. Experimental results demonstrate that our method
> consistently outperforms prior approaches. Our code is available at
> \href{https://github.com/kinredon/SCOPE}{https://github.com/kinredon/SCOPE}.

