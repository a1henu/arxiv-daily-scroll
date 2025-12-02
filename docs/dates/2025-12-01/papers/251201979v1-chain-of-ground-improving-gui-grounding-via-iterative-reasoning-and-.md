---
layout: default
title: Chain-of-Ground: Improving GUI Grounding via Iterative Reasoning and Reference Feedback
---

# Chain-of-Ground: Improving GUI Grounding via Iterative Reasoning and Reference Feedback
**arXiv**：[2512.01979v1](https://arxiv.org/abs/2512.01979) · [PDF](https://arxiv.org/pdf/2512.01979.pdf)  
**作者**：Aiden Yiliu Li, Bizhi Yu, Daoan Lei, Tianhe Ren, Shilong Liu  

**一句话要点**：提出Chain-of-Ground框架，通过迭代推理和参考反馈提升复杂用户界面的GUI定位精度

**关键词**：GUI定位, 多模态大语言模型, 迭代推理, 视觉界面理解, 训练免费框架, 工业控制面板

## 3 点简述
- 核心问题：现有多模态大模型在GUI定位中，对小目标、视觉相似目标和布局模糊性处理不足，源于定位能力有限和推理潜力未充分利用。
- 方法要点：提出无需训练的CoG框架，利用多模态大模型进行迭代视觉推理和假设调整，实现渐进式定位优化。
- 实验或效果：在ScreenSpot Pro基准上达到68.4%准确率，提升4.8点；在TPanel UI数据集上超越Qwen3 VL 235B基线6.9点，验证了跨真实和数字界面的泛化能力。

## 摘要（原文）

> GUI grounding aims to align natural language instructions with precise regions in complex user interfaces. Advanced multimodal large language models show strong ability in visual GUI grounding but still struggle with small or visually similar targets and ambiguity in real world layouts. These limitations arise from limited grounding capacity and from underuse of existing reasoning potential. We present Chain of Ground CoG a training free multi step grounding framework that uses multimodal large language models for iterative visual reasoning and refinement. Instead of direct prediction the model progressively reflects and adjusts its hypotheses leading to more accurate and interpretable localization. Our approach achieves 68.4 accuracy on the ScreenSpot Pro benchmark an improvement of 4.8 points. To measure real world generalization we introduce TPanel UI a dataset of 420 labeled industrial control panels with visual distortions such as blur and masking. On TPanel UI Chain of Ground improves over the strong baseline Qwen3 VL 235B by 6.9 points showing the effectiveness of multi step training free grounding across real world and digital interfaces. These results highlight a direction for unlocking grounding potential through structured iterative refinement instead of additional training.

