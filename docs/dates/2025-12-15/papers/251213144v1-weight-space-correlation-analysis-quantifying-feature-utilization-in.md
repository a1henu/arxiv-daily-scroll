---
layout: default
title: Weight Space Correlation Analysis: Quantifying Feature Utilization in Deep Learning Models
---

# Weight Space Correlation Analysis: Quantifying Feature Utilization in Deep Learning Models
**arXiv**：[2512.13144v1](https://arxiv.org/abs/2512.13144) · [PDF](https://arxiv.org/pdf/2512.13144.pdf)  
**作者**：Chun Kit Wong, Paraskevas Pegios, Nina Weng, Emilie Pi Fogtmann Sejer, Martin Grønnebæk Tolsgaard, Anders Nymark Christensen, Aasa Feragen  

**一句话要点**：提出权重空间相关性分析以量化医学影像深度学习模型的特征利用，验证模型可信度。

**关键词**：医学影像分析, 捷径学习检测, 特征利用量化, 模型可信度验证, 权重空间相关性

## 3 点简述
- 核心问题：医学影像模型易受捷径学习影响，依赖混杂元数据，需判断其是否主动用于预测。
- 方法要点：通过测量主临床任务与辅助元数据任务分类头之间的对齐，量化特征利用。
- 实验或效果：验证方法检测人工诱导捷径学习，应用于早产预测模型，确认其选择性利用临床相关特征。

## 摘要（原文）

> Deep learning models in medical imaging are susceptible to shortcut learning, relying on confounding metadata (e.g., scanner model) that is often encoded in image embeddings. The crucial question is whether the model actively utilizes this encoded information for its final prediction. We introduce Weight Space Correlation Analysis, an interpretable methodology that quantifies feature utilization by measuring the alignment between the classification heads of a primary clinical task and auxiliary metadata tasks. We first validate our method by successfully detecting artificially induced shortcut learning. We then apply it to probe the feature utilization of an SA-SonoNet model trained for Spontaneous Preterm Birth (sPTB) prediction. Our analysis confirmed that while the embeddings contain substantial metadata, the sPTB classifier's weight vectors were highly correlated with clinically relevant factors (e.g., birth weight) but decoupled from clinically irrelevant acquisition factors (e.g. scanner). Our methodology provides a tool to verify model trustworthiness, demonstrating that, in the absence of induced bias, the clinical model selectively utilizes features related to the genuine clinical signal.

