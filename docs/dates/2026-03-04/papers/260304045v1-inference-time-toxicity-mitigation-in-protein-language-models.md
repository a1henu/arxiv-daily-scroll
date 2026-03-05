---
layout: default
title: Inference-Time Toxicity Mitigation in Protein Language Models
---

# Inference-Time Toxicity Mitigation in Protein Language Models
**arXiv**：[2603.04045v1](https://arxiv.org/abs/2603.04045) · [PDF](https://arxiv.org/pdf/2603.04045.pdf)  
**作者**：Manuel Fernández Burda, Santiago Aranguri, Iván Arcuschin Moreno, Enzo Ferrante  

**一句话要点**：提出Logit Diff Amplification作为推理时控制机制，以缓解蛋白质语言模型在特定分类群微调后引发的毒性生成问题。

**关键词**：蛋白质语言模型, 推理时控制, 毒性缓解, Logit Diff Amplification, 安全生成, 蛋白质设计

## 3 点简述
- 核心问题：蛋白质语言模型在针对特定分类群微调时可能无意中引发毒性蛋白质生成，存在双重用途安全风险。
- 方法要点：采用Logit Diff Amplification，通过放大基线模型与毒性微调模型之间的logit差异来调整token概率，无需重新训练。
- 实验或效果：在四个分类群中，LDA一致降低预测毒性率，同时保持生物合理性和结构可行性，优于基于激活的引导方法。

## 摘要（原文）

> Protein language models (PLMs) are becoming practical tools for de novo protein design, yet their dual-use potential raises safety concerns. We show that domain adaptation to specific taxonomic groups can elicit toxic protein generation, even when toxicity is not the training objective. To address this, we adapt Logit Diff Amplification (LDA) as an inference-time control mechanism for PLMs. LDA modifies token probabilities by amplifying the logit difference between a baseline model and a toxicity-finetuned model, requiring no retraining. Across four taxonomic groups, LDA consistently reduces predicted toxicity rate (measured via ToxDL2) below the taxon-finetuned baseline while preserving biological plausibility. We evaluate quality using Fréchet ESM Distance and predicted foldability (pLDDT), finding that LDA maintains distributional similarity to natural proteins and structural viability (unlike activation-based steering methods that tend to degrade sequence properties). Our results demonstrate that LDA provides a practical safety knob for protein generators that mitigates elicited toxicity while retaining generative quality.

