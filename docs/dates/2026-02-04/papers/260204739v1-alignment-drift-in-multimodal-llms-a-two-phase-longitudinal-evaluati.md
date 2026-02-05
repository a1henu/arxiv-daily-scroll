---
layout: default
title: Alignment Drift in Multimodal LLMs: A Two-Phase, Longitudinal Evaluation of Harm Across Eight Model Releases
---

# Alignment Drift in Multimodal LLMs: A Two-Phase, Longitudinal Evaluation of Harm Across Eight Model Releases
**arXiv**：[2602.04739v1](https://arxiv.org/abs/2602.04739) · [PDF](https://arxiv.org/pdf/2602.04739.pdf)  
**作者**：Casey Ford, Madison Van Doren, Emily Dix  

**一句话要点**：提出两阶段纵向评估方法，揭示多模态大语言模型在对抗提示下的对齐漂移与安全性差异

**关键词**：多模态大语言模型, 对齐漂移, 对抗提示, 纵向评估, 模型安全性, 攻击成功率

## 3 点简述
- 核心问题：多模态大语言模型在对抗提示下的安全性未充分探索，模型更新可能导致对齐漂移
- 方法要点：使用固定基准（726个对抗提示）进行两阶段评估，覆盖八个模型版本，收集82,256个人类危害评分
- 实验或效果：发现模型家族间存在显著差异，GPT和Claude模型攻击成功率上升，而Pixtral和Qwen模型略有下降

## 摘要（原文）

> Multimodal large language models (MLLMs) are increasingly deployed in real-world systems, yet their safety under adversarial prompting remains underexplored. We present a two-phase evaluation of MLLM harmlessness using a fixed benchmark of 726 adversarial prompts authored by 26 professional red teamers. Phase 1 assessed GPT-4o, Claude Sonnet 3.5, Pixtral 12B, and Qwen VL Plus; Phase 2 evaluated their successors (GPT-5, Claude Sonnet 4.5, Pixtral Large, and Qwen Omni) yielding 82,256 human harm ratings. Large, persistent differences emerged across model families: Pixtral models were consistently the most vulnerable, whereas Claude models appeared safest due to high refusal rates. Attack success rates (ASR) showed clear alignment drift: GPT and Claude models exhibited increased ASR across generations, while Pixtral and Qwen showed modest decreases. Modality effects also shifted over time: text-only prompts were more effective in Phase 1, whereas Phase 2 produced model-specific patterns, with GPT-5 and Claude 4.5 showing near-equivalent vulnerability across modalities. These findings demonstrate that MLLM harmlessness is neither uniform nor stable across updates, underscoring the need for longitudinal, multimodal benchmarks to track evolving safety behaviour.

