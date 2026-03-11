---
layout: default
title: Emotion is Not Just a Label: Latent Emotional Factors in LLM Processing
---

# Emotion is Not Just a Label: Latent Emotional Factors in LLM Processing
**arXiv**：[2603.09205v1](https://arxiv.org/abs/2603.09205) · [PDF](https://arxiv.org/pdf/2603.09205.pdf)  
**作者**：Benjamin Reichman, Adar Avasian, Samuel Webster, Larry Heck  

**一句话要点**：提出情感正则化框架以提升大语言模型在情感变化文本中的阅读理解性能

**关键词**：情感潜在因素, 注意力几何分析, 情感正则化, AURA-QA数据集, 阅读理解提升, 分布偏移鲁棒性

## 3 点简述
- 核心问题：情感作为潜在因素影响大语言模型的注意力和推理行为，而非仅作为预测目标
- 方法要点：分析情感对注意力几何的影响，并引入情感平衡数据集AURA-QA进行控制研究
- 实验或效果：情感正则化在多个问答基准上提升阅读理解，包括分布偏移和领域内改进

## 摘要（原文）

> Large language models are routinely deployed on text that varies widely in emotional tone, yet their reasoning behavior is typically evaluated without accounting for emotion as a source of representational variation. Prior work has largely treated emotion as a prediction target, for example in sentiment analysis or emotion classification. In contrast, we study emotion as a latent factor that shapes how models attend to and reason over text. We analyze how emotional tone systematically alters attention geometry in transformer models, showing that metrics such as locality, center-of-mass distance, and entropy vary across emotions and correlate with downstream question-answering performance. To facilitate controlled study of these effects, we introduce Affect-Uniform ReAding QA (AURA-QA), a question-answering dataset with emotionally balanced, human-authored context passages. Finally, an emotional regularization framework is proposed that constrains emotion-conditioned representational drift during training. Experiments across multiple QA benchmarks demonstrate that this approach improves reading comprehension in both emotionally-varying and non-emotionally varying datasets, yielding consistent gains under distribution shift and in-domain improvements on several benchmarks.

