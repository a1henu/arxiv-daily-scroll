---
layout: default
title: Learning When to Look: A Disentangled Curriculum for Strategic Perception in Multimodal Reasoning
---

# Learning When to Look: A Disentangled Curriculum for Strategic Perception in Multimodal Reasoning
**arXiv**：[2512.17227v1](https://arxiv.org/abs/2512.17227) · [PDF](https://arxiv.org/pdf/2512.17227.pdf)  
**作者**：Siqi Yang, Zilve Gao, Haibo Qiu, Fanfan Liu, Peng Shi, Zhixiong Zeng, Qingmin Liao, Lin Ma  

**一句话要点**：提出解耦课程框架以解决多模态大语言模型在长链视觉推理中的视觉遗忘问题

**关键词**：多模态大语言模型, 视觉推理, 解耦训练, 强化学习, 课程学习, 策略感知

## 3 点简述
- 核心问题：模型在长链推理中因视觉与逻辑技能过早纠缠导致视觉遗忘和策略感知缺失
- 方法要点：先通过解耦SFT课程构建文本推理骨干，再引入PG-CoT和强化学习奖励学习何时感知
- 实验或效果：未知，但框架旨在将模型从启发式观察者转变为策略性接地推理者

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) demonstrate significant potential but remain brittle in complex, long-chain visual reasoning tasks. A critical failure mode is "visual forgetting", where models progressively lose visual grounding as reasoning extends, a phenomenon aptly described as "think longer, see less". We posit this failure stems from current training paradigms prematurely entangling two distinct cognitive skills: (1) abstract logical reasoning "how-to-think") and (2) strategic visual perception ("when-to-look"). This creates a foundational cold-start deficiency -- weakening abstract reasoning -- and a strategic perception deficit, as models lack a policy for when to perceive. In this paper, we propose a novel curriculum-based framework to disentangle these skills. First, we introduce a disentangled Supervised Fine-Tuning (SFT) curriculum that builds a robust abstract reasoning backbone on text-only data before anchoring it to vision with a novel Perception-Grounded Chain-of-Thought (PG-CoT) paradigm. Second, we resolve the strategic perception deficit by formulating timing as a reinforcement learning problem. We design a Pivotal Perception Reward that teaches the model when to look by coupling perceptual actions to linguistic markers of cognitive uncertainty (e.g., "wait", "verify"), thereby learning an autonomous grounding policy. Our contributions include the formalization of these two deficiencies and the development of a principled, two-stage framework to address them, transforming the model from a heuristic-driven observer to a strategic, grounded reasoner. \textbf{Code}: \url{https://github.com/gaozilve-max/learning-when-to-look}.

