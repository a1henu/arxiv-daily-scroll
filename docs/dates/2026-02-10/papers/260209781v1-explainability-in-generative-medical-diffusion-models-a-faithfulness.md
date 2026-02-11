---
layout: default
title: Explainability in Generative Medical Diffusion Models: A Faithfulness-Based Analysis on MRI Synthesis
---

# Explainability in Generative Medical Diffusion Models: A Faithfulness-Based Analysis on MRI Synthesis
**arXiv**：[2602.09781v1](https://arxiv.org/abs/2602.09781) · [PDF](https://arxiv.org/pdf/2602.09781.pdf)  
**作者**：Surjo Dey, Pallabi Saikia  

**一句话要点**：提出基于忠实度的可解释性框架，分析生成扩散模型在MRI合成中的决策过程。

**关键词**：生成扩散模型, 医学影像合成, 可解释性分析, 忠实度评估, MRI合成, 原型网络

## 3 点简述
- 核心问题：生成扩散模型在医学影像合成中内部决策过程不透明，影响可解释性和可信度。
- 方法要点：采用基于原型的方法（如ProtoPNet、Enhanced ProtoPNet、ProtoPool）结合忠实度分析，关联生成特征与训练特征。
- 实验或效果：Enhanced ProtoPNet在忠实度得分最高（0.1534），提供更可靠的可解释性，提升模型透明度和医疗应用安全性。

## 摘要（原文）

> This study investigates the explainability of generative diffusion models in the context of medical imaging, focusing on Magnetic resonance imaging (MRI) synthesis. Although diffusion models have shown strong performance in generating realistic medical images, their internal decision making process remains largely opaque. We present a faithfulness-based explainability framework that analyzes how prototype-based explainability methods like ProtoPNet (PPNet), Enhanced ProtoPNet (EPPNet), and ProtoPool can link the relationship between generated and training features. Our study focuses on understanding the reasoning behind image formation through denoising trajectory of diffusion model and subsequently prototype explainability with faithfulness analysis. Experimental analysis shows that EPPNet achieves the highest faithfulness (with score 0.1534), offering more reliable insights, and explainability into the generative process. The results highlight that diffusion models can be made more transparent and trustworthy through faithfulness-based explanations, contributing to safer and more interpretable applications of generative AI in healthcare.

