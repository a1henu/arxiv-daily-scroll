---
layout: default
title: Countering the Over-Reliance Trap: Mitigating Object Hallucination for LVLMs via a Self-Validation Framework
---

# Countering the Over-Reliance Trap: Mitigating Object Hallucination for LVLMs via a Self-Validation Framework
**arXiv**：[2601.22451v1](https://arxiv.org/abs/2601.22451) · [PDF](https://arxiv.org/pdf/2601.22451.pdf)  
**作者**：Shiyu Liu, Xinyi Wen, Zhibin Lan, Ante Wang, Jinsong Su  

**一句话要点**：提出自验证框架以缓解大视觉语言模型在图像描述中的物体幻觉问题

**关键词**：物体幻觉, 大视觉语言模型, 图像描述, 自验证框架, 语言先验

## 3 点简述
- 核心问题：大视觉语言模型在图像描述中过度依赖语言先验，导致生成不存在物体的幻觉。
- 方法要点：通过语言先验无关验证和自验证框架，训练免费地验证物体存在并选择或聚合描述。
- 实验或效果：在CHAIRI指标上提升65.6%（LLaVA-v1.5-7B），超越先前SOTA方法。

## 摘要（原文）

> Despite progress in Large Vision Language Models (LVLMs), object hallucination remains a critical issue in image captioning task, where models generate descriptions of non-existent objects, compromising their reliability. Previous work attributes this to LVLMs' over-reliance on language priors and attempts to mitigate it through logits calibration. However, they still lack a thorough analysis of the over-reliance. To gain a deeper understanding of over-reliance, we conduct a series of preliminary experiments, indicating that as the generation length increases, LVLMs' over-reliance on language priors leads to inflated probability of hallucinated object tokens, consequently exacerbating object hallucination. To circumvent this issue, we propose Language-Prior-Free Verification to enable LVLMs to faithfully verify the confidence of object existence. Based on this, we propose a novel training-free Self-Validation Framework to counter the over-reliance trap. It first validates objects' existence in sampled candidate captions and further mitigates object hallucination via caption selection or aggregation. Experiment results demonstrate that our framework mitigates object hallucination significantly in image captioning task (e.g., 65.6% improvement on CHAIRI metric with LLaVA-v1.5-7B), surpassing the previous SOTA methods. This result highlights a novel path towards mitigating hallucination by unlocking the inherent potential within LVLMs themselves.

