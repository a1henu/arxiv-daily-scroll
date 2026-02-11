---
layout: default
title: ArtifactLens: Hundreds of Labels Are Enough for Artifact Detection with VLMs
---

# ArtifactLens: Hundreds of Labels Are Enough for Artifact Detection with VLMs
**arXiv**：[2602.09475v1](https://arxiv.org/abs/2602.09475) · [PDF](https://arxiv.org/pdf/2602.09475.pdf)  
**作者**：James Burgess, Rameen Abdal, Dan Stoddart, Sergey Tulyakov, Serena Yeung-Levy, Kuan-Chieh Jackson Wang  

**一句话要点**：提出ArtifactLens，利用少量标注数据解锁VLM的伪影检测能力

**关键词**：伪影检测, 视觉语言模型, 少样本学习, 上下文学习, 文本指令优化, AIGC检测

## 3 点简述
- 核心问题：图像生成器产生逼真图像，但伪影检测需大量标注数据，成本高且难适应新类型
- 方法要点：基于预训练VLM，结合上下文学习和文本指令优化，仅需每类别数百标注示例
- 实验或效果：在五个基准测试中达到SOTA，数据需求降低数个数量级，并泛化至其他伪影类型和AIGC检测

## 摘要（原文）

> Modern image generators produce strikingly realistic images, where only artifacts like distorted hands or warped objects reveal their synthetic origin. Detecting these artifacts is essential: without detection, we cannot benchmark generators or train reward models to improve them. Current detectors fine-tune VLMs on tens of thousands of labeled images, but this is expensive to repeat whenever generators evolve or new artifact types emerge. We show that pretrained VLMs already encode the knowledge needed to detect artifacts - with the right scaffolding, this capability can be unlocked using only a few hundred labeled examples per artifact category. Our system, ArtifactLens, achieves state-of-the-art on five human artifact benchmarks (the first evaluation across multiple datasets) while requiring orders of magnitude less labeled data. The scaffolding consists of a multi-component architecture with in-context learning and text instruction optimization, with novel improvements to each. Our methods generalize to other artifact types - object morphology, animal anatomy, and entity interactions - and to the distinct task of AIGC detection.

