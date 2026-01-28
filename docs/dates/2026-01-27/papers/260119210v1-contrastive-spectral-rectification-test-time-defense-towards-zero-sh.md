---
layout: default
title: Contrastive Spectral Rectification: Test-Time Defense towards Zero-shot Adversarial Robustness of CLIP
---

# Contrastive Spectral Rectification: Test-Time Defense towards Zero-shot Adversarial Robustness of CLIP
**arXiv**：[2601.19210v1](https://arxiv.org/abs/2601.19210) · [PDF](https://arxiv.org/pdf/2601.19210.pdf)  
**作者**：Sen Nie, Jie Zhang, Zhuo Wang, Shiguang Shan, Xilin Chen  

**一句话要点**：提出对比频谱校正方法，以提升CLIP在零样本对抗攻击下的测试时防御能力。

**关键词**：对抗鲁棒性, 测试时防御, 频谱校正, 零样本学习, 视觉语言模型

## 3 点简述
- 核心问题：CLIP等视觉语言模型在零样本泛化中易受对抗样本攻击，现有测试时防御方法鲁棒性不足且效率低。
- 方法要点：基于对抗样本在频率衰减下的特征不一致性，设计频谱引导的对比目标，自适应优化校正扰动以对齐自然流形。
- 实验或效果：在16个分类基准上，CSR平均优于SOTA方法18.1%，对抗AutoAttack，且推理开销适中，适用性广。

## 摘要（原文）

> Vision-language models (VLMs) such as CLIP have demonstrated remarkable zero-shot generalization, yet remain highly vulnerable to adversarial examples (AEs). While test-time defenses are promising, existing methods fail to provide sufficient robustness against strong attacks and are often hampered by high inference latency and task-specific applicability. To address these limitations, we start by investigating the intrinsic properties of AEs, which reveals that AEs exhibit severe feature inconsistency under progressive frequency attenuation. We further attribute this to the model's inherent spectral bias. Leveraging this insight, we propose an efficient test-time defense named Contrastive Spectral Rectification (CSR). CSR optimizes a rectification perturbation to realign the input with the natural manifold under a spectral-guided contrastive objective, which is applied input-adaptively. Extensive experiments across 16 classification benchmarks demonstrate that CSR outperforms the SOTA by an average of 18.1% against strong AutoAttack with modest inference overhead. Furthermore, CSR exhibits broad applicability across diverse visual tasks. Code is available at https://github.com/Summu77/CSR.

