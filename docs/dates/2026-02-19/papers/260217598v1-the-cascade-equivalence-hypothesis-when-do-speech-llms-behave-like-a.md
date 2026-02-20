---
layout: default
title: The Cascade Equivalence Hypothesis: When Do Speech LLMs Behave Like ASR$\rightarrow$LLM Pipelines?
---

# The Cascade Equivalence Hypothesis: When Do Speech LLMs Behave Like ASR$\rightarrow$LLM Pipelines?
**arXiv**：[2602.17598v1](https://arxiv.org/abs/2602.17598) · [PDF](https://arxiv.org/pdf/2602.17598.pdf)  
**作者**：Jayadev Billa  

**一句话要点**：提出级联等价假设，揭示多数语音大语言模型在任务中行为等效于ASR→LLM级联，并证明其架构依赖性。

**关键词**：语音大语言模型, 级联等价假设, ASR→LLM级联, 匹配骨干测试, 噪声鲁棒性, 架构依赖性

## 3 点简述
- 核心问题：当前语音大语言模型是否在行为上等同于简单的ASR→LLM级联？
- 方法要点：通过匹配骨干测试，比较四种语音大语言模型与对应级联在六个任务上的表现。
- 实验或效果：Ultravox与级联统计不可分，Qwen2-Audio显示差异，表明等价性非普遍，受噪声影响性能下降。

## 摘要（原文）

> Current speech LLMs largely perform implicit ASR: on tasks solvable from a transcript, they are behaviorally and mechanistically equivalent to simple Whisper$\to$LLM cascades. We show this through matched-backbone testing across four speech LLMs and six tasks, controlling for the LLM backbone for the first time. Ultravox is statistically indistinguishable from its matched cascade ($κ{=}0.93$); logit lens reveals literal text emerging in hidden states; LEACE concept erasure confirms text representations are causally necessary in both architectures tested, collapsing accuracy to near-zero. Qwen2-Audio genuinely diverges, revealing cascade equivalence is architecture-dependent, not universal. For most deployed use cases, current speech LLMs are expensive cascades, and under noise, they are worse ones, with clean-condition advantages reversing by up to 7.6% at 0 dB.

