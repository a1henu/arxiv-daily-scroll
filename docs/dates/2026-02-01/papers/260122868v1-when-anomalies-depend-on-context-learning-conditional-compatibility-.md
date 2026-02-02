---
layout: default
title: When Anomalies Depend on Context: Learning Conditional Compatibility for Anomaly Detection
---

# When Anomalies Depend on Context: Learning Conditional Compatibility for Anomaly Detection
**arXiv**：[2601.22868v1](https://arxiv.org/abs/2601.22868) · [PDF](https://arxiv.org/pdf/2601.22868.pdf)  
**作者**：Shashank Mishra, Didier Stricker, Jason Rambach  

**一句话要点**：提出条件兼容性学习框架，以解决视觉领域中上下文依赖的异常检测问题。

**关键词**：上下文异常检测, 条件兼容性学习, 视觉-语言表示, 基准数据集, 有限监督学习

## 3 点简述
- 核心问题：异常检测常假设异常独立于上下文，但现实中异常可能依赖上下文因素。
- 方法要点：利用视觉-语言表示建模主体-上下文关系，在有限监督下学习条件兼容性。
- 实验或效果：在CAAD-3K基准上显著优于现有方法，并在MVTec-AD和VisA上达到先进性能。

## 摘要（原文）

> Anomaly detection is often formulated under the assumption that abnormality is an intrinsic property of an observation, independent of context. This assumption breaks down in many real-world settings, where the same object or action may be normal or anomalous depending on latent contextual factors (e.g., running on a track versus on a highway). We revisit \emph{contextual anomaly detection}, classically defined as context-dependent abnormality, and operationalize it in the visual domain, where anomaly labels depend on subject--context compatibility rather than intrinsic appearance. To enable systematic study of this setting, we introduce CAAD-3K, a benchmark that isolates contextual anomalies by controlling subject identity while varying context. We further propose a conditional compatibility learning framework that leverages vision--language representations to model subject--context relationships under limited supervision. Our method substantially outperforms existing approaches on CAAD-3K and achieves state-of-the-art performance on MVTec-AD and VisA, demonstrating that modeling context dependence complements traditional structural anomaly detection. Our code and dataset will be publicly released.

