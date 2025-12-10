---
layout: default
title: MM-CoT:A Benchmark for Probing Visual Chain-of-Thought Reasoning in Multimodal Models
---

# MM-CoT:A Benchmark for Probing Visual Chain-of-Thought Reasoning in Multimodal Models
**arXiv**：[2512.08228v1](https://arxiv.org/abs/2512.08228) · [PDF](https://arxiv.org/pdf/2512.08228.pdf)  
**作者**：Jusheng Zhang, Kaitong Cai, Xiaoyang Guo, Sidi Liu, Qinhan Lv, Ruiqi Chen, Jing Yang, Yijia Fan, Xiaofei Sun, Jian Wang, Ziliang Chen, Liang Lin, Keze Wang  

**一句话要点**：提出MM-CoT基准以评估多模态模型视觉思维链推理的视觉一致性与逻辑连贯性

**关键词**：多模态模型, 思维链推理, 视觉一致性, 逻辑连贯性, 诊断基准, 视觉语言模型

## 3 点简述
- 核心问题：现有基准忽视验证，无法评估多模态模型思维链推理是否基于视觉证据且逻辑连贯
- 方法要点：设计诊断基准，要求模型选择满足视觉一致性和逻辑连贯性约束的唯一事件链
- 实验或效果：评估领先模型发现其表现不佳，揭示生成流畅性与真实推理保真度间的差距

## 摘要（原文）

> The ability to perform Chain-of-Thought (CoT) reasoning marks a major milestone for multimodal models (MMs), enabling them to solve complex visual reasoning problems. Yet a critical question remains: is such reasoning genuinely grounded in visual evidence and logically coherent? Existing benchmarks emphasize generation but neglect verification, i.e., the capacity to assess whether a reasoning chain is both visually consistent and logically valid. To fill this gap, we introduce MM-CoT, a diagnostic benchmark specifically designed to probe the visual grounding and logical coherence of CoT reasoning in MMs. Instead of generating free-form explanations, models must select the sole event chain that satisfies two orthogonal constraints: (i) visual consistency, ensuring all steps are anchored in observable evidence, and (ii) logical coherence, ensuring causal and commonsense validity. Adversarial distractors are engineered to violate one of these constraints, exposing distinct reasoning failures. We evaluate leading vision-language models on MM-CoT and find that even the most advanced systems struggle, revealing a sharp discrepancy between generative fluency and true reasoning fidelity. MM-CoT shows low correlation with existing benchmarks, confirming that it measures a unique combination of visual grounding and logical reasoning. This benchmark provides a foundation for developing future models that reason not just plausibly, but faithfully and coherently within the visual world.

