---
layout: default
title: PAS : Prelim Attention Score for Detecting Object Hallucinations in Large Vision--Language Models
---

# PAS : Prelim Attention Score for Detecting Object Hallucinations in Large Vision--Language Models
**arXiv**：[2511.11502v1](https://arxiv.org/abs/2511.11502) · [PDF](https://arxiv.org/pdf/2511.11502.pdf)  
**作者**：Nhat Hoang-Xuan, Minh Vu, My T. Thai, Manish Bhattarai  

**一句话要点**：提出Prelim Attention Score以检测大型视觉语言模型中的物体幻觉

**关键词**：物体幻觉检测, 注意力机制, 大型视觉语言模型, 实时推理, 训练无关方法

## 3 点简述
- 核心问题：大型视觉语言模型易产生物体幻觉，常忽略图像依赖先前输出
- 方法要点：基于注意力权重计算PAS，无需额外训练或前向传播
- 实验或效果：在多个模型和数据集上实现SOTA检测，支持实时干预

## 摘要（原文）

> Large vision-language models (LVLMs) are powerful, yet they remain unreliable due to object hallucinations. In this work, we show that in many hallucinatory predictions the LVLM effectively ignores the image and instead relies on previously generated output (prelim) tokens to infer new objects. We quantify this behavior via the mutual information between the image and the predicted object conditioned on the prelim, demonstrating that weak image dependence strongly correlates with hallucination. Building on this finding, we introduce the Prelim Attention Score (PAS), a lightweight, training-free signal computed from attention weights over prelim tokens. PAS requires no additional forward passes and can be computed on the fly during inference. Exploiting this previously overlooked signal, PAS achieves state-of-the-art object-hallucination detection across multiple models and datasets, enabling real-time filtering and intervention.

