---
layout: default
title: Language-Grounded Multi-Domain Image Translation via Semantic Difference Guidance
---

# Language-Grounded Multi-Domain Image Translation via Semantic Difference Guidance
**arXiv**：[2601.07221v1](https://arxiv.org/abs/2601.07221) · [PDF](https://arxiv.org/pdf/2601.07221.pdf)  
**作者**：Jongwon Ryu, Joonhyung Park, Jaeho Han, Yeong-Seok Kim, Hye-rin Kim, Sunjae Yoon, Junyeong Kim  

**一句话要点**：提出LACE框架，通过语义差异引导实现语言驱动的多域图像翻译

**关键词**：多域图像翻译, 语言引导, 语义差异, 可控生成, 跨模态框架

## 3 点简述
- 核心问题：现有方法在多域图像翻译中难以保持结构完整性并提供细粒度属性控制
- 方法要点：结合GLIP-Adapter融合全局语义与局部特征，以及多域控制引导机制将语义差异映射为翻译向量
- 实验或效果：在CelebA(Dialog)和BDD100K数据集上验证了高视觉保真度、结构保持和可解释的域特定控制

## 摘要（原文）

> Multi-domain image-to-image translation re quires grounding semantic differences ex pressed in natural language prompts into corresponding visual transformations, while preserving unrelated structural and seman tic content. Existing methods struggle to maintain structural integrity and provide fine grained, attribute-specific control, especially when multiple domains are involved. We propose LACE (Language-grounded Attribute Controllable Translation), built on two compo nents: (1) a GLIP-Adapter that fuses global semantics with local structural features to pre serve consistency, and (2) a Multi-Domain Control Guidance mechanism that explicitly grounds the semantic delta between source and target prompts into per-attribute translation vec tors, aligning linguistic semantics with domain level visual changes. Together, these modules enable compositional multi-domain control with independent strength modulation for each attribute. Experiments on CelebA(Dialog) and BDD100K demonstrate that LACE achieves high visual fidelity, structural preservation, and interpretable domain-specific control, surpass ing prior baselines. This positions LACE as a cross-modal content generation framework bridging language semantics and controllable visual translation.

