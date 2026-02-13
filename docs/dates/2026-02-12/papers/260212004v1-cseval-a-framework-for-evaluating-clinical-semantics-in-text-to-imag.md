---
layout: default
title: CSEval: A Framework for Evaluating Clinical Semantics in Text-to-Image Generation
---

# CSEval: A Framework for Evaluating Clinical Semantics in Text-to-Image Generation
**arXiv**：[2602.12004v1](https://arxiv.org/abs/2602.12004) · [PDF](https://arxiv.org/pdf/2602.12004.pdf)  
**作者**：Robert Cronshaw, Konstantinos Vilouras, Junyu Yan, Yuning Du, Feng Chen, Steven McDonagh, Sotirios A. Tsaftaris  

**一句话要点**：提出CSEval框架以评估医疗文本到图像生成中的临床语义对齐

**关键词**：文本到图像生成, 临床语义评估, 医疗图像生成, 语言模型, 评估框架

## 3 点简述
- 核心问题：现有评估方法忽视生成图像是否反映临床语义，如解剖位置和病理。
- 方法要点：利用语言模型评估生成图像与提示之间的临床语义对齐。
- 实验或效果：CSEval能识别其他指标忽略的语义不一致，并与专家判断相关。

## 摘要（原文）

> Text-to-image generation has been increasingly applied in medical domains for various purposes such as data augmentation and education. Evaluating the quality and clinical reliability of these generated images is essential. However, existing methods mainly assess image realism or diversity, while failing to capture whether the generated images reflect the intended clinical semantics, such as anatomical location and pathology. In this study, we propose the Clinical Semantics Evaluator (CSEval), a framework that leverages language models to assess clinical semantic alignment between the generated images and their conditioning prompts. Our experiments show that CSEval identifies semantic inconsistencies overlooked by other metrics and correlates with expert judgment. CSEval provides a scalable and clinically meaningful complement to existing evaluation methods, supporting the safe adoption of generative models in healthcare.

