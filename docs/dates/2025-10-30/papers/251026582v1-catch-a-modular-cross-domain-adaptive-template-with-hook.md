---
layout: default
title: CATCH: A Modular Cross-domain Adaptive Template with Hook
---

# CATCH: A Modular Cross-domain Adaptive Template with Hook
**arXiv**：[2510.26582v1](https://arxiv.org/abs/2510.26582) · [PDF](https://arxiv.org/pdf/2510.26582.pdf)  
**作者**：Xinjin Li, Yulie Lu, Jinghan Cao, Yu Ma, Zhenglin Li, Yeyang Zhou  

**一句话要点**：提出CATCH框架以解决视觉问答模型跨域泛化问题

**关键词**：视觉问答, 跨域适应, 轻量级模块, 钩子接口, 多域泛化

## 3 点简述
- 核心问题：VQA模型在遥感、医疗等跨域场景中泛化性能显著下降
- 方法要点：引入轻量级域分类器和双适配器，通过钩子接口动态注入
- 实验或效果：在多个VQA基准上实现性能提升，无需重训练骨干模型

## 摘要（原文）

> Recent advances in Visual Question Answering (VQA) have demonstrated
> impressive performance in natural image domains, with models like LLaVA
> leveraging large language models (LLMs) for open-ended reasoning. However,
> their generalization degrades significantly when transferred to out-of-domain
> scenarios such as remote sensing, medical imaging, or math diagrams, due to
> large distributional shifts and the lack of effective domain adaptation
> mechanisms. Existing approaches typically rely on per-domain fine-tuning or
> bespoke pipelines, which are costly, inflexible, and not scalable across
> diverse tasks. In this paper, we propose CATCH, a plug-and-play framework for
> cross-domain adaptation that improves the generalization of VQA models while
> requiring minimal changes to their core architecture. Our key idea is to
> decouple visual and linguistic adaptation by introducing two lightweight
> modules: a domain classifier to identify the input image type, and a dual
> adapter mechanism comprising a Prompt Adapter for language modulation and a
> Visual Adapter for vision feature adjustment. Both modules are dynamically
> injected via a unified hook interface, requiring no retraining of the backbone
> model. Experimental results across four domain-specific VQA benchmarks
> demonstrate that our framework achieves consistent performance gains without
> retraining the backbone model, including +2.3 BLEU on MathVQA, +2.6 VQA on
> MedVQA-RAD, and +3.1 ROUGE on ChartQA. These results highlight that CATCH
> provides a scalable and extensible approach to multi-domain VQA, enabling
> practical deployment across diverse application domains.

