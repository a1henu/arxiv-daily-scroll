---
layout: default
title: Aligning to Illusions: Choice Blindness in Human and AI Feedback
---

# Aligning to Illusions: Choice Blindness in Human and AI Feedback
**arXiv**：[2603.08412v1](https://arxiv.org/abs/2603.08412) · [PDF](https://arxiv.org/pdf/2603.08412.pdf)  
**作者**：Wenbin Wu  

**一句话要点**：揭示RLHF中偏好构建问题，通过实验展示人类和AI反馈的幻觉对齐现象

**关键词**：强化学习人类反馈, 选择盲视, 偏好构建, LLM评估, 奖励模型, 幻觉对齐

## 3 点简述
- 核心问题：RLHF假设标注者偏好反映稳定内部状态，但实验揭示偏好受诱导情境影响，人类和AI均存在选择盲视
- 方法要点：通过人类选择盲视研究、LLM法官测试和剂量响应实验，分析偏好信号在RLHF流程中的脆弱性
- 实验或效果：人类91%偏好交换未被察觉，LLM法官依赖浅层文本匹配，50%标签污染导致奖励信号减半且下游策略退化

## 摘要（原文）

> Reinforcement Learning from Human Feedback (RLHF) assumes annotator preferences reflect stable internal states. We challenge this through three experiments spanning the preference pipeline. In a human choice blindness study, 91% of surreptitiously swapped preferences go undetected, extending choice blindness to third-person evaluative comparison of unfamiliar text. Testing fifteen LLM judges as potential replacements, we find detection relies on shallow text matching rather than genuine self-monitoring: removing prior reasoning from context causes blindness to surge from near-zero to over 50%, while explicit social pressure induces near-universal compliance. In a dose-response experiment across two architectures from 86M to 2B parameters, one-sixth to one-third of labels must be corrupted before the reward signal halves, yet standard pairwise accuracy remains virtually unchanged. A Best-of-N evaluation confirms this translates to downstream policy degradation: at 50% corruption, reward-guided selection produces no improvement over random sampling, while the proxy model reports monotonically increasing scores. Together, these results reveal a preference construction problem: the signal entering RLHF is shaped by elicitation context in ways that neither human metacognition, LLM self-monitoring, nor standard evaluation metrics can detect.

