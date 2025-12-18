---
layout: default
title: Corrective Diffusion Language Models
---

# Corrective Diffusion Language Models
**arXiv**：[2512.15596v1](https://arxiv.org/abs/2512.15596) · [PDF](https://arxiv.org/pdf/2512.15596.pdf)  
**作者**：Shuibai Zhang, Fred Zhangzhi Peng, Yiheng Zhang, Jin Pan, Grigorios G. Chrysos  

**一句话要点**：提出校正导向后训练方法以提升扩散语言模型的纠错能力

**关键词**：扩散语言模型, 纠错能力, 后训练方法, 代码修订基准, 置信度引导修正

## 3 点简述
- 扩散语言模型在迭代纠错中常无法可靠识别错误令牌，导致置信度引导的修正失效
- 通过校正导向后训练原则，显式监督可见错误令牌，实现错误感知置信度和针对性修正
- 在代码修订任务和可控设置中，该方法显著优于标准掩码扩散语言模型，并提升纯完成性能

## 摘要（原文）

> Diffusion language models are structurally well-suited for iterative error correction, as their non-causal denoising dynamics allow arbitrary positions in a sequence to be revised. However, standard masked diffusion language model (MDLM) training fails to reliably induce this behavior, as models often cannot identify unreliable tokens in a complete input, rendering confidence-guided refinement ineffective. We study corrective behavior in diffusion language models, defined as the ability to assign lower confidence to incorrect tokens and iteratively refine them while preserving correct content. We show that this capability is not induced by conventional masked diffusion objectives and propose a correction-oriented post-training principle that explicitly supervises visible incorrect tokens, enabling error-aware confidence and targeted refinement. To evaluate corrective behavior, we introduce the Code Revision Benchmark (CRB), a controllable and executable benchmark for assessing error localization and in-place correction. Experiments on code revision tasks and controlled settings demonstrate that models trained with our approach substantially outperform standard MDLMs in correction scenarios, while also improving pure completion performance. Our code is publicly available at https://github.com/zhangshuibai/CDLM.

