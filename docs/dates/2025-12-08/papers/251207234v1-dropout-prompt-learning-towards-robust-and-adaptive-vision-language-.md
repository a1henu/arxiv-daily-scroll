---
layout: default
title: Dropout Prompt Learning: Towards Robust and Adaptive Vision-Language Models
---

# Dropout Prompt Learning: Towards Robust and Adaptive Vision-Language Models
**arXiv**：[2512.07234v1](https://arxiv.org/abs/2512.07234) · [PDF](https://arxiv.org/pdf/2512.07234.pdf)  
**作者**：Biao Chen, Lin Zuo, Mengmeng Jing, Kunbin He, Yuchen Wang  

**一句话要点**：提出Dropout Prompt Learning以提升视觉-语言模型在低样本学习和分布外泛化等场景的鲁棒性。

**关键词**：视觉-语言模型, 提示学习, 鲁棒性增强, 低样本学习, 分布外泛化, 正则化技术

## 3 点简述
- 核心问题：视觉-语言模型在低样本学习、长尾分类和分布外泛化等挑战性场景中鲁棒性不足。
- 方法要点：基于token重要性评估，在文本和视觉分支应用自适应dropout，并引入残差熵正则化以平衡语义对齐和多样性。
- 实验或效果：在15个基准测试中有效，在基础到新类别泛化上优于KgCoOp和PromptSRC等方法。

## 摘要（原文）

> Dropout is a widely used regularization technique which improves the generalization ability of a model by randomly dropping neurons. In light of this, we propose Dropout Prompt Learning, which aims for applying dropout to improve the robustness of the vision-language models. Different from the vanilla dropout, we apply dropout on the tokens of the textual and visual branches, where we evaluate the token significance considering both intra-modal context and inter-modal alignment, enabling flexible dropout probabilities for each token. Moreover, to maintain semantic alignment for general knowledge transfer while encouraging the diverse representations that dropout introduces, we further propose residual entropy regularization. Experiments on 15 benchmarks show our method's effectiveness in challenging scenarios like low-shot learning, long-tail classification, and out-of-distribution generalization. Notably, our method surpasses regularization-based methods including KgCoOp by 5.10% and PromptSRC by 2.13% in performance on base-to-novel generalization.

