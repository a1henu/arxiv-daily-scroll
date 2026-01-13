---
layout: default
title: Learning to Trust the Crowd: A Multi-Model Consensus Reasoning Engine for Large Language Models
---

# Learning to Trust the Crowd: A Multi-Model Consensus Reasoning Engine for Large Language Models
**arXiv**：[2601.07245v1](https://arxiv.org/abs/2601.07245) · [PDF](https://arxiv.org/pdf/2601.07245.pdf)  
**作者**：Pranav Kallem  

**一句话要点**：提出多模型共识推理引擎，通过监督元学习提升大型语言模型在查询中的可靠性。

**关键词**：多模型共识, 监督元学习, 图神经网络, 可靠性提升, 语义特征提取, 置信度校准

## 3 点简述
- 核心问题：大型语言模型在实例级别存在幻觉、脆弱失败和置信度校准不佳，导致可靠性不足。
- 方法要点：将多个异构LLM输出作为输入，利用语义嵌入、相似性统计和模型先验等特征，应用梯度提升树和图神经网络进行监督学习。
- 实验或效果：在资源受限数据集上，基于图注意力的共识模型比最强单模型准确率提升4.6个百分点，比多数投票提升8.1个百分点，并减少幻觉。

## 摘要（原文）

> Large language models (LLMs) achieve strong aver- age performance yet remain unreliable at the instance level, with frequent hallucinations, brittle failures, and poorly calibrated confidence. We study reliability through the lens of multi-model consensus: given responses from several heterogeneous LLMs, can we learn which answer is most likely correct for a given query? We introduce a Multi-Model Consensus Reasoning Engine that treats the set of LLM outputs as input to a supervised meta-learner. The system maps natural language responses into structured features using semantic embeddings, pairwise similarity and clustering statistics, lexical and structural cues, reasoning-quality scores, confidence estimates, and model-specific priors, and then applies gradient-boosted trees, listwise ranking, and graph neural networks over similarity graphs of answers. Using three open-weight LLMs evaluated on compact, resource- constrained subsets of GSM8K, ARC-Challenge, HellaSwag, and TruthfulQA, our best graph-attention-based consensus model improves macro-average accuracy by 4.6 percentage points over the strongest single LLM and by 8.1 points over majority vote, while also yielding lower Brier scores and fewer TruthfulQA hal- lucinations. Ablation and feature-importance analyses show that semantic agreement and clustering features are most influential, with reasoning-quality and model-prior features providing com- plementary gains, suggesting supervised multi-model consensus is a practical route toward more reliable LLM behavior, even in a modest single-machine setup.

