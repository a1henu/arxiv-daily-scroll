---
layout: default
title: Interpretable Debiasing of Vision-Language Models for Social Fairness
---

# Interpretable Debiasing of Vision-Language Models for Social Fairness
**arXiv**：[2602.24014v1](https://arxiv.org/abs/2602.24014) · [PDF](https://arxiv.org/pdf/2602.24014.pdf)  
**作者**：Na Min An, Yoonna Jang, Yusuke Hirota, Ryo Hachiuma, Isabelle Augenstein, Hyunjung Shim  

**一句话要点**：提出DeBiasLens框架，通过稀疏自编码器定位并去活社会属性神经元，以缓解视觉语言模型的社会偏见。

**关键词**：视觉语言模型, 社会偏见缓解, 稀疏自编码器, 可解释性, 模型无关框架

## 3 点简述
- 核心问题：视觉语言模型的黑盒推理过程可能导致社会偏见，现有方法未深入探索模型内部动态。
- 方法要点：使用稀疏自编码器在无标签数据上定位社会属性神经元，选择性去活与偏见强相关的神经元。
- 实验或效果：有效缓解模型的社会偏见行为，同时保持语义知识不退化，为未来审计工具奠定基础。

## 摘要（原文）

> The rapid advancement of Vision-Language models (VLMs) has raised growing concerns that their black-box reasoning processes could lead to unintended forms of social bias. Current debiasing approaches focus on mitigating surface-level bias signals through post-hoc learning or test-time algorithms, while leaving the internal dynamics of the model largely unexplored. In this work, we introduce an interpretable, model-agnostic bias mitigation framework, DeBiasLens, that localizes social attribute neurons in VLMs through sparse autoencoders (SAEs) applied to multimodal encoders. Building upon the disentanglement ability of SAEs, we train them on facial image or caption datasets without corresponding social attribute labels to uncover neurons highly responsive to specific demographics, including those that are underrepresented. By selectively deactivating the social neurons most strongly tied to bias for each group, we effectively mitigate socially biased behaviors of VLMs without degrading their semantic knowledge. Our research lays the groundwork for future auditing tools, prioritizing social fairness in emerging real-world AI systems.

