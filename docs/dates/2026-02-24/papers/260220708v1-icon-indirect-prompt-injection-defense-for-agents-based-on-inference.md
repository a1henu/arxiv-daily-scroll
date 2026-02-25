---
layout: default
title: ICON: Indirect Prompt Injection Defense for Agents based on Inference-Time Correction
---

# ICON: Indirect Prompt Injection Defense for Agents based on Inference-Time Correction
**arXiv**：[2602.20708v1](https://arxiv.org/abs/2602.20708) · [PDF](https://arxiv.org/pdf/2602.20708.pdf)  
**作者**：Che Wang, Fuyao Zhang, Jiaming Zhang, Ziqi Zhang, Yinghui Wang, Longtao Huang, Jianbo Gao, Zhong Chen, Wei Yang Bryan Lim  

**一句话要点**：提出ICON框架，通过推理时修正防御间接提示注入攻击，以保护LLM代理的任务连续性。

**关键词**：间接提示注入防御, LLM代理安全, 潜在空间探测, 注意力引导, 推理时修正, 多模态代理

## 3 点简述
- 核心问题：LLM代理易受间接提示注入攻击，现有防御方法因过度拒绝而中断有效工作流。
- 方法要点：利用潜在空间过聚焦特征检测攻击，并通过注意力引导选择性修正对抗性依赖以恢复功能轨迹。
- 实验或效果：在多个骨干模型上评估，攻击成功率降至0.4%，任务效用提升超50%，并展示出良好的OOD泛化和多模态扩展性。

## 摘要（原文）

> Large Language Model (LLM) agents are susceptible to Indirect Prompt Injection (IPI) attacks, where malicious instructions in retrieved content hijack the agent's execution. Existing defenses typically rely on strict filtering or refusal mechanisms, which suffer from a critical limitation: over-refusal, prematurely terminating valid agentic workflows. We propose ICON, a probing-to-mitigation framework that neutralizes attacks while preserving task continuity. Our key insight is that IPI attacks leave distinct over-focusing signatures in the latent space. We introduce a Latent Space Trace Prober to detect attacks based on high intensity scores. Subsequently, a Mitigating Rectifier performs surgical attention steering that selectively manipulate adversarial query key dependencies while amplifying task relevant elements to restore the LLM's functional trajectory. Extensive evaluations on multiple backbones show that ICON achieves a competitive 0.4% ASR, matching commercial grade detectors, while yielding a over 50% task utility gain. Furthermore, ICON demonstrates robust Out of Distribution(OOD) generalization and extends effectively to multi-modal agents, establishing a superior balance between security and efficiency.

