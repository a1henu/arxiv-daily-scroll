---
layout: default
title: FormationEval, an open multiple-choice benchmark for petroleum geoscience
---

# FormationEval, an open multiple-choice benchmark for petroleum geoscience
**arXiv**：[2601.02158v1](https://arxiv.org/abs/2601.02158) · [PDF](https://arxiv.org/pdf/2601.02158.pdf)  
**作者**：Almaz Ermilov  

**一句话要点**：提出FormationEval开放多项选择题基准，用于评估语言模型在石油地质学及地下学科的表现。

**关键词**：石油地质学基准, 语言模型评估, 多项选择题数据集, 开源模型比较, 领域性能分析, 偏差缓解策略

## 3 点简述
- 核心问题：缺乏针对石油地质学等专业领域的语言模型评估基准，需避免版权文本直接复制。
- 方法要点：基于三个权威来源，采用推理模型和概念方法构建505个问题，覆盖七个领域。
- 实验或效果：评估72个模型，顶级模型准确率超97%，开源模型表现接近闭源模型，但领域间存在差距。

## 摘要（原文）

> This paper presents FormationEval, an open multiple-choice question benchmark for evaluating language models on petroleum geoscience and subsurface disciplines. The dataset contains 505 questions across seven domains including petrophysics, petroleum geology and reservoir engineering, derived from three authoritative sources using a reasoning model with detailed instructions and a concept-based approach that avoids verbatim copying of copyrighted text. Each question includes source metadata to support traceability and audit. The evaluation covers 72 models from major providers including OpenAI, Anthropic, Google, Meta and open-weight alternatives. The top performers achieve over 97\% accuracy, with Gemini 3 Pro Preview reaching 99.8\%, while tier and domain gaps persist. Among open-weight models, GLM-4.7 leads at 98.6\%, with several DeepSeek, Llama, Qwen and Mistral models also exceeding 93\%. The performance gap between open-weight and closed models is narrower than expected, with several lower-cost open-weight models exceeding 90\% accuracy. Petrophysics emerges as the most challenging domain across all models, while smaller models show wider performance variance. Residual length bias in the dataset (correct answers tend to be longer) is documented along with bias mitigation strategies applied during construction. The benchmark, evaluation code and results are publicly available.

