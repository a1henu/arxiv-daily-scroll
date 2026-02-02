---
layout: default
title: Visual Personalization Turing Test
---

# Visual Personalization Turing Test
**arXiv**：[2601.22680v1](https://arxiv.org/abs/2601.22680) · [PDF](https://arxiv.org/pdf/2601.22680.pdf)  
**作者**：Rameen Abdal, James Burgess, Sergey Tulyakov, Kuan-Chieh Jackson Wang  

**一句话要点**：提出视觉个性化图灵测试以评估生成内容在上下文中的个性化程度，基于感知不可区分性。

**关键词**：视觉个性化评估, 图灵测试, 生成式人工智能, 感知不可区分性, 检索增强生成

## 3 点简述
- 核心问题：传统评估方法侧重于身份复制，而非内容在上下文中的个性化真实性。
- 方法要点：引入VPTT框架，包括10k人物基准、视觉检索增强生成器和基于文本的VPTT分数。
- 实验或效果：VPTT分数与人类和视觉语言模型判断高度相关，验证其作为感知代理的可靠性。

## 摘要（原文）

> We introduce the Visual Personalization Turing Test (VPTT), a new paradigm for evaluating contextual visual personalization based on perceptual indistinguishability, rather than identity replication. A model passes the VPTT if its output (image, video, 3D asset, etc.) is indistinguishable to a human or calibrated VLM judge from content a given person might plausibly create or share. To operationalize VPTT, we present the VPTT Framework, integrating a 10k-persona benchmark (VPTT-Bench), a visual retrieval-augmented generator (VPRAG), and the VPTT Score, a text-only metric calibrated against human and VLM judgments. We show high correlation across human, VLM, and VPTT evaluations, validating the VPTT Score as a reliable perceptual proxy. Experiments demonstrate that VPRAG achieves the best alignment-originality balance, offering a scalable and privacy-safe foundation for personalized generative AI.

