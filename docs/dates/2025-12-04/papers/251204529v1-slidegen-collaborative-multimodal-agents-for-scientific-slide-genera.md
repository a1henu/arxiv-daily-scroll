---
layout: default
title: SlideGen: Collaborative Multimodal Agents for Scientific Slide Generation
---

# SlideGen: Collaborative Multimodal Agents for Scientific Slide Generation
**arXiv**：[2512.04529v1](https://arxiv.org/abs/2512.04529) · [PDF](https://arxiv.org/pdf/2512.04529.pdf)  
**作者**：Xin Liang, Xiang Zhang, Yiwei Xu, Siqi Sun, Chenyu You  

**一句话要点**：提出SlideGen协作多模态代理框架，以解决科学论文到幻灯片生成中的视觉规划与长上下文理解挑战。

**关键词**：科学幻灯片生成, 多模态代理协作, 视觉规划, 长上下文理解, PPTX生成

## 3 点简述
- 核心问题：现有方法多简化为文本摘要，忽视幻灯片创建的视觉组件和设计密集性。
- 方法要点：采用模块化视觉语言代理协作推理文档结构与语义，生成可编辑PPTX幻灯片。
- 实验或效果：在多样基准测试中，SlideGen在视觉质量、内容忠实度和可读性上优于现有方法。

## 摘要（原文）

> Generating academic slides from scientific papers is a challenging multimodal reasoning task that requires both long context understanding and deliberate visual planning. Existing approaches largely reduce it to text only summarization, overlooking the visual component and design intensive nature of slide creation. In this paper we introduce SlideGen, an agentic, modular, and visual in the loop framework for scientific paper to slide generation. SlideGen orchestrates a group of vision language agents that reason collaboratively over the document structure and semantics, producing editable PPTX slides with logical flow and compelling visual presentation. By integrating coordinated outlining, mapping, arrangement, note synthesis, and iterative refinement, our system consistently delivers slides of expert level quality. Across diverse benchmarks and strong baselines, SlideGen outperforms existing methods in visual quality, content faithfulness, and readability, positioning it as the new state of the art in automated slide generation. Our work establishes a foundation for design aware multimodal slide generation, demonstrating how agentic collaboration can bridge understanding and presentation in complex multimodal reasoning tasks.

