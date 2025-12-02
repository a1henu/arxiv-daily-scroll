---
layout: default
title: H-Neurons: On the Existence, Impact, and Origin of Hallucination-Associated Neurons
---

# H-Neurons: On the Existence, Impact, and Origin of Hallucination-Associated Neurons
**arXiv**：[2512.01797v1](https://arxiv.org/abs/2512.01797) · [PDF](https://arxiv.org/pdf/2512.01797.pdf)  
**作者**：Cheng Gao, Huimin Chen, Chaojun Xiao, Zhiyi Chen, Zhiyuan Liu, Maosong Sun  

**一句话要点**：提出幻觉关联神经元（H-Neurons）以揭示大语言模型幻觉的微观机制

**关键词**：大语言模型, 幻觉检测, 神经元分析, 因果干预, 预训练机制, 可靠性提升

## 3 点简述
- 核心问题：大语言模型常产生幻觉，但神经元级机制未知
- 方法要点：识别稀疏神经元子集预测幻觉，并探究其因果影响与起源
- 实验或效果：神经元预测泛化强，干预显示因果关联，起源可追溯至预训练

## 摘要（原文）

> Large language models (LLMs) frequently generate hallucinations -- plausible but factually incorrect outputs -- undermining their reliability. While prior work has examined hallucinations from macroscopic perspectives such as training data and objectives, the underlying neuron-level mechanisms remain largely unexplored. In this paper, we conduct a systematic investigation into hallucination-associated neurons (H-Neurons) in LLMs from three perspectives: identification, behavioral impact, and origins. Regarding their identification, we demonstrate that a remarkably sparse subset of neurons (less than $0.1\%$ of total neurons) can reliably predict hallucination occurrences, with strong generalization across diverse scenarios. In terms of behavioral impact, controlled interventions reveal that these neurons are causally linked to over-compliance behaviors. Concerning their origins, we trace these neurons back to the pre-trained base models and find that these neurons remain predictive for hallucination detection, indicating they emerge during pre-training. Our findings bridge macroscopic behavioral patterns with microscopic neural mechanisms, offering insights for developing more reliable LLMs.

