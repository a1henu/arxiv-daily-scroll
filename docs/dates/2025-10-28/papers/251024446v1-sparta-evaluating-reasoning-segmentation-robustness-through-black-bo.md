---
layout: default
title: SPARTA: Evaluating Reasoning Segmentation Robustness through Black-Box Adversarial Paraphrasing in Text Autoencoder Latent Space
---

# SPARTA: Evaluating Reasoning Segmentation Robustness through Black-Box Adversarial Paraphrasing in Text Autoencoder Latent Space
**arXiv**：[2510.24446v1](https://arxiv.org/abs/2510.24446) · [PDF](https://arxiv.org/pdf/2510.24446.pdf)  
**作者**：Viktoriia Zinkovich, Anton Antonov, Andrei Spiridonov, Denis Shepelev, Andrey Moskalenko, Daria Pugacheva, Elena Tutubalina, Andrey Kuznetsov, Vlad Shakhuro  

**一句话要点**：提出SPARTA方法，通过黑盒对抗性转述评估多模态大模型在推理分割中的鲁棒性。

**关键词**：推理分割, 对抗性转述, 多模态大模型, 文本自编码器, 强化学习, 鲁棒性评估

## 3 点简述
- 核心问题：多模态大模型对语义等效文本转述的鲁棒性不足，影响真实应用。
- 方法要点：SPARTA在文本自编码器潜在空间进行黑盒优化，使用强化学习生成对抗性转述。
- 实验或效果：在ReasonSeg和LLMSeg-40k数据集上，SPARTA成功率比基线方法高2倍。

## 摘要（原文）

> Multimodal large language models (MLLMs) have shown impressive capabilities
> in vision-language tasks such as reasoning segmentation, where models generate
> segmentation masks based on textual queries. While prior work has primarily
> focused on perturbing image inputs, semantically equivalent textual
> paraphrases-crucial in real-world applications where users express the same
> intent in varied ways-remain underexplored. To address this gap, we introduce a
> novel adversarial paraphrasing task: generating grammatically correct
> paraphrases that preserve the original query meaning while degrading
> segmentation performance. To evaluate the quality of adversarial paraphrases,
> we develop a comprehensive automatic evaluation protocol validated with human
> studies. Furthermore, we introduce SPARTA-a black-box, sentence-level
> optimization method that operates in the low-dimensional semantic latent space
> of a text autoencoder, guided by reinforcement learning. SPARTA achieves
> significantly higher success rates, outperforming prior methods by up to 2x on
> both the ReasonSeg and LLMSeg-40k datasets. We use SPARTA and competitive
> baselines to assess the robustness of advanced reasoning segmentation models.
> We reveal that they remain vulnerable to adversarial paraphrasing-even under
> strict semantic and grammatical constraints. All code and data will be released
> publicly upon acceptance.

