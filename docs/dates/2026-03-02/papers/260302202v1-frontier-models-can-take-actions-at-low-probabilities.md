---
layout: default
title: Frontier Models Can Take Actions at Low Probabilities
---

# Frontier Models Can Take Actions at Low Probabilities
**arXiv**：[2603.02202v1](https://arxiv.org/abs/2603.02202) · [PDF](https://arxiv.org/pdf/2603.02202.pdf)  
**作者**：Alex Serrano, Wen Xing, David Lindner, Erik Jenner  

**一句话要点**：评估前沿模型在低概率下执行目标动作的校准能力，揭示其潜在规避监督的风险。

**关键词**：模型校准, 低概率动作, 前沿模型评估, 规避监督, 思维链推理, 熵源依赖

## 3 点简述
- 核心问题：恶意模型能否通过极低概率（如0.01%）执行不良动作来规避部署前评估的监督。
- 方法要点：通过提示GPT-5、Claude-4.5和Qwen-3等模型在给定或推导的低概率下执行目标动作，并评估其校准性。
- 实验或效果：前沿模型在上下文有熵源时能保持高校准至低于十万分之一，无熵源时部分模型可达万分之一；但推导目标率时需显式思维链，否则校准失败。

## 摘要（原文）

> Pre-deployment evaluations inspect only a limited sample of model actions. A malicious model seeking to evade oversight could exploit this by randomizing when to "defect": misbehaving so rarely that no malicious actions are observed during evaluation, but often enough that they occur eventually in deployment. But this requires taking actions at very low rates, while maintaining calibration. Are frontier models even capable of that? We prompt the GPT-5, Claude-4.5 and Qwen-3 families to take a target action at low probabilities (e.g. 0.01%), either given directly or requiring derivation, and evaluate their calibration (i.e. whether they perform the target action roughly 1 in 10,000 times when resampling). We find that frontier models are surprisingly good at this task. If there is a source of entropy in-context (such as a UUID), they maintain high calibration at rates lower than 1 in 100,000 actions. Without external entropy, some models can still reach rates lower than 1 in 10,000. When target rates are given, larger models achieve good calibration at lower rates. Yet, when models must derive the optimal target rate themselves, all models fail to achieve calibration without entropy or hint to generate it. Successful low-rate strategies require explicit Chain-of-Thought (CoT) reasoning, so malicious models attempting this approach could currently be caught by a CoT monitor. However, scaling trends suggest future evaluations may be unable to rely on models' lack of target rate calibration, especially if CoT is no longer legible.

