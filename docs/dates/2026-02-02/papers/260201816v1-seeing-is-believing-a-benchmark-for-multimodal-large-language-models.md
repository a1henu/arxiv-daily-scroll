---
layout: default
title: Seeing Is Believing? A Benchmark for Multimodal Large Language Models on Visual Illusions and Anomalies
---

# Seeing Is Believing? A Benchmark for Multimodal Large Language Models on Visual Illusions and Anomalies
**arXiv**：[2602.01816v1](https://arxiv.org/abs/2602.01816) · [PDF](https://arxiv.org/pdf/2602.01816.pdf)  
**作者**：Wenjin Hou, Wei Liu, Han Hu, Xiaoxiao Sun, Serena Yeung-Levy, Hehe Fan  

**一句话要点**：提出VIA-Bench基准以评估多模态大语言模型在视觉错觉与异常场景下的鲁棒性

**关键词**：多模态大语言模型, 视觉错觉, 基准评估, 鲁棒性分析, 人工审核, 感知差异

## 3 点简述
- 核心问题：现有评估依赖标准分布数据，未检验模型在违背常识先验的视觉错觉与异常中的鲁棒性
- 方法要点：构建包含六类视觉错觉与异常的1K+高质量问答对，通过人工审核确保数据质量
- 实验或效果：评估20+先进模型，发现显著脆弱性，思维链推理提供有限鲁棒性，揭示机器与人类感知的根本差异

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) have shown remarkable proficiency on general-purpose vision-language benchmarks, reaching or even exceeding human-level performance. However, these evaluations typically rely on standard in-distribution data, leaving the robustness of MLLMs largely unexamined when faced with scenarios that defy common-sense priors. To address this gap, we introduce VIA-Bench, a challenging benchmark designed to probe model performance on visual illusions and anomalies. It includes six core categories: color illusions, motion illusions, gestalt illusions, geometric and spatial illusions, general visual illusions, and visual anomalies. Through careful human-in-the-loop review, we construct over 1K high-quality question-answer pairs that require nuanced visual reasoning. Extensive evaluation of over 20 state-of-the-art MLLMs, including proprietary, open-source, and reasoning-enhanced models, uncovers significant vulnerabilities. Notably, we find that Chain-of-Thought (CoT) reasoning offers negligible robustness, often yielding ``brittle mirages'' where the model's logic collapses under illusory stimuli. Our findings reveal a fundamental divergence between machine and human perception, suggesting that resolving such perceptual bottlenecks is critical for the advancement of artificial general intelligence. The benchmark data and code will be released.

