---
layout: default
title: The Effectiveness of Style Vectors for Steering Large Language Models: A Human Evaluation
---

# The Effectiveness of Style Vectors for Steering Large Language Models: A Human Evaluation
**arXiv**：[2601.21505v1](https://arxiv.org/abs/2601.21505) · [PDF](https://arxiv.org/pdf/2601.21505.pdf)  
**作者**：Diaoulé Diallo, Katharina Dworatzyk, Sophie Jentzsch, Peer Schütt, Sabine Theis, Tobias Hecking  

**一句话要点**：通过激活导向实现大语言模型情感控制：首次人类评估验证其有效性

**关键词**：激活导向, 大语言模型控制, 情感调节, 人类评估, 轻量干预, 模型对齐

## 3 点简述
- 核心问题：大语言模型推理时行为控制需轻量方法，以对齐人类能力与安全要求。
- 方法要点：采用激活导向技术，直接修改内部激活来引导生成，替代提示工程与微调。
- 实验或效果：人类评估显示，中等强度导向可可靠增强目标情感并保持可理解性，模型与人类评分高度一致。

## 摘要（原文）

> Controlling the behavior of large language models (LLMs) at inference time is essential for aligning outputs with human abilities and safety requirements. \emph{Activation steering} provides a lightweight alternative to prompt engineering and fine-tuning by directly modifying internal activations to guide generation. This research advances the literature in three significant directions. First, while previous work demonstrated the technical feasibility of steering emotional tone using automated classifiers, this paper presents the first human evaluation of activation steering concerning the emotional tone of LLM outputs, collecting over 7,000 crowd-sourced ratings from 190 participants via Prolific ($n=190$). These ratings assess both perceived emotional intensity and overall text quality. Second, we find strong alignment between human and model-based quality ratings (mean $r=0.776$, range $0.157$--$0.985$), indicating automatic scoring can proxy perceived quality. Moderate steering strengths ($λ\approx 0.15$) reliably amplify target emotions while preserving comprehensibility, with the strongest effects for disgust ($η_p^2 = 0.616$) and fear ($η_p^2 = 0.540$), and minimal effects for surprise ($η_p^2 = 0.042$). Finally, upgrading from Alpaca to LlaMA-3 yielded more consistent steering with significant effects across emotions and strengths (all $p < 0.001$). Inter-rater reliability was high (ICC $= 0.71$--$0.87$), underscoring the robustness of the findings. These findings support activation-based control as a scalable method for steering LLM behavior across affective dimensions.

