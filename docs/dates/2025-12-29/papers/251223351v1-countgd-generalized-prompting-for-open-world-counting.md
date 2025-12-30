---
layout: default
title: CountGD++: Generalized Prompting for Open-World Counting
---

# CountGD++: Generalized Prompting for Open-World Counting
**arXiv**：[2512.23351v1](https://arxiv.org/abs/2512.23351) · [PDF](https://arxiv.org/pdf/2512.23351.pdf)  
**作者**：Niki Amini-Naieni, Andrew Zisserman  

**一句话要点**：提出CountGD++以扩展开放世界计数的提示灵活性，提升准确性和效率。

**关键词**：开放世界计数, 多模态提示, 自动化标注, 视觉示例扩展, LLM集成

## 3 点简述
- 核心问题：现有方法无法指定不计数对象，且视觉示例需手动标注。
- 方法要点：引入文本/视觉示例描述不计数对象，自动化视觉示例标注，支持自然与合成图像示例。
- 实验或效果：在多个数据集上显著提升准确性、效率和泛化能力，并用作LLM的视觉专家代理。

## 摘要（原文）

> The flexibility and accuracy of methods for automatically counting objects in images and videos are limited by the way the object can be specified. While existing methods allow users to describe the target object with text and visual examples, the visual examples must be manually annotated inside the image, and there is no way to specify what not to count. To address these gaps, we introduce novel capabilities that expand how the target object can be specified. Specifically, we extend the prompt to enable what not to count to be described with text and/or visual examples, introduce the concept of `pseudo-exemplars' that automate the annotation of visual examples at inference, and extend counting models to accept visual examples from both natural and synthetic external images. We also use our new counting model, CountGD++, as a vision expert agent for an LLM. Together, these contributions expand the prompt flexibility of multi-modal open-world counting and lead to significant improvements in accuracy, efficiency, and generalization across multiple datasets. Code is available at https://github.com/niki-amini-naieni/CountGDPlusPlus.

