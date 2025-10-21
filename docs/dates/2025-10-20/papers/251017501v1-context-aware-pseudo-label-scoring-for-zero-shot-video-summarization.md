---
layout: default
title: Context-Aware Pseudo-Label Scoring for Zero-Shot Video Summarization
---

# Context-Aware Pseudo-Label Scoring for Zero-Shot Video Summarization
**arXiv**：[2510.17501v1](https://arxiv.org/abs/2510.17501) · [PDF](https://arxiv.org/pdf/2510.17501.pdf)  
**作者**：Yuanli Wu, Long Zhang, Yue Du, Bin Li  

**一句话要点**：提出基于规则引导伪标签评分的零样本视频摘要方法，以提升泛化性和语义捕捉能力

**关键词**：零样本视频摘要, 伪标签评分, 上下文感知提示, 大语言模型应用, 规则引导评估

## 3 点简述
- 现有方法依赖密集标注或手工提示，泛化性差且成本高
- 利用少量真实标注生成伪标签，构建数据集自适应评分规则指导场景评估
- 在SumMe和TVSum上F1分数达57.58和63.05，超越无监督和零样本基线

## 摘要（原文）

> With the rapid proliferation of video content across social media,
> surveillance, and education platforms, efficiently summarizing long videos into
> concise yet semantically faithful surrogates has become increasingly vital.
> Existing supervised methods achieve strong in-domain accuracy by learning from
> dense annotations but suffer from high labeling costs and limited cross-dataset
> generalization, while unsupervised approaches, though label-free, often fail to
> capture high-level human semantics and fine-grained narrative cues. More
> recently, zero-shot prompting pipelines have leveraged large language models
> (LLMs) for training-free video summarization, yet remain highly sensitive to
> handcrafted prompt templates and dataset-specific score normalization. To
> overcome these limitations, we introduce a rubric-guided, pseudo-labeled
> prompting framework that transforms a small subset of ground-truth annotations
> into high-confidence pseudo labels, which are aggregated into structured,
> dataset-adaptive scoring rubrics guiding interpretable scene evaluation. During
> inference, first and last segments are scored based solely on their
> descriptions, whereas intermediate ones incorporate brief contextual summaries
> of adjacent scenes to assess narrative progression and redundancy. This
> contextual prompting enables the LLM to balance local salience and global
> coherence without parameter tuning. On SumMe and TVSum, our method achieves F1
> scores of \textbf{57.58} and \textbf{63.05}, surpassing unsupervised and prior
> zero-shot baselines while approaching supervised performance. The results
> demonstrate that rubric-guided pseudo labeling effectively stabilizes LLM-based
> scoring and establishes a general, interpretable zero-shot paradigm for video
> summarization.

