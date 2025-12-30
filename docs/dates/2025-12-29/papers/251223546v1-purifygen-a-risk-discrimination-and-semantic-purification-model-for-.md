---
layout: default
title: PurifyGen: A Risk-Discrimination and Semantic-Purification Model for Safe Text-to-Image Generation
---

# PurifyGen: A Risk-Discrimination and Semantic-Purification Model for Safe Text-to-Image Generation
**arXiv**：[2512.23546v1](https://arxiv.org/abs/2512.23546) · [PDF](https://arxiv.org/pdf/2512.23546.pdf)  
**作者**：Zongsheng Cao, Yangfan He, Anran Liu, Jun Xie, Feng Chen, Zepeng Wang  

**一句话要点**：提出PurifyGen以解决文本到图像生成中的不安全内容风险，通过双阶段提示净化保留模型权重。

**关键词**：文本到图像生成, 安全生成, 提示净化, 语义距离, 双空间变换, 训练无关方法

## 3 点简述
- 核心问题：扩散模型生成不安全内容，传统方法如黑名单或分类易规避或需大量数据。
- 方法要点：基于互补语义距离评估提示风险，通过双空间变换净化有害语义并增强安全语义。
- 实验或效果：在五个数据集上超越现有方法减少不安全内容，与依赖训练的方法竞争。

## 摘要（原文）

> Recent advances in diffusion models have notably enhanced text-to-image (T2I) generation quality, but they also raise the risk of generating unsafe content. Traditional safety methods like text blacklisting or harmful content classification have significant drawbacks: they can be easily circumvented or require extensive datasets and extra training. To overcome these challenges, we introduce PurifyGen, a novel, training-free approach for safe T2I generation that retains the model's original weights. PurifyGen introduces a dual-stage strategy for prompt purification. First, we evaluate the safety of each token in a prompt by computing its complementary semantic distance, which measures the semantic proximity between the prompt tokens and concept embeddings from predefined toxic and clean lists. This enables fine-grained prompt classification without explicit keyword matching or retraining. Tokens closer to toxic concepts are flagged as risky. Second, for risky prompts, we apply a dual-space transformation: we project toxic-aligned embeddings into the null space of the toxic concept matrix, effectively removing harmful semantic components, and simultaneously align them into the range space of clean concepts. This dual alignment purifies risky prompts by both subtracting unsafe semantics and reinforcing safe ones, while retaining the original intent and coherence. We further define a token-wise strategy to selectively replace only risky token embeddings, ensuring minimal disruption to safe content. PurifyGen offers a plug-and-play solution with theoretical grounding and strong generalization to unseen prompts and models. Extensive testing shows that PurifyGen surpasses current methods in reducing unsafe content across five datasets and competes well with training-dependent approaches. The code can refer to https://github.com/AI-Researcher-Team/PurifyGen.

