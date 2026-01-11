---
layout: default
title: Vision-Language Introspection: Mitigating Overconfident Hallucinations in MLLMs via Interpretable Bi-Causal Steering
---

# Vision-Language Introspection: Mitigating Overconfident Hallucinations in MLLMs via Interpretable Bi-Causal Steering
**arXiv**：[2601.05159v1](https://arxiv.org/abs/2601.05159) · [PDF](https://arxiv.org/pdf/2601.05159.pdf)  
**作者**：Shuliang Liu, Songbo Yang, Dong Fang, Sihang Jia, Yuqi Tang, Lingfeng Su, Ruoshui Peng, Yibo Yan, Xin Zou, Xuming Hu  

**一句话要点**：提出Vision-Language Introspection框架，通过可解释的双因果调控缓解多模态大语言模型中的过度自信幻觉问题

**关键词**：多模态大语言模型, 对象幻觉, 可解释性, 推理框架, 视觉语言内省, 双因果调控

## 3 点简述
- 核心问题：多模态大语言模型因认知内省失败，过度依赖语言先验而非视觉证据，导致对象幻觉。
- 方法要点：VLI框架无需训练，通过属性内省诊断幻觉风险，并利用可解释双因果调控动态隔离视觉证据和校准置信度。
- 实验或效果：在MMHal-Bench上降低对象幻觉率12.67%，在POPE上提升准确率5.8%，达到先进性能。

## 摘要（原文）

> Object hallucination critically undermines the reliability of Multimodal Large Language Models, often stemming from a fundamental failure in cognitive introspection, where models blindly trust linguistic priors over specific visual evidence. Existing mitigations remain limited: contrastive decoding approaches operate superficially without rectifying internal semantic misalignments, while current latent steering methods rely on static vectors that lack instance-specific precision. We introduce Vision-Language Introspection (VLI), a training-free inference framework that simulates a metacognitive self-correction process. VLI first performs Attributive Introspection to diagnose hallucination risks via probabilistic conflict detection and localize the causal visual anchors. It then employs Interpretable Bi-Causal Steering to actively modulate the inference process, dynamically isolating visual evidence from background noise while neutralizing blind confidence through adaptive calibration. VLI achieves state-of-the-art performance on advanced models, reducing object hallucination rates by 12.67% on MMHal-Bench and improving accuracy by 5.8% on POPE.

