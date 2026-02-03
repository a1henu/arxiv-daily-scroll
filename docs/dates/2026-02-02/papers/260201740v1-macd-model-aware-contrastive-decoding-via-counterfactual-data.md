---
layout: default
title: MACD: Model-Aware Contrastive Decoding via Counterfactual Data
---

# MACD: Model-Aware Contrastive Decoding via Counterfactual Data
**arXiv**：[2602.01740v1](https://arxiv.org/abs/2602.01740) · [PDF](https://arxiv.org/pdf/2602.01740.pdf)  
**作者**：Qixin Xiao, Kun Zhou  

**一句话要点**：提出MACD方法，通过模型感知的反事实数据对比解码，减少视频语言模型的幻觉问题。

**关键词**：视频语言模型, 幻觉减少, 对比解码, 反事实数据, 对象级编辑, 推理策略

## 3 点简述
- 核心问题：视频语言模型在视觉证据弱、模糊或有偏时易产生幻觉，生成不基于证据的内容。
- 方法要点：利用模型反馈识别导致幻觉的对象区域，生成针对性反事实输入，并集成到对比解码中强化证据基础。
- 实验或效果：在多个基准测试中，MACD能持续减少幻觉，保持或提升任务准确性，尤其在处理小、遮挡或共现对象时有效。

## 摘要（原文）

> Video language models (Video-LLMs) are prone to hallucinations, often generating plausible but ungrounded content when visual evidence is weak, ambiguous, or biased. Existing decoding methods, such as contrastive decoding (CD), rely on random perturbations to construct contrastive data for mitigating hallucination patterns. However, such a way is hard to control the visual cues that drive hallucination or well align with model weaknesses. We propose Model-aware Counterfactual Data based Contrastive Decoding (MACD), a new inference strategy that combines model-guided counterfactual construction with decoding. Our approach uses the Video-LLM's own feedback to identify object regions most responsible for hallucination, generating targeted counterfactual inputs at the object level rather than arbitrary frame or temporal modifications. These model-aware counterfactual data is then integrated into CD to enforce evidence-grounded token selection during decoding. Experiments on EventHallusion, MVBench, Perception-test and Video-MME show that MACD consistently reduces hallucination while maintaining or improving task accuracy across diverse Video-LLMs, including Qwen and InternVL families. The method is especially effective in challenging scenarios involving small, occluded, or co-occurring objects. Our code and data will be publicly released.

