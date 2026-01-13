---
layout: default
title: BEAT-Net: Injecting Biomimetic Spatio-Temporal Priors for Interpretable ECG Classification
---

# BEAT-Net: Injecting Biomimetic Spatio-Temporal Priors for Interpretable ECG Classification
**arXiv**：[2601.07316v1](https://arxiv.org/abs/2601.07316) · [PDF](https://arxiv.org/pdf/2601.07316.pdf)  
**作者**：Runze Ma, Caizhi Liao  

**一句话要点**：提出BEAT-Net框架，通过生物启发的QRS标记化将ECG分类转化为语言建模任务，以提升数据效率和可解释性。

**关键词**：心电图分类, 生物启发模型, 语言建模, 可解释性, 数据效率, QRS标记化

## 3 点简述
- 核心问题：现有深度学习方法将ECG视为一维信号或二维图像，导致数据效率低和模型不透明，与医学推理脱节。
- 方法要点：采用QRS标记化策略将连续信号转换为心跳序列，通过专门编码器分解心脏生理结构，建模时空依赖关系。
- 实验或效果：在三个大规模基准测试中，BEAT-Net匹配CNN的准确度，显著提高鲁棒性，仅需30-35%标注数据即可恢复全监督性能，并提供可解释性。

## 摘要（原文）

> Although deep learning has advanced automated electrocardiogram (ECG) diagnosis, prevalent supervised methods typically treat recordings as undifferentiated one-dimensional (1D) signals or two-dimensional (2D) images. This formulation compels models to learn physiological structures implicitly, resulting in data inefficiency and opacity that diverge from medical reasoning. To address these limitations, we propose BEAT-Net, a Biomimetic ECG Analysis with Tokenization framework that reformulates the problem as a language modeling task. Utilizing a QRS tokenization strategy to transform continuous signals into biologically aligned heartbeat sequences, the architecture explicitly decomposes cardiac physiology through specialized encoders that extract local beat morphology while normalizing spatial lead perspectives and modeling temporal rhythm dependencies. Evaluations across three large-scale benchmarks demonstrate that BEAT-Net matches the diagnostic accuracy of dominant convolutional neural network (CNN) architectures while substantially improving robustness. The framework exhibits exceptional data efficiency, recovering fully supervised performance using only 30 to 35 percent of annotated data. Moreover, learned attention mechanisms provide inherent interpretability by spontaneously reproducing clinical heuristics, such as Lead II prioritization for rhythm analysis, without explicit supervision. These findings indicate that integrating biological priors offers a computationally efficient and interpretable alternative to data-intensive large-scale pre-training.

