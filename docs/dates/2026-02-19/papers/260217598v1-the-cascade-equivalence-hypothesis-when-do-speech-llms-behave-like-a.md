---
layout: default
title: The Cascade Equivalence Hypothesis: When Do Speech LLMs Behave Like ASR$\rightarrow$LLM Pipelines?
---

# The Cascade Equivalence Hypothesis: When Do Speech LLMs Behave Like ASR$\rightarrow$LLM Pipelines?
**arXiv**：[2602.17598v1](https://arxiv.org/abs/2602.17598) · [PDF](https://arxiv.org/pdf/2602.17598.pdf)  
**作者**：Jayadev Billa  

**一句话要点**：提出级联等价假设，揭示语音大语言模型在多数任务中行为与ASR→LLM级联等效，但受架构影响。

**关键词**：语音大语言模型, 级联等价假设, ASR→LLM级联, 匹配骨干测试, 概念擦除, 噪声鲁棒性

## 3 点简述
- 核心问题：语音大语言模型是否在行为上等同于ASR→LLM级联，及其普遍性。
- 方法要点：通过匹配骨干测试、logit透镜和LEACE概念擦除，分析四个语音大语言模型在六个任务中的表现。
- 实验或效果：Ultravox与级联统计不可分，Qwen2-Audio显示架构依赖性，噪声下优势反转达7.6%。

## 摘要（原文）

> Current speech LLMs largely perform implicit ASR: on tasks solvable from a transcript, they are behaviorally and mechanistically equivalent to simple Whisper$\to$LLM cascades. We show this through matched-backbone testing across four speech LLMs and six tasks, controlling for the LLM backbone for the first time. Ultravox is statistically indistinguishable from its matched cascade ($κ{=}0.93$); logit lens reveals literal text emerging in hidden states; LEACE concept erasure confirms text representations are causally necessary in both architectures tested, collapsing accuracy to near-zero. Qwen2-Audio genuinely diverges, revealing cascade equivalence is architecture-dependent, not universal. For most deployed use cases, current speech LLMs are expensive cascades, and under noise, they are worse ones, with clean-condition advantages reversing by up to 7.6% at 0 dB.

