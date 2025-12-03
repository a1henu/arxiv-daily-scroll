---
layout: default
title: Emergent Bayesian Behaviour and Optimal Cue Combination in LLMs
---

# Emergent Bayesian Behaviour and Optimal Cue Combination in LLMs
**arXiv**：[2512.02719v1](https://arxiv.org/abs/2512.02719) · [PDF](https://arxiv.org/pdf/2512.02719.pdf)  
**作者**：Julian Ma, Jun Wang, Zafeirios Fountas  

**一句话要点**：提出BayesBench基准与贝叶斯一致性评分，评估LLMs在感知任务中的隐式贝叶斯行为与多模态线索整合。

**关键词**：贝叶斯行为评估, 多模态线索整合, 心理物理学基准, LLMs隐式计算, 不确定性处理, 行为一致性评分

## 3 点简述
- 核心问题：探究LLMs是否在无显式训练下表现出类似人类的近最优贝叶斯策略进行多模态线索整合。
- 方法要点：基于心理物理学范式，设计文本和图像的四种幅度估计任务，通过噪声、上下文和指令提示的受控消融实验。
- 实验或效果：发现能力强的模型常以贝叶斯一致方式适应，但准确性不保证鲁棒性，如GPT-5 Mini文本准确但视觉整合效率低。

## 摘要（原文）

> Large language models (LLMs) excel at explicit reasoning, but their implicit computational strategies remain underexplored. Decades of psychophysics research show that humans intuitively process and integrate noisy signals using near-optimal Bayesian strategies in perceptual tasks. We ask whether LLMs exhibit similar behaviour and perform optimal multimodal integration without explicit training or instruction. Adopting the psychophysics paradigm, we infer computational principles of LLMs from systematic behavioural studies. We introduce a behavioural benchmark - BayesBench: four magnitude estimation tasks (length, location, distance, and duration) over text and image, inspired by classic psychophysics, and evaluate a diverse set of nine LLMs alongside human judgments for calibration. Through controlled ablations of noise, context, and instruction prompts, we measure performance, behaviour and efficiency in multimodal cue-combination. Beyond accuracy and efficiency metrics, we introduce a Bayesian Consistency Score that detects Bayes-consistent behavioural shifts even when accuracy saturates. Our results show that while capable models often adapt in Bayes-consistent ways, accuracy does not guarantee robustness. Notably, GPT-5 Mini achieves perfect text accuracy but fails to integrate visual cues efficiently. This reveals a critical dissociation between capability and strategy, suggesting accuracy-centric benchmarks may over-index on performance while missing brittle uncertainty handling. These findings reveal emergent principled handling of uncertainty and highlight the correlation between accuracy and Bayesian tendencies. We release our psychophysics benchmark and consistency metric (https://bayes-bench.github.io) as evaluation tools and to inform future multimodal architecture designs.

