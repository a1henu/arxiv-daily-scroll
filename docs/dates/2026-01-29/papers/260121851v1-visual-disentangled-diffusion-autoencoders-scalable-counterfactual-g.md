---
layout: default
title: Visual Disentangled Diffusion Autoencoders: Scalable Counterfactual Generation for Foundation Models
---

# Visual Disentangled Diffusion Autoencoders: Scalable Counterfactual Generation for Foundation Models
**arXiv**：[2601.21851v1](https://arxiv.org/abs/2601.21851) · [PDF](https://arxiv.org/pdf/2601.21851.pdf)  
**作者**：Sidney Bender, Marco Morik  

**一句话要点**：提出视觉解耦扩散自编码器以高效生成基础模型的反事实样本

**关键词**：基础模型, 反事实生成, 解耦学习, 扩散自编码器, 知识蒸馏

## 3 点简述
- 基础模型易受虚假关联影响，现有方法依赖标签或计算昂贵
- DiDAE结合冻结基础模型与解耦字典学习，无需梯度生成解耦反事实
- 实验显示DiDAE-CFKD在缓解捷径学习上达到先进性能，提升下游任务表现

## 摘要（原文）

> Foundation models, despite their robust zero-shot capabilities, remain vulnerable to spurious correlations and 'Clever Hans' strategies. Existing mitigation methods often rely on unavailable group labels or computationally expensive gradient-based adversarial optimization. To address these limitations, we propose Visual Disentangled Diffusion Autoencoders (DiDAE), a novel framework integrating frozen foundation models with disentangled dictionary learning for efficient, gradient-free counterfactual generation directly for the foundation model. DiDAE first edits foundation model embeddings in interpretable disentangled directions of the disentangled dictionary and then decodes them via a diffusion autoencoder. This allows the generation of multiple diverse, disentangled counterfactuals for each factual, much faster than existing baselines, which generate single entangled counterfactuals. When paired with Counterfactual Knowledge Distillation, DiDAE-CFKD achieves state-of-the-art performance in mitigating shortcut learning, improving downstream performance on unbalanced datasets.

