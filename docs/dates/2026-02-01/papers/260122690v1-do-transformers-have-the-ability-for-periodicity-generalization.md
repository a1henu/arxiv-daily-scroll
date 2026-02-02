---
layout: default
title: Do Transformers Have the Ability for Periodicity Generalization?
---

# Do Transformers Have the Ability for Periodicity Generalization?
**arXiv**：[2601.22690v1](https://arxiv.org/abs/2601.22690) · [PDF](https://arxiv.org/pdf/2601.22690.pdf)  
**作者**：Huanyu Liu, Ge Li, Yihong Dong, Sihan Wu, Peixu Wang, Sihao Cheng, Taozhi Chen, Kechi Zhang, Hao Zhu, Tongxuan Liu  

**一句话要点**：提出Coper基准以评估Transformer在复合周期性OOD泛化中的局限性

**关键词**：Transformer, 周期性泛化, 分布外泛化, 抽象代数, 可控生成基准, Coper

## 3 点简述
- 核心问题：Transformer在分布外泛化中，特别是周期性场景下表现受限
- 方法要点：从抽象代数和推理角度统一解释周期性，构建可控生成基准Coper
- 实验或效果：实验显示Transformer能记忆训练数据，但无法泛化到未见复合周期性

## 摘要（原文）

> Large language models (LLMs) based on the Transformer have demonstrated strong performance across diverse tasks. However, current models still exhibit substantial limitations in out-of-distribution (OOD) generalization compared with humans. We investigate this gap through periodicity, one of the basic OOD scenarios. Periodicity captures invariance amid variation. Periodicity generalization represents a model's ability to extract periodic patterns from training data and generalize to OOD scenarios. We introduce a unified interpretation of periodicity from the perspective of abstract algebra and reasoning, including both single and composite periodicity, to explain why Transformers struggle to generalize periodicity. Then we construct Coper about composite periodicity, a controllable generative benchmark with two OOD settings, Hollow and Extrapolation. Experiments reveal that periodicity generalization in Transformers is limited, where models can memorize periodic data during training, but cannot generalize to unseen composite periodicity. We release the source code to support future research.

