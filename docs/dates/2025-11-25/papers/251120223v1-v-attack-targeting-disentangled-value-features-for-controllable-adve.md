---
layout: default
title: V-Attack: Targeting Disentangled Value Features for Controllable Adversarial Attacks on LVLMs
---

# V-Attack: Targeting Disentangled Value Features for Controllable Adversarial Attacks on LVLMs
**arXiv**：[2511.20223v1](https://arxiv.org/abs/2511.20223) · [PDF](https://arxiv.org/pdf/2511.20223.pdf)  
**作者**：Sen Nie, Jie Zhang, Jianxin Yan, Shiguang Shan, Xilin Chen  

**一句话要点**：提出V-Attack方法，通过操纵值特征实现可控对抗攻击，解决LVLM中语义操控不精确问题。

**关键词**：对抗攻击, 大型视觉语言模型, 值特征, 语义操控, 可控攻击, 注意力机制

## 3 点简述
- 核心问题：现有对抗攻击方法因语义纠缠难以精确操控图像中特定概念。
- 方法要点：利用值特征作为精确操控手柄，引入自值增强和文本引导值操纵模块。
- 实验或效果：在多种LVLM上攻击成功率平均提升36%，优于现有方法。

## 摘要（原文）

> Adversarial attacks have evolved from simply disrupting predictions on conventional task-specific models to the more complex goal of manipulating image semantics on Large Vision-Language Models (LVLMs). However, existing methods struggle with controllability and fail to precisely manipulate the semantics of specific concepts in the image. We attribute this limitation to semantic entanglement in the patch-token representations on which adversarial attacks typically operate: global context aggregated by self-attention in the vision encoder dominates individual patch features, making them unreliable handles for precise local semantic manipulation. Our systematic investigation reveals a key insight: value features (V) computed within the transformer attention block serve as much more precise handles for manipulation. We show that V suppresses global-context channels, allowing it to retain high-entropy, disentangled local semantic information. Building on this discovery, we propose V-Attack, a novel method designed for precise local semantic attacks. V-Attack targets the value features and introduces two core components: (1) a Self-Value Enhancement module to refine V's intrinsic semantic richness, and (2) a Text-Guided Value Manipulation module that leverages text prompts to locate source concept and optimize it toward a target concept. By bypassing the entangled patch features, V-Attack achieves highly effective semantic control. Extensive experiments across diverse LVLMs, including LLaVA, InternVL, DeepseekVL and GPT-4o, show that V-Attack improves the attack success rate by an average of 36% over state-of-the-art methods, exposing critical vulnerabilities in modern visual-language understanding. Our code and data are available https://github.com/Summu77/V-Attack.

