---
layout: default
title: When Should LLMs Be Less Specific? Selective Abstraction for Reliable Long-Form Text Generation
---

# When Should LLMs Be Less Specific? Selective Abstraction for Reliable Long-Form Text Generation
**arXiv**：[2602.11908v1](https://arxiv.org/abs/2602.11908) · [PDF](https://arxiv.org/pdf/2602.11908.pdf)  
**作者**：Shani Goren, Ido Galil, Ran El-Yaniv  

**一句话要点**：提出选择性抽象框架，通过降低不确定内容的细节来提升长文本生成的可靠性。

**关键词**：长文本生成, 不确定性估计, 选择性抽象, 事实正确性, 原子声明, 风险-覆盖曲线

## 3 点简述
- 核心问题：LLMs在长文本生成中易产生事实错误，现有不确定性估计方法过于限制。
- 方法要点：引入选择性抽象，将响应分解为原子声明，用更抽象但更可靠的表述替换不确定部分。
- 实验或效果：在FactScore和LongFact-Objects基准上，原子级选择性抽象优于基线，风险-覆盖曲线下面积提升达27.73%。

## 摘要（原文）

> LLMs are widely used, yet they remain prone to factual errors that erode user trust and limit adoption in high-risk settings. One approach to mitigate this risk is to equip models with uncertainty estimation mechanisms that abstain when confidence is low. However, this binary "all-or-nothing" approach is excessively restrictive in long-form settings, often discarding valuable information. We introduce Selective Abstraction (SA), a framework that enables LLMs to trade specificity for reliability by selectively reducing the detail of uncertain content. We first formalize SA through the lenses of selective risk and coverage. We then propose Atom-wise Selective Abstraction, a claim-level instantiation that decomposes responses into atomic claims (short, self-contained statements each expressing a single fact) and replaces uncertain atoms with higher confidence, less specific abstractions. To evaluate this framework, we develop a novel end-to-end pipeline for open-ended generation that instantiates risk as factual correctness and measures coverage using an information-theoretic measure of retained information. Across six open-source models on the FactScore and LongFact-Objects benchmarks, atom-wise SA consistently outperforms existing baselines, improving the area under the risk-coverage curve (AURC) by up to 27.73% over claim removal, demonstrating that reducing specificity can boost accuracy and reliability while preserving most of their original meaning.

