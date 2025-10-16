---
layout: default
title: Generative Universal Verifier as Multimodal Meta-Reasoner
---

# Generative Universal Verifier as Multimodal Meta-Reasoner
**arXiv**：[2510.13804v1](https://arxiv.org/abs/2510.13804) · [PDF](https://arxiv.org/pdf/2510.13804.pdf)  
**作者**：Xinchen Zhang, Xiaoying Zhang, Youbin Wu, Yanbin Cao, Renrui Zhang, Ruihang Chu, Ling Yang, Yujiu Yang  

**一句话要点**：提出生成式通用验证器作为多模态元推理器，增强视觉语言模型的可靠反思与优化能力。

**关键词**：多模态推理, 视觉验证, 生成式模型, 测试时优化, 基准评估

## 3 点简述
- 现有视觉语言模型在视觉验证任务中表现不佳，与人类能力存在显著差距。
- 构建ViVerBench基准并训练OmniVerifier-7B，实现通用视觉验证，提升基准性能8.3%。
- 提出OmniVerifier-TTS测试时扩展范式，在多个基准上优于现有方法，提升生成能力。

## 摘要（原文）

> We introduce Generative Universal Verifier, a novel concept and plugin
> designed for next-generation multimodal reasoning in vision-language models and
> unified multimodal models, providing the fundamental capability of reflection
> and refinement on visual outcomes during the reasoning and generation process.
> This work makes three main contributions: (1) We build ViVerBench, a
> comprehensive benchmark spanning 16 categories of critical tasks for evaluating
> visual outcomes in multimodal reasoning. Results show that existing VLMs
> consistently underperform across these tasks, underscoring a substantial gap
> from human-level capability in reliable visual verification. (2) We design two
> automated pipelines to construct large-scale visual verification data and train
> OmniVerifier-7B, the first omni-capable generative verifier trained for
> universal visual verification and achieves notable gains on ViVerBench(+8.3).
> Through training, we identify three atomic capabilities in visual verification
> and demonstrate how they generalize and interact synergistically. (3) We
> propose OmniVerifier-TTS, a sequential test-time scaling paradigm that
> leverages the universal verifier to bridge image generation and editing within
> unified models, enhancing the upper bound of generative ability through
> iterative fine-grained optimization. Beyond generation, we extend universal
> verifier to broader world-modeling interleaved reasoning scenarios.
> Empirically, OmniVerifier-TTS achieves improvements on T2I-ReasonBench(+3.7),
> and GenEval++(+4.3), outperforming existing parallel test-time scaling methods,
> such as Best-of-N. By endowing multimodal reasoning with reliable visual
> verification, OmniVerifier advances both reliable reflection during generation
> and scalable test-time refinement, marking a step toward more trustworthy and
> controllable next-generation reasoning systems.

