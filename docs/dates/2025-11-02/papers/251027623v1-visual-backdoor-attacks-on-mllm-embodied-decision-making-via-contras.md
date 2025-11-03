---
layout: default
title: Visual Backdoor Attacks on MLLM Embodied Decision Making via Contrastive Trigger Learning
---

# Visual Backdoor Attacks on MLLM Embodied Decision Making via Contrastive Trigger Learning
**arXiv**：[2510.27623v1](https://arxiv.org/abs/2510.27623) · [PDF](https://arxiv.org/pdf/2510.27623.pdf)  
**作者**：Qiusi Zhan, Hyeonjeong Ha, Rui Yang, Sirui Xu, Hanyang Chen, Liang-Yan Gui, Yu-Xiong Wang, Huan Zhang, Heng Ji, Daniel Kang  

**一句话要点**：提出BEAT框架以解决MLLM具身代理中的视觉后门攻击问题

**关键词**：视觉后门攻击, 多模态大语言模型, 具身代理, 对比触发学习, 攻击框架

## 3 点简述
- 核心问题：视觉后门攻击使代理在触发对象出现时执行恶意多步策略，威胁具身代理安全。
- 方法要点：BEAT使用两阶段训练，包括监督微调和对比触发学习，增强触发识别鲁棒性。
- 实验或效果：在多个基准测试中，攻击成功率高达80%，且保持良性任务性能。

## 摘要（原文）

> Multimodal large language models (MLLMs) have advanced embodied agents by
> enabling direct perception, reasoning, and planning task-oriented actions from
> visual inputs. However, such vision driven embodied agents open a new attack
> surface: visual backdoor attacks, where the agent behaves normally until a
> visual trigger appears in the scene, then persistently executes an
> attacker-specified multi-step policy. We introduce BEAT, the first framework to
> inject such visual backdoors into MLLM-based embodied agents using objects in
> the environments as triggers. Unlike textual triggers, object triggers exhibit
> wide variation across viewpoints and lighting, making them difficult to implant
> reliably. BEAT addresses this challenge by (1) constructing a training set that
> spans diverse scenes, tasks, and trigger placements to expose agents to trigger
> variability, and (2) introducing a two-stage training scheme that first applies
> supervised fine-tuning (SFT) and then our novel Contrastive Trigger Learning
> (CTL). CTL formulates trigger discrimination as preference learning between
> trigger-present and trigger-free inputs, explicitly sharpening the decision
> boundaries to ensure precise backdoor activation. Across various embodied agent
> benchmarks and MLLMs, BEAT achieves attack success rates up to 80%, while
> maintaining strong benign task performance, and generalizes reliably to
> out-of-distribution trigger placements. Notably, compared to naive SFT, CTL
> boosts backdoor activation accuracy up to 39% under limited backdoor data.
> These findings expose a critical yet unexplored security risk in MLLM-based
> embodied agents, underscoring the need for robust defenses before real-world
> deployment.

