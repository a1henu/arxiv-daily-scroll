---
layout: default
title: ReStyle-TTS: Relative and Continuous Style Control for Zero-Shot Speech Synthesis
---

# ReStyle-TTS: Relative and Continuous Style Control for Zero-Shot Speech Synthesis
**arXiv**：[2601.03632v1](https://arxiv.org/abs/2601.03632) · [PDF](https://arxiv.org/pdf/2601.03632.pdf)  
**作者**：Haitao Li, Chunxiang Jin, Chenglin Li, Wenhao Guan, Zhengxing Huang, Xie Chen  

**一句话要点**：提出ReStyle-TTS框架，实现零样本语音合成中的连续和相对风格控制

**关键词**：零样本语音合成, 风格控制, 解耦无分类器引导, LoRA融合, 音色一致性优化, 连续控制

## 3 点简述
- 核心问题：零样本TTS模型过度依赖参考音频风格，难以灵活合成目标风格
- 方法要点：引入解耦无分类器引导和风格特定LoRA，支持连续多属性控制
- 实验或效果：在风格不匹配场景下保持可懂度和音色，实现用户友好控制

## 摘要（原文）

> Zero-shot text-to-speech models can clone a speaker's timbre from a short reference audio, but they also strongly inherit the speaking style present in the reference. As a result, synthesizing speech with a desired style often requires carefully selecting reference audio, which is impractical when only limited or mismatched references are available. While recent controllable TTS methods attempt to address this issue, they typically rely on absolute style targets and discrete textual prompts, and therefore do not support continuous and reference-relative style control. We propose ReStyle-TTS, a framework that enables continuous and reference-relative style control in zero-shot TTS. Our key insight is that effective style control requires first reducing the model's implicit dependence on reference style before introducing explicit control mechanisms. To this end, we introduce Decoupled Classifier-Free Guidance (DCFG), which independently controls text and reference guidance, reducing reliance on reference style while preserving text fidelity. On top of this, we apply style-specific LoRAs together with Orthogonal LoRA Fusion to enable continuous and disentangled multi-attribute control, and introduce a Timbre Consistency Optimization module to mitigate timbre drift caused by weakened reference guidance. Experiments show that ReStyle-TTS enables user-friendly, continuous, and relative control over pitch, energy, and multiple emotions while maintaining intelligibility and speaker timbre, and performs robustly in challenging mismatched reference-target style scenarios.

