---
layout: default
title: Diffusion-State Policy Optimization for Masked Diffusion Language Models
---

# Diffusion-State Policy Optimization for Masked Diffusion Language Models
**arXiv**：[2602.06462v1](https://arxiv.org/abs/2602.06462) · [PDF](https://arxiv.org/pdf/2602.06462.pdf)  
**作者**：Daisuke Oba, Hiroki Furuta, Naoaki Okazaki  

**一句话要点**：提出DiSPO以优化掩码扩散语言模型的中间填充决策，改进信用分配。

**关键词**：扩散语言模型, 信用分配, 策略优化, 中间决策, 掩码填充, 强化学习

## 3 点简述
- 核心问题：掩码扩散语言模型仅依赖最终完成奖励导致中间决策信用分配粗糙。
- 方法要点：DiSPO在中间掩码状态分支，通过重采样填充并评分，直接优化新填充令牌。
- 实验或效果：在LLaDA-8B-Instruct上，DiSPO在数学和规划基准上优于终端反馈基线。

## 摘要（原文）

> Masked diffusion language models generate by iteratively filling masked tokens over multiple denoising steps, so learning only from a terminal reward on the final completion yields coarse credit assignment over intermediate decisions. We propose DiSPO (Diffusion-State Policy Optimization), a plug-in credit-assignment layer that directly optimizes intermediate filling decisions. At selected intermediate masked states, DiSPO branches by resampling fillings for the currently masked positions from rollout-cached logits, scores the resulting completions, and updates only the newly filled tokens -- without additional multi-step diffusion rollouts. We formalize a fixed-state objective for branched completions and derive a policy-gradient estimator that can be combined with terminal-feedback policy optimization using the same rollouts. On LLaDA-8B-Instruct, DiSPO consistently improves over the terminal-feedback diffu-GRPO baseline on math and planning benchmarks under matched rollout compute and optimizer steps. Our code will be available at https://daioba.github.io/dispo .

